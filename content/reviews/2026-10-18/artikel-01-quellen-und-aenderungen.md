# Prüfbericht – Artikel 01: Ransomware im KMU: Die ersten 60 Minuten richtig handeln

- **Prüfdatum:** 18. Oktober 2026, ISO-Woche 42. Alle hier protokollierten Abrufe erfolgten nach 09:00 Europe/Zurich; die Recherche begann um 09:04.
- **Prüfzeitraum für Änderungen:** 4. Oktober 2026 nach 09:00 bis 18. Oktober 2026, nach 09:00 Europe/Zurich.
- **Geprüfte und gepflegte Dateien:**
  - Artikel: `/home/ubuntu/dkschv-audit/blog-paket/articles/01-ransomware-erste-60-minuten.md`
  - Arbeitsmittel: `/home/ubuntu/dkschv-audit/blog-paket/resources/01-60-minuten-checkliste.md`
- **Wartungsgrundlage:** `/home/ubuntu/dkschv-audit/blog-paket/maintenance-manifest.md`, Eintrag Artikel 01.
- **Paket- und Freigabestatus:** Der Artikel bleibt **Entwurf – nicht freigegeben**, das Arbeitsmittel **Arbeitsvorlage – nicht freigegeben**. Diese Quellenprüfung ist keine fachliche, rechtliche, technische oder publizistische Freigabe.

## Ergebnis

Alle **11 eindeutigen externen Originalquellen** aus den Quellenlisten beider Dateien waren beim Abruf erreichbar und wurden im Original geöffnet. Damit sind alle **11 von 11** Quellenreferenzen des Artikels und alle **8 von 8** Quellenreferenzen des Arbeitsmittels geprüft; die doppelt verwendeten Referenzen wurden nicht als neue, unbestätigte Quellen behandelt. `all_references_verified` ist daher für die **externen Quellenreferenzen** beider Dateien `true`.

Die Prüfung ergab seit dem 4. Oktober keine belegte Änderung der gesetzlichen BACS- oder EDÖB-Meldeschwellen, der gesetzlichen Fristen oder der zentralen Erstreaktionsschritte. Neu und einschlägig ist die BACS-Meldung **«Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion»** vom 6. Oktober 2026. Sie präzisiert, dass ein einzelnes unspezifisches Zeichen wie ein langsames Gerät keine Infektion belegt, mehrere ungewöhnliche Beobachtungen oder eine Sicherheitswarnung aber untersucht werden sollen. Dieser begrenzte Hinweis wurde quellenbelegt in Artikel und Arbeitsmittel ergänzt. Die bereits vorhandene Aussage zur freiwilligen BACS-Meldung wurde zusätzlich mit der aktuellen offiziellen BACS-Meldeoberfläche belegt.

Die vorgegebene BACS-Meldung vom 5. Oktober 2026 zu Oversharing wurde geöffnet und als nicht einschlägig für Artikel 01 eingeordnet. Sie führte nicht zu einer ungenutzten Quellenreferenz. Die BACS-Übersicht **«Im Fokus»** und die neuere Wochenmeldung vom 13. Oktober 2026 wurden ebenfalls geprüft; sie betreffen Online-Shop-Betrug, nicht die Ransomware-Erstreaktion. Es wurde keine zukünftige oder interne Paket-URL als live behauptet oder geprüft.

## Quellenprüfung: Originalquellen in den gepflegten Dateien

