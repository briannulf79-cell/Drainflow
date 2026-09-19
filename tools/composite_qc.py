#!/usr/bin/env python3
"""Composite Rooter 1 transparent onto dark bg for visual QC."""
from PIL import Image

bg = Image.new('RGBA', (1408, 752), (13, 17, 12, 255))
fg = Image.open('images/rooter-1-transparent.png').convert('RGBA')
bg.alpha_composite(fg)
bg.convert('RGB').save('/tmp/rooter-on-dark-full.jpg', quality=92)
bg.convert('RGB').crop((600, 50, 950, 350)).save('/tmp/rooter-on-dark-shoulders.jpg', quality=95)
print('saved')