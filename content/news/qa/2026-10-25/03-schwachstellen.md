# Quellenbefund – Aktiv ausgenutzte Schwachstellen

**Newsfeld:** Aktiv ausgenutzte Schwachstellen  
**Zielgruppe:** Schweizer KMU  
**Berichtsfenster:** 18.10.2026, 09:00 CEST bis 25.10.2026, 09:00 CET, Europe/Zurich  
**Tatsächlicher Abruf:** 25.10.2026, 09:06–09:07 CET, nach Ende des Berichtsfensters. Mit dem Wechsel von CEST auf CET am 25.10. ist die angegebene Zeitzone berücksichtigt.

Der offizielle CISA-KEV-JSON-Datensatz wurde direkt abgerufen. Er meldete beim Abruf `catalogVersion` **2026.10.23**, `dateReleased` **23.10.2026 19:30:18 UTC** (21:30:18 CEST) und 1'756 Einträge. Die nach `dateAdded` vom 18. bis 25.10.2026 gefilterten neuen Einträge waren: Arista VeloCloud Orchestrator (**CVE-2026-114625**, 23.10.), Collabora Online – Built-in CODE Server (**CVE-2026-110447**, 23.10.), EG Secure Solutions SiteGuard Server Edition (**CVE-2026-106931**, 20.10.), Plex Media Server (**CVE-2026-96652**, **-96654**, **-96655**, **-96656**, je 20.10.) sowie Siemens Software Center (**CVE-2026-110936**, 20.10.). [1]

Der Datensatz ist der tatsächlich nach 09:00 CET abgerufene aktuelle Stand, jedoch kein Nachweis des minutengenauen Website-Wortlauts oder einer lückenlosen historischen Veröffentlichung innerhalb des Fensters. Sein ausgewiesener Freigabestand vom 23.10. belegt zudem nicht, wann CISA allfällige spätere Änderungen auf einer Website eingespielt hätte. Eine Vollständigkeitszusage für alle Hersteller- oder Schwachstellenmeldungen wird nicht gemacht.

## 1. Arista VeloCloud Orchestrator On-Prem: KEV-Neueintrag und Fixstände

CISA nahm **CVE-2026-114625** am **23.10.2026** in KEV auf. Arista veröffentlichte das Security Advisory 0199 am **22.10.2026** und bezeichnet die Schwachstelle als aktiv ausgenutzt. Sie betrifft VeloCloud Orchestrator (VCO) On-Prem: Ein authentifizierter Nutzer mit mindestens der Rolle *Enterprise Read Only* kann laut Hersteller Operator-Rechte und Funktionen eines lokalen Superuser-Operators erlangen. Netzwerkzugriff auf das VCO-Webinterface und eine gültige Sitzung sind erforderlich. [1] [2]

**Betroffene Produktzweige und Fix:** Betroffen sind VCO 5.2.x vor **5.2.3.18**, 6.1.x vor **6.1.3.10** und 6.4.x vor **6.4.2.12**. End-of-Support-Versionen wurden nicht bewertet. Der Hersteller nennt die jeweils genannten Versionen und spätere Versionen desselben Zweigs als korrigiert. [2]

**Self-hosted/On-Prem:** Betreiber sollen zuerst Plattform und Versionszweig abgleichen und auf den passenden Fixstand aktualisieren. Bis zum Update empfiehlt Arista, das VCO-Webinterface auf vertrauenswürdige Administrationsnetze zu beschränken sowie Web-, Backend-, System- und Datenbanklogs bei Verdacht vor einer Behebung soweit praktikabel zu sichern. Diese Abschottung ist eine zusätzliche Schutzmassnahme, kein gleichwertiger Fix. [2]

**Cloud/Hosted:** Arista erklärt ausdrücklich, dass gehostete VCO-Instanzen einschliesslich Dedicated betroffen waren, aber bereits gepatcht wurden. Diese Aussage gilt für die von Arista so bezeichneten Hosted-/Dedicated-Angebote; ein Schweizer KMU mit durch einen Dritten betriebenem VCO sollte Vertrags- und Instanzbezug sowie den Patchstatus beim Betreiber bestätigen lassen. [2]

**KMU-Relevanz und Grenze:** Priorität besteht bei eingesetztem VCO mit erreichbarem Administrationsportal, nicht pauschal bei Arista-Netzwerkprodukten. Arista listet etwa VeloCloud Edge und Gateway sowie eine Vielzahl weiterer Arista-Produkte als nicht betroffen. Die im KEV eingetragene US-BOD-Frist vom 26.10. ist keine Schweizer gesetzliche oder regulatorische Pflicht. [1] [2]

## 2. Nextcloud mit Collabora Online – Built-in CODE Server: KEV-Neueintrag, Update oder Entfernung

