---
titel: "DKSchV-Branchennews"
ausgabe: "04.10.2026"
berichtszeitraum: "27.09.–04.10.2026, 09:00 Europe/Zurich"
recherche: "04.10.2026, nach 09:00 Europe/Zurich"
zielgruppe: "Schweizer KMU"
status: "Redaktionelle Arbeitsausgabe – nicht freigegeben"
---

# DKSchV-Branchennews – Sonntag, 4. Oktober 2026

**Kurzlage:** Bei selbst betriebenen, exponierten Citrix-, FortiMail- oder Cisco-Komponenten ist die Schwachstellenprüfung dringlich. Für hybride Microsoft-Umgebungen ist zudem eine Frist bei Entra Connect Sync zu beachten. BACS warnt vor Malware über ClickFix und vor unbedachtem Teilen von Daten, auch mit KI-Tools.

| Datum | Meldung | Für wen relevant? | Konkreter Schritt |
|---|---|---|---|
| 02.10. (Ergänzung) | [CISA ergänzt Erkennungsregel für zwei aktiv ausgenutzte Citrix-NetScaler-Lücken](https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway) (CVE-2026-88771/-88772). **Die KEV-Aufnahme erfolgte bereits am 27.09.** | Betreiber von NetScaler ADC/Gateway für VPN und externe Zugänge. | Exponierung und Version prüfen; bei Verdacht Logs/Spuren **vor** dem Update sichern, dann die [Citrix-Fix-Versionen](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096) einspielen und die neue CISA-SIGMA-Regel prüfen. |
| 01.10. | [Fortinet meldet aktiv ausgenutzte FortiMail-Lücke](https://fortiguard.fortinet.com/psirt/FG-IR-26-175) (CVE-2026-104286). | Betreiber exponierter FortiMail-Webmail-Oberflächen. | IBE laut Hersteller deaktivieren; Internetzugriff auf Webmail sperren oder beschränken; Hersteller-IOCs/Logs prüfen. Die genannten Fix-Builds sind im Quellenstand **noch angekündigt**, nicht als bereits verfügbar bestätigt. |
| 30.09. | [Cisco Catalyst SD-WAN Manager: aktiv ausgenutzter API-Authentifizierungs-Bypass](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU) (CVE-2026-76504). | Betreiber von Cisco Catalyst SD-WAN Manager, besonders bei Internetzugriff. | Auf einen festen Release aktualisieren; bis dahin Managementzugriff auf vertrauenswürdige Hosts beschränken und `serviceproxy-access.log`/`vmanage-server.log` auf die vom Hersteller genannten Anzeichen prüfen. Der Live-Protect-Shield ist nur partiell. |
| 29.09. (aktualisiert) | [Microsoft Entra Connect Sync: neue Mindestversion und Pflicht zur app-basierten Authentisierung](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/security-updates-pks). | KMU mit lokaler AD-zu-Entra-Synchronisierung. | Version, Autoupgrade und Entra Connect Health prüfen. Microsoft empfahl Mindestversion **2.6.84.0 bereits bis 30.09.2026**; spätestens **07.04.2027** sind diese Version und app-basierte Authentisierung zwingend, andernfalls kann die Synchronisierung stoppen. Umsetzung erst im eigenen Tenant testen. |
| 29.09. | [BACS: Malware über ClickFix und manipulierte Bewerbungsabläufe](https://www.bacs.admin.ch/de/26w39-de). | Mitarbeitende im Bewerbungsprozess und heterogene Unternehmensgeräte. | Keine Befehle auf Aufforderung einer Webseite ausführen; Downloads und vermeintliche Stellenbewerbungen über unabhängige Wege prüfen, Geräte aktualisieren und unnötige Browser-Erweiterungen entfernen. |
| 01.10. | [BACS startet Cyber Security Month zu Oversharing und KI-Eingaben](https://www.bacs.admin.ch/de/csm26-s1-de). | Teams, die KI für Texte, Übersetzungen oder Analysen nutzen. | Freigegebene KI-Anwendungsfälle und Datenkategorien festlegen; personenbezogene oder vertrauliche Informationen nicht ungeprüft in KI-Dienste eingeben. |

## Kurz beobachten

- [NIST: Identität und Autorisierung von KI-Agenten](https://www.nist.gov/news-events/news/2026/09/comments-software-and-agentic-ai-identity-concept-paper) (29.09.): Agentenidentitäten und Berechtigungen inventarisieren. Das ist ein **laufendes Projekt**, keine verbindliche Norm.
- [ENISA zu KI-gestützten Betrugsinhalten](https://www.enisa.europa.eu/news/cybersecurity-month-work-employees-skills-under-the-looking-glass) (30.09.): Sensibilisierung für glaubwürdige Phishing- und Betrugsversuche verstärken.
- [EDÖB-Verfügung zu Bodycams bei der BLT](https://www.edoeb.admin.ch/de/bodycams-blt-de) (01.10.): Betrifft ausdrücklich die **BLT** und begründet keine pauschale Aussage zu anderen Unternehmen; bei eigener Bild- oder Tonüberwachung Rechtsgrundlage und Verhältnismässigkeit fachlich prüfen.
- In den im Zeitraum geprüften Fedlex-, EU-Kommissions- und EUR-Lex-Quellen wurde **keine neue einschlägige Rechtsänderung** zu DSG, NIS2 oder DORA belegt. Das ist keine Vollständigkeitsgarantie.

## Redaktioneller Status

**ISO-Woche 40, zweiwöchentliche Artikelpflege durchgeführt.** Der Berichtszeitraum endet am 4. Oktober **um 09:00**; Quellen wurden danach abgerufen. Für nicht versionierte Websites ist deshalb kein minutengenauer historischer Snapshot um 09:00 belegt. Diese Ausgabe ist ein **lokaler, nicht freigegebener Entwurf**; keine CMS-Änderung oder öffentliche Veröffentlichung. Tatsächliche Gerätebetroffenheit, Tenant-Einstellungen und rechtliche Einzelfälle müssen vor Umsetzung gesondert geprüft werden.
