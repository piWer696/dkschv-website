# Prüfbericht – Artikel 03: Datenpanne melden Schweiz

- **Prüfdatum:** 18. Oktober 2026, ISO-Woche 42. Die Quellenabrufe erfolgten am 18. Oktober 2026 nach 09:00 Uhr Europe/Zurich; die direkte HTTP-Erreichbarkeitsprüfung der in Artikel und Arbeitsmittel verwendeten Originalquellen lief von **09:09 bis 09:10 Uhr CEST**.
- **Geprüfter Änderungszeitraum:** 4. Oktober 2026, nach 09:00 Uhr, bis 18. Oktober 2026, nach 09:00 Uhr, Europe/Zurich.
- **Gegenstand:** `/wissen/datenpanne-melden-schweiz` und `/resources/03-datenpanne-entscheidungsbaum`.
- **Verbindliche Grundlage:** Wartungsmanifest, beide vollständigen Entwurfsdateien, Laufstatus und Vorwochenausgabe vom 11. Oktober 2026.
- **Ergebnis:** Alle **11 unterschiedlichen externen Quellenreferenzen** der beiden Dateien wurden am Original abgerufen und auf Erreichbarkeit sowie die konkret verwendeten Aussagen geprüft. `all_references_verified=true` ist damit sachlich gerechtfertigt. Die Prüfung ist **keine individuelle Rechts-, Forensik-, Tenant- oder sektorspezifische Freigabe**.

## Ergebnis seit 4. Oktober 2026

Die manifestierten Primärquellen – DSG, DSV, EDÖB DataBreach und EDÖB-Leitfaden – wurden zuerst geprüft. Die Fedlex-Historien weisen für DSG, DSV, ISG und CSV **keine neue geltende Fassung seit dem vorigen Review** aus. Art. 24 DSG, Art. 15 DSV, die BACS-Meldepflicht nach ISG und die CSV-Regelungen zur Ergänzung bleiben im geprüften Umfang unverändert.[1] [2] [5] [6]

Die BACS-Seiten bestätigen weiterhin die Erstmeldung meldepflichtiger Cyberangriffe innert 24 Stunden nach Entdeckung und den getrennten EDÖB-Meldeweg.[7] [8] Präzisiert wurde die Formulierung zur Ergänzung: Nach Art. 16 CSV **gewährt das BACS** bei innerhalb der 24 Stunden fehlenden Angaben eine Frist von 14 Tagen. Die frühere Formulierung «fehlende Angaben sind innert 14 Tagen nachzureichen» war im Ergebnis nicht widersprüchlich, aber weniger genau.[6]

Der verpflichtend einbezogene BACS-Wochenrückblick vom 6. Oktober 2026 bringt keine neue Meldepflicht. Er trennt jedoch klar zwischen einem Schadsoftwareverdacht und einem bestätigten Angriff: Ein einzelnes Anzeichen beweist keine Infektion; mehrere ungewöhnliche Beobachtungen rechtfertigen eine Untersuchung. Diese eng begrenzte, operative Klarstellung wurde mit neuer Quellenreferenz übernommen.[11]

Der BACS-Beitrag vom 5. Oktober 2026 zu Oversharing wurde als Pflichtquelle für Artikel 09 geprüft. Er enthält keine neue Regel oder Meldepflicht für Artikel 03 und wurde deshalb **nicht** als ungenutzte Referenz in Artikel oder Arbeitsmittel eingefügt.[12] Die aktuelle BACS-Übersicht «Im Fokus» wurde ebenfalls geprüft: Die Einträge vom 12., 13. und 15. Oktober sind für die Meldewege dieses Artikels nicht einschlägig; der KI-Beitrag vom 16. Oktober gehört inhaltlich zu Artikel 09, nicht zu diesem Artikel.[13] [14]

## Geprüfte Originalquellen und Erreichbarkeit

