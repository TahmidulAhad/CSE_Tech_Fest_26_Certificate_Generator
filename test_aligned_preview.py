import os
from PIL import Image, ImageDraw, ImageFont

CERT_DIR = r"C:\Users\HP\OneDrive\Desktop\Certificate"
BG_PATH = os.path.join(CERT_DIR, "cert_bg_clean_2x.png")
LEFT_LOGO_PATH = os.path.join(CERT_DIR, "BGCTUB_Logo_clean.png")
MID_LOGO_PATH = os.path.join(CERT_DIR, "Tech_Fest_Logo_clean.png")
ROBOTICS_LOGO_PATH = os.path.join(CERT_DIR, "BGCTUB_Robotics_Logo.png")
CODING_LOGO_PATH = os.path.join(CERT_DIR, "BGCTUB_Coding_Club_clean.png")
ALEX_FONT = os.path.join(CERT_DIR, "fonts", "AlexBrush-Regular.ttf")
WIN_FONTS = r"C:\Windows\Fonts"

FONT_TITLE = ImageFont.truetype(os.path.join(WIN_FONTS, "georgiab.ttf"), 74)
FONT_SUB = ImageFont.truetype(os.path.join(WIN_FONTS, "georgiab.ttf"), 25)
FONT_RIBBON = ImageFont.truetype(os.path.join(WIN_FONTS, "georgiab.ttf"), 28)
FONT_PREAMBLE = ImageFont.truetype(os.path.join(WIN_FONTS, "georgiai.ttf"), 29)
FONT_NAME = ImageFont.truetype(ALEX_FONT, 102)
FONT_STATEMENT = ImageFont.truetype(os.path.join(WIN_FONTS, "georgia.ttf"), 26)
FONT_SIG_NAME = ImageFont.truetype(os.path.join(WIN_FONTS, "georgiab.ttf"), 24)
FONT_SIG_ROLE = ImageFont.truetype(os.path.join(WIN_FONTS, "georgia.ttf"), 20)

COLOR_NAVY = (11, 23, 42, 255)
COLOR_GOLD = (195, 150, 45, 255)
COLOR_CYAN = (0, 180, 240, 255)
COLOR_TEXT = (30, 41, 59, 255)

