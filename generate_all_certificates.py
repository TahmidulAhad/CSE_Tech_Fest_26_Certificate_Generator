import os
import re
from PIL import Image, ImageDraw, ImageFont

# Base directories
CERT_DIR = r"C:\Users\HP\OneDrive\Desktop\Certificate"
OUT_DIR = os.path.join(CERT_DIR, "Generated_Certificates_PNG")
os.makedirs(OUT_DIR, exist_ok=True)

# Assets (Refined luxury gold & navy tech corners template)
BG_PATH = os.path.join(CERT_DIR, "cert_bg_refined_corners.png")
LEFT_LOGO_PATH = os.path.join(CERT_DIR, "BGCTUB_Logo_clean.png")
MID_LOGO_PATH = os.path.join(CERT_DIR, "Tech_Fest_Logo_clean.png")
ROBOTICS_LOGO_PATH = os.path.join(CERT_DIR, "BGCTUB_Robotics_Logo.png")
CODING_LOGO_PATH = os.path.join(CERT_DIR, "BGCTUB_Coding_Club_clean.png")

# Windows fonts and Custom fonts
WIN_FONTS = r"C:\Windows\Fonts"
ALEX_FONT = os.path.join(CERT_DIR, "fonts", "AlexBrush-Regular.ttf")

FONT_TITLE = ImageFont.truetype(os.path.join(WIN_FONTS, "georgiab.ttf"), 74)
FONT_SUB = ImageFont.truetype(os.path.join(WIN_FONTS, "georgiab.ttf"), 25)
FONT_RIBBON = ImageFont.truetype(os.path.join(WIN_FONTS, "georgiab.ttf"), 28)
FONT_PREAMBLE = ImageFont.truetype(os.path.join(WIN_FONTS, "georgiai.ttf"), 29)

if os.path.exists(ALEX_FONT):
    FONT_NAME = ImageFont.truetype(ALEX_FONT, 102)
else:
    FONT_NAME = ImageFont.truetype(os.path.join(WIN_FONTS, "Gabriola.ttf"), 110)

FONT_STATEMENT = ImageFont.truetype(os.path.join(WIN_FONTS, "georgia.ttf"), 26)
FONT_STATEMENT_BOLD = ImageFont.truetype(os.path.join(WIN_FONTS, "georgiab.ttf"), 27)
FONT_ROLE_HIGHLIGHT = ImageFont.truetype(os.path.join(WIN_FONTS, "georgiab.ttf"), 31)
FONT_SIG_NAME = ImageFont.truetype(os.path.join(WIN_FONTS, "georgiab.ttf"), 24)
FONT_SIG_ROLE = ImageFont.truetype(os.path.join(WIN_FONTS, "georgia.ttf"), 19)

# Colors
COLOR_NAVY = (10, 22, 42, 255)
COLOR_GOLD = (195, 150, 45, 255)
COLOR_GOLD_DARK = (185, 128, 15, 255)
COLOR_GOLD_LINE = (212, 175, 55, 255)
COLOR_CYAN = (0, 180, 240, 255)
COLOR_TEXT = (30, 41, 59, 255)