CISA nahm **CVE-2026-110447** am **23.10.2026** in KEV auf; die Aufnahme ist der Beleg für eine Ausnutzung in der Praxis. Die vom CollaboraOnline-Projekt veröffentlichte Sicherheitsmeldung datiert vom **14.10.2026**. Sie beschreibt eine unauthentifizierte OS-Command-Injection über `proxy.php` in der Nextcloud-App **richdocumentscode** (Collabora Online – Built-in CODE Server). Die Attacke funktioniert laut Hersteller nur, solange der eingebaute CODE-Server nicht läuft, etwa nach Container-Neustart, Upgrade oder Absturz. [1] [3]

**Betroffenes Produkt und Fix:** Betroffen ist ausschliesslich die App `richdocumentscode` vor **26.4.303**. Korrigiert ist Version **26.4.303**. Das bloss Deaktivieren der App reicht laut Hersteller nicht; sie muss mindestens auf 26.4.303 aktualisiert oder entfernt werden. Für End-of-Life-Nextcloud bis einschliesslich Version 29 nennt der Hersteller Upgrade von Nextcloud oder Entfernung der App. Standalone-Collabora-Online-Server sind nicht betroffen. [3]

**Self-hosted:** Für selbst betriebene Nextcloud-Instanzen mit installierter App ist der konkrete App-Stand zu prüfen. Bei einer verwundbaren App muss ein Update auf 26.4.303 oder neuer erfolgen oder die App entfernt werden. Nach Neustarts, Updates und Abstürzen ist die vom Hersteller genannte Sonderbedingung besonders relevant. Eine generelle Aussage über andere Nextcloud-Apps oder einen normalen Standalone-Collabora-Server wäre nicht belegt. [3]

**Cloud/Managed:** Das Originaladvisory ordnet gehostete oder von Dritten betriebene Nextcloud-Angebote nicht als betroffen oder nicht betroffen ein. Aus der KEV-Aufnahme lässt sich daher kein Patchstatus eines Managed- oder Cloud-Tenants ableiten. Betroffene sollten beim jeweiligen Betreiber schriftlich bestätigen lassen, ob `richdocumentscode` eingesetzt wird und welcher Update- oder Entfernungsstatus vorliegt. [1] [3]

**KMU-Relevanz und Grenze:** Der Befund ist für KMU mit selbst betriebenem Nextcloud und der genannten Office-Integrations-App prioritär. Er betrifft nicht allein aufgrund einer Nutzung von Nextcloud oder Collabora jede Installation. Die im KEV aufgeführte US-BOD-Frist vom 26.10. begründet keine Schweizer Pflicht. [1] [3]

## 3. Plex Media Server: vier KEV-Einträge als eine Patch- und Incident-Meldung

CISA nahm am **20.10.2026** vier miteinander verkettbare Plex-Media-Server-Schwachstellen neu in KEV auf: **CVE-2026-96652**, **CVE-2026-96654**, **CVE-2026-96655** und **CVE-2026-96656**. In einer Aktualisierung seiner offiziellen Sicherheitsmeldung vom **19.10.2026 20:17 UTC** (am 20.10. aktualisiert) führt Plex die vier CVEs auf und erklärt, dass sie zusammen einem nicht authentifizierten Remote-Angreifer Code mit den Rechten des Plex-Media-Server-Prozesses erlauben. Plex nennt die Schwachstellen aktiv und breit ausgenutzt und verweist auf einen am 16.10. veröffentlichten öffentlichen Proof of Concept. [1] [4]

**Betroffenes Produkt und Fix:** Plex Media Server **1.43.3.10861 und neuer** ist laut Hersteller nicht betroffen. Der Hersteller bündelt die vier CVEs in einem Patchziel, statt für jede CVE einen abweichenden Fixzweig zu nennen. Besonders zu prüfen sind ältere, aus dem Internet erreichbare Server. [4]

**Self-hosted:** Plex adressiert Betreiber von Plex Media Server auf Windows, macOS, Linux, NAS und Docker. Sie sollen auf mindestens 1.43.3.10861 aktualisieren. Für einen älteren und internet-erreichbaren Server empfiehlt Plex, von einer möglichen Kompromittierung auszugehen und unter anderem unbekannte Prozesse, unübliche Dateien im Codecs-Ordner, ausgehende Verbindungen und hohe CPU-Last zu untersuchen. Bei Befund oder nicht ausschliessbarer Kompromittierung empfiehlt Plex einen Neuaufbau aus einer sauberen Installation, das Abmelden aller Geräte und eine Passwortänderung. Wenn Fernzugriff nicht erforderlich ist, soll er deaktiviert und Port 32400 nicht unnötig weitergeleitet werden. [4]

**Cloud/Managed:** Die Plex-Meldung behandelt das selbst betriebene Produkt Plex Media Server, nicht einen Cloud- oder Managed-Serverdienst. Sie enthält deshalb keinen belastbaren Patchstatus für einen allenfalls von einem IT-Dienstleister betriebenen Server oder für andere Plex-Dienste. Dort ist das konkrete Betriebsmodell und der Fixstand beim Betreiber zu klären; aus der Meldung darf keine pauschale Cloud-Entwarnung abgeleitet werden. [4]

