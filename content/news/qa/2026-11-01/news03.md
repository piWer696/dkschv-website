# Newsfeld 03 – Aktiv ausgenutzte Schwachstellen

**Berichtsfenster:** 25.10.2026, 09:00 CET bis 01.11.2026, 09:00 CET, Europe/Zurich (ISO-KW 44)  
**Tatsächlicher Abruf:** 01.11.2026, ca. 09:04–09:06 CET. Die Quellen wurden nach dem Ende des Berichtsfensters stateless per HTTP abgerufen.  
**Befund:** Drei priorisierte Updates für Schweizer KMU sind belastbar belegt. Die Auswahl stützt sich auf die direkte Abfrage des offiziellen CISA-KEV-JSON und je eine geöffnete Herstelleroriginalquelle. Sie ist keine Vollständigkeitszusage und ersetzt weder eine versions-, umgebungs- oder tenantbezogene Fachprüfung noch eine Rechts- oder Freigabeentscheidung.

Der abgerufene KEV-Feed hatte **catalogVersion 2026.10.30** und `dateReleased` **2026-10-30T17:02:45.3665Z**. Die direkte Filterung auf `dateAdded` vom 25.10. bis einschliesslich 01.11. ergab darin zehn CVEs in acht Produktgruppen. Da dieser Feedstand selbst vom 30.10. stammt, kann er keine noch nicht im Feed publizierte Ergänzung vom 31.10. oder 01.11. belegen. Die drei unten genannten Themen wurden wegen ihrer typischen Relevanz für internet-erreichbare Web-, Entwicklungs- und Fernzugangssysteme priorisiert. [1]

## 1. PHP: KEV-Aufnahme der bereits gemeldeten RCE-Lücken ist die neue Entwicklung

CISA nahm **CVE-2026-109618** und **CVE-2026-109619** am **26.10.2026** in den KEV-Katalog auf. Der Feed beschreibt für beide nicht authentisierte Remote-Code-Ausführung. Die CISA-Warnung wurde am 26.10. entsprechend aktualisiert und nennt die KEV-Aufnahme ausdrücklich. [1] [2]

Dies ist gegenüber der Vorwochennachricht eine belegte **neue Entwicklung**: Die PHP-Sicherheitsreleases und die ursprüngliche Warnung stammen zwar vom 21.10., die Einstufung als neu in KEV gelistete, aktiv ausgenutzte Schwachstellen aber vom 26.10. Die PHP-Originalmitteilung nennt Web-Installationen unter PHP-FPM, Apache mit `mod_php`, `php-cgi`, FrankenPHP und LiteSpeed als betroffenes Einsatzfeld; sie nennt **8.5.12, 8.4.27, 8.3.36 und 8.2.35** als bereinigte Releases. PHP weist zugleich darauf hin, dass Linux-Distributionen und LTS-Anbieter Korrekturen zurückportieren können. [2] [3]

**Für KMU:** Selbst betriebene und durch Dienstleister betriebene PHP-Instanzen erfassen, insbesondere internet-erreichbare Webanwendungen sowie eingebettete Komponenten und Appliances. Den tatsächlichen Fixstand beim Paket- oder Hostinganbieter nachweisen lassen und nicht nur die sichtbare Hauptversion vergleichen. Sind Aktualisierung oder belastbarer Fixnachweis nicht kurzfristig möglich, ist die Exponierung anhand der Hersteller- und Betreiberanweisungen fachlich zu reduzieren; PHP betont, dass nur ein Update vollständig behebt. Ein Update beweist nicht, dass es vorher keinen Angriff gab. [2] [3]

## 2. Selbst betriebenes GitLab CE/EE: aktiv ausgenutzte, nicht authentisierte Server-RCE

CISA nahm **CVE-2026-97229** am **29.10.2026** in KEV auf und führt eine nicht authentisierte Ausführung beliebigen Codes auf dem GitLab-Server über einen speziell präparierten regulären Ausdruck in einer CI/CD-Konfiguration an. Die CISA-Meldung vom selben Datum erklärt, dass die beiden dort genannten KEV-Aufnahmen auf Belegen aktiver Ausnutzung beruhen. [1] [4]

GitLab bestätigt für CE und EE die betroffenen Linien **19.2 vor 19.2.8**, **19.3 vor 19.3.5** und **19.4 vor 19.4.2** und rät selbst betriebenen Installationen zur unverzüglichen Aktualisierung. Laut Hersteller waren GitLab.com und GitLab Dedicated bereits gepatcht; das ist kein Ersatz für die Bestätigung der konkret genutzten Dienstleistung und ihres Stands. Die Hersteller-Patchmitteilung wurde am 12.10. publiziert; die berichtsfensterrelevante Entwicklung ist somit die KEV-Aufnahme am 29.10., nicht ein neuer GitLab-Patch in dieser Woche. [5]