certificates = [
    # 1. Robotics & IoT Project Exhibition (Has Robotics Right Logo & Event Coordinator)
    {"event": "Robotics & IoT Project Exhibition", "cat": "Robotics", "role": "Champion", "name": "Mohammad Jamshidul Hafiz", "coord": "Tanzi Ahmed Chowdhury", "coord_role": "Coordinator\nRobotics & IoT Project Exhibition\nCSE Tech Fest 2026, BGCTUB", "right_logo": ROBOTICS_LOGO_PATH, "has_coord": True},
    {"event": "Robotics & IoT Project Exhibition", "cat": "Robotics", "role": "Champion", "name": "Mst Subrina Sultana", "coord": "Tanzi Ahmed Chowdhury", "coord_role": "Coordinator\nRobotics & IoT Project Exhibition\nCSE Tech Fest 2026, BGCTUB", "right_logo": ROBOTICS_LOGO_PATH, "has_coord": True},
    {"event": "Robotics & IoT Project Exhibition", "cat": "Robotics", "role": "Champion", "name": "Tanjemul Islam", "coord": "Tanzi Ahmed Chowdhury", "coord_role": "Coordinator\nRobotics & IoT Project Exhibition\nCSE Tech Fest 2026, BGCTUB", "right_logo": ROBOTICS_LOGO_PATH, "has_coord": True},
    {"event": "Robotics & IoT Project Exhibition", "cat": "Robotics", "role": "Runner-up", "name": "Md. Abdul Awal Khaled", "coord": "Tanzi Ahmed Chowdhury", "coord_role": "Coordinator\nRobotics & IoT Project Exhibition\nCSE Tech Fest 2026, BGCTUB", "right_logo": ROBOTICS_LOGO_PATH, "has_coord": True},
    {"event": "Robotics & IoT Project Exhibition", "cat": "Robotics", "role": "Runner-up", "name": "Mainul Islam", "coord": "Tanzi Ahmed Chowdhury", "coord_role": "Coordinator\nRobotics & IoT Project Exhibition\nCSE Tech Fest 2026, BGCTUB", "right_logo": ROBOTICS_LOGO_PATH, "has_coord": True},
    {"event": "Robotics & IoT Project Exhibition", "cat": "Robotics", "role": "Runner-up", "name": "Sheikh Mohammod Imran", "coord": "Tanzi Ahmed Chowdhury", "coord_role": "Coordinator\nRobotics & IoT Project Exhibition\nCSE Tech Fest 2026, BGCTUB", "right_logo": ROBOTICS_LOGO_PATH, "has_coord": True},

    # 2. Programming Contest (Has Coding Club Right Logo & Event Coordinator)
    {"event": "Programming Contest", "cat": "Programming", "role": "Champion", "name": "Sourav Palit", "coord": "Md. Asaduzzaman", "coord_role": "Coordinator\nProgramming Contest\nCSE Tech Fest 2026, BGCTUB", "right_logo": CODING_LOGO_PATH, "has_coord": True},
    {"event": "Programming Contest", "cat": "Programming", "role": "Champion", "name": "Turjoy Chakraborty Tushar", "coord": "Md. Asaduzzaman", "coord_role": "Coordinator\nProgramming Contest\nCSE Tech Fest 2026, BGCTUB", "right_logo": CODING_LOGO_PATH, "has_coord": True},
    {"event": "Programming Contest", "cat": "Programming", "role": "Champion", "name": "Simanto Barua", "coord": "Md. Asaduzzaman", "coord_role": "Coordinator\nProgramming Contest\nCSE Tech Fest 2026, BGCTUB", "right_logo": CODING_LOGO_PATH, "has_coord": True},
    {"event": "Programming Contest", "cat": "Programming", "role": "1st Runner-up", "name": "Nurunnabi", "coord": "Md. Asaduzzaman", "coord_role": "Coordinator\nProgramming Contest\nCSE Tech Fest 2026, BGCTUB", "right_logo": CODING_LOGO_PATH, "has_coord": True},
    {"event": "Programming Contest", "cat": "Programming", "role": "1st Runner-up", "name": "MD Istiaq Ahmad Raihan", "coord": "Md. Asaduzzaman", "coord_role": "Coordinator\nProgramming Contest\nCSE Tech Fest 2026, BGCTUB", "right_logo": CODING_LOGO_PATH, "has_coord": True},
    {"event": "Programming Contest", "cat": "Programming", "role": "1st Runner-up", "name": "Monjur Alam", "coord": "Md. Asaduzzaman", "coord_role": "Coordinator\nProgramming Contest\nCSE Tech Fest 2026, BGCTUB", "right_logo": CODING_LOGO_PATH, "has_coord": True},
    {"event": "Programming Contest", "cat": "Programming", "role": "2nd Runner-up", "name": "Sharmin Aktar", "coord": "Md. Asaduzzaman", "coord_role": "Coordinator\nProgramming Contest\nCSE Tech Fest 2026, BGCTUB", "right_logo": CODING_LOGO_PATH, "has_coord": True},
    {"event": "Programming Contest", "cat": "Programming", "role": "2nd Runner-up", "name": "Mohammad Chahad Chalehin", "coord": "Md. Asaduzzaman", "coord_role": "Coordinator\nProgramming Contest\nCSE Tech Fest 2026, BGCTUB", "right_logo": CODING_LOGO_PATH, "has_coord": True},
    {"event": "Programming Contest", "cat": "Programming", "role": "2nd Runner-up", "name": "Probal Barua Nandan", "coord": "Md. Asaduzzaman", "coord_role": "Coordinator\nProgramming Contest\nCSE Tech Fest 2026, BGCTUB", "right_logo": CODING_LOGO_PATH, "has_coord": True},

    # 3. IT Olympiad (NO Right Logo -> 2 Logos: BGCTUB on Left, Tech Fest on Right)
    {"event": "IT Olympiad", "cat": "IT Olympiad", "role": "1st Position", "name": "Mohammad Tareq Aziz", "coord": "Tisha Saha", "coord_role": "Coordinator\nIT Olympiad\nCSE Tech Fest 2026, BGCTUB", "right_logo": None, "has_coord": True},
    {"event": "IT Olympiad", "cat": "IT Olympiad", "role": "2nd Position", "name": "Umma Samia", "coord": "Tisha Saha", "coord_role": "Coordinator\nIT Olympiad\nCSE Tech Fest 2026, BGCTUB", "right_logo": None, "has_coord": True},
    {"event": "IT Olympiad", "cat": "IT Olympiad", "role": "3rd Position", "name": "Lutfur Rahman Adnan", "coord": "Tisha Saha", "coord_role": "Coordinator\nIT Olympiad\nCSE Tech Fest 2026, BGCTUB", "right_logo": None, "has_coord": True},

    # 4. Physics & Math Olympiad (NO Right Logo -> 2 Logos: BGCTUB on Left, Tech Fest on Right)
    {"event": "Physics & Mathematics Olympiad", "cat": "Physics & Math", "role": "1st Position", "name": "Sabina Akter", "coord": "Nurul Absar", "coord_role": "Coordinator\nPhysics & Mathematics Olympiad\nCSE Tech Fest 2026, BGCTUB", "right_logo": None, "has_coord": True},
    {"event": "Physics & Mathematics Olympiad", "cat": "Physics & Math", "role": "2nd Position", "name": "Opy Barua", "coord": "Nurul Absar", "coord_role": "Coordinator\nPhysics & Mathematics Olympiad\nCSE Tech Fest 2026, BGCTUB", "right_logo": None, "has_coord": True},
    {"event": "Physics & Mathematics Olympiad", "cat": "Physics & Math", "role": "3rd Position", "name": "Himu Akter", "coord": "Nurul Absar", "coord_role": "Coordinator\nPhysics & Mathematics Olympiad\nCSE Tech Fest 2026, BGCTUB", "right_logo": None, "has_coord": True},

    # 5. Leadership (NO Right Logo, NO Coordinator -> 2 Logos: BGCTUB on Left, Tech Fest on Right; 2 Symmetrical Signatures)
    {"event": "CSE Tech Fest 2026", "cat": "Leadership", "role": "Documentation & Publication Lead", "name": "Md. Tahmidul Alam Ahad", "coord": None, "coord_role": None, "right_logo": None, "is_lead": True, "lead_title": "Documentation and Publication Lead", "has_coord": False},
    {"event": "CSE Tech Fest 2026", "cat": "Leadership", "role": "Operations & Execution Lead", "name": "Mohammad Tareq Aziz", "coord": None, "coord_role": None, "right_logo": None, "is_lead": True, "lead_title": "Operations & Execution Lead", "has_coord": False}
]