| Nr. | Originalquelle und exakte URL | Belegter Quellenstand | Abruf 18.10.2026 nach 09:00 | Erreichbarkeit und Befund |
|---:|---|---|---|---|
| 1 | DSG, [Fedlex ELI 2022/491][1] | Geltende Fassung: **Stand 7. Juli 2025**; Chronologie nennt als letzten Eintrag eine Berichtigung per 7. Juli 2025. | 09:04–09:10 CEST | **Erreichbar, HTTP 200.** Art. 5 und Art. 24 decken Definition, hohes Risiko, «so rasch als möglich», Auftragsbearbeitung und Betroffeneninformation. |
| 2 | DSV, [Fedlex ELI 2022/568][2] | Geltende Fassung: **Stand 1. Dezember 2025**; letzte ausgewiesene Fassung 1. Dezember 2025. | 09:04–09:10 CEST | **Erreichbar, HTTP 200.** Art. 15 deckt Meldungsinhalt und rasches Nachreichen. |
| 3 | EDÖB DataBreach, [Meldeportal-Information][3] | Undatierte aktuelle Behördenseite; verlinkt den Leitfaden Version 1.2 vom 23. April 2025. | 09:04–09:10 CEST | **Erreichbar, HTTP 200.** Sicheres Online-Formular für Verantwortliche, Bestätigung downloadbar. Keine öffentliche Änderungshistorie. |
| 4 | EDÖB-Leitfaden, [PDF Version 1.2][4] | Vom 6. Februar 2025, **zuletzt angepasst 23. April 2025**, Version 1.2. | 09:04–09:10 CEST | **Erreichbar, HTTP 200.** Schwere und Wahrscheinlichkeit, Sofortmassnahmen, Nichtzuwarten bei Zweifel und Betroffeneninformation bleiben gedeckt. |
| 5 | ISG, [Fedlex ELI 2022/232][5] | Geltende Fassung: **Stand 1. Oktober 2025**; Chronologie/amtliches XML weisen keine neuere Fassung aus. | 09:05–09:10 CEST | **Erreichbar, HTTP 200.** Art. 74a–74f stützen Unterstellung, Kriterien, 24-Stunden-Frist und Übermittlungssystem. |
| 6 | CSV, [Fedlex ELI 2025/169][6] | Einzige ausgewiesene Fassung, **Stand 1. April 2025**. | 09:05–09:10 CEST | **Erreichbar, HTTP 200.** Art. 12 sowie Art. 14–16 stützen Ausnahmen, Konkretisierung der Kriterien und die vom BACS gewährte 14-Tage-Frist. |
| 7 | BACS, [Informationen zur Meldepflicht][7] | Undatierte aktuelle Behördenseite; nennt Inkrafttreten am 1. April 2025. | 09:04–09:10 CEST | **Erreichbar, HTTP 200.** Bestätigt 24 Stunden und 14 Tage bei unvollständiger Erstmeldung. Keine öffentliche Änderungshistorie. |
| 8 | BACS, [Wie muss gemeldet werden?][8] | Undatierte aktuelle Behördenseite. | 09:05–09:10 CEST | **Erreichbar, HTTP 200.** CSH-Formular, Alternative über Meldebutton/E-Mail-Vorlage und gewünschte Weiterleitung an weitere Behörden bestätigt. |
| 9 | BACS, [Ransomware – Was nun?][9] | Undatierte aktuelle Behördenseite. | 09:05–09:10 CEST | **Erreichbar, HTTP 200.** Netztrennung, Log-Sicherung und forensische Sicherung vor Reparaturversuchen oder Neustarts bestätigt. |
| 10 | EUR-Lex, [DSGVO, Art. 33][10] | Amtsblatt vom **4. Mai 2016**; geprüfter Text enthält Art. 33 Abs. 1. | 09:05–09:10 CEST | **Erreichbar, HTTP 200.** Belegt die 72-Stunden-Regel der DSGVO ausschliesslich als EU-Vergleich, nicht als Schweizer Frist. |
| 11 | BACS, [Woche 40: Schadsoftwareverdacht][11] | **Veröffentlicht am 6. Oktober 2026.** | 09:06–09:10 CEST | **Erreichbar, HTTP 200.** Neue, begrenzte Klarstellung zum Umgang mit Verdachtsanzeichen; keine Rechtsänderung. |

### Zusätzlich geprüfte, nicht in Artikel 03 zitierte BACS-Originalquellen

| Quelle | Datierter Quellenstand | Befund und Abgrenzung |
|---|---:|---|
| BACS, [Cyber Security Month: Oversharing][12] | 5. Oktober 2026 | Verpflichtend wegen Prüfhinweis für Artikel 09 einbezogen. Awareness-Beitrag, keine neue Datenschutz- oder BACS-Meldepflicht; für Artikel 03 nicht genutzt. |
| BACS, [Im Fokus][13] | Abgerufen 18. Oktober 2026; relevante Listeneinträge 5., 6., 12., 13. und 15. Oktober 2026 | Auf neuere einschlägige Meldungen geprüft. Nur Woche 40 vom 6. Oktober betraf die Erstreaktion und wurde berücksichtigt. Die weiteren Einträge ändern die Meldewege nicht. |
| BACS, [KI im Berufsalltag][14] | **Veröffentlicht am 16. Oktober 2026.** | Inhaltlich Awareness zu KI/Oversharing und damit Artikel 09 zuzuordnen; keine neue Pflicht und ausserhalb des Gegenstands von Artikel 03. |

