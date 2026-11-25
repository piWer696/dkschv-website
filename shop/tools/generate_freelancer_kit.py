import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# Styling Palette (Schweizer Eleganz: Minimalistisch, Swiss Navy, Slate & Clean White)
NAVY = "1B2A4A"        # Deep Swiss Navy
SLATE = "4A5568"       # Elegant neutral grey
BG_LIGHT = "F8FAFC"    # Soft off-white
BG_CARD = "EDF2F7"     # Card grey
ACCENT_RED = "DC2626"  # Subtle Swiss Red Accent for badges/status
ACCENT_GREEN = "16A34A"# Paid status
BORDER_COLOR = "CBD5E1"# Crisp border

font_title = Font(name="Arial", size=18, bold=True, color=NAVY)
font_subtitle = Font(name="Arial", size=10, italic=True, color=SLATE)
font_header = Font(name="Arial", size=10, bold=True, color="FFFFFF")
font_subhead = Font(name="Arial", size=11, bold=True, color=NAVY)
font_body = Font(name="Arial", size=10, color="1E293B")
font_body_bold = Font(name="Arial", size=10, bold=True, color="1E293B")
font_muted = Font(name="Arial", size=9, color=SLATE)
font_total = Font(name="Arial", size=12, bold=True, color=NAVY)

fill_navy = PatternFill(start_color=NAVY, end_color=NAVY, fill_type="solid")
fill_light = PatternFill(start_color=BG_LIGHT, end_color=BG_LIGHT, fill_type="solid")
fill_card = PatternFill(start_color=BG_CARD, end_color=BG_CARD, fill_type="solid")

thin_border = Border(
    left=Side(style='thin', color=BORDER_COLOR),
    right=Side(style='thin', color=BORDER_COLOR),
    top=Side(style='thin', color=BORDER_COLOR),
    bottom=Side(style='thin', color=BORDER_COLOR)
)
bottom_heavy_border = Border(
    bottom=Side(style='medium', color=NAVY),
    top=Side(style='thin', color=BORDER_COLOR)
)

align_left = Alignment(horizontal='left', vertical='center')
align_right = Alignment(horizontal='right', vertical='center')
align_center = Alignment(horizontal='center', vertical='center')

def style_box(ws, start_c, start_r, end_c, end_r, fill=None, font=None, align=None, border=None):
    for r in range(start_r, end_r + 1):
        for c in range(start_c, end_c + 1):
            cell = ws.cell(row=r, column=c)
            if fill: cell.fill = fill
            if font: cell.font = font
            if align: cell.alignment = align
            if border: cell.border = border

# ==========================================
# 1. TAB: RECHNUNGS-VORLAGE (Schweiz, CHF, MwSt 8.1%)
# ==========================================
ws_inv = wb.active
ws_inv.title = "📑 Rechnungs_Vorlage"
ws_inv.views.sheetView[0].showGridLines = True

# Header & Sender Info (Links)
ws_inv["B2"] = "MUSTER STUDIO GMBH"
ws_inv["B2"].font = font_title
ws_inv["B3"] = "Digital Design & Consulting\nBahnhofstrasse 10\n8001 Zürich\nSchweiz"
ws_inv["B3"].font = font_muted
ws_inv["B3"].alignment = Alignment(wrap_text=True)

# Sender Metadaten (Rechts)
ws_inv["G2"] = "RECHNUNG"
ws_inv["G2"].font = Font(name="Arial", size=20, bold=True, color=NAVY)
ws_inv["G2"].alignment = align_right

ws_inv["F4"] = "Rechnungs-Nr.:"
ws_inv["G4"] = "RE-2026-001"
ws_inv["F5"] = "Rechnungsdatum:"
ws_inv["G5"] = "20.11.2026"
ws_inv["F6"] = "Fälligkeitsdatum:"
ws_inv["G6"] = "20.12.2026 (30 Tage)"
ws_inv["F7"] = "MwSt-Nummer:"
ws_inv["G7"] = "CHE-123.456.789 MWST"