def render_sample(right_logo_path, out_file):
    canvas = Image.open(BG_PATH).convert("RGBA")
    W, H = canvas.size
    draw = ImageDraw.Draw(canvas)

    # UNIFIED HORIZONTAL CENTER AXIS FOR ALL TOP LOGOS
    # In 2048x1364: top gold line is at y=38.
    # Title 'CERTIFICATE' starts at y=320.
    # Therefore, the vertical center for the logos is y=180.
    LOGO_CENTER_Y = 180

    # 1. Left Logo (BGCTUB Logo)
    left_im = Image.open(LEFT_LOGO_PATH).convert("RGBA")
    l_h = 138
    l_w = int(left_im.width * (l_h / left_im.height))
    left_im = left_im.resize((l_w, l_h), Image.Resampling.LANCZOS)
    # Safe distance from corner decoration: x = 230
    l_x = 230
    l_y = LOGO_CENTER_Y - (l_h // 2)
    canvas.paste(left_im, (l_x, l_y), left_im)

    # 2. Middle Logo (Tech Fest 2026 Clean 3D Logo)
    # Scaled to visually balance with left & right logos
    mid_im = Image.open(MID_LOGO_PATH).convert("RGBA")
    m_h = 165
    m_w = int(mid_im.width * (m_h / mid_im.height))
    mid_im = mid_im.resize((m_w, m_h), Image.Resampling.LANCZOS)
    m_x = (W - m_w) // 2
    m_y = LOGO_CENTER_Y - (m_h // 2)
    canvas.paste(mid_im, (m_x, m_y), mid_im)

    # 3. Right Logo (Robotics / Coding Club)
    if right_logo_path and os.path.exists(right_logo_path):
        right_im = Image.open(right_logo_path).convert("RGBA")
        r_h = 142
        r_w = int(right_im.width * (r_h / right_im.height))
        right_im = right_im.resize((r_w, r_h), Image.Resampling.LANCZOS)
        # Symmetrical right margin: W - 230 - r_w
        r_x = W - 230 - r_w
        r_y = LOGO_CENTER_Y - (r_h // 2)
        canvas.paste(right_im, (r_x, r_y), right_im)

    # Title "CERTIFICATE"
    title_text = "CERTIFICATE"
    bbox = draw.textbbox((0, 0), title_text, font=FONT_TITLE)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) // 2, 300), title_text, font=FONT_TITLE, fill=COLOR_NAVY)

    # Subtitle with gold flourishes & diamond
    sub_text = "OF ACHIEVEMENT"
    bbox_sub = draw.textbbox((0, 0), sub_text, font=FONT_SUB)
    sw = bbox_sub[2] - bbox_sub[0]
    sy = 395
    draw.text(((W - sw) // 2, sy), sub_text, font=FONT_SUB, fill=COLOR_GOLD)
    draw.line([((W - sw) // 2 - 130, sy + 14), ((W - sw) // 2 - 25, sy + 14)], fill=COLOR_GOLD, width=3)
    draw.polygon([((W - sw) // 2 - 134, sy + 14), ((W - sw) // 2 - 130, sy + 10), ((W - sw) // 2 - 126, sy + 14), ((W - sw) // 2 - 130, sy + 18)], fill=COLOR_GOLD)
    draw.line([((W + sw) // 2 + 25, sy + 14), ((W + sw) // 2 + 130, sy + 14)], fill=COLOR_GOLD, width=3)
    draw.polygon([((W + sw) // 2 + 126, sy + 14), ((W + sw) // 2 + 130, sy + 10), ((W + sw) // 2 + 134, sy + 14), ((W + sw) // 2 + 130, sy + 18)], fill=COLOR_GOLD)

    # Faceted Tech Ribbon Banner
    ribbon_label = "ROBOTICS & IOT PROJECT EXHIBITION"
    r_bbox = draw.textbbox((0, 0), ribbon_label, font=FONT_RIBBON)
    rw = r_bbox[2] - r_bbox[0]
    ry = 460
    pad_x = 55
    rx1 = (W - rw) // 2 - pad_x
    rx2 = (W + rw) // 2 + pad_x
    rh = 54
    chamfer = 14
    poly = [
        (rx1 + chamfer, ry),
        (rx2 - chamfer, ry),
        (rx2, ry + chamfer),
        (rx2, ry + rh - chamfer),
        (rx2 - chamfer, ry + rh),
        (rx1 + chamfer, ry + rh),
        (rx1, ry + rh - chamfer),
        (rx1, ry + chamfer)
    ]
    draw.polygon(poly, fill=COLOR_NAVY, outline=COLOR_GOLD, width=3)
    # Side diamond accents inside ribbon
    draw.polygon([(rx1 + 22, ry + rh // 2), (rx1 + 26, ry + rh // 2 - 5), (rx1 + 30, ry + rh // 2), (rx1 + 26, ry + rh // 2 + 5)], fill=COLOR_GOLD)
    draw.polygon([(rx2 - 30, ry + rh // 2), (rx2 - 26, ry + rh // 2 - 5), (rx2 - 22, ry + rh // 2), (rx2 - 26, ry + rh // 2 + 5)], fill=COLOR_GOLD)
    draw.text(((W - rw) // 2, ry + 11), ribbon_label, font=FONT_RIBBON, fill=(255, 255, 255, 255))

    # Preamble
    preamble = "This is to certify that"
    p_bbox = draw.textbbox((0, 0), preamble, font=FONT_PREAMBLE)
    draw.text(((W - (p_bbox[2] - p_bbox[0])) // 2, 550), preamble, font=FONT_PREAMBLE, fill=(70, 85, 105, 255))

    # Recipient Name (Alex Brush)
    name_text = "Mohammad Jamshidul Hafiz"
    n_bbox = draw.textbbox((0, 0), name_text, font=FONT_NAME)
    nw = n_bbox[2] - n_bbox[0]
    draw.text(((W - nw) // 2, 595), name_text, font=FONT_NAME, fill=COLOR_NAVY)

    # Gold Underline with Diamond Center
    draw.line([(W // 2 - 360, 720), (W // 2 + 360, 720)], fill=COLOR_GOLD, width=3)
    draw.polygon([(W // 2, 712), (W // 2 + 8, 720), (W // 2, 728), (W // 2 - 8, 720)], fill=COLOR_GOLD)

    # Achievement Statement
    l1 = "has secured the Champion title in the Robotics & IOT Project Exhibition"
    l2 = "as a part of CSE Tech Fest 2026,"
    l3 = "organized by the Department of Computer Science & Engineering, BGC Trust University Bangladesh."

    for offset, line in enumerate([l1, l2, l3]):
        b = draw.textbbox((0, 0), line, font=FONT_STATEMENT)
        lw = b[2] - b[0]
        draw.text(((W - lw) // 2, 765 + offset * 40), line, font=FONT_STATEMENT, fill=COLOR_TEXT)

    # Signatures
    sig_y_line = 1110
    col_w = 420
    x_left = 180
    x_mid = (W - col_w) // 2
    x_right = W - 180 - col_w

    coord_name = "Mr. Tanzi Ahmed Chowdhury"
    coord_role = "Coordinator, Robotics & IOT Project Exhibition\nCSE Tech Fest 2026\nDepartment of CSE, BGCTUB"
    chair_name = "Mohammad Salah Uddin Chowdury"
    chair_role = "Chairman\nDepartment of CSE, BGCTUB"
    vc_name = "Prof. Dr. Md. Manzoorul Kibria"
    vc_role = "Vice Chancellor\nBGC Trust University Bangladesh"

    for x_pos in [x_left, x_mid, x_right]:
        draw.line([(x_pos + 40, sig_y_line), (x_pos + col_w - 40, sig_y_line)], fill=COLOR_NAVY, width=3)

    # Left: Coordinator
    b = draw.textbbox((0, 0), coord_name, font=FONT_SIG_NAME)
    draw.text((x_left + (col_w - (b[2] - b[0])) // 2, sig_y_line + 14), coord_name, font=FONT_SIG_NAME, fill=COLOR_NAVY)
    for i, line in enumerate(coord_role.split("\n")):
        b = draw.textbbox((0, 0), line, font=FONT_SIG_ROLE)
        draw.text((x_left + (col_w - (b[2] - b[0])) // 2, sig_y_line + 46 + i * 25), line, font=FONT_SIG_ROLE, fill=(70, 85, 105, 255))

    # Center: Chairman
    b = draw.textbbox((0, 0), chair_name, font=FONT_SIG_NAME)
    draw.text((x_mid + (col_w - (b[2] - b[0])) // 2, sig_y_line + 14), chair_name, font=FONT_SIG_NAME, fill=COLOR_NAVY)
    for i, line in enumerate(chair_role.split("\n")):
        b = draw.textbbox((0, 0), line, font=FONT_SIG_ROLE)
        draw.text((x_mid + (col_w - (b[2] - b[0])) // 2, sig_y_line + 46 + i * 25), line, font=FONT_SIG_ROLE, fill=(70, 85, 105, 255))

    # Right: Vice Chancellor
    b = draw.textbbox((0, 0), vc_name, font=FONT_SIG_NAME)
    draw.text((x_right + (col_w - (b[2] - b[0])) // 2, sig_y_line + 14), vc_name, font=FONT_SIG_NAME, fill=COLOR_NAVY)
    for i, line in enumerate(vc_role.split("\n")):
        b = draw.textbbox((0, 0), line, font=FONT_SIG_ROLE)
        draw.text((x_right + (col_w - (b[2] - b[0])) // 2, sig_y_line + 46 + i * 25), line, font=FONT_SIG_ROLE, fill=(70, 85, 105, 255))

    canvas.save(out_file, "PNG")
    print("Saved aligned sample to", out_file)

if __name__ == "__main__":
    render_sample(ROBOTICS_LOGO_PATH, os.path.join(CERT_DIR, "test_aligned_robotics.png"))
