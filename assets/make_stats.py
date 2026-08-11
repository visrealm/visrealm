#!/usr/bin/env python3
"""Generate stats.svg from live GitHub API data, in the same CRT panel style.

Self-hosted on purpose: the usual third-party stats-card services rate-limit
and go down, and a broken image on a profile page is worse than no image.
Refreshed by .github/workflows/stats.yml, which passes a token so the language
walk does not run into the 60/hour unauthenticated limit.

    python assets/make_stats.py [user]
"""

import json
import os
import sys
import urllib.error
import urllib.request

from pixelfont import PAL, panel, text, text_centred, text_right, text_width, write

USER = "visrealm"
API = "https://api.github.com"

W, H = 880, 214
MARGIN = 40
TILE_W = 200

# Languages are coloured from the palette rather than GitHub's own colours, so
# the panel stays inside the 15 the VDP has.
LANG_COLOURS = [
    PAL["med_green"], PAL["cyan"], PAL["light_blue"], PAL["magenta"],
    PAL["light_yellow"], PAL["light_red"], PAL["light_green"], PAL["dark_yellow"],
]
MAX_LANGS = 6


def api(path):
    req = urllib.request.Request(
        API + path,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "visrealm-profile-stats",
        },
    )
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        req.add_header("Authorization", "Bearer " + token)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def cache_path():
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".cache")
    if not os.path.isdir(d):
        os.makedirs(d)
    return os.path.join(d, "languages.json")


def load_cache():
    try:
        with open(cache_path(), encoding="utf-8") as f:
            return json.load(f)
    except (IOError, ValueError):
        return {}


def collect(user):
    profile = api("/users/%s" % user)

    repos, page = [], 1
    while True:
        batch = api("/users/%s/repos?per_page=100&page=%d" % (user, page))
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    own = [r for r in repos if not r["fork"]]
    stars = sum(r["stargazers_count"] for r in own)
    forks = sum(r["forks_count"] for r in own)

    # One /languages call per repo, cached against pushed_at so repeated local
    # runs stay well inside the 60/hour unauthenticated budget.
    cache = load_cache()
    langs, failed = {}, []
    for r in own:
        key = "%s@%s" % (r["full_name"], r["pushed_at"])
        if key not in cache:
            try:
                cache[key] = api("/repos/%s/languages" % r["full_name"])
            except urllib.error.HTTPError as e:
                failed.append("%s (HTTP %s)" % (r["name"], e.code))
                continue
        for name, size in cache[key].items():
            langs[name] = langs.get(name, 0) + size

    with open(cache_path(), "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=1, sort_keys=True)

    # Partial language data yields plausible-looking but wrong percentages, so
    # refuse to write the panel rather than publish them.
    if failed:
        raise SystemExit(
            "language data incomplete for %d repo(s): %s\n"
            "Set GITHUB_TOKEN to raise the rate limit, or retry after reset."
            % (len(failed), ", ".join(failed))
        )

    return {
        "followers": profile["followers"],
        "repos": len(own),
        "stars": stars,
        "forks": forks,
        "langs": sorted(langs.items(), key=lambda kv: -kv[1]),
    }


def thousands(n):
    return "{:,}".format(n)


def legend_labels(langs):
    total = sum(size for _, size in langs) or 1
    return [
        "%s %d%%" % (name.upper(), round(100.0 * size / total))
        for name, size in langs
    ]


def legend_width(langs, gap=20):
    """Swatch + label per entry, plus the inter-entry gaps."""
    labels = legend_labels(langs)
    return sum(14 + text_width(l, 2) for l in labels) + gap * (len(labels) - 1)


def build(data):
    tiles = [
        ("stars", thousands(data["stars"]), PAL["light_yellow"]),
        ("repos", thousands(data["repos"]), PAL["cyan"]),
        ("forks", thousands(data["forks"]), PAL["light_green"]),
        ("followers", thousands(data["followers"]), PAL["magenta"]),
    ]

    body = []
    for i, (label, value, colour) in enumerate(tiles):
        cx = MARGIN + i * TILE_W + TILE_W // 2
        body.append(text_centred(value, cx, 34, 4, colour))
        body.append(
            '<g opacity="0.55">%s</g>'
            % text_centred(label, cx, 76, 2, PAL["grey"])
        )
        if i:
            x = MARGIN + i * TILE_W
            body.append(
                '<path d="M%d 30V90" stroke="%s" stroke-opacity="0.16"/>'
                % (x, PAL["grey"])
            )

    bar_x, bar_y, bar_w, bar_h = MARGIN, 140, W - 2 * MARGIN, 18

    # Legend sits on one justified row, so drop languages until it fits.
    langs = data["langs"][:MAX_LANGS]
    while len(langs) > 2 and legend_width(langs) > bar_w:
        langs = langs[:-1]
    total = sum(size for _, size in langs) or 1

    body.append(text("languages", MARGIN, 116, 2, PAL["med_green"]))

    x, cells = bar_x, []
    for i, (_, size) in enumerate(langs):
        # Last cell takes the rounding slack so the bar always ends flush.
        w = (bar_x + bar_w - x) if i == len(langs) - 1 else int(bar_w * size / total)
        cells.append(
            '<rect x="%d" y="%d" width="%d" height="%d" fill="%s"/>'
            % (x, bar_y, max(w - 2, 1), bar_h, LANG_COLOURS[i % len(LANG_COLOURS)])
        )
        x += w
    body.append(
        '<g stroke="%s" stroke-opacity="0.3">%s</g>' % (PAL["grey"], "".join(cells))
    )

    labels = legend_labels(langs)
    gap = (bar_w - legend_width(langs, gap=0)) // max(len(labels) - 1, 1)
    legend, lx = [], MARGIN
    for i, label in enumerate(labels):
        legend.append(
            '<rect x="%d" y="176" width="8" height="8" fill="%s"/>'
            % (lx, LANG_COLOURS[i % len(LANG_COLOURS)])
        )
        legend.append(text(label, lx + 14, 176, 2, PAL["grey"]))
        lx += 14 + text_width(label, 2) + gap
    body.append("".join(legend))

    body.append(
        '<g opacity="0.4">%s</g>'
        % text_right("public repos, forks excluded", W - MARGIN, 116, 2, PAL["grey"])
    )

    return panel(W, H, "".join(body), label="visrealm GitHub statistics")


def main():
    user = sys.argv[1] if len(sys.argv) > 1 else USER
    data = collect(user)
    print("  stars=%d repos=%d forks=%d followers=%d" % (
        data["stars"], data["repos"], data["forks"], data["followers"]))
    print("  langs=%s" % ", ".join(n for n, _ in data["langs"][:MAX_LANGS]))
    here = os.path.dirname(os.path.abspath(__file__))
    write(os.path.join(here, "stats.svg"), build(data))


if __name__ == "__main__":
    main()