for r in range(4, 8):
    ws_inv[f"F{r}"].font = font_muted
    ws_inv[f"F{r}"].alignment = align_right
    ws_inv[f"G{r}"].font = font_body_bold
    ws_inv[f"G{r}"].alignment = align_right

# Empfänger Info
ws_inv["B6"] = "RECHNUNGSEMPFÄNGER:"
ws_inv["B6"].font = font_muted
ws_inv["B7"] = "Kunde AG\nFrau Sandra Meier\nBundesplatz 12\n3005 Bern"
ws_inv["B7"].font = font_body
ws_inv["B7"].alignment = Alignment(wrap_text=True)

# Betreff
ws_inv["B10"] = "Projekt: Redesign Firmen-Website & SEO-Setup"
ws_inv["B10"].font = Font(name="Arial", size=12, bold=True, color=NAVY)

# Positions-Tabelle (Row 12)
pos_headers = [("B", "Pos"), ("C", "Beschreibung der Dienstleistung"), ("D", "Menge"), ("E", "Einheit"), ("F", "Ansatz (CHF)"), ("G", "Betrag (CHF)")]
for col_l, text in pos_headers:
    cell = ws_inv[f"{col_l}12"]
    cell.value = text
    cell.font = font_header
    cell.fill = fill_navy
    cell.alignment = align_right if col_l in ["D","F","G"] else align_left
ws_inv.row_dimensions[12].height = 24

positions = [
    (1, "Konzeption & UI/UX Wireframing", 12.5, "Stunden", 140.00),
    (2, "Frontend-Entwicklung & Mobile Optimierung", 28.0, "Stunden", 140.00),
    (3, "SEO-Grundoptimierung & Performance Tuning", 1.0, "Pauschal", 650.00),
    (4, "Hosting-Setup & Domain-Konfiguration", 2.0, "Stunden", 140.00),
]

for idx, p in enumerate(positions, start=13):
    ws_inv[f"B{idx}"] = p[0]
    ws_inv[f"C{idx}"] = p[1]
    ws_inv[f"D{idx}"] = p[2]
    ws_inv[f"E{idx}"] = p[3]
    ws_inv[f"F{idx}"] = p[4]
    ws_inv[f"G{idx}"] = f"=D{idx}*F{idx}"
    
    style_box(ws_inv, 2, idx, 7, idx, border=thin_border)
    ws_inv[f"B{idx}"].alignment = align_center
    ws_inv[f"C{idx}"].alignment = align_left
    ws_inv[f"D{idx}"].alignment = align_right
    ws_inv[f"D{idx}"].number_format = '#,##0.0'
    ws_inv[f"E{idx}"].alignment = align_center
    ws_inv[f"F{idx}"].alignment = align_right
    ws_inv[f"F{idx}"].number_format = '#,##0.00'
    ws_inv[f"G{idx}"].alignment = align_right
    ws_inv[f"G{idx}"].number_format = '#,##0.00'
    ws_inv[f"G{idx}"].font = font_body_bold
    ws_inv.row_dimensions[idx].height = 22

# Totals Block (Rows 18-22)
ws_inv["F18"] = "Zwischensumme Netto:"
ws_inv["G18"] = "=SUM(G13:G16)"
ws_inv["F19"] = "MwSt (8.1% CH-Normalsatz):"
ws_inv["G19"] = "=G18*0.081"
ws_inv["F20"] = "Rundungsdifferenz (5 Rappen):"
ws_inv["G20"] = "=MROUND(G18+G19, 0.05) - (G18+G19)"
ws_inv["F21"] = "GESAMTBETRAG (CHF):"
ws_inv["G21"] = "=MROUND(G18+G19, 0.05)"

