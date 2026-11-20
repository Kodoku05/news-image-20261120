"""Render the front page to entry.png with Pillow.

The news itself lives in news.py; this file only draws it, so the page
can be refreshed by editing news.py and re-running this script.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from news import (
    DATE_LINE,
    FOOTER_LINES,
    LEAD_DECK,
    LEAD_TITLE,
    MASTHEAD,
    STORIES,
)


SIZE = 1024
MARGIN = 44
RIGHT = SIZE - MARGIN
PAPER = "#f7f3ea"
NAVY = "#101f34"
RED = "#bc332c"
RULE = "#b8b4ad"


def font_files():
    root = Path("/usr/share/fonts/truetype")
    for directory, regular, bold in (
        ("dejavu", "DejaVuSans.ttf", "DejaVuSans-Bold.ttf"),
        ("noto", "NotoSans-Regular.ttf", "NotoSans-Bold.ttf"),
    ):
        pair = root / directory / regular, root / directory / bold
        if all(path.is_file() for path in pair):
            return pair
    raise FileNotFoundError("DejaVu Sans or Noto Sans is required")


def wrap(draw, text, font, width):
    def fits(line):
        left, _, right, _ = draw.textbbox((0, 0), line, font=font, anchor="la")
        return right - min(left, 0) <= width

    lines = []
    line = ""
    for word in text.split():
        candidate = f"{line} {word}" if line else word
        if fits(candidate):
            line = candidate
        else:
            if not line or not fits(word):
                raise ValueError(f"Word does not fit in column: {word}")
            lines.append(line)
            line = word
    return [*lines, line]


def block(draw, text, font, x, y, width, leading, fill=NAVY, centered=False):
    """Draw wrapped lines on a fixed rhythm and return the bottom of the ink."""
    bottom = y
    for line in wrap(draw, text, font, width):
        anchor = "ma" if centered else "la"
        left = draw.textbbox((0, 0), line, font=font, anchor=anchor)[0]
        position = (x + (width // 2 if centered else -min(left, 0)), y)
        bounds = draw.textbbox(position, line, font=font, anchor=anchor)
        if bounds[0] < x or bounds[2] > x + width or bounds[3] > SIZE:
            raise ValueError(f"Text exceeds its bounds: {line}")
        draw.text(position, line, font=font, fill=fill, anchor=anchor)
        bottom = bounds[3]
        y += leading
    return bottom


def render():
    regular, bold = font_files()
    masthead = ImageFont.truetype(bold, 69)
    date = ImageFont.truetype(bold, 32)
    lead = ImageFont.truetype(bold, 53)
    lead_deck = ImageFont.truetype(regular, 24)
    headline = ImageFont.truetype(bold, 30)
    deck = ImageFont.truetype(regular, 20)
    footer = ImageFont.truetype(regular, 17)

    image = Image.new("RGB", (SIZE, SIZE), PAPER)
    draw = ImageDraw.Draw(image)
    width = RIGHT - MARGIN
    draw.rectangle((0, 0, SIZE - 1, 130), fill=NAVY)
    block(draw, MASTHEAD, masthead, MARGIN, 0, width, 75, PAPER, True)
    block(draw, DATE_LINE, date, MARGIN, 80, width, 38, PAPER, True)
    draw.rectangle((0, 131, SIZE - 1, 136), fill=RED)

    lead_bottom = block(draw, LEAD_TITLE, lead, MARGIN, 143, width, 55)
    deck_bottom = block(draw, LEAD_DECK, lead_deck, MARGIN, lead_bottom + 5,
                        width, 29)

    gutter = 34
    column = (width - gutter) // 2
    y = deck_bottom + 15
    for i in range(0, len(STORIES), 2):
        row = STORIES[i:i + 2]
        draw.line((MARGIN, y, RIGHT, y), fill=RED if i == 0 else RULE,
                  width=3 if i == 0 else 1)
        bottoms = []
        for j, (title, summary) in enumerate(row):
            x = MARGIN + j * (column + gutter)
            cell_width = column if len(row) == 2 else width
            title_bottom = block(draw, title, headline, x, y + 7, cell_width, 34)
            bottoms.append(block(draw, summary, deck, x, title_bottom + 2,
                                 cell_width, 25))
        if len(row) == 2:
            mid = SIZE // 2
            draw.line((mid, y + 11, mid, max(bottoms)), fill=RULE)
        y = max(bottoms) + 10

    footer_top = 950
    if y > footer_top:
        raise ValueError(f"Story grid overlaps footer: {y} > {footer_top}")
    draw.rectangle((0, footer_top, SIZE - 1, SIZE - 1), fill=NAVY)
    draw.rectangle((0, footer_top, SIZE - 1, footer_top + 3), fill=RED)
    block(draw, FOOTER_LINES[0], footer, MARGIN, 961, width, 22, PAPER, True)
    block(draw, FOOTER_LINES[1], footer, MARGIN, 984, width, 22, PAPER, True)
    image.save(Path(__file__).with_name("entry.png"), optimize=True)


if __name__ == "__main__":
    render()
