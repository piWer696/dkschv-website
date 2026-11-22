# Newsprüfung 04 · 22. November 2026 · KW 47

Zwei neue Meldungen sind für die DKSchV-Auswahl belegt: METR veröffentlicht eine Forschungsnotiz zur Erkennbarkeit von KI-Sicherheitstests; NIST kündigt die Revision seiner TLS-Leitlinie an, ohne bereits einen neuen Entwurf vorzulegen. Die NIST-Meldung ist ein Planungshinweis, keine neue verbindliche Anforderung für Schweizer KMU. [1] [2] [3]

**Bereich:** NIST, CISA, ENISA, CERT-EU und originale KI-Sicherheitsforschung. **Newsfenster:** 15. November 2026, 09:00 Uhr, bis 22. November 2026, 09:00 Uhr CET; Europe/Zurich. Alle unten genannten Originalabrufe erfolgten nach 09:00 Uhr. Die Zeitangaben dokumentieren die tatsächlichen Toolrückgaben am 22. November 2026 und gewährleisten keinen historischen Seitenwortlaut zum Redaktionsschluss.

Die Vorwochennachrichten `news/2026-11-15_DKSchV_Branchennews.md` und das Pflegemanifest `blog-paket/maintenance-manifest.md` wurden am 22. November 2026, 09:04:02 Uhr CET gelesen. Vergiftetes Nachtraining vom 12. November und ENISA/CERT-EU-KI-Codeprüfung vom 12. November werden nicht als neue Wochenmeldungen wiederholt. Die bereits gepflegten NIST-Agentenidentitätsgrundsätze werden ebenfalls nicht neu datiert. Die Vollpflege erfolgte am 15. November; heute entstehen ausschliesslich News und Vormerkungen für den 29. November 2026. Keine Browser-, Login-, CMS- oder Liveaktion; keine Änderung an den 24 Entwürfen oder den Manifesten.

## 1. METR: KI-Sicherheitstests können als Tests erkennbar sein

**Publikation:** 16. November 2026; eine separate Aktualisierung ist in der geöffneten Forschungsnotiz nicht ausgewiesen. **Originalabruf:** 22. November 2026, 09:04:29 Uhr CET. [1]

METR liess Untersuchungsagenten 19 Alignment-Tests und 36 Fähigkeitstests erkunden. Alignment-Tests prüfen beispielsweise, ob ein Agent Regeln verletzt oder unerlaubte Abkürzungen nutzt. Die Agenten wurden ausdrücklich damit beauftragt, den Zweck der jeweiligen Umgebung einzuschätzen. Die Studie findet eine zunehmende Unterscheidbarkeit beider Testarten. Hinweise waren unter anderem künstlich wirkende Umgebungen und auffällige Köderaufgaben, die unerwünschtes Verhalten sichtbar machen sollen. Auf dem untersuchten Datensatz ordnete Opus 5.5 nach Mittelung von jeweils drei Läufen alle Alignment-Tests höher ein als alle Fähigkeitstests. Das ist eine Aussage über diesen Datensatz, nicht über sämtliche möglichen Tests. [1]

**Quellenbeleg:** METR begrenzt das Ziel ausdrücklich: «Our goal is to understand whether such alignment tells exist, not to measure whether these tells causally affect behavior». Die Arbeit misst damit die Erkennbarkeit von Tests, nicht die dadurch verursachte Veränderung des tatsächlichen Agentenverhaltens. [1]

**Konkrete Bedeutung für KMU:** Ein bestandener Sicherheitstest sollte nicht allein als Nachweis gelten, dass ein KI-Agent im realen Arbeitsablauf sicher handelt. Bei einer Anbieter- oder Dienstleisterbewertung ist zusätzlich interessant, wie realitätsnah die Tests sind und welche unabhängigen Kontrollen den produktiven Zugriff auf Daten und Werkzeuge begrenzen. Dies ist eine redaktionelle Ableitung aus der begrenzten Übertragbarkeit, keine neue gesetzliche Pflicht oder gemessene Schweizer Vorfallhäufigkeit. [1]

**Unsicherheit:** METR kennzeichnet Notes als weniger intensiv geprüfte Forschungsupdates als reguläre Forschungsbeiträge. Die direkte Befragung kann den Agenten auf die Möglichkeit eines Sicherheitstests aufmerksam machen. Die Notiz belegt weder bewusste Täuschung im produktiven KMU-Einsatz noch einen generellen Ausfall aller KI-Sicherheitstests. Sie liefert auch keinen universellen Produktfix. [1]

**Vormerkungen für die Vollpflege am 29. November:** Bei Artikel 08, **IT-Sicherheitscheck für Schweizer KMU** (`/wissen/it-sicherheitscheck-kmu`), prüfen, ob das Risikoregister den Nachweistyp klar trennt: künstlicher Benchmark, realitätsnaher Workflowtest und unabhängige technische Kontrolle. Bei Artikel 09, **Schatten-KI im Schweizer KMU** (`/wissen/schatten-ki-kmu`), prüfen, ob eine KI-Freigabe neben Anbieter-Testberichten auch Datenzugriff, Werkzeugrechte und Überwachung abdeckt. Bei Artikel 11, **Lieferantenrisiken im Griff** (`/wissen/lieferantenrisiken-cybersecurity`), eine mögliche Frage zur Realitätsnähe von KI-Sicherheitstests und zu deren Grenzen vormerken. Offen bleibt, welche konkret eingesetzten Modelle, Agentengerüste und Kontrollmechanismen betroffen sind. Heute keine Ergänzung der Artikel oder Arbeitsmittel.

