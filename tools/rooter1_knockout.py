#!/usr/bin/env python3
"""Flood-fill knockout v2 for Rooter 1: catches gray drop shadow + defringes edge halo."""
from PIL import Image, ImageFilter
import numpy as np

try:
    from scipy import ndimage
    HAVE = True
except ImportError:
    HAVE = False
print('scipy:', HAVE)

src = Image.open('images/Rooter 1.jfif').convert('RGB')
a = np.array(src).astype(int)
mn, mx = a.min(axis=2), a.max(axis=2)
sat = mx - mn

# generous background candidate: any low-saturation light-to-mid pixel (white bg + gray shadow)
bgish = (sat < 40) & (mn > 110)

if HAVE:
    lab, _ = ndimage.label(bgish)
    border_labels = set(lab[0, :]) | set(lab[-1, :]) | set(lab[:, 0]) | set(lab[:, -1])
    border_labels.discard(0)
    bg = np.isin(lab, list(border_labels))
else:
    bg = bgish.copy()
    bg[1:-1, 1:-1] = False
    for _ in range(600):
        grown = bg.copy()
        grown[1:, :] |= bg[:-1, :]
        grown[:-1, :] |= bg[1:, :]
        grown[:, 1:] |= bg[:, :-1]
        grown[:, :-1] |= bg[:, 1:]
        grown &= bgish
        if (grown == bg).all():
            break
        bg = grown

# subject alpha, then defringe: erode subject 2px to strip white-contaminated ring
subject = (~bg).astype(np.uint8) * 255
sub_img = Image.fromarray(subject)
for _ in range(2):
    sub_img = sub_img.filter(ImageFilter.MinFilter(3))
# soften 1px
sub_img = sub_img.filter(ImageFilter.GaussianBlur(0.8))

rgb = np.array(src).astype(np.float64)
alpha = np.array(sub_img).astype(np.float64) / 255.0

# decontaminate: un-mix residual white at semi-transparent edge pixels
white = 245.0
amt = (1.0 - alpha)
for c in range(3):
    rgb[:, :, c] = np.clip((rgb[:, :, c] - amt * white) / np.maximum(alpha, 1e-3), 0, 255)

out = Image.fromarray(np.dstack([rgb.astype(np.uint8), (alpha * 255).astype(np.uint8)]), 'RGBA')
out.save('images/rooter-1-transparent.png')
print('bbox', out.getchannel('A').getbbox())
