import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# Define Color Palette (Modern Dark RPG / Catppuccin-inspired)
BG_DARK = "1E1E2E"       # Base deep dark
BG_CARD = "282A36"       # Card surface
BG_CARD_LIGHT = "313244" # Header / lighter surface
BORDER_COLOR = "45475A"  # Subtle borders
TEXT_MAIN = "CDD6F4"     # Primary text (soft white)
TEXT_MUTED = "9399B2"    # Muted grey text
TEXT_DARK = "11111B"     # For bright badges

GOLD = "F9E2AF"          # XP / Gold / Level accent
GREEN = "A6E3A1"         # Health / Success / HP
RED = "F38BA8"           # Danger / Graveyard / Expenses
BLUE = "89B4FA"          # Mana / Investments / Info
PURPLE = "CBA6F7"        # Epic Loot / Special

# Standard Styles
font_title = Font(name="Segoe UI", size=18, bold=True, color=GOLD)
font_subtitle = Font(name="Segoe UI", size=11, italic=True, color=TEXT_MUTED)
font_section = Font(name="Segoe UI", size=14, bold=True, color=TEXT_MAIN)
font_card_header = Font(name="Segoe UI", size=11, bold=True, color=GOLD)
font_header = Font(name="Segoe UI", size=11, bold=True, color=TEXT_MAIN)
font_body = Font(name="Segoe UI", size=10, color=TEXT_MAIN)
font_body_bold = Font(name="Segoe UI", size=10, bold=True, color=TEXT_MAIN)
font_muted = Font(name="Segoe UI", size=9, color=TEXT_MUTED)
font_big_val = Font(name="Segoe UI", size=18, bold=True, color=GOLD)
font_big_green = Font(name="Segoe UI", size=18, bold=True, color=GREEN)
font_big_blue = Font(name="Segoe UI", size=18, bold=True, color=BLUE)
font_big_red = Font(name="Segoe UI", size=18, bold=True, color=RED)

fill_dark = PatternFill(start_color=BG_DARK, end_color=BG_DARK, fill_type="solid")
fill_card = PatternFill(start_color=BG_CARD, end_color=BG_CARD, fill_type="solid")
fill_card_head = PatternFill(start_color=BG_CARD_LIGHT, end_color=BG_CARD_LIGHT, fill_type="solid")
fill_gold_badge = PatternFill(start_color=GOLD, end_color=GOLD, fill_type="solid")
fill_green_badge = PatternFill(start_color=GREEN, end_color=GREEN, fill_type="solid")
fill_red_badge = PatternFill(start_color=RED, end_color=RED, fill_type="solid")

thin_border_side = Side(style='thin', color=BORDER_COLOR)
card_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)

align_center = Alignment(horizontal='center', vertical='center', wrap_text=True)
align_left = Alignment(horizontal='left', vertical='center')
align_right = Alignment(horizontal='right', vertical='center')

def style_range(ws, start_col, start_row, end_col, end_row, fill=None, font=None, alignment=None, border=None):
    for r in range(start_row, end_row + 1):
        for c in range(start_col, end_col + 1):
            cell = ws.cell(row=r, column=c)
            if fill: cell.fill = fill
            if font: cell.font = font
            if alignment: cell.alignment = alignment
            if border: cell.border = border

def apply_base_background(ws, max_r=50, max_c=16):
    ws.views.sheetView[0].showGridLines = True
    for r in range(1, max_r + 1):
        for c in range(1, max_c + 1):
            cell = ws.cell(row=r, column=c)
            cell.fill = fill_dark
            cell.font = font_body

# ==========================================
# 1. TAB: QUEST DASHBOARD
# ==========================================
ws1 = wb.active
ws1.title = "🎮 Quest_Dashboard"
apply_base_background(ws1, 45, 12)

# Title Block
ws1.merge_cells("B2:J2")
ws1["B2"] = "⚔️ QUESTLOG: FINANCIAL RPG TRACKER"
ws1["B2"].font = font_title
ws1["B2"].alignment = align_left
ws1.row_dimensions[2].height = 30

ws1.merge_cells("B3:J3")
ws1["B3"] = "Level up your wealth, master your budget & slay unnecessary expenses."
ws1["B3"].font = font_subtitle
ws1["B3"].alignment = align_left
ws1.row_dimensions[3].height = 20

