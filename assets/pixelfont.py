#!/usr/bin/env python3
"""Shared pixel-font and CRT-panel drawing used by the profile SVG generators.

Text is drawn as 5x7 glyphs on an 8x8 cell grid, the way a TMS9918A pattern
table works, and coloured from the 15 palette entries the VDP actually has.
No web fonts, no third-party badge services: the SVGs are self-contained.
"""

# TMS9918A palette, from vrEmuTms9918/src/vrEmuTms9918Util.c
PAL = {
    "black":        "#000000",
    "med_green":    "#21c942",
    "light_green":  "#5edc78",
    "dark_blue":    "#5455ed",
    "light_blue":   "#7d75fc",
    "dark_red":     "#d3524d",
    "cyan":         "#43ebf6",
    "med_red":      "#fd5554",
    "light_red":    "#ff7978",
    "dark_yellow":  "#d3c153",
    "light_yellow": "#e5ce80",
    "dark_green":   "#21b03c",
    "magenta":      "#c95bba",
    "grey":         "#cccccc",
    "white":        "#ffffff",
}

# Palette order as the VDP sees it. Colour 0 is transparent, so it is omitted.
PAL_BAR = [
    PAL["black"], PAL["med_green"], PAL["light_green"], PAL["dark_blue"],
    PAL["light_blue"], PAL["dark_red"], PAL["cyan"], PAL["med_red"],
    PAL["light_red"], PAL["dark_yellow"], PAL["light_yellow"],
    PAL["dark_green"], PAL["magenta"], PAL["grey"], PAL["white"],
]

