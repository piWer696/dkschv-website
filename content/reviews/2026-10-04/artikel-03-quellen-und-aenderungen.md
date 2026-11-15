# Prüfbericht – Artikel 03: Datenpanne melden Schweiz

- **Prüfdatum:** 4. Oktober 2026; die tatsächlichen Quellenabrufe erfolgten nach 09:00 Uhr. **Berichts-Stichtag:** 09:00 Uhr, Europe/Zurich. Unversionierte Webseiten sind nicht minutengenau rückdatierbar.
- **Geprüfter Zeitraum:** 20. September 2026 bis einschliesslich 4. Oktober 2026, 09:00 Uhr, Europe/Zurich
- **Gegenstand:** `/wissen/datenpanne-melden-schweiz` und das zugehörige Arbeitsmittel `/resources/03-datenpanne-entscheidungsbaum`
- **Ausgangsstatus:** beide Dateien nicht freigegeben; der Artikel ist ein Entwurf.
- **Prüfumfang:** Im Wartungsmanifest für Artikel 03 genannte Primärquellen (DSG, DSV, EDÖB DataBreach, EDÖB-Leitfaden) sowie die im Artikel und Arbeitsmittel für die BACS-Spur zitierten amtlichen Primärquellen und offiziellen BACS-Meldewegseiten.

## Ergebnis

**Keine materielle Änderung** der dargestellten EDÖB- oder BACS-Meldepflicht im Prüfzeitraum festgestellt. Die fachlichen Aussagen zu Art. 24 DSG, Art. 15 DSV sowie zu den geltenden BACS-Fristen, dem Geltungsbereich, den Meldekriterien und dem Meldeweg bleiben durch die geprüften amtlichen Quellen gedeckt.

Als konkrete, aber **nicht geltende** Entwicklung wurde eine BACS-Mitteilung vom 25. September 2026 ermittelt: Der Bundesrat beauftragte das VBS, bis Juni 2027 eine Vernehmlassungsvorlage für ein neues Cybersicherheitsgesetz auszuarbeiten. Die seit April 2025 geltende ISG-Meldepflicht soll künftig überführt werden. Dies ist keine bereits wirksame Änderung und löst keine Textänderung aus.

Die geprüften Rechtsquellen weisen keine neue Fassung im Prüfzeitraum aus:

- DSG-Chronologie: jüngste ausgewiesene Fassung vom **7. Juli 2025** (Berichtigung).
- DSV: Stand **1. Dezember 2025**; Art. 15 unverändert geprüft.
- ISG: Stand **1. Oktober 2025**.
- CSV: Stand **1. April 2025**.

## Durchgeführte Dateianpassungen

| Datei | Änderung | Begründung |
|---|---|---|
| `/home/ubuntu/dkschv-audit/blog-paket/articles/03-datenpanne-melden-schweiz.md` | Metadaten `rechtsstand` und `stand` von **20. September 2026** auf **4. Oktober 2026** aktualisiert. | Quellenprüfung wurde zum Stichtag durchgeführt; keine materielle Korrektur belegt. |
| `/home/ubuntu/dkschv-audit/blog-paket/resources/03-datenpanne-entscheidungsbaum.md` | `version` und die sichtbare Angabe `Rechtsstand` von **20. September 2026** auf **4. Oktober 2026** aktualisiert. | Quellenprüfung wurde zum Stichtag durchgeführt; keine materielle Korrektur belegt. |

**Nicht verändert:** Slugs, Veröffentlichungsdatum, Status, vollständige Langfassung, Struktur, Quellenverzeichnisse und alle vorhandenen `[FACHPRÜFUNG ERFORDERLICH]`-Marker. Im Artikel bestehen weiterhin 4, im Arbeitsmittel weiterhin 6 solcher Marker. Kein CMS, kein Manifest, kein Freigabestatus und keine weiteren Inhalte wurden verändert.

## Geprüfte Primärquellen und Quellenstände

