import math
from PIL import Image, ImageDraw, ImageFont

def create_refined_corner_template(out_path="cert_bg_refined_corners.png", W=2048, H=1364):
    # Canvas: crisp, bright off-white / ivory
    img = Image.new("RGBA", (W, H), (254, 254, 255, 255))
    draw = ImageDraw.Draw(img)

    # 1. Subtle background guilloche / luxury tech geometric watermarks
    # Very faint gold/slate concentric circles & diamond lattice at center
    cx, cy = W // 2, H // 2 + 20
    for r in [260, 320, 380, 440]:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(235, 230, 215, 90), width=1)
    
    # Subtle 12-point star / diamond radial
    for i in range(12):
        angle = math.radians(i * 30)
        x1 = cx + 260 * math.cos(angle)
        y1 = cy + 260 * math.sin(angle)
        x2 = cx + 440 * math.cos(angle)
        y2 = cy + 440 * math.sin(angle)
        draw.line([(x1, y1), (x2, y2)], fill=(235, 230, 215, 70), width=1)

    # 2. COLOR PALETTE (Prestigious Midnight Navy + Polished Metallic Gold)
    NAVY_DARK = (10, 22, 42, 255)       # Deep midnight navy
    NAVY_MED  = (18, 38, 70, 255)       # Medium navy
    GOLD_DARK = (170, 130, 40, 255)     # Deep burnished gold
    GOLD_MAIN = (205, 165, 60, 255)     # Rich gold
    GOLD_LITE = (240, 210, 120, 255)    # Highlights
    GOLD_PALE = (250, 235, 175, 255)    # Very light gold
    CYAN_ACC  = (0, 190, 240, 255)      # Cyan tech accent

    # 3. OUTER BORDER SYSTEM
    # Outer dark navy border
    m_out = 32
    draw.rectangle([m_out, m_out, W - m_out, H - m_out], outline=NAVY_DARK, width=12)

    # Rich metallic gold double frame
    m_g1 = 52
    draw.rectangle([m_g1, m_g1, W - m_g1, H - m_g1], outline=GOLD_MAIN, width=3)

    m_g2 = 62
    draw.rectangle([m_g2, m_g2, W - m_g2, H - m_g2], outline=GOLD_DARK, width=1)

    # Inner hairline border
    m_in = 74
    draw.rectangle([m_in, m_in, W - m_in, H - m_in], outline=(225, 215, 195, 255), width=1)

    # 4. REFINED CORNER DESIGN
    # Compact, modern, faceted 3D tech-luxury corner plates
    # Crucial: designed so they do NOT obstruct logos at top (x: 180 to W-180, y: 70 to 260)
    # and do NOT obstruct coordinator text at bottom (x: 160 to W-160, y: 1050 to 1250)
    c_size = 125
    chamf = 45

    def draw_corner(cx, cy, flip_x=False, flip_y=False):
        dx = -1 if flip_x else 1
        dy = -1 if flip_y else 1

        # Layer 1: Solid angled midnight navy faceted shield
        p1 = (cx, cy)
        p2 = (cx + dx * c_size, cy)
        p3 = (cx + dx * (c_size - chamf), cy + dy * chamf)
        p4 = (cx + dx * chamf, cy + dy * (c_size - chamf))
        p5 = (cx, cy + dy * c_size)
        draw.polygon([p1, p2, p3, p4, p5], fill=NAVY_DARK)
        # Gold beveled outer edge
        draw.line([p2, p3, p4, p5], fill=GOLD_MAIN, width=4)

        # Layer 2: Inner secondary navy facet
        ip1 = (cx + dx * 16, cy + dy * 16)
        ip2 = (cx + dx * (c_size - 32), cy + dy * 16)
        ip3 = (cx + dx * (c_size - 32 - chamf + 16), cy + dy * (chamf - 4))
        ip4 = (cx + dx * (chamf - 4), cy + dy * (c_size - 32 - chamf + 16))
        ip5 = (cx + dx * 16, cy + dy * (c_size - 32))
        draw.polygon([ip1, ip2, ip3, ip4, ip5], fill=NAVY_MED)
        draw.line([ip2, ip3, ip4, ip5], fill=GOLD_LITE, width=2)

        # Layer 3: Corner Gold Diamond Motif
        dp1 = (cx + dx * 32, cy + dy * 32)
        dp_rad = 12
        draw.polygon([
            (dp1[0], dp1[1] - dp_rad),
            (dp1[0] + dp_rad, dp1[1]),
            (dp1[0], dp1[1] + dp_rad),
            (dp1[0] - dp_rad, dp1[1])
        ], fill=GOLD_MAIN, outline=GOLD_LITE, width=1)
        # Center tiny cyan pin
        draw.ellipse([dp1[0]-3, dp1[1]-3, dp1[0]+3, dp1[1]+3], fill=CYAN_ACC)

        # Subtle gold pinstripe extending along edges
        # Horizontal accent
        hx1 = cx + dx * (c_size + 8)
        hy1 = cy + dy * 16
        hx2 = cx + dx * (c_size + 85)
        draw.line([(hx1, hy1), (hx2, hy1)], fill=GOLD_MAIN, width=2)
        draw.line([(hx2, hy1), (hx2 + dx * 12, hy1 + dy * 12)], fill=GOLD_MAIN, width=2)
        draw.ellipse([hx2 + dx * 12 - 3, hy1 + dy * 12 - 3, hx2 + dx * 12 + 3, hy1 + dy * 12 + 3], fill=GOLD_LITE)

        # Vertical accent
        vx1 = cx + dx * 16
        vy1 = cy + dy * (c_size + 8)
        vy2 = cy + dy * (c_size + 85)
        draw.line([(vx1, vy1), (vx1, vy2)], fill=GOLD_MAIN, width=2)
        draw.line([(vx1, vy2), (vx1 + dx * 12, vy2 + dy * 12)], fill=GOLD_MAIN, width=2)
        draw.ellipse([vx1 + dx * 12 - 3, vy2 + dy * 12 - 3, vx1 + dx * 12 + 3, vy2 + dy * 12 + 3], fill=GOLD_LITE)

    # Top-Left
    draw_corner(m_out, m_out, flip_x=False, flip_y=False)
    # Top-Right
    draw_corner(W - m_out, m_out, flip_x=True, flip_y=False)
    # Bottom-Left
    draw_corner(m_out, H - m_out, flip_x=False, flip_y=True)
    # Bottom-Right
    draw_corner(W - m_out, H - m_out, flip_x=True, flip_y=True)

    # 5. ELEGANT GOLD ACCENTS ALONG BORDER MIDPOINTS
    # Top midpoint gold motif
    mid_x = W // 2
    top_bar_y = 52
    draw.polygon([(mid_x - 16, top_bar_y), (mid_x, top_bar_y - 6), (mid_x + 16, top_bar_y), (mid_x, top_bar_y + 6)], fill=GOLD_MAIN)
    draw.ellipse([mid_x - 3, top_bar_y - 3, mid_x + 3, top_bar_y + 3], fill=NAVY_DARK)

    # Bottom midpoint gold motif
    bot_bar_y = H - 52
    draw.polygon([(mid_x - 16, bot_bar_y), (mid_x, bot_bar_y - 6), (mid_x + 16, bot_bar_y), (mid_x, bot_bar_y + 6)], fill=GOLD_MAIN)
    draw.ellipse([mid_x - 3, bot_bar_y - 3, mid_x + 3, bot_bar_y + 3], fill=NAVY_DARK)

    # Left & Right midpoints
    mid_y = H // 2
    draw.polygon([(52, mid_y - 14), (58, mid_y), (52, mid_y + 14), (46, mid_y)], fill=GOLD_MAIN)
    draw.polygon([(W - 52, mid_y - 14), (W - 46, mid_y), (W - 52, mid_y + 14), (W - 58, mid_y)], fill=GOLD_MAIN)

    img.save(out_path, "PNG")
    print(f"Refined luxury corner template successfully generated: {out_path} ({W}x{H})")

if __name__ == "__main__":
    create_refined_corner_template()