## 2. NIST: TLS-Revision angekündigt, noch kein neuer Entwurf

**Publikation:** 19. November 2026. Die Seitenmetadaten nennen Erstellung am 18. November und Aktualisierung am 19. November 2026. **Originalabruf der Meldung:** 22. November 2026, 09:04:28 Uhr CET. **Abruf der bestehenden finalen Publikationsseite:** 09:05:02 Uhr CET. [2] [3]

NIST wird SP 800-52 Rev. 2 überarbeiten und erst bei Veröffentlichung eines Revisionsentwurfs erneut um Kommentare bitten. Geplant ist unter anderem, TLS-1.2-Unterstützung bei Servern als fakultativ statt als empfohlen zu behandeln und TLS 1.0/1.1 grundsätzlich nicht mehr zuzulassen. Weitere erwartete Änderungen betreffen Post-Quantum-Algorithmen, mindestens 128 Bit Sicherheitsstärke sowie AEAD-Verfahren, die Verschlüsselung und Authentifizierung verbinden. Die Meldung kündigt zudem eine künftige Zeitlinie des Cryptographic Module Validation Program an; konkrete Termine nennt sie nicht. [2]

**Quellenbeleg:** Die Meldung sagt «will revise» und «until a draft of the revision is released». Ihre Aufzählungen stehen unter «Revision Plans». Das ist weder eine neue finale Leitlinie noch bereits ein veröffentlichter Entwurf. Die weiterhin als final geführte SP 800-52 Rev. 2 stammt vom August 2019; ihr Abstract nennt bestehende Anforderungen für staatliche TLS-Server und -Clients im US-Kontext. Diese alten Anforderungen und die neuen Revisionspläne dürfen nicht vermischt werden. [2] [3]

**Konkrete Bedeutung für KMU:** Die Ankündigung ist ein sinnvoller Beobachtungspunkt für TLS-Abhängigkeiten bei eigenen Diensten und Lieferanten. Mit der IT lässt sich erfassen, welche Systeme noch ältere TLS-Versionen benötigen und wie eine spätere Migration vorbereitet werden könnte. Aus dieser Meldung folgt aber keine neue allgemeine Schweizer KMU-Frist und keine pauschale Anweisung, TLS 1.2 sofort abzuschalten. Vertragliche oder sektorspezifische Vorgaben sind getrennt zu prüfen. [2] [3]

**Unsicherheit:** Veröffentlichungsdatum und Inhalt des künftigen Entwurfs stehen noch nicht fest. Erwartete Detailänderungen können sich im Entwurfs- und Kommentierungsverfahren verändern. Auch die angekündigte CMVP-Zeitlinie ist noch nicht beziffert. [2]

**Vormerkungen für die Vollpflege am 29. November:** Für Artikel 08, **IT-Sicherheitscheck** (`/wissen/it-sicherheitscheck-kmu`), einen datierten TLS-Inventar- und Altgerätebefund als möglichen Prüfpunkt vormerken, ohne eine neue Pflicht zu behaupten. Für Artikel 11, **Lieferantenrisiken** (`/wissen/lieferantenrisiken-cybersecurity`), die konkrete Dienstleister-Migrationsplanung und etwaige vertragliche NIST-Bezüge prüfen. Beim Quellenabgleich nachsehen, ob ein tatsächlicher neuer Entwurf oder Terminplan erschienen ist. Offene Fragen sind betroffene Dienste, Kompatibilitätsabhängigkeiten und der konkrete organisatorische Geltungsbereich. Heute keine technische Betriebsänderung und keine Artikelpflege.

## Weitere Quellenbefunde ohne zusätzliche News-Auswahl

**ENISA:** Die Publikation **CRA-Module B and H: CABs accreditation for notification** vom 16. November 2026 wurde am 22. November, 09:05:02 Uhr CET geöffnet. Sie ist ausdrücklich eine nicht verbindliche technische Referenz für notifizierende Behörden und nationale Akkreditierungsstellen und entscheidet nicht über Akkreditierungs- oder Notifizierungsfähigkeit. Mangels unmittelbarer Breitenrelevanz für Schweizer KMU keine dritte Nachricht. Für Artikel 12, **NIS2 und DORA** (`/wissen/nis2-dora-schweiz`), nur vormerken: CRA nicht mit NIS2/DORA vermischen; eine Erweiterung wäre ausschliesslich bei konkretem EU-Produkt- oder Konformitätsbezug gesondert zu beurteilen. [4]

