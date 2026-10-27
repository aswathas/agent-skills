#!/usr/bin/env python3
"""Render a branded 1200x1200 card for a LinkedIn AI-news post.

The image is generated locally from the headline, so there is no publisher
artwork to licence and no external image API to fail at 09:00. Defaults are
tuned for a dark feed; pass --light for a light card.

    python make-card.py --headline "OpenAI ships ..." --source "The Verge" --out card.png
"""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SIZE = 1200
MARGIN = 84
ACCENT = (40, 90, 255)
INK = (245, 247, 250)
MUTED = (138, 147, 163)
BG_TOP = (10, 12, 17)
BG_BOTTOM = (20, 26, 38)
LIGHT_BG = (247, 248, 251)
LIGHT_INK = (16, 19, 26)
LIGHT_MUTED = (90, 98, 112)

FONT_CANDIDATES = [
    ("C:/Windows/Fonts/seguisb.ttf", "C:/Windows/Fonts/segoeui.ttf"),
    ("C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/segoeui.ttf"),
    ("C:/Windows/Fonts/arialbd.ttf", "C:/Windows/Fonts/arial.ttf"),
    ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ("/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/System/Library/Fonts/Supplemental/Arial.ttf"),
]


def load_fonts() -> tuple[str | None, str | None]:
    for bold, regular in FONT_CANDIDATES:
        if Path(bold).exists():
            return bold, regular if Path(regular).exists() else bold
    return None, None


def font(path: str | None, size: int) -> ImageFont.FreeTypeFont:
    if path:
        return ImageFont.truetype(path, size)
    return ImageFont.load_default(size=size)


def gradient(top: tuple[int, int, int], bottom: tuple[int, int, int]) -> Image.Image:
    img = Image.new("RGB", (SIZE, SIZE), top)
    draw = ImageDraw.Draw(img)
    for y in range(SIZE):
        t = y / (SIZE - 1)
        color = tuple(round(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        draw.line([(0, y), (SIZE, y)], fill=color)
    return img


def tracked(draw: ImageDraw.ImageDraw, xy, text: str, f, fill, tracking: int) -> int:
    """Draw text with letter spacing; returns the width used."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=f, fill=fill)
        x += draw.textlength(ch, font=f) + tracking
    return int(x - xy[0])


def wrap(draw: ImageDraw.ImageDraw, text: str, f, max_width: int) -> list[str]:
    words, lines, line = text.split(), [], ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if draw.textlength(candidate, font=f) <= max_width or not line:
            line = candidate
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def fit_headline(draw, text: str, bold: str | None, max_width: int, max_lines: int):
    for size in range(92, 43, -4):
        f = font(bold, size)
        lines = wrap(draw, text, f, max_width)
        if len(lines) <= max_lines:
            return f, lines, size
    f = font(bold, 44)
    return f, wrap(draw, text, f, max_width)[:max_lines], 44


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--headline", required=True)
    ap.add_argument("--source", default="")
    ap.add_argument("--kicker", default="GEN AI")
    ap.add_argument("--handle", default="@aswathas")
    ap.add_argument("--date", default="")
    ap.add_argument("--out", required=True)
    ap.add_argument("--light", action="store_true")
    args = ap.parse_args()

    bold, regular = load_fonts()
    bg = gradient(LIGHT_BG, (235, 238, 244)) if args.light else gradient(BG_TOP, BG_BOTTOM)
    ink = LIGHT_INK if args.light else INK
    muted = LIGHT_MUTED if args.light else MUTED

    draw = ImageDraw.Draw(bg)

    # A single soft accent plane keeps the card from reading as a plain slide.
    if not args.light:
        glow = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow)
        gdraw.ellipse([SIZE - 420, -260, SIZE + 260, 420], fill=(40, 90, 255, 38))
        bg = Image.alpha_composite(bg.convert("RGBA"), glow).convert("RGB")
        draw = ImageDraw.Draw(bg)

    # Top rail: accent tick + kicker on the left, date on the right.
    draw.rectangle([MARGIN, MARGIN, MARGIN + 34, MARGIN + 6], fill=ACCENT)
    kicker_font = font(bold, 26)
    tracked(draw, (MARGIN + 48, MARGIN - 8), args.kicker.upper(), kicker_font, ACCENT, 3)

    date_text = args.date or dt.date.today().strftime("%d %b %Y").upper()
    date_font = font(regular, 24)
    dw = draw.textlength(date_text, font=date_font)
    draw.text((SIZE - MARGIN - dw, MARGIN - 6), date_text, font=date_font, fill=muted)

    # Headline.
    max_width = SIZE - MARGIN * 2
    f, lines, _ = fit_headline(draw, args.headline, bold, max_width, max_lines=6)
    line_height = int(f.size * 1.14)
    block_h = line_height * len(lines)
    y = (SIZE - block_h) // 2 - 40
    for line in lines:
        draw.text((MARGIN, y), line, font=f, fill=ink)
        y += line_height

    # Accent rule under the headline.
    rule_y = y + 42
    draw.rectangle([MARGIN, rule_y, MARGIN + 96, rule_y + 5], fill=ACCENT)

    # Footer: source on the left, handle on the right.
    foot_font = font(regular, 24)
    if args.source:
        draw.text((MARGIN, SIZE - MARGIN - 20), args.source, font=foot_font, fill=muted)
    hw = draw.textlength(args.handle, font=foot_font)
    draw.text((SIZE - MARGIN - hw, SIZE - MARGIN - 20), args.handle, font=foot_font, fill=ACCENT)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    bg.save(out, "PNG", optimize=True)
    print(out)


if __name__ == "__main__":
    main()
