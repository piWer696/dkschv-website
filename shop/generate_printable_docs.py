#!/usr/bin/env python3
"""
DKSchV.CH // Generator für druckfertige Vorlagen (Printable HTML / PDF)
Generiert aus den Markdown-Dateien elegante, druckreife Schweizer Dokumente
mit offiziellem DKSchV-Header, Wasserzeichen und Unterschriftenfeldern.
"""

import os
import re

TEMPLATES_DIR = "/home/kali/dkschv-shop/templates"
OUTPUT_DIR = "/home/kali/dkschv-shop/templates_printable"
os.makedirs(OUTPUT_DIR, exist_ok=True)

HTML_SHELL = """<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <title>{title} // DKSchV Schweiz</title>
  <style>
    @page {{
      size: A4;
      margin: 20mm 15mm 20mm 15mm;
      @bottom-right {{
        content: "Seite " counter(page) " von " counter(pages);
      }}
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      color: #1e293b;
      line-height: 1.55;
      font-size: 10pt;
      background: #f8fafc;
      padding: 2rem 0;
    }}
    .document-page {{
      background: #ffffff;
      width: 210mm;
      min-height: 297mm;
      margin: 0 auto;
      padding: 25mm 20mm;
      box-shadow: 0 4px 20px rgba(0,0,0,0.08);
      box-sizing: border-box;
      position: relative;
    }}
    .doc-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 2px solid #0f172a;
      padding-bottom: 1rem;
      margin-bottom: 1.5rem;
    }}
    .brand-title {{
      font-size: 16pt;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.5px;
    }}
    .brand-accent {{ color: #dc2626; }}
    .brand-sub {{
      font-size: 8pt;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .header-meta {{
      text-align: right;
      font-size: 8pt;
      color: #475569;
    }}
    .badge-swiss {{
      display: inline-block;
      background: #fee2e2;
      color: #991b1b;
      border: 1px solid #fca5a5;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 8pt;
      font-weight: 700;
      margin-bottom: 4px;
    }}
    h1 {{ font-size: 16pt; color: #0f172a; margin-top: 1.5rem; margin-bottom: 0.8rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.4rem; }}
    h2 {{ font-size: 13pt; color: #1e293b; margin-top: 1.3rem; margin-bottom: 0.6rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 0.3rem; }}
    h3 {{ font-size: 11pt; color: #334155; margin-top: 1rem; margin-bottom: 0.4rem; }}
    p, ul, ol {{ margin-bottom: 0.8rem; }}
    ul, ol {{ padding-left: 1.5rem; }}
    li {{ margin-bottom: 0.3rem; }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 1rem 0;
      font-size: 9pt;
    }}
    th, td {{
      border: 1px solid #cbd5e1;
      padding: 6px 10px;
      text-align: left;
    }}
    th {{
      background-color: #f1f5f9;
      color: #0f172a;
      font-weight: 700;
    }}
    tr:nth-child(even) {{ background-color: #f8fafc; }}
    .alert-box {{
      background: #fff1f2;
      border-left: 4px solid #e11d48;
      padding: 10px 14px;
      border-radius: 0 6px 6px 0;
      margin: 1rem 0;
      font-size: 9.5pt;
    }}
    .signature-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
      margin-top: 2.5rem;
      padding-top: 1rem;
      border-top: 1px dashed #cbd5e1;
    }}
    .sig-line {{
      border-bottom: 1px solid #475569;
      height: 40px;
      margin-bottom: 6px;
    }}
    .sig-label {{ font-size: 8pt; color: #64748b; text-transform: uppercase; }}
    .print-bar {{
      max-width: 210mm;
      margin: 0 auto 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #0f172a;
      color: #fff;
      padding: 0.8rem 1.5rem;
      border-radius: 8px;
    }}
    .btn-print {{
      background: #10b981;
      color: #042f2e;
      border: none;
      padding: 0.5rem 1.2rem;
      border-radius: 6px;
      font-weight: 700;
      cursor: pointer;
      font-size: 9pt;
    }}
    @media print {{
      body {{ background: none; padding: 0; }}
      .print-bar {{ display: none; }}
      .document-page {{
        box-shadow: none;
        padding: 0;
        width: 100%;
      }}
    }}
  </style>
</head>
<body>

  <div class="print-bar">
    <div><strong>DKSchV Schweiz</strong> // Druck- & Exportansicht für KMU</div>
    <button class="btn-print" onclick="window.print()">🖨️ Jetzt als PDF speichern / Drucken</button>
  </div>

  <div class="document-page">
    <div class="doc-header">
      <div>
        <div class="brand-title">DKSchV<span class="brand-accent">.CH</span></div>
        <div class="brand-sub">Dini Cyber-Security & Datenschutz Schweiz</div>
      </div>
      <div class="header-meta">
        <div class="badge-swiss">🇨🇭 Schweizer KMU Standard</div>
        <div>Dokumenten-Nr.: CH-SEC-2026</div>
        <div>DKSchV Dini // Naters (Wallis)</div>
      </div>
    </div>

    <div class="doc-body">
      {content}
    </div>
  </div>

</body>
</html>
"""

