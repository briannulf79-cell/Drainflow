#!/usr/bin/env python3
"""Find enclosed white pockets (between tubes/body) in the Rooter 1 knockout."""
from PIL import Image
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
white = (mn > 180) & ((mx - mn) < 60) & (a[:, :, 3] > 100)
print('white px:', int(white.sum()))
lab, n = ndimage.label(white)
sizes = np.bincount(lab.ravel())
big = [(int(i), int(s)) for i, s in enumerate(sizes) if s > 300]
print('regions>300:', len(big))
for i, s in sorted(big, key=lambda x: -x[1])[:15]:
    ys, xs = np.where(lab == i)
    print(f'  region {i}: {s}px  bbox x[{xs.min()}..{xs.max()}] y[{ys.min()}..{ys.max()}]')