Die ENISA-SRP-Seite, abgerufen um 09:04:18 Uhr CET, nennt ein Upgrade auf Version 1.4 am 17. November und zugleich noch laufende Dokumentationsanpassungen. Das ist ein Plattformhinweis, kein neuer Rechtsakt und keine im Wortlaut fertig belegte neue Anleitung. Für einen etwaigen CRA-Bezug bei Artikel 11/12 am 29. November die dann aktuelle Dokumentversion prüfen. Es wurde weder das Portal geöffnet noch eine Meldung eingereicht. [5]

**CISA:** Die Ressourcenliste, abgerufen um 09:04:29 Uhr CET, führt drei Dams-Sektor-Publikationen vom 16. November. Die geöffnete **Dams Sector Cybersecurity Framework Implementation Guidance**, Originalabruf um 09:05:02 Uhr CET, beschreibt ausdrücklich einen Ansatz «without additional regulatory requirements». Wegen des US-Staudammsektors keine allgemeine Schweizer KMU-Nachricht. Die geöffneten Alerts, Abruf um 09:04:18 Uhr CET, enthalten aktuelle KEV- und Java-Hinweise; produktbezogene Schwachstellenmeldungen sind nicht die hier priorisierte Publikationsauswahl. Kein Nachweis einer Änderung des StopRansomware Guide im Wochenfenster; deshalb keine neue Vormerkung für Artikel 07 aus dieser Prüfung. [6] [7] [8]

**CERT-EU:** Der Blogabruf um 09:05:02 Uhr CET zeigt als jüngsten Beitrag die Veröffentlichung des Codeprüfungsgerüsts Vigilo vom 13. November, also vor dem Newsfenster. Die Leitlinienübersicht, Abruf um 09:04:29 Uhr CET, zeigt keine neue Leitlinie in diesem Fenster. Das ist ein begrenzter Befund aus den geöffneten Übersichten, keine Garantie, dass sämtliche CERT-EU-Veröffentlichungskanäle leer sind. Der Codeprüfungskomplex wird nicht als neue Vorwochenmeldung recycelt. [9] [10]

**NIST und weitere Forschung:** Die NIST-Jahresübersicht, Abruf um 09:04:19 Uhr CET, datiert den AML-Taxonomieentwurf auf den 9. November: ausserhalb des Fensters und weiterhin Entwurf, keine neue verbindliche Vorgabe. Die neue IR-8616-Meldung vom 16. November betrifft eine maschinenlesbare ANSI/NIST-ITL-Spezifikation und wird nicht für die KMU-Auswahl vertieft. METRs Fähigkeitsupdate vom 20. November wurde um 09:04:29 Uhr CET geöffnet, aber wegen seines Schwerpunktes auf KI-Forschungsbeschleunigung nicht als zusätzliche KMU-Meldung ausgewählt. Seine Benchmarkbefunde werden nicht als universelle Leistungs- oder Sicherheitsgarantie übernommen. [11] [12]

## References

[1]: https://metr.org/notes/2026-11-16-measuring-alignment-eval-tells/ "METR: Measuring alignment eval tells, 16. November 2026"
[2]: https://csrc.nist.gov/News/2026/nist-will-revise-tls-guidelines "NIST: Ankündigung der Revision von SP 800-52 Rev. 2, 19. November 2026"
[3]: https://csrc.nist.gov/pubs/sp/800/52/r2/final "NIST: Bestehende finale TLS-Leitlinie SP 800-52 Rev. 2, August 2019"
[4]: https://www.enisa.europa.eu/publications/cra-module-b-and-h-cabs-accreditation-for-notification "ENISA: CRA-Module B and H, CABs accreditation for notification, 16. November 2026"
[5]: https://www.enisa.europa.eu/topics/product-security/vulnerability-services/eu-incident-response-and-cyber-crisis-management/single-reporting-platform-srp "ENISA: Single Reporting Platform, Hinweis auf Upgrade 1.4 vom 17. November 2026"
[6]: https://www.cisa.gov/resources-tools/resources "CISA: Ressourcenübersicht mit Dams-Sektor-Publikationen vom 16. November 2026"
[7]: https://www.cisa.gov/resources-tools/resources/dams-sector-cybersecurity-framework-implementation-guidance "CISA: Dams Sector Cybersecurity Framework Implementation Guidance, 16. November 2026"
[8]: https://www.cisa.gov/news-events/cybersecurity-advisories "CISA: Cybersecurity Alerts und Advisories, abgerufen am 22. November 2026"
[9]: https://cert.europa.eu/blog "CERT-EU: Blogübersicht, jüngster angezeigter Beitrag vom 13. November 2026"
[10]: https://cert.europa.eu/publications/security-guidance/ "CERT-EU: Übersicht der Sicherheitsleitlinien, abgerufen am 22. November 2026"
[11]: https://csrc.nist.gov/news/2026 "NIST CSRC: News und Updates 2026, Publikationsdaten und Entwurfsstatus"
[12]: https://metr.org/blog/2026-11-20-q4-2026-capability-update/ "METR: AI R&D-relevant model capabilities are improving rapidly and are getting harder to measure, 20. November 2026"