**Für KMU:** Falls GitLab CE/EE selbst betrieben wird, laufende Version, öffentliche Erreichbarkeit und Upgradepfad mit der zuständigen Betriebsstelle abgleichen und auf eine der genannten korrigierten Linien oder einen neueren freigegebenen Patch aktualisieren. GitLabs bereitgestellte Erkennungsregeln können bei der Vorfallabklärung helfen; die Bewertung auffälliger Befunde gehört in den konkreten Incident-Response-Prozess. Eine KEV-Aufnahme belegt keine Kompromittierung der eigenen GitLab-Instanz. [4] [5]

## 3. Ivanti Connect Secure: zwei neu gelistete Glieder einer bereits beobachteten Angriffskette

CISA nahm **CVE-2026-111357** und **CVE-2026-118527** am **30.10.2026** in KEV auf. Der Feed verknüpft beide mit **CVE-2026-104935** als potenzielle Angriffskette. Die Einträge beschreiben eine Rechteausweitung nach lokaler Authentisierung beziehungsweise das Hochladen kontrollierter Inhalte an einen vorhersehbaren Speicherort nach Remote-Authentisierung. [1]

Ivanti aktualisierte sein Herstelleradvisory am **29.10.2026**. Es berichtet von Ausnutzung bei einer begrenzten Zahl Kunden zum Zeitpunkt der Offenlegung, wenn die drei CVEs verkettet werden. Für die zwei neu in KEV aufgenommenen CVEs nennt Ivanti als bereinigte Versionen **25.1.1.3** und **22.8R2.6**; die konkreten Hard- und Softwarepfade müssen gegen die Herstellermatrix abgeglichen werden. [6]

**Für KMU:** Ivanti Connect Secure nicht als generischen «VPN»-Fall behandeln, sondern Produktlinie, Version, Erreichbarkeit und Herstellerfix gegen die konkrete Instanz prüfen. Betroffene Versionen nach der Ivanti-Matrix auf einen bereinigten Stand bringen und bei Hinweisen auf einen Angriff die vom Hersteller verlinkten Wiederherstellungs- und Integrity-Checker-Schritte mit Incident-Response-Fachleuten einordnen. Die Meldung belegt aktive Ausnutzung der beschriebenen Kette, nicht einen Befund auf einer bestimmten Schweizer Instanz. [1] [6]

## Auswahl, Auslassungen und Fristen

Die zehn im direkten KEV-Filter vorhandenen CVEs betreffen PHP (zwei), Adobe Commerce/Magento, Google Brotli, VMware ESX, Linux Kernel, Cisco Secure Firewall ASA/FTD, GitLab und Ivanti Connect Secure (zwei). Aus dem Nachrichtenfeld wurden Adobe, Brotli, VMware und Linux nicht als eigene Meldung aufgenommen: Adobe publizierte den verfügbaren Fix bereits im Juli, Brotli und Linux sind komponenten- beziehungsweise distributionsabhängig, und die vom Hersteller beschriebene VMware-Lücke setzt Administratorzugriff voraus und ist mit CVSS 2.7 als niedrig eingestuft. Diese Auslassungen sind keine Aussage, dass sie in einer konkreten Umgebung unwichtig seien. [1] [8] [9] [10] [11]

Cisco ASA/FTD ist ebenfalls neu im KEV-Filter. Cisco bestätigt aktive Ausnutzung und Fixe für eine nicht authentisierte Denial-of-Service-Lücke im SSL-Remote-Access-VPN, sofern dessen Erreichbarkeit und die im Advisory beschriebene Sekundärauthentisierungskonfiguration vorliegen. Wegen der bedingten Konfiguration und des laut Advisory auf Verfügbarkeit beschränkten Effekts wurde es gegenüber den drei priorisierten RCE- beziehungsweise Angriffsketten-Themen nicht als vierte Meldung ausgegeben. [1] [12]

Plex Media Server, Arista VeloCloud Orchestrator On-Prem und Nextcloud `richdocumentscode` wurden in der Vorwoche bereits behandelt. Sie waren nicht Teil des neuen `dateAdded`-Filters; innerhalb dieses begrenzten Newsfelds wurde keine neue, geöffnete Herstellerentwicklung belegt und daher keine Wiederholung ausgegeben. PHP erscheint nur wegen der ausdrücklich belegten KEV-Aufnahme vom 26.10. erneut.

Die im KEV-Feed enthaltenen US-`dueDate`-Angaben und die CISA-BOD-26-04-Hinweise sind Anforderungen beziehungsweise Leitlinien für US-Bundesbehörden. Sie sind **keine Schweizer Pflicht oder Frist**. Für Schweizer Organisationen ergibt sich aus diesem Befund keine pauschale rechtliche Melde-, Patch- oder Incident-Frist. [1] [4] [7]

## Geöffnete Originalquellen und jeweilige Reichweite