# Card 1: Character Status (B5:E11)
style_range(ws1, 2, 5, 5, 11, fill=fill_card, border=card_border)
style_range(ws1, 2, 5, 5, 5, fill=fill_card_head)
ws1.merge_cells("B5:E5")
ws1["B5"] = "👤 CHARACTER PROFILE"
ws1["B5"].font = font_card_header
ws1["B5"].alignment = align_left

ws1["B6"] = "Hero Name:"
ws1["C6"] = "GoldSeeker"
ws1["B7"] = "Character Class:"
ws1["C7"] = '=IF(C9<5,"🪙 Münz-Knappe", IF(C9<10,"🛡️ Spar-Krieger", IF(C9<20,"⚔️ Zins-Paladin", "👑 Finanz-Grossmeister")))'
ws1["B8"] = "Total XP (Ersparnisse):"
ws1["C8"] = "='⚔️ Monats_Log'!G28"  # Net Savings from Log
ws1["B9"] = "Current Level:"
ws1["C9"] = '=MAX(1, INT(C8/500) + 1)'
ws1["B10"] = "Next Level XP:"
ws1["C10"] = '=C9*500'

for r in range(6, 11):
    ws1.cell(row=r, column=2).font = font_body_bold
    ws1.cell(row=r, column=3).font = font_body
ws1["C9"].font = font_big_val
ws1["C7"].font = font_body_bold

# Card 2: Health & Mana Bars (G5:J11)
style_range(ws1, 7, 5, 10, 11, fill=fill_card, border=card_border)
style_range(ws1, 7, 5, 10, 5, fill=fill_card_head)
ws1.merge_cells("G5:J5")
ws1["G5"] = "❤️ HP & 🔮 MANA GAUGES"
ws1["G5"].font = font_card_header

ws1["G6"] = "HP (Notgroschen):"
ws1["H6"] = 7500
ws1["G7"] = "HP Target (3-6 Mt.):"
ws1["H7"] = 10000
ws1["G8"] = "HP Gauge:"
ws1["G8"].font = font_body_bold
ws1.merge_cells("H8:J8")
ws1["H8"] = '=REPT("🟩", MIN(10, MAX(0, INT((H6/H7)*10)))) & REPT("⬛", 10 - MIN(10, MAX(0, INT((H6/H7)*10)))) & " " & TEXT(H6/H7, "0%")'
ws1["H8"].alignment = align_left
ws1["H8"].font = font_body_bold

ws1["G9"] = "Mana (Depot / Crypto):"
ws1["H9"] = 15200
ws1["G10"] = "Mana Target (Jahr):"
ws1["H10"] = 20000
ws1["G11"] = "Mana Gauge:"
ws1["G11"].font = font_body_bold
ws1.merge_cells("H11:J11")
ws1["H11"] = '=REPT("🟦", MIN(10, MAX(0, INT((H9/H10)*10)))) & REPT("⬛", 10 - MIN(10, MAX(0, INT((H9/H10)*10)))) & " " & TEXT(H9/H10, "0%")'
ws1["H11"].alignment = align_left
ws1["H11"].font = font_body_bold

for r in [6, 7, 9, 10]:
    ws1.cell(row=r, column=7).font = font_body_bold
    ws1.cell(row=r, column=8).font = font_body
    ws1.cell(row=r, column=8).number_format = '#,##0.00 "CHF"'

# Card 3: Aktueller Monats-Status (B13:E19)
style_range(ws1, 2, 13, 5, 19, fill=fill_card, border=card_border)
style_range(ws1, 2, 13, 5, 13, fill=fill_card_head)
ws1.merge_cells("B13:E13")
ws1["B13"] = "🎯 MONATS-QUEST STATUS"
ws1["B13"].font = font_card_header

ws1["B14"] = "Monats-Einnahmen:"
ws1["D14"] = "='⚔️ Monats_Log'!E9"
ws1["B15"] = "Gesamtausgaben:"
ws1["D15"] = "='⚔️ Monats_Log'!E27"
ws1["B16"] = "Ersparnis (XP Loot):"
ws1["D16"] = "='⚔️ Monats_Log'!G28"
ws1["B17"] = "Sparquote:"
ws1["D17"] = "='⚔️ Monats_Log'!G29"