| Nr. | Originalquelle und URL | Nachweisbarer Quellenstand | Tatsächlicher Abruf am 18.10.2026 | Erreichbarkeit und Abgleichresultat |
|---:|---|---|---|---|
| 1 | BACS, [Ransomware – Was nun?](https://www.bacs.admin.ch/de/ransomware-was-nun) | Aktuelle BACS-Seite ohne angezeigtes Veröffentlichungs- oder Änderungsdatum. | 09:04 | **Erreichbar.** Bestätigt Netztrennung, Sicherung von Logs, frühen Forensikentscheid vor Reparatur/Neustart, Neuinstallation vor Wiederherstellung, Kantonspolizei bei Strafanzeige/Lösegeld und Abraten von Lösegeld. Die Seite nennt für erfasste Organisationen 24 Stunden für die Erstmeldung und 14 Tage für die Vervollständigung; der Artikel behauptet als Gesetzeswortlaut nur die Ergänzung bei neuen Informationen. |
| 2 | BACS, [Informationen zur Meldepflicht](https://www.bacs.admin.ch/de/informationen-zur-meldepflicht) | Aktuelle BACS-Seite ohne angezeigten eigenen Seitenstand; sie nennt die Inkraftsetzung per 1. April 2025. | 09:04 | **Erreichbar.** Bestätigt Meldepflicht für bestimmte kritische Infrastrukturen, 24 Stunden ab Entdeckung und BACS-/CSV-Grundlage. Keine seit 04.10.2026 dargestellte Änderung. |
| 3 | Fedlex, [DSG, SR 235.1](https://www.fedlex.admin.ch/eli/cc/2022/491/de) | Amtliche aktuelle Fassung. Die Fedlex-Historie weist als letzten Fassungszeitpunkt eine Berichtigung mit Inkrafttreten am **7. Juli 2025** aus. | 09:04; Historie 09:06 | **Erreichbar.** Art. 5 definiert die Verletzung der Datensicherheit; Art. 24 verlangt die Meldung durch den Verantwortlichen «so rasch als möglich» bei voraussichtlich hohem Risiko, regelt Mindestinhalt und Betroffeneninformation. Die amtliche XML-Fassung vom 07.07.2025 wurde zusätzlich abgerufen. |
| 4 | EDÖB, [Leitfaden nach Art. 24 DSG, Version 1.2, PDF](https://www.edoeb.admin.ch/dam/de/sd-web/T64CAUyvAMcF/1_2%20Leitfaden%20des%20ED%C3%96B%20betreffend%20die%20Meldung%20von%20Datensicherheitsverletzungen%20und%20Information%20der%20Betroffenen%20nach%20Art.%2024%20DSG_DE.pdf) | Version 1.2; der EDÖB weist das PDF mit **23. April 2025** aus. | 09:04 | **Erreichbar.** Bestätigt, dass bei nicht innert kurzer Zeit ausschliessbarem voraussichtlich hohem Risiko nicht bis zum Ende längerer Abklärungen zugewartet werden darf; Ransomware kann je nach Umständen ein solcher Fall sein. Keine neuere Leitfadenversion auf der geprüften EDÖB-DataBreach-Seite. |
| 5 | CISA, [I’ve Been Hit By Ransomware!](https://www.cisa.gov/stopransomware/ive-been-hit-ransomware) | Die Seite verweist auf den #StopRansomware Guide, aktualisiert im **Mai 2023**. | 09:04 | **Erreichbar.** Bestätigt koordinierte Isolation, externen Kommunikationsweg, Ausschalten nur falls Netzwerkisolation nicht möglich ist, frühe Evidenzsicherung und Wiederherstellung aus Offline-Backups ohne Reinfektion. Sie ist technische US-Orientierung, keine Schweizer Rechtsquelle. |
| 6 | BACS, [Das Notfallkonzept als Schlüssel zur Cyberresilienz](https://www.bacs.admin.ch/de/notfallkonzept) | Aktuelle BACS-Seite ohne angezeigtes eigenes Änderungsdatum; sie verlinkt unter anderem ein KMU-Template vom **18. Mai 2026**. | 09:05 | **Erreichbar.** Bestätigt Krisenorganisation, Kommunikation, Notfallkontakte sowie die Phasen Vorbereitung, Vorfall, Vorfallsbewältigung und Nachbearbeitung. |
| 7 | NIST, [SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | **Veröffentlicht April 2025**; Finalfassung vom 03.04.2025 laut Dokumenthistorie. | 09:05 | **Erreichbar.** Der Abstract bestätigt die Einbettung von Incident Response in das Cyberrisikomanagement. |
| 8 | Fedlex, [ISG, SR 128](https://www.fedlex.admin.ch/eli/cc/2022/232/de) | Amtliche aktuelle Fassung **Stand am 1. Oktober 2025**. Die Fedlex-Historie weist danach keine spätere Fassung aus. | 09:05; Historie 09:06 | **Erreichbar.** Art. 74b–74e stützen die Einzelfallprüfung der Erfassung, die Meldeauslöser, die 24-Stunden-Frist und die Ergänzung, sobald neue Informationen vorliegen. Die amtliche Änderungsfassung AS 2024 257 wurde zusätzlich geöffnet. |
| 9 | Suisse ePolice, [Cyberkriminalität anzeigen](https://www.suisse-epolice.ch/cybercrime-case) | Aktuelle Seite ohne angezeigtes Veröffentlichungs- oder Änderungsdatum. | 09:05 | **Erreichbar.** Sie bietet Anzeigenkategorien und verweist für blosse Meldungen auf die nationale Plattform. Die BACS-Ransomware-Seite stützt zusätzlich die Kantonspolizei am Geschäftssitz. |
| 10 | BACS, [Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion](https://www.bacs.admin.ch/de/26w40-de) | **Veröffentlicht am 6. Oktober 2026.** | 09:05 | **Erreichbar.** Neue einschlägige Quelle seit der letzten Prüfung: ein langsames Gerät allein ist kein Beweis; mehrere ungewöhnliche Beobachtungen rechtfertigen eine Untersuchung. Bei Geschäftsgeräten soll die IT informiert werden. Die BACS-Empfehlung zum Neuaufsetzen und Passwortwechsel bezieht sich auf eine bestätigte Infektion; daraus wurde keine eigenmächtige Reset-Anweisung abgeleitet. |
| 11 | BACS, [Freiwillige Meldung eines Cybervorfalls](https://www.report.ncsc.admin.ch/de/chat?path=406%3E407%3E1) | Aktuelle offizielle BACS-Meldeoberfläche ohne angezeigtes Veröffentlichungs- oder Änderungsdatum. | 09:07 | **Erreichbar.** Enthält ausdrücklich die Option «Ich möchte freiwillig einen Cybervorfall melden». Sie stützt die bestehende allgemeine Aussage zur freiwilligen Meldemöglichkeit, nicht eine Pflicht. |

## Zusätzliche primäre Prüfquellen und Aktualisierungscheck

| Quelle und URL | Nachweisbarer Quellenstand | Abruf | Ergebnis für Artikel 01 |
|---|---|---:|---|
| BACS, [Im Fokus](https://www.bacs.admin.ch/de/im-fokus) | Listet am Abrufzeitpunkt als jüngsten einschlägigen Beitrag Woche 40 vom 06.10.2026; später gelistete Beiträge vom 12., 13. und 15.10.2026. | 09:05 | Geprüft. Nach Woche 40 keine neuere gelistete BACS-Meldung zu Ransomware-Erstreaktion, Malware-Verdacht oder Wiederanlauf festgestellt. |
| BACS, [Woche 41: Online-Shops mit Rücksendeadressen in Asien](https://www.bacs.admin.ch/de/26w41-de) | **Veröffentlicht am 13.10.2026.** | 09:07 | Geprüft. Online-Shop-/Betrugsthema, nicht einschlägig für Ransomware-Erstreaktion; keine Ergänzung. |
| BACS, [Cyber Security Month 2026: «Oversharing»](https://www.bacs.admin.ch/de/csm26-s2-de) | **Veröffentlicht am 05.10.2026.** | 09:05 | Auftragsgemäss einbezogen. Thema ist persönliches Oversharing, einschliesslich ungeprüfter Eingabe interner Dokumente in KI-Tools; keine neue Meldepflicht und keine sachliche Relevanz für Artikel 01. Nicht als ungenutzte Referenz ergänzt. |
| BACS, [Wer muss melden?](https://www.bacs.admin.ch/de/wer-muss-melden) | Aktuelle BACS-Seite ohne angezeigtes eigenes Änderungsdatum. | 09:05 | Erreichbar. Verweist für Meldepflichtige auf ISG Art. 74b und für Ausnahmen auf CSV. Stützt den Vorbehalt der Einzelfallprüfung. |
| BACS, [Was muss gemeldet werden?](https://www.bacs.admin.ch/de/was-muss-gemeldet-werden) | Aktuelle BACS-Seite ohne angezeigtes eigenes Änderungsdatum. | 09:06 | Erreichbar. Bestätigt Funktionsfähigkeitsgefährdung, Manipulation, Informationsabfluss sowie Erpressung, Drohung oder Nötigung; Verschlüsselungstrojaner wird als Beispiel genannt. |
| EDÖB, [DataBreach](https://www.edoeb.admin.ch/de/databreach) | Aktuelle Seite; verlinkt den Leitfaden vom **23.04.2025**. | 09:06 | Erreichbar. Bestätigt das Portal für Verantwortliche sowie die Schwelle «voraussichtlich hohes Risiko». Keine aktuellere Leitfadenversion sichtbar. |
| Fedlex, [DSG-Historie](https://www.fedlex.admin.ch/eli/cc/2022/491/de/history) und [amtliche XML-Fassung](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml) | Letzte Fassung/ Berichtigung **07.07.2025**. | 09:06 | Erreichbar. Bei JavaScript-Fedlex nicht auf einen ungesicherten Browserstand gestützt: Chronologie und amtliche XML wurden direkt geprüft. Keine Rechtsänderung seit 04.10.2026 belegt. |
| Fedlex, [ISG-Historie](https://www.fedlex.admin.ch/eli/cc/2022/232/de/history) und [AS 2024 257](https://www.fedlex.admin.ch/eli/oc/2024/257/de) | Letzte aktuelle ISG-Fassung **01.10.2025**. | 09:06 | Erreichbar. Chronologie und amtlicher Originaltext geprüft; keine Rechtsänderung seit 04.10.2026 belegt. |
| Fedlex, [DSV, SR 235.11, Art. 15](https://www.fedlex.admin.ch/eli/cc/2022/568/de) und [Historie](https://www.fedlex.admin.ch/eli/cc/2022/568/de/history) | Aktuelle Fassung seit **01.12.2025**. | 09:06–09:07 | Erreichbar. Art. 15 konkretisiert Angaben, Nachreichen fehlender Angaben «so rasch als möglich» und Dokumentation. Keine neuere Fassung in der Historie. Diese Quelle steht nicht in den Quellenlisten, wurde aber wegen des im Manifest genannten DSV-Triggers geprüft. |
| Suisse ePolice, [Im Notfall](https://www.suisse-epolice.ch/emergency) | Aktuelle Seite ohne Datum. | 09:07 | Erreichbar. Nennt 117 oder 112 für Notfälle. Kein Anlass, die differenzierte Artikelpassage zu Strafanzeige und Kantonspolizei zu verändern. |

## Abgleich wichtiger Tatsachen

- **BACS-Meldepflicht:** Die Aussage bleibt begrenzt auf die im ISG/der CSV erfassten Behörden und Organisationen. Die genaue Einordnung und eine mögliche Ausnahme werden weiterhin nicht simuliert. Für meldepflichtige Cyberangriffe gilt die gesetzliche Frist von 24 Stunden ab Entdeckung. Art. 74e Abs. 3 ISG verlangt die Ergänzung, sobald neue Informationen vorliegen. Die BACS-Webseite und -Meldeoberfläche nennen zusätzlich 14 Tage für die Schlussmeldung beziehungsweise Vervollständigung; daraus wurde keine starre gesetzliche 14-Tage-Behauptung abgeleitet.
- **EDÖB-Meldung:** Art. 24 DSG sowie EDÖB-Leitfaden Version 1.2 sind unverändert erreichbar. Der Text verbleibt bei der gesetzlichen Schwelle des voraussichtlich hohen Risikos und bei «so rasch als möglich». Eine konkrete Risiko-, Meldungs- oder Betroffeneninformationsentscheidung wurde nicht getroffen.
- **Erstreaktion:** Die vorhandenen Aussagen zu Isolation, Log- und Beweissicherung, frühem Forensikentscheid, Backup-Schutz und Wiederherstellung in einer bereinigten Umgebung bleiben durch BACS und CISA gedeckt. Die neue BACS-Woche-40-Meldung ergänzt nur die saubere Abgrenzung zwischen unspezifischem Verdacht und untersuchungsbedürftigen Beobachtungen.
- **BACS Im Fokus:** Die aktuelle Übersicht zeigte nach Woche 40 keine neue einschlägige Meldung zur Ransomware-Erstreaktion. Die Meldung 26w41 vom 13.10.2026 ist thematisch nicht einschlägig.

## Dokumentierte Änderungen

### Artikel

Datei: `/home/ubuntu/dkschv-audit/blog-paket/articles/01-ransomware-erste-60-minuten.md`

| Betroffener Abschnitt | Vorher | Nachher | Grund und Quellenbeleg |
|---|---|---|---|
| Frontmatter `stand` | `4. Oktober 2026` | `18. Oktober 2026` | Datum dieser Quellenprüfung, **nicht** Fachfreigabedatum. |
| Neues Frontmatter `quellenpruefung_umfang` | Feld fehlte. | `11 von 11 externen Quellenreferenzen geprüft; BACS Im Fokus auf neuere einschlägige Meldungen geprüft` | Ehrlicher dokumentierter Prüfumfang. |
| Neues Frontmatter `quellenpruefung_status` | Feld fehlte. | `Vollständig für die Quellenreferenzen; interne relative Ziele nicht live geprüft` | Alle externen Referenzen wurden geöffnet; Paketziele wurden auftragsgemäss nicht als live behandelt. |
| «Minute 0–15», nach dem Lagebild | Kein spezifischer Hinweis zur Beweiskraft einzelner Symptome. | Hinweis ergänzt: Ein einzelnes unspezifisches Zeichen wie ein langsamer Computer belegt keine Infektion; mehrere Beobachtungen oder Sicherheitswarnungen sollen untersucht werden; bei Geschäftsgeräten IT informieren. | BACS Woche 40 vom 06.10.2026, neu numerisch als [10] zitiert. Kein Reset- oder Forensikvorgehen vorgegeben. |
| «BACS: Pflicht …» | Freiwillige BACS-Meldung war nur mit [2] und [9] gebündelt. | Freiwillige BACS-Meldung mit eigener Quelle [11] belegt; Polizeikontakt bleibt getrennt bei [9]. | Aktuelle offizielle BACS-Meldeoberfläche zeigt die freiwillige Meldeoption. |
| «Grenzen dieses Sofortleitfadens» | Allgemeine Orientierung «per 4. Oktober 2026». | Orientierung «auf dem Stand der Quellenprüfung vom 18. Oktober 2026; dieser Stand ist keine Fachfreigabe». | Erforderliche Standaktualisierung ohne Freigabeaussage. |
| Quellen | Neun Quellenreferenzen. | Quellen [10] und [11] ergänzt und beide im Text verwendet. | Keine ungenutzte Referenz. |

**Unverändert erhalten:** Original-Slug `/wissen/ransomware-erste-60-minuten`, Veröffentlichungsdatum `01.10.2026`, Status «Entwurf – nicht freigegeben», H1, Kurzantwort, Meta-Title, Meta-Description, Struktur, alle bestehenden **[FACHPRÜFUNG ERFORDERLICH]**-Marker und alle internen relativen Links. Meta-Title und Meta-Description blieben unverändert, weil die begrenzte Verdachtsklarstellung keine Anpassung verlangt.

### Arbeitsmittel

Datei: `/home/ubuntu/dkschv-audit/blog-paket/resources/01-60-minuten-checkliste.md`

| Betroffener Abschnitt | Vorher | Nachher | Grund und Quellenbeleg |
|---|---|---|---|
| Frontmatter `version` | `Stand 4. Oktober 2026` | `Stand 18. Oktober 2026` | Datum dieser Quellenprüfung, **nicht** Fachfreigabedatum. |
| Neues Frontmatter `quellenpruefung_umfang` | Feld fehlte. | `8 von 8 externen Quellenreferenzen geprüft` | Ehrlicher dokumentierter Prüfumfang für die Quellenliste des Arbeitsmittels. |
| Neues Frontmatter `quellenpruefung_status` | Feld fehlte. | `Vollständig für die Quellenreferenzen; interne relative Ziele nicht live geprüft` | Alle externen Quellenreferenzen wurden geöffnet. |
| Abschnitt B, nach «Kurzlage» | Kein Hinweis zur Einordnung einzelner unspezifischer Symptome. | BACS-Hinweis ergänzt: ein langsames Gerät allein ist kein Beweis; mehrere Beobachtungen oder Sicherheitswarnungen für die Untersuchung dokumentieren und IT informieren. | Konsistente, beschränkte Übernahme der BACS-Woche-40-Meldung, als [8] zitiert. |
| «Grenzen und fachliche Prüfung» | Allgemeines Arbeitsmittel ohne aktuellen Quellenstand. | Quellenstand 18. Oktober 2026 sowie ausdrücklicher Hinweis, dass dies keine Fachfreigabe ist. | Standhinweis an Artikel angepasst. |
| Quellen | Sieben Quellenreferenzen. | Quelle [8] ergänzt und im Text verwendet. | Keine ungenutzte Referenz. |

**Unverändert erhalten:** Original-Slug `/resources/01-60-minuten-checkliste`, Status «Arbeitsvorlage – nicht freigegeben», Titel, Meta-Title, Meta-Description, Bezug zum Artikel, Tabellen, Checklistenstruktur, der bestehende **[FACHPRÜFUNG ERFORDERLICH]**-Marker und der interne relative Bezug. Meta-Title und Meta-Description blieben unverändert.

## Nicht verifizierte Punkte und exakte offene Fachfragen

1. **Organisationale BACS-Erfassung:** Ist die konkrete Organisation nach Art. 74b ISG meldepflichtig, oder greift eine Ausnahme nach Art. 74c ISG beziehungsweise CSV? Das wurde nicht und kann mit dem allgemeinen Artikel nicht entschieden werden.
2. **Konkreter BACS-Meldefall:** Liegt in einem konkreten Ereignis mindestens ein gesetzlicher Auslöser nach Art. 74d ISG vor, welche Angaben sind bereits verfügbar, und welche Fristen beziehungsweise der aktuelle Meldeweg gelten für diese Organisation? Das wurde nicht entschieden.
3. **Konkreter EDÖB-Fall:** Sind Personendaten betroffen, besteht ein voraussichtlich hohes Risiko, müssen Betroffene zu ihrem Schutz informiert werden, und welche Angaben gehören in die Meldung? Das wurde nicht entschieden.
4. **Forensik und Wiederanlauf:** Welche Systeme, Daten, Volatilspuren, Zugangsdaten, Backups, Versicherungsbedingungen und Wiederanlaufreihenfolgen im konkreten Unternehmen betroffen sind, wurde nicht geprüft. Die BACS-Woche-40-Hinweise werden nicht als organisationsspezifische Reset- oder Forensikfreigabe ausgegeben.
5. **Lösegeld, Straf-, Sanktions-, Vertrags- und Versicherungsfragen:** Keine Einzelfallprüfung und keine Freigabe. Die vorhandenen Fachprüfungsmarker bleiben deshalb bestehen.
6. **Interne und geplante Webziele:** Relative Paketlinks wurden erhalten, aber nicht auf Live-Erreichbarkeit geprüft oder als veröffentlicht behauptet. Laut Prüfhinweisen war die vorgesehene Artikel-URL am 11.10.2026 HTTP 404; es erfolgte kein CMS-Vorgang.
7. **Historische Zwischenstände:** BACS- und EDÖB-Webseiten veröffentlichen überwiegend keine lückenlose Seitenhistorie. Aktueller Inhalt und datierte Dokumentstände wurden geprüft; eine nicht publizierte redaktionelle Änderung zwischen 04.10. und 18.10.2026 ist damit nicht ausschliessbar. Für Fedlex wurden ausdrücklich Historie und amtliche XML/AS-Quellen verwendet.

## Publikationsblocker

1. **Keine Fachfreigabe:** Status und alle vorhandenen **[FACHPRÜFUNG ERFORDERLICH]**-Marker bleiben unverändert.
2. **Erforderliche Einzelfallprüfung:** BACS-Erfassung/Meldepflicht, EDÖB-Risiko/Meldung/Betroffeneninformation, Forensik, Wiederanlauf und Lösegeldbezug benötigen die dafür zuständigen Fachpersonen.
3. **Organisationale Einsatzreife fehlt als Nachweis:** Kontaktwege, Incident Lead, externe Forensik, sichere Kommunikationswege, Backup-Administrationswege, Versicherer und kantonale Abläufe müssen organisationsspezifisch verifiziert und geübt werden.
4. **Kein CMS- oder Live-Nachweis:** Diese Pflege hat weder veröffentlicht noch eine Live-URL validiert. Die Paketlinks dürfen vor Go-live nicht als live angenommen werden.

## Abschluss

Es wurden **ausschliesslich** der Artikel, das zugehörige Arbeitsmittel und dieser Prüfbericht gepflegt. Die 18.-Oktober-Quellenprüfung umfasst alle Quellenreferenzen in beiden Dateien und die verlangte Prüfung der BACS-Meldungen vom 05. und 06. Oktober sowie von BACS «Im Fokus». Die Texte bleiben Entwürfe; aus der Aktualisierung folgt keine Fach- oder Veröffentlichungsfreigabe.