- **CISA KEV-JSON**, abgerufen am 01.11.2026 ca. 09:04 CET: offizieller maschinenlesbarer Katalogstand mit `dateAdded`, Kurzbeschreibung, CISA-Aktion, US-`dueDate` und verlinkten Quellen. Er belegt die im Snapshot vorhandenen KEV-Aufnahmen, nicht die Betroffenheit einer einzelnen Umgebung. [1]
- **CISA PHP-Alert**, abgerufen am 01.11.2026 ca. 09:05 CET: amtliche Ergänzung zur KEV-Aufnahme beider PHP-CVEs am 26.10. und CISA-Handlungshinweise. Er ist keine Herstellerfreigabe für eine konkrete PHP-Distribution. [2]
- **PHP-Archiv/Sicherheitsmitteilung**, abgerufen am 01.11.2026 ca. 09:05 CET: Herstellerangaben zu betroffenen Web-Betriebsarten, bereinigten PHP-Releases, Backports und begrenzten Zwischenmassnahmen. [3]
- **CISA-Alert vom 29.10.**, abgerufen am 01.11.2026 ca. 09:05 CET: amtliche Bestätigung der KEV-Aufnahme von GitLab und Cisco wegen Belegen aktiver Ausnutzung; die BOD-Geltung beschränkt der Alert selbst auf FCEB-Behörden. [4]
- **GitLab Patch Release**, abgerufen am 01.11.2026 ca. 09:05 CET: Herstellerangaben zu betroffenen GitLab-Linien, Fixversionen, verwalteten GitLab-Angeboten und Erkennungsregeln. [5]
- **Ivanti Connect Secure Advisory**, abgerufen am 01.11.2026 ca. 09:05 CET: Herstellerangaben zur beobachteten Kette, zu betroffenen und bereinigten Versionen sowie zum Änderungsdatum 29.10. Ein abgerufener Inhalt war ohne Anmeldung lesbar; er deckt keine konkrete Appliance-Konfiguration oder einen forensischen Befund ab. [6]
- **CISA-Alert vom 26.10.**, abgerufen am 01.11.2026 ca. 09:06 CET: amtliche Meldung zur KEV-Aufnahme der PHP-CVEs und BOD-Abgrenzung. [7]
- **Adobe Commerce Bulletin**, abgerufen am 01.11.2026 ca. 09:06 CET: Herstellerfixmatrix und Angaben zu CVE-2026-48356; der Herstellertext vom Juli sagt, Adobe sei damals keine Ausnutzung bekannt gewesen. Die spätere KEV-Aufnahme ist deshalb nur durch CISA, nicht durch diesen älteren Adobe-Text, belegt. [8]
- **Google Brotli Release 1.2.1**, abgerufen am 01.11.2026 ca. 09:06 CET: Hersteller-/Projektrelease vom 21.10. mit CVE-2026-111497 und Fixrelease; keine vollständige Liste betroffener Drittprodukte. [9]
- **Broadcom ESX Advisory**, abgerufen am 01.11.2026 ca. 09:06 CET: Herstellerbeschreibung, Schweregrad und Fixmatrix für CVE-2026-41709; die aktive Ausnutzung stammt aus dem CISA-KEV-Befund. [10]
- **Linux Stable Commit**, abgerufen am 01.11.2026 ca. 09:05 CET: Upstream-Stable-Backport des von CISA verlinkten Fixes für den technischen Fehler; er ist keine vollständige Distributions- oder Appliance-Fixmatrix. [11]
- **Cisco ASA/FTD Advisory**, abgerufen am 01.11.2026 ca. 09:06 CET: Herstellerangaben zu Konfigurationsvoraussetzungen, Fixreleases, fehlenden Workarounds und aktiver Ausnutzung im Oktober. [12]

## References

[1]: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json "CISA – Catalog of Known Exploited Vulnerabilities JSON"
[2]: https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching "CISA – Critical Vulnerabilities in PHP Require Immediate Patching"
[3]: https://www.php.net/archive/2026.php "PHP – News Archive 2026"
[4]: https://www.cisa.gov/news-events/alerts/2026/10/29/cisa-adds-two-known-exploited-vulnerabilities-catalog "CISA – Adds Two Known Exploited Vulnerabilities to Catalog on 29 October 2026"
[5]: https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/ "GitLab – Critical Patch Release 19.4.2, 19.3.5, 19.2.8"
[6]: https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-CVE-2026-104935?language=en_US "Ivanti – Security Advisory Ivanti Connect Secure CVE-2026-104935"
[7]: https://www.cisa.gov/news-events/alerts/2026/10/26/cisa-adds-two-known-exploited-vulnerabilities-catalog "CISA – Adds Two Known Exploited Vulnerabilities to Catalog on 26 October 2026"
[8]: https://www.adobe.com/trust/security/products/commerce/apsb26-73.html "Adobe – Security update available for Adobe Commerce APSB26-73"
[9]: https://github.com/google/brotli/releases/tag/v1.2.1 "Google Brotli – Release v1.2.1"
[10]: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017 "Broadcom – VMware security advisory 38017"
[11]: https://git.kernel.org/stable/c/3599e6b3cc1ada96883d496a50a210d3afbb6987 "Linux stable tree – preserve shared-frag marker during coalescing"
[12]: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-tunnel-dos-s6mgkb75 "Cisco – ASA and FTD Remote Access SSL VPN Tunnel Denial of Service Vulnerability"