ws1.merge_cells("B18:E18")
ws1["B18"] = "Status:"
ws1["B18"].font = font_body_bold
ws1.merge_cells("B19:E19")
ws1["B19"] = '=IF(D16>=1000, "🏆 QUEST COMPLETE: LEGENDARY SAVER!", IF(D16>0, "⚔️ IN BATTLE: IM PLUS!", "💀 DEFEAT: IM MINUS!"))'
ws1["B19"].font = font_big_val
ws1["B19"].alignment = align_center

for r in [14, 15, 16]:
    ws1.cell(row=r, column=2).font = font_body_bold
    ws1.cell(row=r, column=4).font = font_body_bold
    ws1.cell(row=r, column=4).number_format = '#,##0.00 "CHF"'
ws1["D17"].font = font_body_bold
ws1["D17"].number_format = '0.0%'

# Card 4: Quick Summary Abo-Friedhof (G13:J19)
style_range(ws1, 7, 13, 10, 19, fill=fill_card, border=card_border)
style_range(ws1, 7, 13, 10, 13, fill=fill_card_head)
ws1.merge_cells("G13:J13")
ws1["G13"] = "🪦 QUICK GRAVEYARD STATS"
ws1["G13"].font = font_card_header

ws1["G14"] = "Aktive Abos:"
ws1["I14"] = "=COUNTIF('🪦 Abo_Friedhof'!H8:H25, \"Aktiv\")"
ws1["G15"] = "Beerdigte Abos (Killed):"
ws1["I15"] = "=COUNTIF('🪦 Abo_Friedhof'!H8:H25, \"🪦 Beerdigt\")"
ws1["G16"] = "Laufende Kosten (Jahr):"
ws1["I16"] = "='🪦 Abo_Friedhof'!E5"
ws1["G17"] = "Bereits gerettetes Geld (Jahr):"
ws1["I17"] = "='🪦 Abo_Friedhof'!I5"

for r in [14, 15]:
    ws1.cell(row=r, column=7).font = font_body_bold
    ws1.cell(row=r, column=9).font = font_body_bold
for r in [16, 17]:
    ws1.cell(row=r, column=7).font = font_body_bold
    ws1.cell(row=r, column=9).font = font_big_green if r==17 else font_big_red
    ws1.cell(row=r, column=9).number_format = '#,##0.00 "CHF"'


# ==========================================
# 2. TAB: ABO-FRIEDHOF (Subscription Graveyard)
# ==========================================
ws2 = wb.create_sheet(title="🪦 Abo_Friedhof")
apply_base_background(ws2, 35, 12)

ws2.merge_cells("B2:K2")
ws2["B2"] = "🪦 DER SUBSCRIPTION-FRIEDHOF"
ws2["B2"].font = font_title
ws2.row_dimensions[2].height = 30

ws2.merge_cells("B3:K3")
ws2["B3"] = "Wo unbemerkte monatliche Kleinstbeträge zu gigantischen Vermögenskillern heranwachsen..."
ws2["B3"].font = font_subtitle
ws2.row_dimensions[3].height = 20

# KPI Cards row 5
style_range(ws2, 2, 5, 5, 5, fill=fill_card, border=card_border)
ws2.merge_cells("B5:C5")
ws2["B5"] = "Laufende Kosten/Jahr:"
ws2["B5"].font = font_body_bold
ws2.merge_cells("D5:E5")
ws2["D5"] = '=SUMIF(H8:H25, "Aktiv", F8:F25)'
ws2["D5"].font = font_big_red
ws2["D5"].number_format = '#,##0.00 "CHF"'

style_range(ws2, 7, 5, 10, 5, fill=fill_card, border=card_border)
ws2.merge_cells("G5:H5")
ws2["G5"] = "🏆 Gerettetes Geld/Jahr:"
ws2["G5"].font = font_body_bold
ws2.merge_cells("I5:J5")
ws2["I5"] = '=SUMIF(H8:H25, "🪦 Beerdigt", F8:F25)'
ws2["I5"].font = font_big_green
ws2["I5"].number_format = '#,##0.00 "CHF"'

