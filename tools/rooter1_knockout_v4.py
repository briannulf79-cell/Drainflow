#!/usr/bin/env python3
"""Rooter 1 knockout v4: border flood-fill + TARGETED seed pockets (size-capped) + defringe.
Never clears enclosed regions globally, so chrome plates / specular highlights survive."""
from PIL import Image, ImageFilter
import numpy as np
import subprocess
from collections import deque

try:
    from scipy import ndimage
except ImportError:
    subprocess.run(['pip', 'install', '--quiet', 'scipy'], check=False)
    from scipy import ndimage

src = Image.open('images/Rooter 1.jfif').convert('RGB')
a = np.array(src).astype(int)
H, W = a.shape[:2]
mn, mx = a.min(axis=2), a.max(axis=2)
sat = mx - mn
lightish = (sat < 40) & (mn > 180)  # tight: bg is flat ~235; armor highlights are tinted/textured

pocketish = (sat < 60) & (mn > 110)  # permissive: pockets are shaded gray, bounded by outlines

# 1) background: flood from borders
lab, _ = ndimage.label(lightish)
border = set(lab[0, :]) | set(lab[-1, :]) | set(lab[:, 0]) | set(lab[:, -1])
border.discard(0)
bg = np.isin(lab, list(border))

# 2) targeted pockets: seed floods, each capped at 3500 px (pockets are <=2400)
seeds = [(206, 817), (556, 462), (178, 642), (117, 796)]  # pocket centers only; never near chest highlights
for (sy, sx) in seeds:
    # snap seed to nearest lightish pixel within 25px
    found = None
    for dy in range(-25, 26, 2):
        for dx in range(-25, 26, 2):
            y, x = sy + dy, sx + dx
            if 0 <= y < H and 0 <= x < W and pocketish[y, x] and not bg[y, x]:
                found = (y, x)
                break
        if found:
            break
    if not found:
        print(f'seed {(sy, sx)}: no light pixel nearby (already bg or inside artwork) - skip')
        continue
    # BFS flood limited to lightish & size cap
    region = set()
    q = deque([found])
    seen = {found}
    escaped = False
    while q:
        y, x = q.popleft()
        region.add((y, x))
        if len(region) > 3500:
            escaped = True
            break
        for ny, nx in ((y-1,x),(y+1,x),(y,x-1),(y,x+1)):
            if 0 <= ny < H and 0 <= nx < W and (ny,nx) not in seen and pocketish[ny,nx] and not bg[ny,nx]:
                seen.add((ny,nx))
                q.append((ny,nx))
    if escaped:
        print(f'seed {(sy, sx)}: region >3500px (artwork, not pocket) - aborted')
    else:
        for (y, x) in region:
            bg[y, x] = True
        print(f'seed {(sy, sx)}: cleared {len(region)}px')

# 3) defringe: erode subject 3px + feather + white decontamination
subject = (~bg).astype(np.uint8) * 255
sim = Image.fromarray(subject)
for _ in range(3):
    sim = sim.filter(ImageFilter.MinFilter(3))
alpha = np.array(sim).astype(np.float64) / 255.0
alpha = np.array(Image.fromarray((alpha * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.9))).astype(np.float64) / 255.0

rgb = a.astype(np.float64)
rem = 1.0 - alpha
for c in range(3):
    rgb[:, :, c] = np.clip((rgb[:, :, c] - rem * 245.0) / np.maximum(alpha, 1e-3), 0, 255)
    rgb[:, :, c] = rgb[:, :, c] * (0.5 + 0.5 * alpha)

out = Image.fromarray(np.dstack([rgb.astype(np.uint8), (alpha * 255).astype(np.uint8)]), 'RGBA')
out.save('images/rooter-1-transparent.png')
print('saved, bbox', out.getchannel('A').getbbox())