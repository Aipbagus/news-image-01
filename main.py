#!/usr/bin/env python3
"""news-image-01 — front page of the world, Friday 13 November 2026.

Deterministic programmatic illustration (PIL). No network access.
Running `python main.py` writes the image to /output/entry.png;
two runs produce byte-identical files.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.png")

# --------------------------------------------------------------- palette ---
INK        = (18, 18, 24)      # near-black paper edge / rules
PAPER      = (242, 237, 225)   # newsprint cream
RUSSIA_RED = (178, 34, 34)
USA_BLUE   = (28, 60, 114)
MIDEAST    = (196, 130, 32)    # desert amber
GREEN      = (34, 110, 66)
GREY       = (110, 106, 96)
TECH       = (90, 96, 110)

def load_font(size, bold=False):
    for name in (["DejaVuSans-Bold.ttf", "DejaVuSans.ttf"] if bold else ["DejaVuSans.ttf"]):
        p = os.path.join("/usr/share/fonts/truetype/dejavu", name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def draw_text(d, xy, text, size, fill, anchor="la", bold=False, tracking=0):
    f = load_font(size, bold)
    if tracking == 0:
        d.text(xy, text, font=f, fill=fill, anchor=anchor)
        return
    # letter-spaced text (for kickers), anchored at left baseline
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill, anchor="ls")
        x += d.textlength(ch, font=f) + tracking

# ---------------------------------------------------------------- drawing ---
def build():
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img)

    # paper margin
    d.rectangle([14, 14, W - 14, H - 14], fill=PAPER)
    mx0, mx1 = 52, W - 52

    # ------------------------------------------------ masthead -------------
    draw_text(d, ((W - 6) // 2, 44), "FRIDAY, NOVEMBER 13, 2026", 24, INK,
              anchor="ms", bold=True, tracking=2)
    draw_text(d, ((W - 6) // 2, 112), "THE WORLD IN ONE DAY", 56, INK,
              anchor="ms", bold=True)
    d.line([mx0, 148, mx1, 148], fill=INK, width=5)
    d.line([mx0, 156, mx1, 156], fill=INK, width=2)

    # --------------------------------------------------- main story --------
    # Ukraine–Russia war: mass drone strikes (lead visual, top-left)
    s = 420  # square panel, 52..472 x 176..596
    px0, py0 = mx0, 176
    d.rectangle([px0, py0, px0 + s, py0 + s], fill=(28, 32, 52))
    # night sky gradient bands
    for i, c in enumerate([(40, 46, 72), (30, 35, 58), (22, 26, 44)]):
        d.rectangle([px0, py0 + i * s // 3, px0 + s, py0 + (i + 1) * s // 3], fill=c)
    # tracer arcs (deterministic positions)
    for x0, y0, x1, y1 in [(60, 300, 200, 160), (120, 330, 260, 200),
                           (180, 360, 330, 250), (90, 250, 190, 190),
                           (240, 340, 380, 270)]:
        d.line([px0 + x0, py0 + y0, px0 + x1, py0 + y1], fill=(230, 180, 90), width=4)
    # exploding drones
    for x, y in [(200, 160), (260, 200), (330, 250), (190, 190), (380, 270)]:
        d.ellipse([px0 + x - 14, py0 + y - 14, px0 + x + 14, py0 + y + 14],
                  fill=(240, 150, 60))
        d.ellipse([px0 + x - 6, py0 + y - 6, px0 + x + 6, py0 + y + 6],
                  fill=(255, 230, 180))
    # refinery on fire, bottom of panel
    fx, fy = px0 + 90, py0 + s - 96
    for dx, h in [(0, 90), (50, 70), (100, 100), (150, 80)]:
        d.rectangle([fx + dx, fy + 40 - h // 2, fx + dx + 34, fy + 40 + h // 2],
                    fill=(60, 64, 80))
        # flame
        d.polygon([(fx + dx + 17, fy - h // 2 + 8), (fx + dx + 5, fy - h // 2 + 44),
                   (fx + dx + 29, fy - h // 2 + 44)], fill=(235, 120, 40))
        d.polygon([(fx + dx + 17, fy - h // 2 + 22), (fx + dx + 9, fy - h // 2 + 44),
                   (fx + dx + 25, fy - h // 2 + 44)], fill=(250, 190, 70))
    d.rectangle([px0, py0 + s - 20, px0 + s, py0 + s], fill=(40, 44, 60))  # ground
    draw_text(d, (px0 + 16, py0 + 24), "1,200 DRONES", 34, (240, 235, 220),
              bold=True)
    draw_text(d, (px0 + 16, py0 + 62), "OVER RUSSIA", 34, (240, 235, 220), bold=True)

    # headline + deck under the panel
    draw_text(d, (mx0, 620), "MASS DRONE WAR", 52, INK, bold=True)
    draw_text(d, (mx0, 678), "Largest air exchange of the war; oil refineries", 27, GREY)
    draw_text(d, (mx0, 710), "burn; envoys head to Moscow as POW swap agreed", 27, GREY)

    # --------------------------------------------- right-hand story stack --
    rx0 = mx0 + s + 34
    rx1 = mx1
    rw = rx1 - rx0
    # US–Iran confrontation
    d.rectangle([rx0, 176, rx1, 386], fill=USA_BLUE)
    # US / Iran halves
    d.rectangle([rx0, 176, rx0 + rw // 2, 386], fill=USA_BLUE)
    d.rectangle([rx0 + rw // 2, 176, rx1, 386], fill=MIDEAST)
    draw_text(d, (rx0 + rw // 2 - 62, 268), "IRAN", 44, PAPER, anchor="ms", bold=True)
    # star + flag stripes on US half
    d.rectangle([rx0 + 26, 200, rx0 + 58, 232], fill=PAPER)
    for i in range(3):
        d.rectangle([rx0 + 26, 200 + i * 12, rx0 + 58, 206 + i * 12], fill=USA_BLUE)
    for i in range(4):
        d.rectangle([rx0 + 26, 244 + i * 16, rx0 + 58, 252 + i * 16], fill=USA_BLUE)
    for i in range(4):
        d.rectangle([rx0 + 26, 312 + i * 14, rx0 + 58, 318 + i * 14], fill=(120, 160, 90))
    draw_text(d, (rx0 + 42, 340), "USA", 40, PAPER, anchor="ms", bold=True)
    draw_text(d, (rx0 + 20, 172), "GULF", 34, (18, 18, 24), bold=True)
    draw_text(d, (rx0 + 16, 174), "", 1, PAPER)  # no-op keep layout
    # US-Russia diplomacy chip
    d.rectangle([rx0, 404, rx1, 470], fill=(214, 208, 192))
    draw_text(d, (rx0 + 18, 424), "PEACE ENVOYS", 26, INK, bold=True)
    draw_text(d, (rx0 + 18, 450), "IN MOSCOW", 26, INK, bold=True)

    # Nvidia CEO resigns (tech grey panel)
    d.rectangle([rx0, 488, rx1, 610], fill=TECH)
    # stylised chip
    cx, cy = rx0 + rw // 2, 540
    d.rectangle([cx - 46, cy - 46, cx + 46, cy + 46], fill=(60, 64, 78))
    d.rectangle([cx - 30, cy - 30, cx + 30, cy + 30], fill=(150, 200, 120))
    for i in range(-2, 3):
        d.rectangle([cx - 60, cy + i * 20 - 3, cx - 46, cy + i * 20 + 3], fill=(30, 32, 40))
        d.rectangle([cx + 46, cy + i * 20 - 3, cx + 60, cy + i * 20 + 3], fill=(30, 32, 40))
    draw_text(d, (rx0 + 16, 490), "NVIDIA", 30, (235, 232, 224), bold=True)
    draw_text(d, (rx0 + 16, 574), "CEO QUITS", 30, (235, 232, 224), bold=True)

    # -------------------------------------------------- bottom strip -------
    by0, by1 = 760, 770
    d.line([mx0, by0, mx1, by0], fill=INK, width=3)

    # Trump/Cuba (blue block, left)
    d.rectangle([mx0, by1, mx0 + 268, 880], fill=USA_BLUE)
    draw_text(d, (mx0 + 18, 806), "TRUMP: \"GET", 30, PAPER, bold=True)
    draw_text(d, (mx0 + 18, 840), "CUBA DONE\"", 30, PAPER, bold=True)

    # Microsoft outage (grey, middle)
    d.rectangle([mx0 + 292, by1, mx0 + 292 + 268, 880], fill=TECH)
    # four-pane window logo
    lx, ly = mx0 + 316, 806
    for ox, oy, c in [(0, 0, (244, 114, 40)), (24, 0, (120, 190, 70)),
                      (0, 24, (70, 150, 220)), (24, 24, (240, 90, 90))]:
        d.rectangle([lx + ox, ly + oy, lx + ox + 18, ly + oy + 18], fill=c)
    draw_text(d, (mx0 + 372, 822), "MICROSOFT", 26, PAPER, bold=True)
    draw_text(d, (mx0 + 372, 848), "OUTAGE", 26, PAPER, bold=True)

    # Delhi smog (hazardous, right)
    d.rectangle([mx0 + 584, by1, mx1, 880], fill=(150, 130, 60))
    # smog layers + city silhouette
    for i, c in enumerate([(120, 108, 60), (135, 120, 68), (150, 134, 78)]):
        d.rectangle([mx0 + 584, 806 + i * 24, mx1, 830 + i * 24], fill=c)
    for x, w, h in [(40, 26, 60), (78, 20, 44), (108, 30, 70), (150, 22, 52)]:
        d.rectangle([mx0 + 584 + x, 880 - h, mx0 + 584 + x + w, 880], fill=(70, 62, 40))
    draw_text(d, (mx0 + 600, 816), "DELHI SMOG", 30, (30, 26, 16), bold=True)
    draw_text(d, (mx0 + 600, 848), "#1 POLLUTED", 30, (30, 26, 16), bold=True)

    # ------------------------------------------------- footer wires --------
    d.line([mx0, 898, mx1, 898], fill=INK, width=3)
    wires = [
        ("US-IRAN", "Trump: strikes \"no hesitation\"; tanker hits in Gulf", RUSSIA_RED),
        ("MIDEAST", "Houthi drones on Saudi oil lines; radar duel in Bahrain", MIDEAST),
        ("GAZA", "Israeli strikes kill 11; 53 states demand access", GREEN),
        ("INDIA", "US-India trade deal nears finish line", TECH),
    ]
    y = 908
    for tag, text, color in wires:
        d.rectangle([mx0, y - 12, mx0 + 104, y + 12], fill=color)
        draw_text(d, (mx0 + 52, y + 5), tag, 18, PAPER, anchor="mm", bold=True)
        draw_text(d, (mx0 + 118, y + 5), text, 19, INK, anchor="lm")
        y += 26

    # page number / edition line
    draw_text(d, (mx0, 1002), "No. 317 — make.fun news-image-01", 16, GREY, anchor="lm")
    draw_text(d, (mx1, 1002), "AI-generated front page", 16, GREY, anchor="rm")

    return img

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    img = build()
    img.save(OUT_PATH, "PNG", optimize=True)

if __name__ == "__main__":
    main()
