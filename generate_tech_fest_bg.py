import math
from PIL import Image, ImageDraw, ImageFont

def create_tech_fest_background(out_path="cert_bg_tech_fest_vibe.png", width=2048, height=1364):
    # 1. Base canvas: crisp clean off-white/pearl with very subtle tech warmth
    # RGB (252, 253, 255)
    img = Image.new("RGBA", (width, height), (252, 253, 255, 255))
    draw = ImageDraw.Draw(img)

    # 2. Subtle Tech Grid / Dot Matrix in the background
    # Soft cyan-slate dots every 40px with low opacity
    grid_color = (210, 225, 240, 110)
    for y in range(80, height - 80, 40):
        for x in range(80, width - 80, 40):
            # Hex/circuit dot pattern
            if (x // 40 + y // 40) % 2 == 0:
                draw.ellipse([x - 1, y - 1, x + 1, y + 1], fill=grid_color)

    # 3. Very subtle central watermark: Cyber Circuit Ring / Tech Fest crest at low opacity
    wm_cx, wm_cy = width // 2, height // 2 + 30
    wm_color = (220, 232, 245, 90)
    wm_color_accent = (205, 222, 240, 120)
    for r in [280, 310, 360, 410]:
        draw.ellipse([wm_cx - r, wm_cy - r, wm_cx + r, wm_cy + r], outline=wm_color, width=2)
    # Hexagon outline
    hex_pts = []
    for i in range(6):
        angle = math.radians(60 * i + 30)
        hex_pts.append((wm_cx + 340 * math.cos(angle), wm_cy + 340 * math.sin(angle)))
    draw.polygon(hex_pts, outline=wm_color_accent, width=2)

    # Radials from center
    for i in range(12):
        angle = math.radians(30 * i)
        x1 = wm_cx + 280 * math.cos(angle)
        y1 = wm_cy + 280 * math.sin(angle)
        x2 = wm_cx + 360 * math.cos(angle)
        y2 = wm_cy + 360 * math.sin(angle)
        draw.line([(x1, y1), (x2, y2)], fill=wm_color, width=2)

    # 4. COLOR PALETTE
    COLOR_NAVY_DARK = (8, 18, 36, 255)       # #081224 Deep tech midnight
    COLOR_NAVY_MED  = (16, 32, 60, 255)      # #10203c
    COLOR_GOLD_RICH = (195, 150, 45, 255)    # #c3962d Polished metallic gold
    COLOR_GOLD_LIGHT= (230, 195, 95, 255)    # #e6c35f Bright gold accent
    COLOR_CYAN_NEON = (0, 180, 240, 255)     # #00b4f0 Electric cyber cyan
    COLOR_CYAN_SOFT = (0, 180, 240, 130)
    COLOR_SLATE     = (100, 120, 150, 255)

    # 5. OUTER BORDER SYSTEM
    # Outer dark midnight edge
    m1 = 28
    draw.rectangle([m1, m1, width - m1, height - m1], outline=COLOR_NAVY_DARK, width=12)

    # Gold pinstripe
    m2 = 45
    draw.rectangle([m2, m2, width - m2, height - m2], outline=COLOR_GOLD_RICH, width=3)

    # Electric Cyan hairline
    m3 = 54
    draw.rectangle([m3, m3, width - m3, height - m3], outline=COLOR_CYAN_NEON, width=1)

    # Inner subtle frame
    m4 = 66
    draw.rectangle([m4, m4, width - m4, height - m4], outline=(200, 215, 230, 255), width=1)

    # 6. HIGH-TECH CORNER BRACKETS & CIRCUIT TRACES
    # Kept compact in top corners so header zone (x:150 to W-150, y:60 to 220) is 100% open
    corner_size = 85
    chamfer = 32

    def draw_tech_corner(cx, cy, flip_x=False, flip_y=False):
        dx = -1 if flip_x else 1
        dy = -1 if flip_y else 1

        # Solid geometric faceted corner plate
        p1 = (cx, cy)
        p2 = (cx + dx * corner_size, cy)
        p3 = (cx + dx * (corner_size - chamfer), cy + dy * chamfer)
        p4 = (cx + dx * chamfer, cy + dy * (corner_size - chamfer))
        p5 = (cx, cy + dy * corner_size)
        draw.polygon([p1, p2, p3, p4, p5], fill=COLOR_NAVY_DARK)
        draw.line([p2, p3, p4, p5], fill=COLOR_GOLD_RICH, width=3)

        # High-tech cyan accent notch inside corner plate
        np1 = (cx + dx * 14, cy + dy * 14)
        np2 = (cx + dx * 38, cy + dy * 14)
        np3 = (cx + dx * 14, cy + dy * 38)
        draw.line([np2, np1, np3], fill=COLOR_CYAN_NEON, width=2)
        draw.ellipse([np1[0]-3, np1[1]-3, np1[0]+3, np1[1]+3], fill=COLOR_GOLD_LIGHT)

        # Microchip circuit traces along borders (compact, safe from logos)
        # Horizontal trace
        hx1 = cx + dx * (corner_size + 6)
        hy1 = cy + dy * 14
        hx2 = cx + dx * (corner_size + 55)
        draw.line([(hx1, hy1), (hx2, hy1)], fill=COLOR_GOLD_RICH, width=2)
        # 45-deg step
        hx3 = hx2 + dx * 12
        hy3 = hy1 + dy * 12
        draw.line([(hx2, hy1), (hx3, hy3)], fill=COLOR_GOLD_RICH, width=2)
        hx4 = hx3 + dx * 30
        draw.line([(hx3, hy3), (hx4, hy3)], fill=COLOR_CYAN_NEON, width=2)
        draw.ellipse([hx4 - 3, hy3 - 3, hx4 + 3, hy3 + 3], fill=COLOR_CYAN_NEON, outline=COLOR_NAVY_DARK, width=1)

        # Vertical trace
        vx1 = cx + dx * 14
        vy1 = cy + dy * (corner_size + 6)
        vy2 = cy + dy * (corner_size + 55)
        draw.line([(vx1, vy1), (vx1, vy2)], fill=COLOR_GOLD_RICH, width=2)
        # 45-deg step inward
        vx3 = vx1 + dx * 12
        vy3 = vy2 + dy * 12
        draw.line([(vx1, vy2), (vx3, vy3)], fill=COLOR_GOLD_RICH, width=2)
        vy4 = vy3 + dy * 30
        draw.line([(vx3, vy3), (vx3, vy4)], fill=COLOR_CYAN_NEON, width=2)
        draw.ellipse([vx3 - 3, vy4 - 3, vx3 + 3, vy4 + 3], fill=COLOR_CYAN_NEON, outline=COLOR_NAVY_DARK, width=1)

    # Top-Left Corner
    draw_tech_corner(m1, m1, flip_x=False, flip_y=False)
    # Top-Right Corner
    draw_tech_corner(width - m1, m1, flip_x=True, flip_y=False)
    # Bottom-Left Corner
    draw_tech_corner(m1, height - m1, flip_x=False, flip_y=True)
    # Bottom-Right Corner
    draw_tech_corner(width - m1, height - m1, flip_x=True, flip_y=True)

    # 7. BOTTOM CYBER BANNER / METADATA ACCENTS (Placed precisely in frame channel)
    bot_y = height - 37
    try:
        font_tech = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 13)
    except:
        font_tech = ImageFont.load_default()

    tag_left = "[ CSE TECH FEST 2026 // BGC TRUST UNIVERSITY BANGLADESH ]"
    tag_right = "[ AUTH-CODE: 2026-CSE-TF // VERIFIED CREDENTIAL ]"
    draw.text((90, bot_y - 6), tag_left, font=font_tech, fill=COLOR_SLATE)
    
    # Measure right text
    b_tr = draw.textbbox((0, 0), tag_right, font=font_tech)
    draw.text((width - 90 - (b_tr[2] - b_tr[0]), bot_y - 6), tag_right, font=font_tech, fill=COLOR_SLATE)

    # Center technical diamond motif on bottom edge
    mid_bx = width // 2
    draw.polygon([(mid_bx - 10, bot_y), (mid_bx, bot_y - 6), (mid_bx + 10, bot_y), (mid_bx, bot_y + 6)], fill=COLOR_GOLD_RICH)
    draw.ellipse([mid_bx - 3, bot_y - 3, mid_bx + 3, bot_y + 3], fill=COLOR_CYAN_NEON)

    # 8. TOP HEADER TECH MARKING (Placed cleanly in top frame channel)
    top_y = 37
    top_tag = "* * * DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING * * *"
    b_tt = draw.textbbox((0, 0), top_tag, font=font_tech)
    draw.text(((width - (b_tt[2] - b_tt[0])) // 2, top_y - 6), top_tag, font=font_tech, fill=COLOR_GOLD_RICH)

    img.save(out_path, "PNG")
    print(f"Ultra-professional Tech Fest background successfully generated: {out_path} ({width}x{height})")

if __name__ == "__main__":
    create_tech_fest_background()