# Table Headers row 7
headers_abo = [
    ("B", "Dienst / Abo"),
    ("C", "Kategorie"),
    ("D", "Intervall"),
    ("E", "Preis (Mt.)"),
    ("F", "Kosten / Jahr"),
    ("G", "5-Jahres-Grabstein"),
    ("H", "Status"),
    ("I", "Kündigungsfrist"),
    ("J", "Notizen")
]

for col_letter, h_text in headers_abo:
    c = ws2[f"{col_letter}7"]
    c.value = h_text
    c.font = font_header
    c.fill = fill_card_head
    c.alignment = align_center
    c.border = card_border
ws2.row_dimensions[7].height = 25

sample_abos = [
    ("Netflix Premium", "Streaming", "Monatlich", 24.90, "Aktiv", "30 Tage", "Teilen lohnt sich"),
    ("Spotify Family", "Musik", "Monatlich", 20.90, "Aktiv", "Monatlich", "Täglich im Einsatz"),
    ("Fitnesscenter Gym", "Fitness", "Monatlich", 99.00, "Auf Bewährung", "3 Monate vor Ablauf", "War seit 2 Monaten nicht mehr..."),
    ("iCloud 2TB", "Cloud", "Monatlich", 10.00, "Aktiv", "Monatlich", "Backup unverzichtbar"),
    ("Audible Hörbücher", "Unterhaltung", "Monatlich", 14.95, "🪦 Beerdigt", "Sofort", "Gekündigt! Spart 179.40/Jahr"),
    ("Adobe Creative Cloud", "Software", "Monatlich", 65.00, "🪦 Beerdigt", "Jährliche Verlängerung", "Alternative: Affinity Suite"),
    ("HelloFresh Kochbox", "Food", "Monatlich", 120.00, "🪦 Beerdigt", "Wöchentlich pausierbar", "Zu viel Plastikmüll"),
    ("YouTube Premium", "Streaming", "Monatlich", 15.90, "Aktiv", "Monatlich", "Keine Werbung"),
    ("Headspace Meditations-App", "Gesundheit", "Monatlich", 12.50, "Auf Bewährung", "Monatlich", "Nutze ich es wirklich?"),
]

for idx, item in enumerate(sample_abos, start=8):
    ws2[f"B{idx}"] = item[0]
    ws2[f"C{idx}"] = item[1]
    ws2[f"D{idx}"] = item[2]
    ws2[f"E{idx}"] = item[3]
    ws2[f"F{idx}"] = f"=E{idx}*12"
    ws2[f"G{idx}"] = f"=F{idx}*5"
    ws2[f"H{idx}"] = item[4]
    ws2[f"I{idx}"] = item[5]
    ws2[f"J{idx}"] = item[6]
    
    style_range(ws2, 2, idx, 10, idx, fill=fill_card, border=card_border)
    ws2[f"B{idx}"].font = font_body_bold
    for col_l in ["C", "D", "H", "I", "J"]:
        ws2[f"{col_l}{idx}"].font = font_body
        ws2[f"{col_l}{idx}"].alignment = align_left if col_l in ["B","J"] else align_center
    for col_l in ["E", "F", "G"]:
        ws2[f"{col_l}{idx}"].font = font_body_bold
        ws2[f"{col_l}{idx}"].number_format = '#,##0.00 "CHF"'
        ws2[f"{col_l}{idx}"].alignment = align_right
    if item[4] == "🪦 Beerdigt":
        ws2[f"H{idx}"].font = font_body_bold
    ws2.row_dimensions[idx].height = 22

# ==========================================
# 3. TAB: MONATS-LOG (Quest Budget)
# ==========================================
ws3 = wb.create_sheet(title="⚔️ Monats_Log")
apply_base_background(ws3, 40, 10)

ws3.merge_cells("B2:H2")
ws3["B2"] = "⚔️ MONATLICHE BUDGET-QUESTS"
ws3["B2"].font = font_title
ws3.row_dimensions[2].height = 30

ws3.merge_cells("B3:H3")
ws3["B3"] = "Behalte die Kontrolle über deine Ausgaben und schütze dein Mana!"
ws3["B3"].font = font_subtitle
ws3.row_dimensions[3].height = 20

