"""Build the GitHub social card from the approved DJ Bandit hero artwork."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "site/assets/dj-bandit-hero.png"
OUTPUT = ROOT / "site/assets/dj-bandit-social.png"
WIDTH, HEIGHT = 1200, 630
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


def main() -> None:
    hero = Image.open(SOURCE).convert("RGB")
    scale = max(WIDTH / hero.width, HEIGHT / hero.height)
    hero = hero.resize((round(hero.width * scale), round(hero.height * scale)), Image.Resampling.LANCZOS)
    left = hero.width - WIDTH
    card = hero.crop((left, 0, left + WIDTH, HEIGHT)).convert("RGBA")

    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (4, 11, 23, 0))
    pixels = overlay.load()
    for x in range(WIDTH):
        strength = max(0, min(235, int(235 * (1 - x / 690))))
        for y in range(HEIGHT):
            pixels[x, y] = (4, 11, 23, strength)
    card.alpha_composite(overlay)

    draw = ImageDraw.Draw(card)
    draw.rectangle((52, 54, 57, 118), fill=(110, 216, 255, 255))
    draw.text((76, 54), "CODEX PET COLLECTIVE", font=font(FONT_BOLD, 20), fill=(244, 242, 235, 255))
    draw.text((76, 84), "OPEN SOURCE PETS FOR CODEX", font=font(FONT_REGULAR, 13), fill=(161, 184, 208, 255))
    draw.text((55, 228), "DJ", font=font(FONT_BOLD, 110), fill=(244, 242, 235, 255))
    draw.text((55, 334), "BANDIT", font=font(FONT_BOLD, 110), fill=(255, 114, 191, 255))
    draw.text((60, 477), "SCRATCH · DANCE · BACKWARD MOONWALK", font=font(FONT_BOLD, 16), fill=(110, 216, 255, 255))
    draw.text((60, 552), "CREATED BY OMAR TAVAREZ  /  DESIGNEDBYOMAR.COM", font=font(FONT_REGULAR, 13), fill=(244, 242, 235, 235))
    card.convert("RGB").save(OUTPUT, quality=92)


if __name__ == "__main__":
    main()
