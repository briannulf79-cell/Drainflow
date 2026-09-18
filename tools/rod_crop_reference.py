from PIL import Image
import numpy as np

src = Image.open('/home/monster-pc/.hermes/cache/images/img_34ed774e937e.jpg').convert('RGB')
body = src.crop((0, 90, src.width, src.height - 100))
a = np.array(body).astype(int)
mx = a.max(axis=2); mn = a.min(axis=2); sat = mx - mn

darkfrac_rows = ((a < 60).all(axis=2)).mean(axis=1)
ok_rows = darkfrac_rows < 0.5
colorful = (sat > 40) & (mx > 60)
colorful[~ok_rows, :] = False
nonwhite = ~(mn > 215)
nonwhite[~ok_rows, :] = False

y0 = int(np.where(colorful.sum(axis=1) > 20)[0].min())
y1 = y0 + int(np.where(nonwhite[y0:].sum(axis=1) > 20)[0].max())
xs = np.where(nonwhite[y0:y1].sum(axis=0) > 10)[0]
x0, x1 = int(xs.min()), int(xs.max())
print('bbox', x0, y0, x1, y1, '| touches left edge:', x0 == 0, '| touches bottom:', y1 >= body.height - 3)

crop = body.crop((x0, y0, x1 + 1, y1 + 1))
print('crop', crop.size)
crop.save('/tmp/rodding_full.png')

c = np.array(crop.convert('RGBA'))
whiteish = (c[:, :, 0] > 235) & (c[:, :, 1] > 235) & (c[:, :, 2] > 235)
c[whiteish, 3] = 0
emblem = Image.fromarray(c)

side = max(emblem.size)
sq = Image.new('RGBA', (side, side), (0, 0, 0, 0))
sq.alpha_composite(emblem, ((side - emblem.width) // 2, (side - emblem.height) // 2))
sq.save('/tmp/rodding_transparent.png')

row = Image.new('RGB', (3 * 280, 340), (14, 23, 16))
for i, s in enumerate([64, 96, 128]):
    e = sq.resize((s, s), Image.LANCZOS)
    card = Image.new('RGBA', (s + 40, s + 40), (14, 23, 16, 255))
    card.alpha_composite(e, (20, 20))
    im = card.convert('RGB')
    row.paste(im, (i * 280 + (280 - im.width) // 2, (340 - im.height) // 2))
row.save('/tmp/rodding_scale_test.png')
print('saved scale test 840x340')