**KMU-Relevanz und Grenze:** Die Meldung ist vor allem relevant, wenn ein KMU einen Plex-Media-Server auf eigener Infrastruktur, NAS oder Docker betreibt und dieser extern erreichbar ist. Die vier KEV-CVEs sind hier als ein zusammenhängender Patch- und möglicher Incident-Fall dargestellt, nicht als vier voneinander unabhängige News. Die verschiedenen CISA-US-Fristen vom 23.10. beziehungsweise 03.11. sind keine Schweizer Pflicht. [1] [4]

## Nicht als Meldung ausgewählt

Der KEV-Abruf zeigte ferner CVE-2026-106931 in EG Secure Solutions SiteGuard Server Edition und CVE-2026-110936 in Siemens Software Center. SiteGuard wurde wegen des ohne weiteren belegten Einsatzkontext engen, produktspezifischen Bezugs und Siemens Software Center wegen des im KEV beschriebenen lokal authentifizierten Angriffswegs nicht unter die höchstens drei für Schweizer KMU priorisierten Meldungen aufgenommen. Die vier Plex-CVEs wurden aus dem oben begründeten gemeinsamen Herstellerfix als eine Meldung gezählt. Die in der Vorwoche behandelten PAN-OS CVE-2026-0322, Atlassian CVE-2026-21589 und BeyondTrust CVE-2026-102764 erscheinen nicht erneut.

## Vormerkungen für Pflege am 01.11.2026

Diese Vormerkungen sind nur Prüfanlässe für die nächste turnusmässige Pflege. Sie sind **kein** heutiger Quellenstand, keine Textänderung und keine Fachfreigabe der zwölf Artikelentwürfe.

1. **Artikel 08 – IT-Sicherheitscheck für Schweizer KMU:** Prüfen, ob Inventar- und Risikoregistervorlage ausdrücklich nach selbst betriebenen, internet-erreichbaren Administrations- und Kollaborationsdiensten (VCO, Nextcloud mit `richdocumentscode`, Plex Media Server) sowie nach verantwortetem Betriebsmodell fragen sollte. Der Prüfungspunkt muss KEV als Priorisierungssignal und keine Schweizer Rechtsfrist darstellen.
2. **Artikel 07 – Ransomware-Wiederherstellung testen:** Prüfen, ob die Restore-Checkliste bei einem möglichen kompromittierten Server den Neuaufbau aus sauberer Installation und die getrennte Beurteilung von Sicherungen, Log-Erhalt und Zugangsdaten ausreichend klar abgrenzt. Ausgangspunkt ist der Plex-Herstellerhinweis; daraus darf keine allgemeine Plex- oder Incident-Anweisung ohne organisationsbezogene Prüfung werden.
3. **Artikel 11 – Lieferantenrisiken im Griff:** Prüfen, ob die Lieferantenfragen bei gehosteten VCO- und Managed-Nextcloud-Angeboten eine Anbieterbestätigung zum konkret eingesetzten Produkt beziehungsweise zur App und zum Patchstatus verlangen. Die Originalquellen belegen keinen allgemeinen Managed-Nextcloud-Patchstatus.

## Geöffnete Originalquellen und Abrufdaten

* Offizieller CISA-KEV-JSON-Datensatz, direkt abgerufen am 25.10.2026 um 09:06 CET: `catalogVersion` 2026.10.23, `dateReleased` 23.10.2026 19:30:18 UTC.
* Arista Security Advisory 0199, publiziert 22.10.2026, geöffnet am 25.10.2026 um 09:06 CET.
* CollaboraOnline GitHub Security Advisory GHSA-g3vx-3m76-fghh, publiziert 14.10.2026, geöffnet am 25.10.2026 um 09:06 CET.
* Plex-Meldung im offiziellen Plex-Forum, ursprünglicher Beitrag 01.09.2026; CVE-/Ausnutzungsaktualisierung erstellt am 19.10.2026 20:17 UTC und zuletzt bearbeitet am 20.10.2026 14:34 UTC, geöffnet am 25.10.2026 um 09:06 CET.

## References

[1]: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json "CISA Known Exploited Vulnerabilities JSON Catalog"
[2]: https://www.arista.com/en/support/advisories-notices/security-advisory/24838-security-advisory-0199 "Arista Security Advisory 0199"
[3]: https://github.com/CollaboraOnline/online/security/advisories/GHSA-g3vx-3m76-fghh "Collabora Online Unauthenticated OS command injection in the richdocumentscode proxy"
[4]: https://forums.plex.tv/t/important-security-update-for-plex-media-server-v1-43-2-and-earlier/942319 "Plex Important Security Update for Plex Media Server v1.43.2 and earlier"