| Quelle | Echte URL | Abgleich / Quellenstand | Befund für Artikel und Arbeitsmittel |
|---|---|---|---|
| Fedlex – Datenschutzgesetz (DSG), Art. 5 Bst. h und Art. 24 | https://www.fedlex.admin.ch/eli/cc/2022/491/de | Chronologie: https://www.fedlex.admin.ch/eli/cc/2022/491/de/history. Jüngste ausgewiesene Fassung 7. Juli 2025; im Prüfzeitraum keine neue Fassung. | Begriff der Datensicherheitsverletzung, Meldung durch Verantwortlichen «so rasch als möglich» bei voraussichtlich hohem Risiko, Meldung des Auftragsbearbeiters an den Verantwortlichen sowie getrennte Prüfung der Betroffeneninformation sind unverändert gedeckt. |
| Fedlex – Datenschutzverordnung (DSV), Art. 15 | https://www.fedlex.admin.ch/eli/cc/2022/568/de | Stand 1. Dezember 2025; Chronologie: https://www.fedlex.admin.ch/eli/cc/2022/568/de/history. Keine neue Fassung im Prüfzeitraum. | Die aufgezählten Mindestangaben, das rasche Nachreichen fehlender Angaben und die Dokumentationspflicht bleiben gedeckt. |
| EDÖB – DataBreach | https://www.edoeb.admin.ch/de/databreach | Aktuelle abgerufene Seite nennt weiterhin das sichere Online-Formular für Verantwortliche, Download einer Bestätigung und das Portal https://databreach.edoeb.admin.ch/report. | Kein belegter Wechsel des EDÖB-Meldewegs. Die Trennung zwischen Verantwortlichen und Betroffenen bleibt richtig beschrieben. |
| EDÖB – Leitfaden DataBreach | https://www.edoeb.admin.ch/de/leitfaden-data-breach | Mitteilung vom 7. Februar 2025; verweist auf den Leitfaden vom 23. April 2025. | Kein neuer Leitfaden oder neue Version im Prüfzeitraum ermittelt. |
| EDÖB – Leitfaden zur Meldung von Datensicherheitsverletzungen und Information der Betroffenen nach Art. 24 DSG | https://www.edoeb.admin.ch/dam/de/sd-web/T64CAUyvAMcF/1_2%20Leitfaden%20des%20ED%C3%96B%20betreffend%20die%20Meldung%20von%20Datensicherheitsverletzungen%20und%20Information%20der%20Betroffenen%20nach%20Art.%2024%20DSG_DE.pdf | Vom 6. Februar 2025, zuletzt angepasst am 23. April 2025, **Version 1.2**. | Stützt die Aussagen zu hohem Risiko, sofortigen Minderungsmassnahmen, Ransomware, zeitnaher Meldung, Rolle des Auftragsbearbeiters und Betroffeneninformation. Keine abweichende neue Fassung ermittelt. |
| Fedlex – Informationssicherheitsgesetz (ISG), Art. 74a–74f | https://www.fedlex.admin.ch/eli/cc/2022/232/de | Stand 1. Oktober 2025; Chronologie: https://www.fedlex.admin.ch/eli/cc/2022/232/de/history. Keine neue Fassung im Prüfzeitraum. | Art. 74b (Unterstellung), Art. 74d (Meldekriterien), Art. 74e (24 Stunden nach Entdeckung) und Art. 74f (System/Weiterleitung) bestätigen die BACS-Spur. |
| Fedlex – Cybersicherheitsverordnung (CSV), Art. 12, 14–16 | https://www.fedlex.admin.ch/eli/cc/2025/169/de | Stand 1. April 2025; einzige ausgewiesene Fassung seit Inkrafttreten. | CSV-Ausnahmen, Konkretisierung der Kriterien und 14 Tage zur Ergänzung, sofern Angaben binnen der 24 Stunden fehlen, bleiben gedeckt. |
| BACS – Informationen zur Meldepflicht | https://www.bacs.admin.ch/de/informationen-zur-meldepflicht | Aktuelle abgerufene Seite: geltende Meldepflicht seit 1. April 2025; 24 Stunden ab Entdeckung, bei fehlenden Angaben 14 Tage zur Vervollständigung. | Keine Abweichung von den im Artikel und Arbeitsmittel genannten Fristen und Grundzügen. |
| BACS – Wie muss gemeldet werden? | https://www.bacs.admin.ch/de/wie-muss-gemeldet-werden | Aktuelle abgerufene Seite: Meldeformular im Cyber Security Hub (CSH); alternative Meldemöglichkeit und E-Mail-Vorlage über https://www.report.ncsc.admin.ch/de/; Weiterleitung an weitere Behörden auf Wunsch. | Kein belegter Wechsel des BACS-Meldewegs. Der Hinweis, eine Weiterleitung nicht ungeprüft als Erledigung der separaten EDÖB-Prüfung zu behandeln, bleibt sachgerecht. |
| BACS – Wer muss melden? | https://www.bacs.admin.ch/de/wer-muss-melden | Aktuelle abgerufene Seite verweist weiterhin auf Art. 74b ISG und CSV. | Bestätigt, dass die BACS-Pflicht nicht alle Schweizer KMU pauschal trifft. |
| BACS – Was muss gemeldet werden? | https://www.bacs.admin.ch/de/was-muss-gemeldet-werden | Aktuelle abgerufene Seite. | Bestätigt Gefährdung der Funktionsfähigkeit, Manipulation/Abfluss und Erpressung, Drohung oder Nötigung als Kriterien. |
| BACS – Ransomware: Was nun? | https://www.bacs.admin.ch/de/ransomware-was-nun | Aktuelle abgerufene Seite. | Empfehlungen zu Netztrennung, Log-Sicherung sowie Sicherung von Zwischenspeicher und Festplatten vor Reparaturversuchen/Neustarts bleiben gedeckt. |
| BACS – Medienmitteilung zum geplanten Cybersicherheitsgesetz | https://www.bacs.admin.ch/de/newnsb/zX9oNK8tuI-Z | Veröffentlicht am 25. September 2026. | Ausschliesslich Planung: Vernehmlassungsvorlage bis Juni 2027. Keine aktuelle Änderung der im Beitrag dargestellten Meldepflicht. |

