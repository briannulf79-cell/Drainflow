from PIL import Image, ImageDraw, ImageFont
import numpy as np, os

JOBS = [
    ('img_830c09106a31', 'Hydro Jetting*'),
    ('img_4d1f00b8d07d', 'Power Rodding & Snaking'),
    ('img_8e5223ea48c5', 'Sewer Line Repair'),
    ('img_c8f6b1eb875a', 'Emergency Backup Defense'),
    ('img_3f7292963f7d', 'Camera Inspection'),
    ('img_75fb2a5fe5c3', 'Preventive Maintenance'),
]
CACHE = '/home/monster-pc/.hermes/cache/images'
OUT = '/home/monster-pc/projects/drainflow/images/icons'
os.makedirs(OUT, exist_ok=True)
TILE = 76  # real site icon size

def process(path):
    src = Image.open(path).convert('RGB')
    a = np.array(src).astype(int)
    mn = a.min(axis=2)
    nearwhite = mn > 215
    # exclude fully-dark rows (phone status bars), if any
    darkfrac = ((a < 60).all(axis=2)).mean(axis=1)
    bad = darkfrac > 0.5
    nw = nearwhite.copy()
    nw[bad, :] = True  # treat strip rows as "background"
    row_nw = nw.mean(axis=1)
    content_rows = np.where(row_nw < 0.9)[0]
    if len(content_rows) == 0:
        return None
    y0, y1 = int(content_rows.min()), int(content_rows.max())
    col_nw = nw[y0:y1 + 1].mean(axis=0)
    xs = np.where(col_nw < 0.98)[0]
    x0, x1 = int(xs.min()), int(xs.max())
    pad = 4
    crop = src.crop((max(0, x0 - pad), max(0, y0 - pad),
                     min(src.width, x1 + 1 + pad), min(src.height, y1 + 1 + pad)))
    c = np.array(crop.convert('RGBA'))
    c[(c[:, :, 0] > 235) & (c[:, :, 1] > 235) & (c[:, :, 2] > 235), 3] = 0
    emblem = Image.fromarray(c)
    side = max(emblem.size)
    sq = Image.new('RGBA', (side, side), (0, 0, 0, 0))
    sq.alpha_composite(emblem, ((side - emblem.width) // 2, (side - emblem.height) // 2))
    return sq, (x0 == 0 or y0 <= (5 if src.height > 1000 else -1))

tiles = []
for name, label in JOBS:
    p = os.path.join(CACHE, name + '.jpg')
    res = process(p)
    sq, clipped = res
    e = sq.resize((TILE, TILE), Image.LANCZOS)
    card = Image.new('RGBA', (TILE + 36, TILE + 36), (14, 23, 16, 255))
    card.alpha_composite(Image.new('RGBA', card.size, (57, 255, 20, 20)))
    card.alpha_composite(e, (18, 18))
    tiles.append((card.convert('RGB'), label, clipped))
    # save production assets (2x for retina)
    sq.resize((TILE * 2, TILE * 2), Image.LANCZOS).convert('RGBA').save(
        os.path.join(OUT, f'icon-{label.split("(")[0].lower().replace(" ", "-").replace("&", "and")}.png'))

# preview grid: 3 columns x 2 rows, labels under each tile
font = ImageFont.load_default(size=15)
cols, rows = 3, 2
cw, ch = 300, 210
grid = Image.new('RGB', (cols * cw, rows * ch), (14, 23, 16))
d = ImageDraw.Draw(grid)
for i, (card, label, clipped) in enumerate(tiles):
    cx, cy = (i % cols) * cw, (i // cols) * ch
    grid.paste(card, (cx + (cw - card.width) // 2, cy + 16))
    text = label + ('  [clipped src]' if clipped else '')
    d.text((cx + 10, cy + ch - 30), text, fill=(102, 255, 68), font=font)
grid.save('/tmp/icons-all-tiles.png')
print('saved /tmp/icons-all-tiles.png', grid.size)