# Section 1: Einnahmen
ws3.merge_cells("B5:E5")
ws3["B5"] = "💰 GOLD-QUELLEN (EINNAHMEN)"
ws3["B5"].font = font_card_header
ws3["B5"].fill = fill_card_head
ws3.merge_cells("F5:G5")
ws3["F5"] = "BETRAG"
ws3["F5"].font = font_card_header
ws3["F5"].fill = fill_card_head
ws3["F5"].alignment = align_right
style_range(ws3, 2, 5, 7, 5, border=card_border)

income_items = [
    ("Haupteinkommen (Lohn netto)", 5800.00),
    ("Side Hustle / Digitales Chrüsimüsi", 450.00),
    ("Dividenden / Zinsen", 75.00),
]
for idx, inc in enumerate(income_items, start=6):
    ws3.merge_cells(f"B{idx}:E{idx}")
    ws3[f"B{idx}"] = inc[0]
    ws3.merge_cells(f"F{idx}:G{idx}")
    ws3[f"F{idx}"] = inc[1]
    style_range(ws3, 2, idx, 7, idx, fill=fill_card, border=card_border)
    ws3[f"B{idx}"].font = font_body
    ws3[f"F{idx}"].font = font_body_bold
    ws3[f"F{idx}"].number_format = '#,##0.00 "CHF"'
    ws3[f"F{idx}"].alignment = align_right

ws3.merge_cells("B9:D9")
ws3["B9"] = "TOTAL GOLD EINNAHMEN:"
ws3["B9"].font = font_body_bold
ws3.merge_cells("E9:G9")
ws3["E9"] = "=SUM(F6:F8)"
ws3["E9"].font = font_big_green
ws3["E9"].number_format = '#,##0.00 "CHF"'
ws3["E9"].alignment = align_right
style_range(ws3, 2, 9, 7, 9, fill=fill_card_head, border=card_border)

# Section 2: Ausgaben & Budget
ws3["B12"] = "Kategorie"
ws3["C12"] = "Budget (Soll)"
ws3["D12"] = "Ist-Ausgaben"
ws3["E12"] = "Differenz"
ws3["F12"] = "Auslastung"
ws3["G12"] = "Status"
for c_l in ["B","C","D","E","F","G"]:
    c = ws3[f"{c_l}12"]
    c.font = font_header
    c.fill = fill_card_head
    c.alignment = align_center
    c.border = card_border
ws3.row_dimensions[12].height = 25

budget_items = [
    ("🏠 Miete & Wohnen", 1650.00, 1650.00),
    ("🏥 Krankenkasse & Gesundheit", 420.00, 420.00),
    ("🛒 Lebensmittel & Haushaltsbedarf", 600.00, 540.00),
    ("🚆 ÖV / Mobilität / Benzin", 250.00, 195.00),
    ("🍽️ Restaurants & Take-Away", 300.00, 360.00),
    ("🎮 Entertainment & Hobbys", 200.00, 150.00),
    ("👕 Shopping & Kleidung", 150.00, 220.00),
    ("🪦 Laufende Abos (aus Friedhof)", 150.00, "='🪦 Abo_Friedhof'!D5/12"),
    ("🛡️ Sparrate Notgroschen", 500.00, 500.00),
    ("🔮 Investitionen (ETF / Depot)", 1000.00, 1000.00),
    ("☕ Kleinkram & Sonstiges", 150.00, 85.00),
]

for idx, (cat, bud, actual) in enumerate(budget_items, start=13):
    ws3[f"B{idx}"] = cat
    ws3[f"C{idx}"] = bud
    ws3[f"D{idx}"] = actual
    ws3[f"E{idx}"] = f"=C{idx}-D{idx}"
    ws3[f"F{idx}"] = f"=D{idx}/C{idx}"
    ws3[f"G{idx}"] = f'=IF(F{idx}>1, "💀 OVERBUDGET", IF(F{idx}>0.85, "⚠️ WARNUNG", "🛡️ SAFE"))'
    
    style_range(ws3, 2, idx, 7, idx, fill=fill_card, border=card_border)
    ws3[f"B{idx}"].font = font_body_bold
    for col_l in ["C", "D", "E"]:
        ws3[f"{col_l}{idx}"].font = font_body
        ws3[f"{col_l}{idx}"].number_format = '#,##0.00 "CHF"'
        ws3[f"{col_l}{idx}"].alignment = align_right
    ws3[f"F{idx}"].font = font_body
    ws3[f"F{idx}"].number_format = '0.0%'
    ws3[f"F{idx}"].alignment = align_center
    ws3[f"G{idx}"].font = font_body_bold
    ws3[f"G{idx}"].alignment = align_center
    ws3.row_dimensions[idx].height = 22