**Unklarheiten:** Bei den unversionierten EDÖB- und BACS-Webseiten ist keine vollständige öffentliche Änderungshistorie vorhanden. Der aktuelle Originalinhalt und die Erreichbarkeit sind belegt; eine minutengenaue Negativfeststellung zu jeder redaktionellen Änderung seit 4. Oktober ist nicht möglich. Für Fedlex wurde ausdrücklich die amtliche Chronologie beziehungsweise XML-Fassung genutzt; keine Fassung wurde aus einer Javascript-Ansicht abgeleitet oder erfunden.

## Durchgeführte Änderungen

### Artikel `/wissen/datenpanne-melden-schweiz`

| Betroffener Abschnitt | Vorher | Nachher | Quellenbelegte Begründung |
|---|---|---|---|
| Frontmatter | `rechtsstand` und `stand`: 4. Oktober 2026; keine Angaben zur Quellenprüfung. | `stand` auf **18. Oktober 2026** aktualisiert; `rechtsstand` bleibt **4. Oktober 2026**. `quellenpruefung_umfang` und `quellenpruefung_status` ergänzt. | Die Quellen wurden am 18. Oktober geprüft. Ohne juristische Fachfreigabe wird daraus kein neuer Rechtsstand abgeleitet. |
| Kurzantwort | «fehlende Angaben sind innert 14 Tagen nachzureichen». | «für fehlende Angaben gewährt das BACS eine Frist von 14 Tagen zur Ergänzung». | Art. 16 CSV.[6] |
| «Zuerst stabilisieren, dann beurteilen» | Kein Hinweis auf den Unterschied zwischen Verdacht und bestätigtem Angriff. | Neuer kurzer Absatz: Einzelanzeichen sind kein Beweis; mehrere ungewöhnliche Beobachtungen rechtfertigen Untersuchung und bei Geschäftsgeräten die Einbindung der zuständigen IT. | BACS Woche 40 vom 6. Oktober.[11] |
| BACS-Abschnitt | Die Ergänzungsfrist war nur allgemein beschrieben. | Frist dem Verfahren zugeordnet: BACS gewährt bei fehlenden Angaben 14 Tage; Art. 74e ISG und Art. 16 CSV zitiert. | ISG und CSV.[5] [6] |
| Quellen | ISG als Art. 74a–74d und CSV nur Art. 12 bezeichnet. | ISG auf Art. 74a–74f und CSV auf Art. 12 sowie Art. 14–16 präzisiert; neue Quelle 11 definiert und verwendet. | Präzise Übereinstimmung mit den im Text verwendeten Normen; keine ungenutzte Referenz. |

**Unverändert:** Original-Slug, Veröffentlichungsdatum, Status «Entwurf – nicht freigegeben», H1, Kurzantwort-Struktur, Meta-Title, Meta-Description, bestehende interne relative Links, Schweizer Schreibweise sowie alle **4** vorhandenen `[FACHPRÜFUNG ERFORDERLICH]`-Marker. Meta-Title und Meta-Description wurden nicht geändert, weil die inhaltlichen Präzisierungen ihren Gegenstand nicht verändern. Keine künftige oder interne Ziel-URL wurde als live behauptet oder geprüft.

### Arbeitsmittel `/resources/03-datenpanne-entscheidungsbaum`

| Betroffener Abschnitt | Vorher | Nachher | Quellenbelegte Begründung |
|---|---|---|---|
| Frontmatter und sichtbarer Stand | `version` und «Rechtsstand»: 4. Oktober 2026; keine Angaben zur Quellenprüfung. | `version` und «Rechtsstand» bleiben **4. Oktober 2026**; `stand` und sichtbare «Quellenprüfung» nennen **18. Oktober 2026**. Zwei ehrliche Felder zu Umfang und Status der Quellenprüfung ergänzt. | Die Quellenprüfung ist aktuell, ersetzt aber keine juristische Fachfreigabe und setzt keinen neuen Rechtsstand. |
| Zweck, Diagramm und BACS-Nachreichung | Unpräzise Formulierung «Ergänzung innert 14 Tagen». | Ergänzt «BACS gewährt bei fehlenden Angaben 14 Tage zur Ergänzung»; Checkliste und Erklärung nennen Art. 74e ISG und Art. 16 CSV. | Art. 74e ISG und Art. 16 CSV.[5] [6] |
| Sofortkontrollpunkte | Kein Hinweis zur Beweisgrenze eines einzelnen Malware-Anzeichens. | Quellenbelegter Hinweis «Verdacht ist kein Beweis» und Aufforderung zur Untersuchung bei mehreren Auffälligkeiten. | BACS Woche 40 vom 6. Oktober.[11] |
| Quellen | ISG- und CSV-Beschriftungen weniger vollständig; keine Quelle zur neuen Verdachtsklarstellung. | ISG auf Art. 74a–74f und CSV auf Art. 12 sowie Art. 14–16 präzisiert; Quelle 9 ergänzt und im Text verwendet. | Keine ungenutzte Referenz. |