for r in range(18, 21):
    ws_inv[f"F{r}"].font = font_body
    ws_inv[f"F{r}"].alignment = align_right
    ws_inv[f"G{r}"].font = font_body
    ws_inv[f"G{r}"].alignment = align_right
    ws_inv[f"G{r}"].number_format = '#,##0.00'

ws_inv["F21"].font = font_total
ws_inv["F21"].alignment = align_right
ws_inv["G21"].font = font_total
ws_inv["G21"].alignment = align_right
ws_inv["G21"].number_format = '#,##0.00 "CHF"'
style_box(ws_inv, 6, 21, 7, 21, fill=fill_card, border=bottom_heavy_border)

# Footer & Bankangaben (Für QR-Rechnung Vorbereitung)
ws_inv["B24"] = "ZAHLUNGSINFORMATIONEN (SCHWEIZ):"
ws_inv["B24"].font = font_subhead
ws_inv["B25"] = "Bank: Zürcher Kantonalbank (ZKB)\nIBAN: CH93 0070 0110 0000 0000 0\nKonto lautend auf: Muster Studio GmbH\nZahlungszweck: RE-2026-001\nZahlungsfrist: 30 Tage netto ohne Abzug"
ws_inv["B25"].font = font_body
ws_inv["B25"].alignment = Alignment(wrap_text=True)

# ==========================================
# 2. TAB: STUNDENERFASSUNG (Timesheet)
# ==========================================
ws_time = wb.create_sheet(title="⏱️ Stundenerfassung")
ws_time.views.sheetView[0].showGridLines = True

ws_time["B2"] = "⏱️ ZEITERFASSUNG & PROJEKT-STUNDEN"
ws_time["B2"].font = font_title
ws_time["B3"] = "Erfasse deine Stunden taggenau. Berechnet automatisch verrechenbare Beträge."
ws_time["B3"].font = font_subtitle

time_headers = [("B", "Datum"), ("C", "Kunde / Projekt"), ("D", "Tätigkeit"), ("E", "Stunden"), ("F", "Stundensatz (CHF)"), ("G", "Total Betrag (CHF)"), ("H", "Abrechnungs-Status")]
for col_l, t_text in time_headers:
    c = ws_time[f"{col_l}5"]
    c.value = t_text
    c.font = font_header
    c.fill = fill_navy
    c.alignment = align_right if col_l in ["E","F","G"] else align_left
ws_time.row_dimensions[5].height = 24

sample_time = [
    ("12.11.2026", "Kunde AG", "Kickoff & Anforderungsanalyse", 3.0, 140.00, "Verrechnet"),
    ("13.11.2026", "Kunde AG", "Wireframes Figma", 5.5, 140.00, "Verrechnet"),
    ("14.11.2026", "Kunde AG", "Feedback-Schleife Wireframes", 2.0, 140.00, "Verrechnet"),
    ("17.11.2026", "Kunde AG", "Code Setup Next.js & Tailwind", 8.0, 140.00, "Verrechnet"),
    ("18.11.2026", "Kunde AG", "Responsive Mobile Anpassungen", 6.0, 140.00, "Verrechnet"),
    ("19.11.2026", "Muster Corp", "Beratung KI-Automatisierung", 4.0, 160.00, "Offen"),
    ("20.11.2026", "Muster Corp", "Workflow-Script Erstellung", 3.5, 160.00, "Offen"),
]

