#!/usr/bin/env python3
"""Rooter 1 knockout v3: flood-fill bg + clear pockets + 3px defringe + black-lean edge."""
from PIL import Image, ImageFilter
import numpy as np
import subprocess

try:
    from scipy import ndimage
except ImportError:
    subprocess.run(['pip', 'install', '--quiet', 'scipy'], check=False)
    from scipy import ndimage

src = Image.open('images/Rooter 1.jfif').convert('RGB')
a = np.array(src).astype(int)
mn, mx = a.min(axis=2), a.max(axis=2)
sat = mx - mn
bgish = (sat < 55) & (mn > 130)

# 1) flood-fill background from borders
lab, n = ndimage.label(bgish)
border = set(lab[0, :]) | set(lab[-1, :]) | set(lab[:, 0]) | set(lab[:, -1])
border.discard(0)
bg = np.isin(lab, list(border))
# 2) enclosed pockets = non-border labeled bgish regions not connected to border
for i in range(1, n + 1):
    if i not in border:
        size = int((lab == i).sum())
        if size < 60000:  # pocket
            bg |= (lab == i)

subject = (~bg).astype(np.uint8) * 255
# 3) defringe: erode subject by 3px
sim = Image.fromarray(subject)
for _ in range(3):
    sim = sim.filter(ImageFilter.MinFilter(3))
alpha = np.array(sim).astype(np.float64) / 255.0
# feather 1px
alpha = np.array(Image.fromarray((alpha * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.9))).astype(np.float64) / 255.0

rgb = a.astype(np.float64)
rem = 1.0 - alpha
white = 245.0
for c in range(3):
    rgb[:, :, c] = (rgb[:, :, c] - rem * white) / np.maximum(alpha, 1e-3)
    rgb[:, :, c] = np.clip(rgb[:, :, c], 0, 255)
# darken the semi-transparent band toward black (comic outlines are black; bg is dark)
for c in range(3):
    rgb[:, :, c] = rgb[:, :, c] * (0.35 + 0.65 * alpha)

out = Image.fromarray(np.dstack([rgb.astype(np.uint8), (alpha * 255).astype(np.uint8)]), 'RGBA')
out.save('images/rooter-1-transparent.png')
print('saved, bbox', out.getchannel('A').getbbox())