def render_certificate(c, idx):
    canvas = Image.open(BG_PATH).convert("RGBA")
    W, H = canvas.size
    draw = ImageDraw.Draw(canvas)

    # UNIFIED HORIZONTAL CENTER AXIS FOR ALL TOP LOGOS
    # In 2048x1364: top gold frame is at y=52, "CERTIFICATE" starts at y=315.
    # Therefore, the vertical center for the logos is y=168.
    LOGO_CENTER_Y = 168

    # TOP LOGOS:
    # If right club logo exists (Robotics, Programming) -> 3 logos: Left=BGCTUB, Mid=Tech Fest, Right=Club
    # If NO right club logo (IT, Math/Phys, Leadership) -> 2 logos: Left=BGCTUB, Right=Tech Fest (Symmetrical across canvas)
    has_club_logo = bool(c.get("right_logo") and os.path.exists(c["right_logo"]))

    if has_club_logo:
        # 1. Left Logo (BGCTUB Logo)
        left_im = Image.open(LEFT_LOGO_PATH).convert("RGBA")
        l_h = 145
        l_w = int(left_im.width * (l_h / left_im.height))
        left_im = left_im.resize((l_w, l_h), Image.Resampling.LANCZOS)
        l_x = 210
        l_y = LOGO_CENTER_Y - (l_h // 2)
        canvas.paste(left_im, (l_x, l_y), left_im)

        # 2. Middle Logo (Tech Fest 2026 Clean 3D Logo)
        mid_im = Image.open(MID_LOGO_PATH).convert("RGBA")
        m_h = 175
        m_w = int(mid_im.width * (m_h / mid_im.height))
        mid_im = mid_im.resize((m_w, m_h), Image.Resampling.LANCZOS)
        m_x = (W - m_w) // 2
        m_y = LOGO_CENTER_Y - (m_h // 2)
        canvas.paste(mid_im, (m_x, m_y), mid_im)

        # 3. Right Logo (Club Logo)
        right_im = Image.open(c["right_logo"]).convert("RGBA")
        r_h = 150 if "Robotics" in c.get("right_logo") else 135
        r_w = int(right_im.width * (r_h / right_im.height))
        right_im = right_im.resize((r_w, r_h), Image.Resampling.LANCZOS)
        r_x = W - 210 - r_w
        r_y = LOGO_CENTER_Y - (r_h // 2)
        canvas.paste(right_im, (r_x, r_y), right_im)
    else:
        # 2 LOGOS: Left=BGCTUB, Right=Tech Fest (Clean, balanced, no empty side)
        # Left Logo (BGCTUB)
        left_im = Image.open(LEFT_LOGO_PATH).convert("RGBA")
        l_h = 150
        l_w = int(left_im.width * (l_h / left_im.height))
        left_im = left_im.resize((l_w, l_h), Image.Resampling.LANCZOS)
        l_x = 210
        l_y = LOGO_CENTER_Y - (l_h // 2)
        canvas.paste(left_im, (l_x, l_y), left_im)

        # Right Logo (Tech Fest 2026 3D Logo)
        tech_im = Image.open(MID_LOGO_PATH).convert("RGBA")
        t_h = 165
        t_w = int(tech_im.width * (t_h / tech_im.height))
        tech_im = tech_im.resize((t_w, t_h), Image.Resampling.LANCZOS)
        t_x = W - 210 - t_w
        t_y = LOGO_CENTER_Y - (t_h // 2)
        canvas.paste(tech_im, (t_x, t_y), tech_im)

    # 4. Title "CERTIFICATE"
    title_text = "CERTIFICATE"
    bbox = draw.textbbox((0, 0), title_text, font=FONT_TITLE)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) // 2, 315), title_text, font=FONT_TITLE, fill=COLOR_NAVY)

    # Subtitle with gold flourishes & diamond
    sub_text = "OF APPRECIATION" if c.get("is_lead") else "OF ACHIEVEMENT"
    bbox_sub = draw.textbbox((0, 0), sub_text, font=FONT_SUB)
    sw = bbox_sub[2] - bbox_sub[0]
    sy = 405
    draw.text(((W - sw) // 2, sy), sub_text, font=FONT_SUB, fill=COLOR_GOLD)
    draw.line([((W - sw) // 2 - 130, sy + 14), ((W - sw) // 2 - 25, sy + 14)], fill=COLOR_GOLD, width=3)
    draw.polygon([((W - sw) // 2 - 134, sy + 14), ((W - sw) // 2 - 130, sy + 10), ((W - sw) // 2 - 126, sy + 14), ((W - sw) // 2 - 130, sy + 18)], fill=COLOR_GOLD)
    draw.line([((W + sw) // 2 + 25, sy + 14), ((W + sw) // 2 + 130, sy + 14)], fill=COLOR_GOLD, width=3)
    draw.polygon([((W + sw) // 2 + 126, sy + 14), ((W + sw) // 2 + 130, sy + 10), ((W + sw) // 2 + 134, sy + 14), ((W + sw) // 2 + 130, sy + 18)], fill=COLOR_GOLD)

    # 5. Cyber Tech Ribbon (Faceted Tech Badge)
    ribbon_label = "LEADERSHIP & RECOGNITION" if c.get("is_lead") else c["event"].upper()
    # Ensure IoT is formatted properly in ribbon
    if "IOT" in ribbon_label:
        ribbon_label = ribbon_label.replace("IOT", "IoT")
    r_bbox = draw.textbbox((0, 0), ribbon_label, font=FONT_RIBBON)
    rw = r_bbox[2] - r_bbox[0]
    ry = 465
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

    # 6. Preamble
    preamble = "This certificate is proudly presented to" if c.get("is_lead") else "This is to certify that"
    p_bbox = draw.textbbox((0, 0), preamble, font=FONT_PREAMBLE)
    draw.text(((W - (p_bbox[2] - p_bbox[0])) // 2, 555), preamble, font=FONT_PREAMBLE, fill=(70, 85, 105, 255))

    # 7. Recipient Name
    name_text = c["name"]
    n_bbox = draw.textbbox((0, 0), name_text, font=FONT_NAME)
    nw = n_bbox[2] - n_bbox[0]
    draw.text(((W - nw) // 2, 595), name_text, font=FONT_NAME, fill=COLOR_NAVY)

    # Gold Underline with Diamond Center
    draw.line([(W // 2 - 380, 720), (W // 2 + 380, 720)], fill=COLOR_GOLD, width=3)
    draw.polygon([(W // 2, 712), (W // 2 + 8, 720), (W // 2, 728), (W // 2 - 8, 720)], fill=COLOR_GOLD)

    # 8. Achievement Statement (Sir's Exact Review Format with Highlighted Position)
    if c.get("is_lead"):
        line1_segs = [
            ("in recognition of outstanding contribution and leadership as", FONT_STATEMENT, COLOR_TEXT, False)
        ]
        line2_segs = [
            (c["lead_title"], FONT_ROLE_HIGHLIGHT, COLOR_GOLD_DARK, True),
            (" for ", FONT_STATEMENT, COLOR_TEXT, False),
            ("CSE Tech Fest 2026", FONT_STATEMENT_BOLD, COLOR_NAVY, False),
            (",", FONT_STATEMENT, COLOR_TEXT, False)
        ]
        line3_segs = [
            ("organized by the Department of Computer Science & Engineering, BGC Trust University Bangladesh.", FONT_STATEMENT, COLOR_TEXT, False)
        ]
    else:
        if "Position" in c["role"]:
            line1_segs = [
                ("has achieved the ", FONT_STATEMENT, COLOR_TEXT, False),
                (c["role"], FONT_ROLE_HIGHLIGHT, COLOR_GOLD_DARK, True),
                (" in the ", FONT_STATEMENT, COLOR_TEXT, False),
                (c["event"], FONT_STATEMENT_BOLD, COLOR_NAVY, False)
            ]
        else:
            line1_segs = [
                ("has achieved the ", FONT_STATEMENT, COLOR_TEXT, False),
                (c["role"], FONT_ROLE_HIGHLIGHT, COLOR_GOLD_DARK, True),
                (" position in the ", FONT_STATEMENT, COLOR_TEXT, False),
                (c["event"], FONT_STATEMENT_BOLD, COLOR_NAVY, False)
            ]
        line2_segs = [
            ("at ", FONT_STATEMENT, COLOR_TEXT, False),
            ("CSE Tech Fest 2026", FONT_STATEMENT_BOLD, COLOR_NAVY, False),
            (",", FONT_STATEMENT, COLOR_TEXT, False)
        ]
        line3_segs = [
            ("organized by the Department of Computer Science & Engineering, BGC Trust University Bangladesh.", FONT_STATEMENT, COLOR_TEXT, False)
        ]

    y_lines = [790, 832, 874]
    for segs, y_base in zip([line1_segs, line2_segs, line3_segs], y_lines):
        total_w = 0
        seg_widths = []
        for text, font, col, is_hl in segs:
            bbox = draw.textbbox((0, y_base), text, font=font, anchor="ls")
            w = bbox[2] - bbox[0]
            seg_widths.append(w)
            total_w += w

        cur_x = (W - total_w) // 2
        for (text, font, col, is_hl), w in zip(segs, seg_widths):
            # No underline - rich gold color for highlighted position is clean and balanced
            draw.text((cur_x, y_base), text, font=font, fill=col, anchor="ls")
            cur_x += w

    # 9. Signatures (Well inside frame, 0 overflow)
    sig_y_line = 1105
    chair_name = "Mohammad Salah Uddin Chowdury"
    chair_role = "Chairman\nDepartment of CSE, BGCTUB"
    vc_name = "Prof. Dr. Md. Manzoorul Kibria"
    vc_role = "Vice Chancellor\nBGC Trust University Bangladesh"

    if c.get("has_coord", True):
        # 3 Columns: Coordinator, Chairman, Vice Chancellor
        col_w = 440
        x_left = 180
        x_mid = (W - col_w) // 2
        x_right = W - 180 - col_w

        for x_pos in [x_left, x_mid, x_right]:
            draw.line([(x_pos + 40, sig_y_line), (x_pos + col_w - 40, sig_y_line)], fill=COLOR_NAVY, width=3)

        # Left: Coordinator
        b = draw.textbbox((0, 0), c["coord"], font=FONT_SIG_NAME)
        draw.text((x_left + (col_w - (b[2] - b[0])) // 2, sig_y_line + 14), c["coord"], font=FONT_SIG_NAME, fill=COLOR_NAVY)
        for i, line in enumerate(c["coord_role"].split("\n")):
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
    else:
        # 2 Symmetrical Columns: Chairman & Vice Chancellor (No Coordinator)
        col_w = 460
        gap = 260
        total_w = col_w * 2 + gap
        x_chair = (W - total_w) // 2
        x_vc = x_chair + col_w + gap

        for x_pos in [x_chair, x_vc]:
            draw.line([(x_pos + 40, sig_y_line), (x_pos + col_w - 40, sig_y_line)], fill=COLOR_NAVY, width=3)

        # Left: Chairman
        b = draw.textbbox((0, 0), chair_name, font=FONT_SIG_NAME)
        draw.text((x_chair + (col_w - (b[2] - b[0])) // 2, sig_y_line + 14), chair_name, font=FONT_SIG_NAME, fill=COLOR_NAVY)
        for i, line in enumerate(chair_role.split("\n")):
            b = draw.textbbox((0, 0), line, font=FONT_SIG_ROLE)
            draw.text((x_chair + (col_w - (b[2] - b[0])) // 2, sig_y_line + 46 + i * 25), line, font=FONT_SIG_ROLE, fill=(70, 85, 105, 255))

        # Right: Vice Chancellor
        b = draw.textbbox((0, 0), vc_name, font=FONT_SIG_NAME)
        draw.text((x_vc + (col_w - (b[2] - b[0])) // 2, sig_y_line + 14), vc_name, font=FONT_SIG_NAME, fill=COLOR_NAVY)
        for i, line in enumerate(vc_role.split("\n")):
            b = draw.textbbox((0, 0), line, font=FONT_SIG_ROLE)
            draw.text((x_vc + (col_w - (b[2] - b[0])) // 2, sig_y_line + 46 + i * 25), line, font=FONT_SIG_ROLE, fill=(70, 85, 105, 255))



    # Save High-Resolution PNG strictly at A4 Landscape (3508 x 2480 px @ 300 DPI)
    clean_name = re.sub(r'[^a-zA-Z0-9]', '_', c['name'])
    clean_role = re.sub(r'[^a-zA-Z0-9]', '_', c['role'])
    filename = f"{idx+1:02d}_{clean_name}_{clean_role}.png"
    out_path = os.path.join(OUT_DIR, filename)

    # Scale canvas to standard A4 Landscape at 300 DPI (3508 x 2480)
    canvas_a4 = canvas.resize((3508, 2480), Image.Resampling.LANCZOS)
    canvas_a4.save(out_path, "PNG", dpi=(300, 300))
    print(f"[{idx+1}/23] Saved A4 300 DPI: {filename}")
    return out_path

print("Generating all 23 High-Resolution A4 Certificates with Tech Fest Cyber Vibe theme...")
all_png_paths = []
for idx, cert in enumerate(certificates):
    png_path = render_certificate(cert, idx)
    all_png_paths.append(png_path)

# Save combined multi-page PDF strictly with standard A4 Landscape (297 x 210 mm)
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas as pdf_canvas

pdf_path = os.path.join(CERT_DIR, "CSE_Tech_Fest_2026_All_23_Certificates.pdf")
c_pdf = pdf_canvas.Canvas(pdf_path, pagesize=landscape(A4))
w_a4, h_a4 = landscape(A4) # 841.89 x 595.28 pt (exactly 297 x 210 mm)

for png_p in all_png_paths:
    c_pdf.drawImage(png_p, 0, 0, width=w_a4, height=h_a4)
    c_pdf.showPage()

c_pdf.save()
print(f"\nAll 23 certificates generated at A4 size (3508x2480 @ 300 DPI) in {OUT_DIR}")
print(f"Standard A4 Landscape PDF (297x210 mm) saved to {pdf_path}")