for idx, st in enumerate(sample_time, start=6):
    ws_time[f"B{idx}"] = st[0]
    ws_time[f"C{idx}"] = st[1]
    ws_time[f"D{idx}"] = st[2]
    ws_time[f"E{idx}"] = st[3]
    ws_time[f"F{idx}"] = st[4]
    ws_time[f"G{idx}"] = f"=E{idx}*F{idx}"
    ws_time[f"H{idx}"] = st[5]
    
    style_box(ws_time, 2, idx, 8, idx, border=thin_border)
    ws_time[f"B{idx}"].alignment = align_center
    ws_time[f"C{idx}"].alignment = align_left
    ws_time[f"D{idx}"].alignment = align_left
    ws_time[f"E{idx}"].alignment = align_right
    ws_time[f"E{idx}"].number_format = '#,##0.0'
    ws_time[f"F{idx}"].alignment = align_right
    ws_time[f"F{idx}"].number_format = '#,##0.00'
    ws_time[f"G{idx}"].alignment = align_right
    ws_time[f"G{idx}"].number_format = '#,##0.00'
    ws_time[f"G{idx}"].font = font_body_bold
    ws_time[f"H{idx}"].alignment = align_center
    if st[5] == "Offen":
        ws_time[f"H{idx}"].font = Font(name="Arial", size=10, bold=True, color=ACCENT_RED)
    else:
        ws_time[f"H{idx}"].font = Font(name="Arial", size=10, bold=True, color=ACCENT_GREEN)
    ws_time.row_dimensions[idx].height = 22

# ==========================================
# 3. TAB: JAHRES-ÜBERSICHT & MWST-DASHBOARD
# ==========================================
ws_dash = wb.create_sheet(title="📊 Jahres_Dashboard")
ws_dash.views.sheetView[0].showGridLines = True

ws_dash["B2"] = "📊 JAHRES-DASHBOARD & MWST-RÜCKSTELLUNG"
ws_dash["B2"].font = font_title
ws_dash["B3"] = "Finanzielle Übersicht für Schweizer Selbstständige & Einzelunternehmen."
ws_dash["B3"].font = font_subtitle

# KPI Cards row 5
cards = [
    ("B5:C6", "Total verrechnete Stunden:", "=SUM('⏱️ Stundenerfassung'!E6:E12)", '#,##0.0 "Std"'),
    ("D5:E6", "Total Umsatz Netto (CHF):", "=SUM('⏱️ Stundenerfassung'!G6:G12)", '#,##0.00 "CHF"'),
    ("F5:G6", "Offene Forderungen (CHF):", "=SUMIF('⏱️ Stundenerfassung'!H6:H12, \"Offen\", '⏱️ Stundenerfassung'!G6:G12)", '#,##0.00 "CHF"'),
    ("H5:I6", "MwSt-Rückstellung (8.1%):", "=D5*0.081", '#,##0.00 "CHF"')
]

for pos, label, form, num_fmt in cards:
    start_c, start_r = pos.split(":")[0][0], int(pos.split(":")[0][1:])
    end_c, end_r = pos.split(":")[1][0], int(pos.split(":")[1][1:])
    
    ws_dash[f"{start_c}5"] = label
    ws_dash[f"{start_c}5"].font = font_muted
    ws_dash[f"{start_c}6"] = form
    ws_dash[f"{start_c}6"].font = font_total
    ws_dash[f"{start_c}6"].number_format = num_fmt
    
    c_start_num = ord(start_c) - 64
    c_end_num = ord(end_c) - 64
    style_box(ws_dash, c_start_num, 5, c_end_num, 6, fill=fill_card, border=thin_border)

# Set Clean Column Widths
widths_inv = {"A": 4, "B": 8, "C": 42, "D": 12, "E": 14, "F": 22, "G": 22, "H": 4}
widths_time = {"A": 4, "B": 14, "C": 22, "D": 38, "E": 12, "F": 20, "G": 22, "H": 20, "I": 4}
widths_dash = {"A": 4, "B": 18, "C": 18, "D": 18, "E": 18, "F": 18, "G": 18, "H": 18, "I": 18, "J": 4}

for col_l, w in widths_inv.items(): ws_inv.column_dimensions[col_l].width = w
for col_l, w in widths_time.items(): ws_time.column_dimensions[col_l].width = w
for col_l, w in widths_dash.items(): ws_dash.column_dimensions[col_l].width = w

out_file = "/home/iwer/Swiss_Freelancer_Starterkit_CHF.xlsx"
wb.save(out_file)
print(f"Successfully generated Swiss Freelancer Starterkit at: {out_file}")