## Fachlicher Abgleich der zentralen Trigger

| Aussage / Trigger | Prüfergebnis |
|---|---|
| EDÖB-Meldung nur bei voraussichtlich hohem Risiko; keine fixe 72-Stunden-Frist im DSG | Unverändert richtig nach Art. 24 Abs. 1 DSG und EDÖB-Leitfaden Version 1.2. |
| Auftragsbearbeiter meldet Verletzungen so rasch als möglich dem Verantwortlichen | Unverändert richtig nach Art. 24 Abs. 3 DSG; der EDÖB-Leitfaden präzisiert, dass diese Information nicht von der Risikoabwägung abhängt. |
| DSV-Angaben und rasches Nachreichen | Unverändert richtig nach Art. 15 Abs. 1–2 DSV. |
| BACS: 24 Stunden ab Entdeckung, bei unvollständiger Erstmeldung 14 Tage zur Ergänzung | Unverändert richtig; Art. 74e Abs. 1 ISG und Art. 16 CSV sowie BACS-Informationen. |
| BACS-Unterstellung und Cyberangriff getrennt prüfen | Unverändert richtig; Art. 74b–74d ISG und Art. 12 CSV. |
| EDÖB- und BACS-Meldung können parallel bestehen | Unverändert richtig. Die BACS-Systemweiterleitung ist optional; sie ersetzt nicht die separate fachliche Prüfung der jeweils einschlägigen Pflicht. |

## Nicht verifizierte Punkte und Grenzen der Prüfung

1. **Änderungshistorien behördlicher Webseiten:** Für DataBreach, die BACS-Meldewegseiten und die Ransomware-Seite liegt auf den abgerufenen Seiten keine vollständige, maschinenlesbare Versions- oder Änderungshistorie für den Zeitraum 20. September bis 4. Oktober 2026 vor. Es wurde der aktuelle Originalinhalt abgerufen und gegen die im Entwurf verwendeten Aussagen geprüft. Eine lückenlose Negativfeststellung zu jeder rein redaktionellen Webseitenänderung ist damit nicht möglich.
2. **Konkreter Einzelfall:** Die Unterstellung nach Art. 74b ISG, CSV-Ausnahmen, die Einordnung als Cyberangriff, das voraussichtlich hohe Risiko nach Art. 24 DSG, die Betroffeneninformation, sektorspezifische Pflichten sowie vertragliche Pflichten sind ohne konkrete Tatsachen nicht entscheidbar. Die vorhandenen `[FACHPRÜFUNG ERFORDERLICH]`-Marker bleiben deshalb unverändert erforderlich.
3. **URL-Verfügbarkeit nach dem Prüfzeitpunkt:** Die genannten Originalseiten wurden während der Prüfung abgerufen. Eine Erreichbarkeit zu einem späteren Veröffentlichungszeitpunkt wird nicht zugesichert und ist vor Veröffentlichung erneut zu prüfen.
4. **Geplantes Cybersicherheitsgesetz:** Die BACS-Mitteilung vom 25. September 2026 dokumentiert eine künftige Gesetzesvorlage, nicht bereits geltendes Recht. Sie darf nicht als gegenwärtige Pflichtänderung dargestellt werden; spätere Vernehmlassungs- oder Inkrafttretensschritte bleiben nachzuverfolgen.

## Klare Blocker vor Veröffentlichung

1. **Keine fachliche Freigabe:** Artikel und Arbeitsmittel tragen weiterhin den Status «nicht freigegeben» und enthalten zwingende `[FACHPRÜFUNG ERFORDERLICH]`-Marker. Eine datenschutz- und gegebenenfalls sektorrechtliche Fachprüfung/Freigabe steht aus.
2. **Vor konkretem Meldefall:** Die Meldepflicht darf nicht allein anhand dieses allgemeinen Beitrags entschieden werden. Zuständigkeit, BACS-Unterstellung/CSV-Ausnahme, Angriffstatbestand, Risiko für Betroffene, weitere Aufsichtspflichten und geeignete Kommunikation sind zeitnah anhand des konkreten Sachverhalts zu prüfen.
3. **Vor technischer Veröffentlichung:** EDÖB-DataBreach-Portal, BACS-Meldeweg, Weiterleitungsumfang und die verlinkten Originalquellen erneut prüfen; die Prüfung vom 4. Oktober 2026 ersetzt keine spätere Erreichbarkeitsprüfung.
4. **Artikel 01 bleibt unberührt:** Die terminliche Fälligkeit des Artikels 01 seit 1. Oktober 2026 und dessen fehlende Freigabe wurden nicht als Anlass für eine Veröffentlichung oder sonstige Änderung behandelt.

## Veröffentlichungs- und CMS-Status

**Keine Veröffentlichung veranlasst. Kein CMS wurde geöffnet oder geändert. Kein Freigabestatus wurde verändert.**
