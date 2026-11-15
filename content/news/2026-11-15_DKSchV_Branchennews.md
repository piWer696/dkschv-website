---
datum: "15.11.2026"
stand: "15. November 2026"
kalenderwoche: "KW 46"
status: "Redaktioneller Entwurf – nicht veröffentlicht"
newsfenster: "08.11.2026 09:00 bis 15.11.2026 09:00 CET"
zeitzone: "Europe/Zurich"
befundzeiten: "Originalrückgaben der News-Einzelberichte am 15.11.2026, 09:05:57–09:08:20 CET; ergänzende lokale Lektüre bis 09:08:22 CET"
---

# DKSchV Branchennews · 15. November 2026

Sechs priorisierte neue Meldungen für Schweizer KMU. Die dokumentierten Originalabrufe erfolgten **nach 09:00 CET** und sind Befundzeiten, kein Nachweis des historischen Seitenwortlauts zum Redaktionsschluss. Die Auswahl ist begrenzt; Quellenlektüre ersetzt keine Einzelfallprüfung oder Fachfreigabe.

## 1. Outlook und Chromium: aktiv ausgenutzte Lücken beheben

**Neu am 9./10. November:** Microsoft bestätigt Ausnutzung von Outlook CVE-2026-124194; eine präparierte Datei muss geöffnet werden, die Vorschau ist kein Angriffsvektor. Möglich ist die Offenlegung eines NTLMv2-Hashes. Sicherheitsupdates erschienen am 10. November. [1] [2] Google bestätigt aktive Ausnutzung von Chromium CVE-2026-125350 und veröffentlichte am 9. November Chrome-Fixes; belegt ist Codeausführung innerhalb der Sandbox, kein Sandbox-Ausbruch. [3] [4] Beide CVEs kamen am 10. November in KEV. [5]

**KMU-Prüfpunkt:** Office-Linie, Kanal und Build sowie Browserprodukt, Plattform und laufende Version mit der IT abgleichen; Edge hat eigene Fixstände. [2] [6] **Unsicherheit:** Kein Schweizer Gerät wurde untersucht. Ein Update beweist keine Bereinigung; US-KEV-Fristen sind keine Schweizer Fristen.

## 2. Kühlsteuerungen: BACS warnt vor Angriffen

**10. November:** Das BACS meldet Angriffe auch in der Schweiz und warnt vor internetexponierten Kühlsteuerungen, veralteter Firmware und nicht mehr unterstützten Systemen. Neu ist die Warnung, nicht ein belegter Angriffsbeginn oder Firmwarefix. [7]

**KMU-Prüfpunkt:** Modell, Firmware, Wartungszugänge und Ersatzplanung mit Anlagenfachpersonen und Dienstleister prüfen. **Unsicherheit:** Das belgische CCB meldete am 12. November sechs weitere Danfoss-Lücken bis einschliesslich 5.3.2, damals ohne Patch. [8] Danfoss-Softwareseite und verlinkte Readme nennen abweichende Paketstände; eine aktuell sichere Buildversion ist nicht bestätigt. [9] [10] Ein älteres Update erlaubt keine pauschale Entwarnung.

## 3. ScreenConnect: auch Technikerzugänge betrachten

**13. November:** Microsoft beschreibt SCKit-Missbrauch von ScreenConnect zur Installation weiterer Fernzugangsclients und Angriffe auf authentifizierte Technikersitzungen. [11] ConnectWise ergänzte vorbeugende Erweiterungshinweise; der relevante Clientfix 26.6.5 stammt bereits vom September, nicht aus dieser Woche. [12]

**KMU-Prüfpunkt:** Beim IT-Dienstleister Instanzen, Erweiterungen, Technikerclients und verwaltete Geräte getrennt erfassen lassen; einen unabhängigen Vorfallkanal vorsehen. **Unsicherheit:** Einstieg und Gesamtscope bleiben in Untersuchung. Rund 400 Erweiterungsinstallationen sind nicht 400 bestätigte Kompromittierungen; Toolkitfähigkeiten belegen keine vollständige Ausbreitungskette. [12]

## 4. Coding-Agenten: vergiftete Modelle können Werkzeuge missbrauchen

**12. November:** Microsoft zeigt experimentell, wie vergiftete Nachtrainingsdaten oder manipulierte Modell-Checkpoints versteckte schädliche Werkzeugaufrufe auslösen können. [13]

**KMU-Prüfpunkt:** Herkunft und Integrität fremder Modellartefakte dokumentieren, Secrets und Werkzeugrechte begrenzen, Ausführung isolieren und folgenreiche Aktionen kontrollieren lassen. **Unsicherheit:** Laborforschung ist keine gemessene KMU-Inzidenz oder nachgewiesene Schwäche normaler Standardkonfigurationen. Ein universeller Fixbuild ist nicht belegt; Filter allein bestätigen keine Modellintegrität. [13]

## 5. ENISA/CERT-EU: KI-Codeprüfung braucht menschliche Validierung

