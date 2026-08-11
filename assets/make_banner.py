#!/usr/bin/env python3
"""Generate banner.svg and divider.svg for the visrealm profile README.

    python assets/make_banner.py
"""

import os

from pixelfont import PAL, PAL_BAR, SPRITES, panel, rects, text, text_right, write

W, H = 880, 260
MARGIN = 56

TITLE = "VISREALM"
TITLE_SCALE = 8
TITLE_X, TITLE_Y = MARGIN, 52

# One palette colour per letter, sweeping cool to warm. The two darkest
# entries (black, dark blue) are skipped: they vanish against the screen.
TITLE_COLOURS = [
    PAL["med_green"], PAL["light_green"], PAL["cyan"], PAL["light_blue"],
    PAL["magenta"], PAL["light_red"], PAL["light_yellow"], PAL["white"],
]

SUB = "TROY SCHRAPEL"
TAG = "RETRO COMPUTING - HARDWARE EMULATION"
LOC = "SOUTH AUSTRALIA"
SPEC = ("TMS9918A VDP", "256 X 192 / 15 COLOURS", "32 SPRITES / 4 PER LINE")

BAR_Y, BAR_H, BAR_CELL = 222, 14, 51
RIGHT = 821


def sprite_band(css, y, scale, entries):
    """entries: (sprite, colour, duration, delay, right_to_left)"""
    out = []
    for i, (name, colour, dur, delay, rev) in enumerate(entries):
        frm, to = (W, -8 * scale) if rev else (-8 * scale, W)
        cls = "r%d" % i if rev else "s%d" % i
        css.append(
            "@keyframes %s{from{transform:translateX(%dpx)}"
            "to{transform:translateX(%dpx)}}"
            ".%s{animation:%s %.1fs linear %.1fs infinite}"
            % (cls, frm, to, cls, cls, dur, delay)
        )
        out.append(
            '<g class="%s" fill="%s">%s</g>'
            % (cls, colour, rects(SPRITES[name], 0, y, scale))
        )
    return "".join(out)


def build_banner():
    css = [
        "@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}",
        ".cur{animation:blink 1.06s steps(1,end) infinite}",
        "@keyframes sweep{from{transform:translateX(-160px)}"
        "to{transform:translateX(%dpx)}}" % (W + 20),
        ".sweep{animation:sweep 5.5s ease-in-out infinite}",
    ]

    sprites = sprite_band(css, 22, 3, [
        ("ball", PAL["cyan"], 17.0, 0.0, False),
        ("diamond", PAL["magenta"], 23.0, 4.0, False),
        ("star", PAL["light_yellow"], 29.0, 11.0, False),
    ]) + sprite_band(css, 190, 3, [
        ("ring", PAL["light_green"], 21.0, 2.0, True),
        ("ball", PAL["light_red"], 27.0, 9.0, True),
    ])

    # Stroked, so colour 1 (black) still reads as a cell against the screen.
    bar = '<g stroke="%s" stroke-opacity="0.3">%s</g>' % (PAL["grey"], "".join(
        '<rect x="%d" y="%d" width="%d" height="%d" fill="%s"/>'
        % (MARGIN + i * BAR_CELL, BAR_Y, BAR_CELL - 3, BAR_H, c)
        for i, c in enumerate(PAL_BAR)
    ))

    cursor_x = TITLE_X + len(TITLE) * 6 * TITLE_SCALE
    cursor_y = TITLE_Y + 7 * TITLE_SCALE

    body = "".join([
        sprites,
        text(TITLE, TITLE_X, TITLE_Y, TITLE_SCALE, TITLE_COLOURS),
        '<rect class="cur" x="%d" y="%d" width="%d" height="%d" fill="%s"/>'
        % (cursor_x, cursor_y, 5 * TITLE_SCALE, TITLE_SCALE, PAL["grey"]),
        '<g opacity="0.5">%s</g>' % "".join(
            text_right(line, RIGHT, 56 + i * 22, 2, PAL["grey"])
            for i, line in enumerate(SPEC)
        ),
        text(SUB, MARGIN + 2, 132, 3, PAL["white"]),
        text(TAG, MARGIN + 2, 168, 2, PAL["med_green"]),
        text_right(LOC, RIGHT, 194, 2, PAL["dark_yellow"]),
        bar,
        '<g class="sweep"><rect x="0" y="%d" width="160" height="%d" '
        'fill="url(#gloss)"/></g>' % (BAR_Y, BAR_H),
    ])

    return panel(
        W, H, body, css,
        label="visrealm - Troy Schrapel - retro computing and hardware emulation",
    )


def build_divider():
    cell = 58
    cells = "".join(
        '<rect x="%.1f" y="0.5" width="%d" height="7" fill="%s"/>'
        % (i * cell + 0.5, cell - 3, c)
        for i, c in enumerate(PAL_BAR)
    )
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 870 8" '
        'width="870" height="8" role="img" aria-label="TMS9918A palette">'
        '<g stroke="%s" stroke-opacity="0.35" stroke-width="1">%s</g>'
        "</svg>\n" % (PAL["grey"], cells)
    )


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    write(os.path.join(here, "banner.svg"), build_banner())
    write(os.path.join(here, "divider.svg"), build_divider())


if __name__ == "__main__":
    main()