FONT = {
    "A": (".###.", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"),
    "B": ("####.", "#...#", "#...#", "####.", "#...#", "#...#", "####."),
    "C": (".###.", "#...#", "#....", "#....", "#....", "#...#", ".###."),
    "D": ("####.", "#...#", "#...#", "#...#", "#...#", "#...#", "####."),
    "E": ("#####", "#....", "#....", "####.", "#....", "#....", "#####"),
    "F": ("#####", "#....", "#....", "####.", "#....", "#....", "#...."),
    "G": (".###.", "#...#", "#....", "#.###", "#...#", "#...#", ".###."),
    "H": ("#...#", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"),
    "I": ("#####", "..#..", "..#..", "..#..", "..#..", "..#..", "#####"),
    "J": ("..###", "...#.", "...#.", "...#.", "...#.", "#..#.", ".##.."),
    "K": ("#...#", "#..#.", "#.#..", "##...", "#.#..", "#..#.", "#...#"),
    "L": ("#....", "#....", "#....", "#....", "#....", "#....", "#####"),
    "M": ("#...#", "##.##", "#.#.#", "#...#", "#...#", "#...#", "#...#"),
    "N": ("#...#", "##..#", "#.#.#", "#..##", "#...#", "#...#", "#...#"),
    "O": (".###.", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."),
    "P": ("####.", "#...#", "#...#", "####.", "#....", "#....", "#...."),
    "Q": (".###.", "#...#", "#...#", "#...#", "#.#.#", "#..#.", ".##.#"),
    "R": ("####.", "#...#", "#...#", "####.", "#.#..", "#..#.", "#...#"),
    "S": (".####", "#....", "#....", ".###.", "....#", "....#", "####."),
    "T": ("#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."),
    "U": ("#...#", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."),
    "V": ("#...#", "#...#", "#...#", "#...#", "#...#", ".#.#.", "..#.."),
    "W": ("#...#", "#...#", "#...#", "#...#", "#.#.#", "##.##", "#...#"),
    "X": ("#...#", "#...#", ".#.#.", "..#..", ".#.#.", "#...#", "#...#"),
    "Y": ("#...#", "#...#", ".#.#.", "..#..", "..#..", "..#..", "..#.."),
    "Z": ("#####", "....#", "...#.", "..#..", ".#...", "#....", "#####"),
    "0": (".###.", "#...#", "#..##", "#.#.#", "##..#", "#...#", ".###."),
    "1": ("..#..", ".##..", "..#..", "..#..", "..#..", "..#..", ".###."),
    "2": (".###.", "#...#", "....#", "...#.", "..#..", ".#...", "#####"),
    "3": ("####.", "....#", "....#", ".###.", "....#", "....#", "####."),
    "4": ("...#.", "..##.", ".#.#.", "#..#.", "#####", "...#.", "...#."),
    "5": ("#####", "#....", "####.", "....#", "....#", "#...#", ".###."),
    "6": ("..##.", ".#...", "#....", "####.", "#...#", "#...#", ".###."),
    "7": ("#####", "....#", "...#.", "..#..", ".#...", ".#...", ".#..."),
    "8": (".###.", "#...#", "#...#", ".###.", "#...#", "#...#", ".###."),
    "9": (".###.", "#...#", "#...#", ".####", "....#", "...#.", ".##.."),
    " ": (".....", ".....", ".....", ".....", ".....", ".....", "....."),
    "-": (".....", ".....", ".....", "#####", ".....", ".....", "....."),
    ".": (".....", ".....", ".....", ".....", ".....", ".##..", ".##.."),
    ",": (".....", ".....", ".....", ".....", ".##..", ".##..", ".#..."),
    ":": (".....", ".##..", ".##..", ".....", ".##..", ".##..", "....."),
    "+": (".....", "..#..", "..#..", "#####", "..#..", "..#..", "....."),
    "%": ("##..#", "##.#.", "..#..", ".#...", "#..##", ".#.##", "....."),
    "/": ("....#", "....#", "...#.", "..#..", ".#...", "#....", "#...."),
    ">": ("#....", ".#...", "..#..", "...#.", "..#..", ".#...", "#...."),
    "'": ("..#..", "..#..", ".....", ".....", ".....", ".....", "....."),
}

# 8x8 sprite patterns, drawn on the sprite plane the way the VDP would.
SPRITES = {
    "ball": (
        "..####..", ".######.", "########", "########",
        "########", "########", ".######.", "..####..",
    ),
    "diamond": (
        "...##...", "..####..", ".######.", "########",
        "########", ".######.", "..####..", "...##...",
    ),
    "star": (
        "...##...", "...##...", "#.####.#", "########",
        "########", "#.####.#", "...##...", "...##...",
    ),
    "ring": (
        "..####..", ".#....#.", "#......#", "#......#",
        "#......#", "#......#", ".#....#.", "..####..",
    ),
}

GLYPH_W, GLYPH_H, ADVANCE = 5, 7, 6


def runs(rows):
    """Row-major run-length encode a pattern, merging identical runs vertically."""
    flat = []
    for y, row in enumerate(rows):
        x = 0
        while x < len(row):
            if row[x] == "#":
                w = 1
                while x + w < len(row) and row[x + w] == "#":
                    w += 1
                flat.append([x, y, w, 1])
                x += w
            else:
                x += 1
    flat.sort(key=lambda r: (r[0], r[2], r[1]))
    merged = []
    for x, y, w, h in flat:
        if merged:
            px, py, pw, ph = merged[-1]
            if px == x and pw == w and py + ph == y:
                merged[-1][3] += h
                continue
        merged.append([x, y, w, h])
    return merged


def rects(pattern, ox, oy, scale):
    return "".join(
        '<rect x="%d" y="%d" width="%d" height="%d"/>'
        % (ox + x * scale, oy + y * scale, w * scale, h * scale)
        for x, y, w, h in runs(pattern)
    )


def text(s, ox, oy, scale, colours, advance=ADVANCE):
    """Render s as pixel glyphs. colours is one colour or one per character."""
    if isinstance(colours, str):
        colours = [colours]
    parts = []
    for i, ch in enumerate(s.upper()):
        pattern = FONT.get(ch)
        if pattern is None:
            raise KeyError("no glyph for %r" % ch)
        body = rects(pattern, ox + i * advance * scale, oy, scale)
        if body:
            parts.append('<g fill="%s">%s</g>' % (colours[i % len(colours)], body))
    return "".join(parts)


def text_width(s, scale, advance=ADVANCE):
    if not s:
        return 0
    return (len(s) * advance - (advance - GLYPH_W)) * scale


def text_centred(s, cx, oy, scale, colours, advance=ADVANCE):
    return text(s, cx - text_width(s, scale, advance) // 2, oy, scale, colours, advance)


def text_right(s, rx, oy, scale, colours, advance=ADVANCE):
    return text(s, rx - text_width(s, scale, advance), oy, scale, colours, advance)


def grid(w, h, step=32, inset=12):
    return "".join(
        '<path d="M%d %dV%d"/>' % (x, inset, h - inset)
        for x in range(inset + step, w - inset, step)
    ) + "".join(
        '<path d="M%d %dH%d"/>' % (inset, y, w - inset)
        for y in range(inset + step, h - inset, step)
    )


PANEL_DEFS = """\
<clipPath id="screen"><rect x="10" y="10" width="{iw}" height="{ih}" rx="7"/></clipPath>
<pattern id="scan" width="4" height="3" patternUnits="userSpaceOnUse">
<rect width="4" height="1" fill="#000" opacity="0.55"/></pattern>
<radialGradient id="vig" cx="50%" cy="46%" r="72%">
<stop offset="55%" stop-color="#000" stop-opacity="0"/>
<stop offset="100%" stop-color="#000" stop-opacity="0.75"/></radialGradient>
<linearGradient id="band" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="#fff" stop-opacity="0"/>
<stop offset="50%" stop-color="#fff" stop-opacity="0.05"/>
<stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="gloss" x1="0" y1="0" x2="1" y2="0">
<stop offset="0%" stop-color="#fff" stop-opacity="0"/>
<stop offset="50%" stop-color="#fff" stop-opacity="0.22"/>
<stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>"""


def panel(w, h, body, css=(), label="", extra_defs=""):
    """Wrap body in the standard CRT panel: bezel, cell grid, vignette, scanlines.

    body is drawn clipped to the screen area, beneath the CRT overlays.
    """
    css = list(css) + [
        "@keyframes roll{from{transform:translateY(-70px)}"
        "to{transform:translateY(%dpx)}}" % (h + 10),
        ".roll{animation:roll 7s linear infinite}",
    ]
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" \
width="{w}" height="{h}" role="img" aria-label="{label}">
<title>{label}</title>
<defs>
<style>{css}</style>
{defs}{extra}
</defs>
<rect width="{w}" height="{h}" rx="11" fill="#05070a"/>
<rect x="6" y="6" width="{ow}" height="{oh}" rx="8" fill="none" stroke="{green}" \
stroke-opacity="0.22" stroke-width="1"/>
<g clip-path="url(#screen)">
<rect x="10" y="10" width="{iw}" height="{ih}" fill="#000"/>
<g stroke="{green}" stroke-opacity="0.07" stroke-width="1" fill="none">{grid}</g>
{body}
<rect x="10" y="10" width="{iw}" height="{ih}" fill="url(#vig)"/>
<g class="roll"><rect x="10" y="0" width="{iw}" height="70" fill="url(#band)"/></g>
<rect x="10" y="10" width="{iw}" height="{ih}" fill="url(#scan)"/>
</g>
</svg>
""".format(
        w=w, h=h, ow=w - 12, oh=h - 12, iw=w - 20, ih=h - 20,
        css="".join(css), defs=PANEL_DEFS.format(iw=w - 20, ih=h - 20),
        extra=extra_defs, label=label, green=PAL["med_green"],
        grid=grid(w, h), body=body,
    )


def write(path, data):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(data)
    print("wrote %s (%d bytes)" % (path, len(data.encode("utf-8"))))