**12. November:** Der neue Bericht beschreibt 27 Codebasen und 220 potenzielle KI-Befunde. Von 88 bereits beurteilten Befunden wurden 95 Prozent bestätigt. [14] [15]

**KMU-Prüfpunkt:** KI-Codeprüfungen isolieren; Dienstleister sollen potenzielle Hinweise, reproduzierte Schwachstellen und bestätigte Behebungen unterscheiden. Vorgeschlagene Patches fachlich prüfen lassen. **Unsicherheit:** Die Quote gilt nur für die beurteilte Teilmenge. Produktionskontext und Live-Tests fehlten; genannte CVE-IDs belegen keine neue Patchveröffentlichung. [15]

## 6. KI-Fakeshops und Paket-Phishing vor Black Friday

**10. November:** Das BACS berichtet über mehr Meldungen zu Fakeshops und Logistik-Phishing sowie zunehmend KI-generierte Shoptexte, Bilder und Rezensionen. [16]

**KMU-Prüfpunkt:** Einkauf und Empfang sensibilisieren; Lieferstatus über selbst aufgerufene offizielle Transportseiten prüfen. Rezensionen allein sind kein Vertrauensnachweis. **Unsicherheit:** Der Anstieg und KI-Anteil sind nicht quantifiziert; eine Schweizer KMU-Schadenquote ist nicht belegt. Neu ist der Wochenbericht, nicht die Betrugsmasche. [16]

**Nächste News:** 22. November 2026, KW 47. Die nachrangige DSA-Konsultation bleibt im Einzelbericht; alte EDÖB-, NIST-, Entra-GA- und Rechtsmeldungen werden nicht neu datiert. Keine Veröffentlichung oder technische Betriebsfreigabe.

 **Pflegestatus:** Zwölf Artikel samt Arbeitsmitteln sind lokal aktualisiert; CMS-Metadaten und Linkziele sind abgeglichen, der Paketvalidator meldet 0 Fehler. Keine Live-Änderung. Webador-Zugang, Fachfreigaben und wirksamer Kundenzugriffsschutz bleiben offen: Der Wiederherstellungsartikel liefert trotz Login-Hinweis umfangreichen Text ohne Anmeldung. Die genauen Blocker stehen im [Pflegebericht](../reviews/2026-11-15/DKSchV_Pflegebericht_KW46.md). Nächste Vollpflege: **29. November, KW48**.

## References

[1]: https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-124194 "Microsoft MSRC: Outlook CVE-2026-124194, 10. November 2026"
[2]: https://learn.microsoft.com/en-us/officeupdates/microsoft365-apps-security-updates "Microsoft Learn: Office-Sicherheitsupdates und kanalgenaue Builds"
[3]: https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop_018223192.html "Google: Chrome Desktop Stable, 9. November 2026"
[4]: https://www.cve.org/CVERecord?id=CVE-2026-125350 "Chrome-CNA: CVE-2026-125350, Codeausführung innerhalb der Sandbox"
[5]: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json "CISA: Vollständiger offizieller KEV-Katalog, Stand 13. November 2026"
[6]: https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security "Microsoft Learn: Edge-Sicherheitsreleases und produktspezifische Fixstände"
[7]: https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de "BACS: Warnung zu Kühl- und Kältesteuerungen, 10. November 2026"
[8]: https://ccb.belgium.be/advisories/warning-six-new-danfoss-vulnerabilities-refrigeration-controllers-risk-immediate-action "CCB: Sechs weitere Danfoss-Lücken, 12. November 2026"
[9]: https://www.danfoss.com/en-us/service-and-support/downloads/dcs/adap-kool-software/ak-sm-800a/ "Danfoss: AK-SM 800A Softwareseite, Paketbezeichnung 5.3.x"
[10]: https://www.danfoss.com/en/service-and-support/downloads/dcs/adap-kool-software/ak-sm-800a/license-agreement/ "Danfoss: Verlinkte Readme mit abweichendem Downloadstand 5.1.1"
[11]: https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/ "Microsoft: SCKit, ScreenConnect und Technikersitzungen, 13. November 2026"
[12]: https://www.connectwise.com/company/trust/advisories "ConnectWise: ScreenConnect-Untersuchung, Stand 13. November 2026, 21:15 UTC"
[13]: https://www.microsoft.com/en-us/security/blog/2026/11/12/trained-to-betray-how-post-training-supply-chain-attacks-hijack-coding-agents/ "Microsoft: Vergiftetes Nachtraining und Coding-Agenten, 12. November 2026"
[14]: https://www.enisa.europa.eu/publications/joint-advisory-on-the-use-of-frontier-ai-models-for-code-review "ENISA: Publikation zur KI-Codeprüfung, 12. November 2026"
[15]: https://www.enisa.europa.eu/sites/default/files/2026-11/ENISA_CERTEU_JOINTREPORT_Final.pdf "ENISA/CERT-EU: Originalbericht zur KI-gestützten Codeprüfung"
[16]: https://www.bacs.admin.ch/de/26w45-de "BACS: KI-Fakeshops und Paket-Phishing, 10. November 2026"