def md_to_html(md_text):
    # Einfache Markdown-Umwandlung für saubere Druckausgabe
    html = md_text
    
    # Alert Boxes
    html = re.sub(r'> \[!(CAUTION|WARNING|IMPORTANT)\]\n> (.*?)\n', r'<div class="alert-box"><strong>ACHTUNG:</strong> \2</div>', html, flags=re.DOTALL)
    html = re.sub(r'> \[!(NOTE|TIP)\]\n> (.*?)\n', r'<div class="alert-box" style="background:#eff6ff; border-color:#3b82f6;"><strong>HINWEIS:</strong> \2</div>', html, flags=re.DOTALL)
    
    # Headers
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.M)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.M)
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.M)
    
    # Bold / Italic
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # Tables
    lines = html.split('\n')
    in_table = False
    table_lines = []
    new_lines = []
    
    for line in lines:
        if line.strip().startswith('|') and line.strip().endswith('|'):
            if not in_table:
                in_table = True
                table_lines = [line]
            else:
                table_lines.append(line)
        else:
            if in_table:
                # Render table
                in_table = False
                headers = [c.strip() for c in table_lines[0].split('|')[1:-1]]
                rows = []
                for row_line in table_lines[2:]:
                    cells = [c.strip() for c in row_line.split('|')[1:-1]]
                    rows.append(cells)
                t_html = '<table><thead><tr>'
                for h in headers:
                    t_html += f'<th>{h}</th>'
                t_html += '</tr></thead><tbody>'
                for r in rows:
                    t_html += '<tr>'
                    for c in r:
                        t_html += f'<td>{c}</td>'
                    t_html += '</tr>'
                t_html += '</tbody></table>'
                new_lines.append(t_html)
                table_lines = []
            new_lines.append(line)
            
    html = '\n'.join(new_lines)
    
    # Lists
    html = re.sub(r'^- \[[ x]\] (.*?)$', r'<li>☐ \1</li>', html, flags=re.M)
    html = re.sub(r'^- (.*?)$', r'<li>\1</li>', html, flags=re.M)
    
    # Paragraphs
    paragraphs = html.split('\n\n')
    processed_p = []
    for p in paragraphs:
        p = p.strip()
        if not p.startswith('<') and p:
            processed_p.append(f'<p>{p}</p>')
        else:
            processed_p.append(p)
    return '\n'.join(processed_p)

# Konvertiere alle 4 Templates
for fname in os.listdir(TEMPLATES_DIR):
    if fname.endswith(".md"):
        path = os.path.join(TEMPLATES_DIR, fname)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        title = fname.replace(".md", "").replace("_", " ")
        body_html = md_to_html(content)
        
        # Anfügen der Unterschriftenzeile für offizielle Dokumente
        body_html += """
        <div class="signature-grid">
          <div>
            <div class="sig-line"></div>
            <div class="sig-label">Ort, Datum & Unterschrift Geschäftsleitung</div>
          </div>
          <div>
            <div class="sig-line"></div>
            <div class="sig-label">Ort, Datum & Unterschrift IT- / Datenschutzverantwortlicher</div>
          </div>
        </div>
        """
        
        full_html = HTML_SHELL.format(title=title, content=body_html)
        out_name = fname.replace(".md", ".html")
        out_path = os.path.join(OUTPUT_DIR, out_name)
        with open(out_path, "w", encoding="utf-8") as out:
            out.write(full_html)
        print(f"Generiert: {out_path}")

print("Alle druckfertigen Vorlagen erfolgreich erzeugt!")
