import sys
from PIL import Image

BASE = "/ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/4_gen_paper_repo/_4_assemble_paper/paper/workspace/qa/"

for name in ["phone_full.png", "desktop_full.png"]:
    im = Image.open(BASE + name).convert("RGB")
    w, h = im.size
    px = im.load()
    print(f"=== {name} {w}x{h} ===")

    # 1. dominant colors
    colors = im.getcolors(maxcolors=w * h)
    colors.sort(reverse=True)
    print("top colors:", [(c, '#' + '%02x%02x%02x' % rgb) for c, rgb in colors[:5]])

    # 2. right-edge band (24 px) should be background only
    edge = im.crop((w - 24, 0, w, h))
    ec = edge.getcolors(maxcolors=24 * h)
    ec.sort(reverse=True)
    print("right-edge top colors:", [(c, '#' + '%02x%02x%02x' % rgb) for c, rgb in ec[:3]])

    # 3. ink density per horizontal band (dark pixels = text)
    dark = 0
    bands = []
    band_h = 120
    for y0 in range(0, h, band_h):
        band = im.crop((0, y0, w, min(y0 + band_h, h)))
        bp = band.getcolors(maxcolors=band.size[0] * band.size[1])
        d = sum(c for c, rgb in bp if sum(rgb) < 300) / band.size[0]
        bands.append(round(d, 1))
        dark += d
    print("dark-pixel density per 120px band:", bands)

    # 4. text-column margins: find min/max x of dark pixels per row-quartile
    for label, y0, y1 in [("top", 0, h // 4), ("mid", h // 2, 3 * h // 4), ("bottom", 3 * h // 4, h)]:
        xs = []
        for y in range(y0, min(y1, h), 3):
            for x in range(0, w, 2):
                r, g, b = px[x, y]
                if r + g + b < 300:
                    xs.append(x)
        if xs:
            print(f"content x-range in {label} quarter: {min(xs)}..{max(xs)} (page width {w})")
        else:
            print(f"content x-range in {label} quarter: EMPTY")