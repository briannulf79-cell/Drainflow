#!/usr/bin/env python3
"""Locate remaining interior transparent hole in chest area of the knockout."""
from PIL import Image
import numpy as np
a = np.array(Image.open('images/rooter-1-transparent.png'))
transparent = a[:, :, 3] < 60
# search chest region x[550..750], y[250..450] for transparent clusters
sub = transparent[250:450, 550:750]
ys, xs = np.where(sub)
if len(ys):
    print('transparent px in chest region:', len(ys))
    print('bbox y[%d..%d] x[%d..%d]' % (ys.min()+250, ys.max()+250, xs.min()+550, xs.max()+550))
else:
    print('none in that window')
# also check upper chest y[200..300]
sub2 = transparent[200:300, 550:750]
ys2, xs2 = np.where(sub2)
print('y200-300 window px:', len(ys2), ('bbox y[%d..%d] x[%d..%d]' % (ys2.min()+200, ys2.max()+200, xs2.min()+550, xs2.max()+550)) if len(ys2) else '')