# Totals row 25
last_r = 13 + len(budget_items)
ws3[f"B{last_r}"] = "TOTAL AUSGABEN:"
ws3[f"C{last_r}"] = f"=SUM(C13:C{last_r-1})"
ws3[f"D{last_r}"] = f"=SUM(D13:D{last_r-1})"
ws3[f"E{last_r}"] = f"=SUM(E13:E{last_r-1})"
ws3[f"F{last_r}"] = f"=D{last_r}/C{last_r}"
ws3[f"G{last_r}"] = f'=IF(F{last_r}<=1, "🏆 IM BUDGET", "💀 CRITICAL")'

style_range(ws3, 2, last_r, 7, last_r, fill=fill_card_head, border=card_border)
ws3[f"B{last_r}"].font = font_header
for col_l in ["C", "D", "E"]:
    ws3[f"{col_l}{last_r}"].font = font_header
    ws3[f"{col_l}{last_r}"].number_format = '#,##0.00 "CHF"'
    ws3[f"{col_l}{last_r}"].alignment = align_right
ws3[f"F{last_r}"].font = font_header
ws3[f"F{last_r}"].number_format = '0.0%'
ws3[f"F{last_r}"].alignment = align_center
ws3[f"G{last_r}"].font = font_header
ws3[f"G{last_r}"].alignment = align_center
ws3.row_dimensions[last_r].height = 26

# Monthly Summary Result Card (Rows 27-29)
ws3.merge_cells("B27:D27")
ws3["B27"] = "GESAMTAUSGABEN DIESER MONAT:"
ws3["B27"].font = font_body_bold
ws3.merge_cells("E27:G27")
ws3["E27"] = f"=D{last_r}"
ws3["E27"].font = font_big_red
ws3["E27"].number_format = '#,##0.00 "CHF"'
ws3["E27"].alignment = align_right
style_range(ws3, 2, 27, 7, 27, fill=fill_card, border=card_border)

ws3.merge_cells("B28:D28")
ws3["B28"] = "ERSPARNIS DIESER MONAT (XP REINGEHOLT):"
ws3["B28"].font = font_body_bold
ws3.merge_cells("E28:G28")
ws3["E28"] = f"=E9-E27"
ws3["E28"].font = font_big_green
ws3["E28"].number_format = '#,##0.00 "CHF"'
ws3["E28"].alignment = align_right
style_range(ws3, 2, 28, 7, 28, fill=fill_card, border=card_border)

ws3.merge_cells("B29:D29")
ws3["B29"] = "SPARQUOTE (% DES GOLDES GERETTET):"
ws3["B29"].font = font_body_bold
ws3.merge_cells("E29:G29")
ws3["E29"] = f"=E28/E9"
ws3["E29"].font = font_big_val
ws3["E29"].number_format = '0.0%'
ws3["E29"].alignment = align_right
style_range(ws3, 2, 29, 7, 29, fill=fill_card, border=card_border)


# ==========================================
# 4. TAB: ACHIEVEMENTS (Errungenschaften)
# ==========================================
ws4 = wb.create_sheet(title="🏆 Achievements")
apply_base_background(ws4, 30, 8)

ws4.merge_cells("B2:G2")
ws4["B2"] = "🏆 QUEST ACHIEVEMENTS & TROPHIES"
ws4["B2"].font = font_title
ws4.row_dimensions[2].height = 30

ws4.merge_cells("B3:G3")
ws4["B3"] = "Schalte Trophäen frei, wenn du finanzielle Meilensteine erreichst!"
ws4["B3"].font = font_subtitle
ws4.row_dimensions[3].height = 20

