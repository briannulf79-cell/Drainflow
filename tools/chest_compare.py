#!/usr/bin/env python3
"""Side-by-side: original chest zone vs knockout-on-dark chest zone."""
from PIL import Image

orig = Image.open('images/Rooter 1.jfif').convert('RGB').crop((520, 180, 800, 500))
dark = Image.open('/tmp/rooter-on-dark-full.jpg').crop((520, 180, 800, 500))
w, h = orig.size
combo = Image.new('RGB', (w * 2 + 8, h), (255, 0, 0))
combo.paste(orig, (0, 0))
combo.paste(dark, (w + 8, 0))
combo.save('/tmp/chest-compare.jpg', quality=95)
print('saved')