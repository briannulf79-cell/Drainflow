#!/usr/bin/env python3
"""Clear enclosed white pockets (trapped background between tubes/body) in Rooter 1 knockout."""
from PIL import Image, ImageFilter
import numpy as np
import subprocess

try:
    from scipy import ndimage
except ImportError:
    subprocess.run(['pip', 'install', '--quiet', 'scipy'], check=False)
    from scipy import ndimage

im = Image.open('images/rooter-1-transparent.png')
a = np.array(im)
mn = a[:, :, :3].min(axis=2).astype(int)
mx = a[:, :, :3].max(axis=2).astype(int)
# white-ish pocket candidates (alpha kept, low-sat light pixels)
white = (mn > 170) & ((mx - mn) < 70) & (a[:, :, 3] > 60)

lab, n = ndimage.label(white)
border = set(lab[0, :]) | set(lab[-1, :]) | set(lab[:, 0]) | set(lab[:, -1])
border.discard(0)

removed = 0
for i in range(1, n + 1):
    if i in border:
        continue
    size = int((lab == i).sum())
    if size < 6000:  # pockets only; big enclosed regions = legit white artwork
        a[lab == i, 3] = 0
        removed += size
print('removed pocket px:', removed)

out = Image.fromarray(a, 'RGBA')
out.save('images/rooter-1-transparent.png')
print('saved, bbox', out.getchannel('A').getbbox())
