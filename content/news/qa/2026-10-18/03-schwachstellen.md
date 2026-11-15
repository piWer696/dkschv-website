# Schwachstellenrecherche – 18.10.2026

**Berichtsfenster:** 11.10.2026 09:00 bis 18.10.2026 09:00 Europe/Zurich. Quellenabrufe erfolgten am 18.10.2026 nach 09:00; die Abrufzeit ist technisch protokolliert, ein historisch minutengenauer Website-Stand wird nicht behauptet.

## Abgrenzung zur Vorwoche

Die Ausgabe vom 11.10.2026 behandelte FortiMail CVE-2026-104286 sowie NetScaler CVE-2026-88779 und verwies auf den neueren Citrix-Fix für CVE-2026-107406. FortiMail und NetScaler werden diese Woche nicht nochmals als eigene Meldung geführt: Die geöffneten Originalbulletins zeigen keine materielle Änderung nach dem Vorwochenstand (Fortinet Timeline endet 07.10.; Citrix CTX697174 Changelog 03.10., CTX697191 08.10.).

## Neue KEV-Aufnahmen / aktive Ausnutzung

### 1. PAN-OS CVE-2026-0322

CISA führt CVE-2026-0322 mit Date Added 14.10.2026 und Due Date 17.10.2026. Die Originalwarnung von Palo Alto Networks ist vom 14.10., aktualisiert 15.10., und bezeichnet die Exploit-Reife als ATTACKED; es wurde sehr begrenzte Ausnutzung gegen die Management-Schnittstelle beobachtet. Betroffen sind PA-Series, VM-Series und Panorama auf den in der Warnung genannten PAN-OS-Zweigen; Cloud NGFW und Prisma Access sind nicht betroffen. Fixe: PAN-OS 12.2.4+, 12.1.4-h12/12.1.7-h8/12.1.10-h2 je Zweig, 11.2.4-h22/7-h21/10-h15/13-h3/16, 11.1.4-h37/6-h39/7-h11/10-h35/13-h15/16-h3 sowie 10.2.7-h38/10-h41/13-h26/16-h11/18-h12. Kein allgemeiner Workaround; Risikoreduktion durch Managementzugriff nur aus vertrauenswürdigen Netzen/Jumphost. Signaturen 510046/510047 bieten nur begrenzte Abdeckung und ersetzen den Fix nicht. KMU mit exponierter Firewall-Administration sollten vor dem Patch Zugriffe beschränken und Logs auf Kompromittierung prüfen.

### 2. Atlassian Data Center CVE-2026-21589

CISA führt CVE-2026-21589 mit Date Added 15.10.2026 und Due Date 18.10.2026. Die Atlassian-Originalwarnung wurde am 05.10.2026 veröffentlicht und zuletzt am 05.10.2026 geändert; CISA-Aufnahme ist deshalb die neue Meldung im Berichtsfenster. Atlassian bestätigt eine kritische Arbitrary-File-Access-Lücke in allen Versionen der betroffenen Data-Center-Produkte: Bitbucket, Confluence, Jira Service Management, Jira Software, Bamboo, Crowd, Crucible und Fisheye. Cloud-Produkte sind gepatcht; Atlassian fand dort keine Ausnutzung. Fixe Versionen stehen je Produkt im Bulletin, darunter Bitbucket 9.4.26/10.2.8/10.5.1, Confluence 9.2.26/10.2.19, Jira 10.3.26/11.3.12 und weitere produktspezifische Stände. Fix bevorzugen. Workarounds getrennt: Instanz aus dem Internet nehmen oder WAF-/Proxy-Regel gegen Pfadtraversal; alternativ produktspezifische Tomcat-RewriteValve- bzw. Bitbucket-urlrewrite-Regeln. Atlassian kann nicht bestätigen, ob einzelne Instanzen betroffen waren; Zugriffslogs nach URL-Decoding auf Traversal-Muster prüfen.

### 3. BeyondTrust Remote Support CVE-2026-102764

CISA führt CVE-2026-102764 mit Date Added 16.10.2026 und Due Date 19.10.2026. Das BeyondTrust-Originalbulletin BT26-05 ist vom 15.10.2026 und bestätigt eine kritische Schwachstelle in Remote Support, die entfernte Dateioperationen auf der Appliance ermöglichen kann. Betroffen: alle Remote-Support-Versionen <=26.2.3. Fix: BT26-05-RS-Patch für Versionen 24.3.1 bis 26.2.3; ältere als 24.3.1 müssen zuerst auf eine neuere Version aktualisiert werden. Remote-Support-SaaS wurde laut BeyondTrust bereits am 09.10.2026 gepatcht; Self-hosted-Kunden müssen den Patch manuell installieren, sofern automatische Updates nicht aktiviert sind. Ein separater Workaround ist im geöffneten Bulletin nicht genannt; SaaS-Patch bzw. Self-hosted-Patch sind daher nicht gleichzusetzen mit einer blossen Mitigation. Für KMU ist zuerst Betriebsmodell und Version zu klären, danach Patchstand und Appliance-Logs auf unübliche Dateioperationen zu prüfen.

## Weitere geprüfte KEV-Einträge, nicht als Meldung aufgenommen

Der aktuelle CISA-Katalog zeigte im selben Abruf ausserdem neue Einträge vom 14.–16.10.2026, darunter Fortinet CVE-2025-61624 (Date Added 16.10.; Original-Fortinet-Bulletin bereits 14.04.), Ahsay CVE-2026-105133 und Cisco Secure Email Gateway CVE-2026-76519 (14.10.). Wegen der Begrenzung auf maximal drei substanzielle Meldungen und fehlender zusätzlicher, im Zeitraum veröffentlichter Herstelleränderung wurden sie nicht als Items ausgegeben. Die Fortinet-Quelle wurde geöffnet und Fixe/Virtual Patch geprüft; der Cisco-Link aus dem KEV-Katalog war beim Abruf nicht verfügbar. Diese Auswahl ist keine Vollständigkeitszusage.

## Direkt geöffnete Originalquellen

- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/news-events/alerts/2026/10/13/cisa-adds-two-known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/news-events/alerts/2026/10/15/cisa-adds-one-known-exploited-vulnerability-catalog
- https://security.paloaltonetworks.com/CVE-2026-0322
- https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html
- https://www.beyondtrust.com/trust-center/security-advisories/bt26-05
- https://fortiguard.fortinet.com/psirt/FG-IR-26-122
- https://fortiguard.fortinet.com/psirt/FG-IR-26-175
- https://support.citrix.com/external/article/CTX697174/citrix-netscaler-adc-and-citrix-netscale.html
- https://support.citrix.com/external/article/CTX697191/citrix-netscaler-adc-and-citrix-netscale.html
- https://forums.ivanti.com/s/article/CVE-2026-104935 (kein extrahierbarer Inhalt beim Abruf)
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sma-path-trav-2026 (Seite nicht verfügbar beim Abruf)