**Unverändert:** Original-Slug, Status «Arbeitsvorlage – nicht freigegeben», Bezug zum Artikel, H1, Meta-Title, Meta-Description, interne relative Verlinkung und alle **6** vorhandenen `[FACHPRÜFUNG ERFORDERLICH]`-Marker. Das Arbeitsmittel entscheidet weiterhin keine Meldepflicht und simuliert weder eine organisationsspezifische Forensik- noch eine Rechtsfreigabe.

## Metadaten, Links und Referenzintegrität

Beide Dateien enthalten nach der Pflege für jede verwendete Quellenziffer eine Definition und keine ungenutzte Quellenreferenz. Alle externen Referenz-URLs wurden erfolgreich abgerufen. Die internen Paketlinks blieben unverändert; sie wurden weder als veröffentlicht noch als künftig erreichbar bestätigt. Meta-Title und Meta-Description blieben in beiden Dateien unverändert.

## Offene Fach- und Publikationsblocker

1. **Fachfreigabe fehlt weiterhin:** Der Artikel bleibt «Entwurf – nicht freigegeben», das Arbeitsmittel «Arbeitsvorlage – nicht freigegeben». Die vier beziehungsweise sechs bestehenden `[FACHPRÜFUNG ERFORDERLICH]`-Marker wurden nicht entfernt.
2. **Exakte offene Rechtsfrage im Meldefall:** Führt die konkret festgestellte Datensicherheitsverletzung unter den tatsächlichen Datenarten, Empfängern, Schutzmassnahmen und Folgen **voraussichtlich zu einem hohen Risiko nach Art. 24 Abs. 1 DSG**, und ist eine Betroffeneninformation zum Schutz erforderlich oder einzuschränken? Das lässt sich ohne Einzelfallfakten nicht entscheiden.
3. **Exakte offene BACS-Frage im Meldefall:** Fällt die konkrete Organisation unter Art. 74b ISG oder eine CSV-Ausnahme, liegt ein absichtlich ausgelöster Cyberangriff mit mindestens einem Tatbestand aus Art. 74d ISG vor, und wann wurde er rechtlich massgeblich entdeckt? Das BACS kann zur Unterstellung Auskunft erteilen beziehungsweise auf Antrag verfügen; diese Prüfung wurde nicht simuliert.[5] [6]
4. **Veröffentlichung weiterhin blockiert:** Es liegt keine Fachfreigabe vor. Gemäss Wartungsmanifest war in den vorausgehenden Läufen kein authentifizierter CMS-Zugang verifiziert; in diesem Lauf wurde kein CMS geöffnet oder geändert. Vor einer etwaigen Veröffentlichung müssen die dann relevanten externen Meldewege und sämtliche öffentliche Zielseiten erneut geprüft werden.

## Veröffentlichungs- und CMS-Status

**Keine Veröffentlichung veranlasst. Kein CMS bearbeitet. Kein Freigabe- oder Live-Status verändert.**

## Quellen

[1]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz DSG"
[2]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Verordnung über den Datenschutz DSV"
[3]: https://www.edoeb.admin.ch/de/databreach "EDÖB – DataBreach"
[4]: https://www.edoeb.admin.ch/dam/de/sd-web/T64CAUyvAMcF/1_2%20Leitfaden%20des%20ED%C3%96B%20betreffend%20die%20Meldung%20von%20Datensicherheitsverletzungen%20und%20Information%20der%20Betroffenen%20nach%20Art.%2024%20DSG_DE.pdf "EDÖB – Leitfaden zu Datensicherheitsverletzungen Version 1.2"
[5]: https://www.fedlex.admin.ch/eli/cc/2022/232/de "Fedlex – Informationssicherheitsgesetz ISG"
[6]: https://www.fedlex.admin.ch/eli/cc/2025/169/de "Fedlex – Cybersicherheitsverordnung CSV"
[7]: https://www.bacs.admin.ch/de/informationen-zur-meldepflicht "BACS – Informationen zur Meldepflicht"
[8]: https://www.bacs.admin.ch/de/wie-muss-gemeldet-werden "BACS – Wie muss gemeldet werden"
[9]: https://www.bacs.admin.ch/de/ransomware-was-nun "BACS – Ransomware Was nun"
[10]: https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:32016R0679 "EUR-Lex – Datenschutz-Grundverordnung Art. 33"
[11]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40: Schadsoftwareverdacht und Massnahmen"
[12]: https://www.bacs.admin.ch/de/csm26-s2-de "BACS – Cyber Security Month 2026: Oversharing"
[13]: https://www.bacs.admin.ch/de/im-fokus "BACS – Im Fokus"
[14]: https://www.bacs.admin.ch/de/csm26-s3-de "BACS – KI im Berufsalltag: Chancen nutzen, Daten schützen"