# Trophy Table Headers
ach_headers = [("B", "Icon"), ("C", "Trophäen-Name"), ("D", "Bedingung / Quest"), ("E", "Belohnung"), ("F", "Freigeschaltet?")]
for col_l, text in ach_headers:
    c = ws4[f"{col_l}5"]
    c.value = text
    c.font = font_header
    c.fill = fill_card_head
    c.alignment = align_center
    c.border = card_border
ws4.row_dimensions[5].height = 25

achievements = [
    ("🪓", "Abo-Slayer I", "Kündige mindestens 1 ungenutztes Abo im Friedhof", "+100 XP", "JA"),
    ("⚔️", "Abo-Slayer II", "Kündige 3 oder mehr Abos und spare > 300 CHF/Jahr", "+350 XP", "JA"),
    ("🪙", "Kupfer-Sammler", "Erreiche deine ersten 500 CHF Gesamtersparnis", "+150 XP", "JA"),
    ("🛡️", "Schildwall", "Baue deinen Notgroschen auf mind. 3 Monatsausgaben auf", "+500 XP", "JA"),
    ("🥦", "Rations-Meister", "Bleibe einen Monat lang komplett im Food-Budget", "+200 XP", "JA"),
    ("🏰", "Eiserne Festung", "3 Monate in Folge eine positive Sparquote erzielt", "+600 XP", "NEIN"),
    ("🧙‍♂️", "Zinseszins-Magier", "Ersten ETF-Sparplan eingerichtet & gestartet", "+400 XP", "JA"),
    ("🐉", "Drachenhort", "10'000 CHF Nettovermögen überschritten", "+1'000 XP", "JA"),
    ("👑", "Finanz-Paladin", "Sparquote von über 35% in einem Monat erreicht", "+800 XP", "NEIN"),
    ("⚡", "Prokrastinations-Bann", "Budget am Monatsanfang in unter 15 Min eingetragen", "+100 XP", "JA"),
]

for idx, (icon, name, desc, rew, unlocked) in enumerate(achievements, start=6):
    ws4[f"B{idx}"] = icon
    ws4[f"C{idx}"] = name
    ws4[f"D{idx}"] = desc
    ws4[f"E{idx}"] = rew
    ws4[f"F{idx}"] = unlocked
    
    style_range(ws4, 2, idx, 6, idx, fill=fill_card, border=card_border)
    ws4[f"B{idx}"].font = Font(name="Segoe UI", size=14)
    ws4[f"B{idx}"].alignment = align_center
    ws4[f"C{idx}"].font = font_body_bold
    ws4[f"D{idx}"].font = font_body
    ws4[f"E{idx}"].font = font_body_bold
    ws4[f"E{idx}"].alignment = align_center
    ws4[f"F{idx}"].font = font_body_bold
    ws4[f"F{idx}"].alignment = align_center
    if unlocked == "JA":
        ws4[f"F{idx}"].font = Font(name="Segoe UI", size=10, bold=True, color=GREEN)
    else:
        ws4[f"F{idx}"].font = Font(name="Segoe UI", size=10, bold=True, color=TEXT_MUTED)
    ws4.row_dimensions[idx].height = 24

# Set nice column widths for all sheets
col_widths = {
    ws1: {"A": 4, "B": 22, "C": 20, "D": 18, "E": 18, "F": 4, "G": 22, "H": 20, "I": 18, "J": 18, "K": 4},
    ws2: {"A": 4, "B": 26, "C": 18, "D": 14, "E": 16, "F": 16, "G": 20, "H": 18, "I": 24, "J": 30, "K": 4},
    ws3: {"A": 4, "B": 32, "C": 18, "D": 18, "E": 18, "F": 16, "G": 18, "H": 4},
    ws4: {"A": 4, "B": 8, "C": 24, "D": 48, "E": 14, "F": 16, "G": 4}
}

for sheet, widths in col_widths.items():
    for col_l, width in widths.items():
        sheet.column_dimensions[col_l].width = width

output_path = "/home/iwer/QuestBudget_RPG_Finance_Tracker.xlsx"
wb.save(output_path)
print(f"Successfully generated RPG finance tracker at: {output_path}")
