# DKSchV – Laufstatus vom 11. Oktober 2026

**ISO-Woche 41 (ungerade):** Die [Sonntagsnews](2026-10-11_DKSchV_Branchennews.md) sind erstellt. Heute war keine vollständige zweiwöchentliche Artikelpflege fällig. Der letzte gezielte Quellenstand der zwölf Artikel und zwölf Arbeitsmittel bleibt **4. Oktober 2026**. Dieser Lauf behauptet keine neue vollständige Quellenprüfung je Artikel.

## Veröffentlichung blockiert

Die aktuelle Connector-Konfiguration enthält keinen Webador-Connector; der Zugriff über My Browser ist deaktiviert. Ein authentifizierter CMS-Zugang zum Webador-Projekt **DKSchV Pro** ist in diesem Lauf nicht verifiziert. Frühere Anmeldungen werden nicht als aktuelle Authentifizierung behandelt. Es wurden keine Zugangseinstellungen, Editorinhalte oder öffentlichen Beiträge verändert.

**Artikel 01 – Ransomware, geplant 01.10.2026:** Status «Entwurf – nicht freigegeben», Fachprüfungsmarker offen. Die vorgesehene URL `https://www.dkschv.ch/wissen/ransomware-erste-60-minuten` lieferte beim Abruf am 11.10.2026 **HTTP 404**. Vor Veröffentlichung sind insbesondere die markierten rechtlichen, datenschutzrechtlichen und forensischen Passagen tatsächlich fachlich freizugeben; ein verstrichener Termin erteilt keine Freigabe.

**Artikel 02 – CEO-Betrug/BEC, geplant 08.10.2026:** Status «Entwurf – nicht freigegeben», Fachprüfungsmarker offen. Die vorgesehene URL `https://www.dkschv.ch/wissen/ceo-betrug-business-email-compromise` lieferte **HTTP 404**. Markierte Mailbox-/Personendatenfragen sowie die organisatorischen und rechtlichen Aussagen bleiben vor Veröffentlichung zu klären.

Die übrigen zehn Beiträge bleiben ebenfalls Entwürfe. Die News sind ein lokaler redaktioneller Entwurf, nicht eine neu veröffentlichte Website-Seite. Es liegen **keine erfolgreichen Live-Änderungen** vor; daher gibt es keine Live-URL-/Änderungsprotokolle für diesen Lauf.

## Für den nächsten Review am 18. Oktober vorgemerkt

Die [BACS-Meldung vom 6. Oktober](https://www.bacs.admin.ch/de/26w40-de) betrifft Malware-Verdacht, Untersuchung und Wiederanlauf. Sie ist beim nächsten Review von **Artikel 01 und 07** auf Ergänzungsbedarf zu prüfen; sie begründet heute weder eine individuelle Forensik-Anweisung noch eine Veröffentlichung.

Der [BACS-Oversharing-Folgebeitrag vom 5. Oktober](https://www.bacs.admin.ch/de/csm26-s2-de) ist ein Kontextbeleg für **Artikel 09 (Schatten-KI)**. Er ist keine neue gesetzliche Pflicht. Anbieter-Datenflüsse und konkrete KI-Nutzungsfreigaben bleiben gesondert zu prüfen.

Neue Herstellerhinweise zu FortiMail und NetScaler sind in den News dokumentiert. Das Artikelpaket enthält keine dedizierten produktbezogenen Beiträge dazu; es wurde deshalb kein generischer Artikel allein wegen eines neuen Hersteller-Bulletins geändert.

## QA und Nachweise

Der bestehende Validator `blog-paket/qa/validate_package.py` wurde ausgeführt: **12 Artikel, 12 Arbeitsmittel, 12 Artikel-Slugs, 12 Arbeitsmittel-Slugs, 0 Fehler, 0 Warnungen**. Das ist eine Struktur- und Paketprüfung, keine Fachfreigabe oder erneute Live-Linkprüfung sämtlicher Ziele. Die 24 Artikel-/Arbeitsmittel-Dateien wurden nicht verändert; ihr Entwurfsstatus, Metadaten und Quellenstände bleiben bestehen.

Die fünf Themenrecherchen samt Endkorrekturen liegen unter `news/qa/2026-10-11/`. Ein unvollständiger erster Schweizer Quellenbefund wurde vor Auslieferung korrigiert: Die BACS-Meldung für die vergangene Woche befindet sich unter **26w40**, nicht **26w41**. Der neuere Citrix-Fixhinweis vom 8. Oktober wurde ebenfalls berücksichtigt, statt ausschliesslich einen älteren Fixstand zu empfehlen.

**Nächster bestehender Sonntagslauf:** 18.10.2026, 09:00 Europe/Zurich; **ISO-Woche 42**, daher News plus vollständige turnusgemässe Artikelpflege. Vor jeder etwaigen Veröffentlichung sind authentifizierter CMS-Zugang, tatsächliche Fachfreigabe, aktuelle Originalquellen und alle öffentlichen Zielseiten erneut zu prüfen.
