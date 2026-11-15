# Aktiv ausgenutzte Schwachstellen – 15.11.2026, ISO-KW 46

**Drei Meldungen sind belegt:** neue KEV-Aufnahmen für Outlook und Chromium am 10. November sowie eine materielle SonicWall-Advisoryrevision vom 9. November. SonicWall ist keine neue Katalogaufnahme und kein neu veröffentlichter Patch. Der vollständig direkt abgerufene offizielle CISA-JSON enthält zwölf Einträge mit `2026-11-08 <= dateAdded <= 2026-11-15`; nicht alle werden als KMU-News ausgewählt. [1] [2] [3] [4] [7]

**Newsfenster:** 08.11.2026, 09:00 bis 15.11.2026, 09:00 CET, Europe/Zurich. **Tatsächliche Quellenrückgaben:** 15.11.2026, 09:05:58–09:07:36 CET. Das vollständige KEV-Dokument wurde um 09:06:23 CET strukturell eingelesen. Alle Abrufe fanden nach Redaktionsschluss statt. Die Zeiten unten sind protokollierte Werkzeugrückgaben; nur beim ergänzenden Google-HTTP-Abruf wurde die tatsächliche HTTP-Rückgabe zusätzlich mit der Systemuhr protokolliert. Es wird kein historischer sekundengenauer Seitenstand um 09:00 behauptet.

Der Katalogstand ist `2026.11.13`, `dateReleased` ist `2026-11-13T20:24:18.3008Z`, und alle **1781** Datensätze wurden aus dem vollständigen gespeicherten Abruf mit einem JSON-Parser eingelesen. Die Datensatzanzahl stimmt mit `count` überein. Der Abruf umfasst 1 854 379 Bytes; SHA-256: `4028ec035856331a717d3305e87e45be37d400fc500da34a5464f05fc2773764`. Die direkte Abrufkopie liegt unter [news03-kev-original.json](news03-kev-original.json). Der Filter lief über sämtliche Datensätze, nicht nur über den gekürzten Werkzeugauszug. Die zwölf Treffer verteilen sich auf den 9., 10. und 13. November; es gibt keine Treffer an den zeitlich mehrdeutigen Randtagen 8. oder 15. November. `dateAdded` ist ein Aufnahmetag, kein Datum des Angriffsbeginns oder eines neuen Patches. [1]

## 1. Outlook: Neue KEV-Aufnahme und Sicherheitsupdates vom 10. November

**Datum und Fakt:** CISA nahm **CVE-2026-124194** am **10.11.2026** in KEV auf. Microsoft veröffentlichte am selben Tag das Advisory und Sicherheitsupdates und weist `Exploited: Yes` aus. Die Schwachstelle kann beim Öffnen einer präparierten Nachrichtendatei eine Verbindung zu einem vom Angreifer kontrollierten Netzwerkziel ohne die übliche Warnung vor externem Inhalt auslösen. Microsoft nennt die mögliche Offenlegung eines NTLMv2-Hashes, mit dem sich ein Angreifer als Benutzer authentifizieren könnte. [1] [2] [3]

Die Nutzerinteraktion ist eine wichtige Einschränkung: Der Benutzer muss eine bösartige Datei öffnen; **die Vorschau ist laut Microsoft kein Angriffsvektor**. Der KEV-Titel mit «Missing User Interaction» darf deshalb nicht als Beleg für eine voraussetzungslose Zero-Click-Lücke übersetzt werden. Microsoft klassifiziert die Lücke als Spoofing, nicht als hier belegte Remote-Codeausführung. Die neue Katalogaufnahme, die Advisorypublikation und die Patchveröffentlichung liegen hier tatsächlich alle im Wochenfenster. [3]

### Hersteller-Fixmatrix

Die MSRC-CVE-Seite nennt Microsoft 365 Apps for Enterprise sowie Office LTSC 2024 und 2021 jeweils in 32 und 64 Bit. Für die Apps verweist sie auf die Sicherheitsrelease-Liste. Deren Abschnitt vom 10. November enthält CVE-2026-124194 und die folgenden kanalgenauen Builds. [3] [5]

| Produkt bzw. Updatekanal | Dokumentierter Sicherheitsstand vom 10.11.2026 |
|---|---|
| Microsoft 365 Apps, Current Channel | Version 2610, Build **20527.20196** |
| Monthly Enterprise Channel, Version 2610 | Build **20527.20194** |
| Monthly Enterprise Channel, Version 2609 | Build **20430.20264** |
| Monthly Enterprise Channel, Version 2608 | Build **20326.20320** |
| Semi-Annual Enterprise Channel, laut Quelle mit Monthly-Enterprise-Builds, Version 2610 | Build **20527.20192** |
| Derselbe Semi-Annual-Kanal, Version 2609 | Build **20430.20262** |
| Derselbe Semi-Annual-Kanal, Version 2608 | Build **20326.20318** |
| Office LTSC 2024, 32/64 Bit, Volumenlizenz | Version 2408, Build **17932.21140**; MSRC: **16.0.17932.21140** |
| Office LTSC 2021, 32/64 Bit, Volumenlizenz | Version 2108, Build **14334.21048**; MSRC: **16.0.14334.21048** |

**Fixumfang und Unsicherheit:** Dies sind dokumentierte Releasebuilds, keine pauschale kanalübergreifende Mindestversion. Die allgemeine Sicherheitsrelease-Liste gilt auch für Microsoft 365 Apps for Business und weitere Office-Linien; die geöffnete CVE-Seite benennt dagegen ausdrücklich die sechs Enterprise-/LTSC-Produktzeilen. Für nicht dort ausdrücklich genannte Installationsformen wird keine ungeprüfte CVE-spezifische Betroffenheit oder Fixzuordnung ergänzt. Eine Aussage zu Outlook im Web, zum neuen Outlook oder zu sämtlichen Microsoft-365-Diensten ist damit nicht belegt. [3] [5]

**KMU-Relevanz und Prüfpunkt:** Geschäfts-E-Mail auf betroffenen Outlook-Desktopinstallationen ist relevant für Konto- und Identitätsmissbrauch. Mit dem IT-Dienstleister Produkt, Architektur, Updatekanal und tatsächlich installierten Build abgleichen. Bei verdächtigen Dateien oder Authentifizierungen ist eine fachliche Vorfallabklärung separat erforderlich; ein Update allein belegt weder Nichtbetroffenheit noch Bereinigung. Es wurde kein Gerät, Konto oder Tenant geprüft.

**Originalbeleg-URLs:** [CISA-JSON][1], [CISA-Aufnahmemeldung][2], [Microsoft-CVE-Advisory][3] und [Microsoft-Sicherheitsrelease-Liste][5].

## 2. Chromium: Aktive Ausnutzung, Chrome- und Edge-Fixes im Wochenfenster

**Datum und Fakt:** CISA nahm **CVE-2026-125350** am **10.11.2026** auf. Googles Desktop-Release vom **09.11.2026** beschreibt einen Use-after-free-Fehler in XML und bestätigt einen existierenden Exploit «in the wild». Der vom Chrome-CNA publizierte CVE-Datensatz nennt mögliche Codeausführung **innerhalb der Sandbox** über eine präparierte HTML-Seite. Daraus folgt kein belegter Sandbox-Ausbruch oder vollständiger Gerätezugriff. Hier sind sowohl der Herstellerpatch als auch die spätere KEV-Aufnahme neu im Fenster. [1] [2] [4] [6]

### Hersteller-Fixmatrix

| Produkt und Plattform | Direkt dokumentierter CVE-Fixrelease | Datum |
|---|---|---|
| Google Chrome Stable, Windows und Mac | **157.0.8103.50 / 157.0.8103.51** | 09.11.2026 |
| Google Chrome Stable, Linux | **157.0.8103.50** | 09.11.2026 |
| Microsoft Edge Stable | **157.0.4341.46**; Hersteller nennt den CVE-Fix ausdrücklich | 09.11.2026 |
| Microsoft Edge für Android | **157.0.4341.53**; Hersteller nennt den CVE-Fix ausdrücklich | 11.11.2026 |

Die Chrome-Versionsgrenze `prior to 157.0.8103.50` ist im CNA-Beschreibungstext dokumentiert. Googles Release kündigt eine gestaffelte Auslieferung über die folgenden Tage bzw. Wochen an; die Publikation beweist nicht die Installation auf einem konkreten Arbeitsplatz. Microsoft listet zusätzlich Edge Stable **157.0.4341.57** vom 13. November, dort ohne erneute ausdrückliche CVE-Zuordnung. Als direkt CVE-verifizierter Fixrelease wird deshalb die explizite Zeile vom 9. November verwendet, nicht eine erfundene neue Erstbehebung am 13. November. [4] [6] [8]

**Fixumfang und Unsicherheit:** Google-Chrome-Versionen sind nicht als Fixnummern für Edge, Opera oder andere Chromium-Produkte übertragbar. Ein eigener Opera-Fix, Chrome-Mobile-Fix, Edge-iOS-Fix oder Extended-Stable-Fix wurde hier nicht verifiziert. Die maschinell extrahierte CVE-Produktzeile formuliert die Versionsgrenze unklar; die Matrix stützt sich auf den eindeutigen CNA-Beschreibungstext und die direkt gelesenen Herstellerreleases. [6] [8]

**KMU-Relevanz und Prüfpunkt:** Webbrowser werden auf Geschäftsarbeitsplätzen breit eingesetzt. Browserprodukt, Plattform und Kanal erfassen und den laufenden Versionsstand nach angewandtem Update und erforderlichem Neustart bestätigen lassen. Die Quelle belegt bekannte aktive Ausnutzung, nicht einen Angriff auf ein Schweizer KMU und nicht eine Ransomware-Kampagne.

**Originalbeleg-URLs:** [CISA-JSON][1], [CISA-Aufnahmemeldung][2], [Google-Release][4], [Chrome-CNA-Datensatz][6] und [Microsoft-Edge-Sicherheitsreleases][8].

## 3. SonicWall: Neuer Workaround in Revision 1.1, kein neuer Patch

**Datum und Fakt:** Advisory **SNWLID-2026-0014** weist `Last Updated: 2026-11-09` und Revision **1.1 vom 09.11.2026** aus. Die Historie benennt die Aktualisierung des Workaround-Abschnitts für **CVE-2026-19868**. Gegenüber dem Vorwochenbericht, der keinen Workaround vorfand, ist dies eine neue datierte materielle Änderung. Die zusätzlich geänderten Credits sind nicht der Newsgrund. Die KEV-Aufnahme bleibt **06.11.2026**; es wird keine neue Aufnahme oder Patchveröffentlichung behauptet. [1] [7]

Der neue Herstellerworkaround lautet: Wenn SAML verwendet wird und ein Firmwareupgrade nicht möglich ist, sollen aktive **LDAP-, RADIUS- und TACACS+-Authentifizierungsserver**, die auf der Firewall konfiguriert sind, deaktiviert oder gelöscht werden. Das ist keine allgemeine Empfehlung, unkontrolliert Unternehmensverzeichnisdienste abzuschalten. Die Lücke betrifft weiterhin nur SSLVPN mit aktiviertem SAML; gültige Zugangsdaten einer alternativen Authentifizierungsmethode können SAML-Kontrollen und gegebenenfalls die darüber erzwungene MFA umgehen. [7]

### Erneut geöffnete Hersteller-Fixmatrix

| Plattformumfang des Advisorys | Betroffen laut Hersteller | Unveränderter Fixstand |
|---|---|---|
| Aufgeführte Gen7-Hardware-Firewalls und Gen7 NSv | **7.3.3-7015 und ältere Versionen** | **7.3.4-7013 und höher** |
| Aufgeführte Gen8-Hardware-Firewalls und Gen8 NSv | **8.2.2-8015 und ältere Versionen** | **8.2.3-8015 und höher** |

**Fixumfang und Unsicherheit:** Die Plattformmatrix umfasst die im Original einzeln aufgeführten TZ-, NSa-, NSsp- und NSv-Modelle; sie gilt nicht ungeprüft für andere Generationen oder SonicWall-Produkte. Das Original weist `First Published: 2026-11-06` aus, während die initiale Historienzeile `05-Nov-2026` nennt. Diese ältere Metadatenabweichung bleibt offen; die neue materielle Revision ist dagegen eindeutig mit 9. November datiert. SonicWall selbst spricht weiterhin von untersuchter potenzieller Ausnutzung; der stärkere Nachweis bekannter Ausnutzung stammt aus KEV. Die übrigen CVEs des Sammeladvisorys werden nicht als aktiv ausgenutzt ausgegeben. [1] [7]

**KMU-Relevanz und Prüfpunkt:** Für SAML-geschützte Fernzugänge ist der neu dokumentierte Übergangsweg relevant. Modell, Firmwarebuild, SAML-Konfiguration und alternative Authentifizierungsserver mit dem zuständigen Dienstleister abgleichen. Vor einem Workaround müssen die Auswirkungen auf andere Anmeldungen und die Verfügbarkeit beurteilt werden; dieser Bericht ist keine Konfigurations- oder Produktfreigabe. Bestehende MFA allein ist kein Nachweis der Nichtbetroffenheit.

**Originalbeleg-URLs:** [CISA-JSON][1] und [SonicWall-Advisory samt Revisionshistorie][7].

## Vormerkungen und begrenzte Nichtfunde

**WordPress und Apple werden nicht erneut als News ausgegeben.** Für WordPress CVE-2026-119977 bleibt KEV-`dateAdded` auf 3. November. Die erneut geöffnete offizielle Dokumentation nennt 7.1.4 vom 28. Oktober und die bereits in der Vorwoche dokumentierten Backports; hinter «Last updated» ist kein Datum auslesbar. Eine neue datierte materielle Revision im Wochenfenster ist in dieser geprüften Quelle nicht belegt. Das ist ein begrenzter Nichtfund, kein Nachweis, dass es nirgends eine Änderung gab. [1] [9]

Für Apple CVE-2024-27834 bleibt KEV-`dateAdded` auf 4. November. Das erneut geöffnete Safari-17.5-Original nennt weiterhin den Release vom 13. Mai 2024 und das Seitenpublikationsdatum 15. Januar 2025, ohne neue datierte materielle Änderung zur CVE. Apples allgemeine Übersicht enthält neue Releases vom 9.–13. November; deren blosse Existenz belegt aber keine Revision oder neue aktive Ausnutzung der Vorwochen-CVE. Die fünf anderen historischen Apple-CVE-Advisories und sämtliche neuen Releaseadvisories wurden nicht vollständig erneut geöffnet. Es wird deshalb ausdrücklich kein umfassender Apple-Nichtfund behauptet. [1] [10] [11]

**OpenSSH ist zurückgestellt, nicht veraltet oder widerlegt:** CVE-2026-123158 wurde am 9. November neu in KEV aufgenommen. Die geöffneten OpenSSH-/Alpine-Originale datieren den Upstreamfix **10.6p2** jedoch bereits auf **5. November**. Eine spätere autorisierte, systemspezifische Prüfung muss musl, deaktiviertes PAM, Passwortanmeldung und die genannten Kontovoraussetzungen unterscheiden; nicht alle OpenSSH-Installationen sind betroffen. Alpine dokumentiert distributionsspezifische Backports und den erforderlichen Neustart von `sshd`. Wegen der Obergrenze von drei Meldungen und der materiellen SonicWall-Revision bleibt dies eine Vormerkung, keine vierte ausformulierte News. Die KEV-Aufnahme vom 9. November darf in einer späteren Ausgabe nicht allein wegen dieser Zurückstellung als dann neue Meldung erscheinen. [1] [12] [13] [14]

Weitere nicht priorisierte neue Katalogtreffer betreffen UnrealIRCd, Check Point, Openwave, Cisco BroadWorks, zwei Barracuda-CVEs, GPUStack, FreeSwitch und IBM Aspera Faspex. Deren Herstellerfixmatrix wurde nicht recherchiert. Sie können für einzelne KMU oder Dienstleister relevant sein; die Auswahl ist keine vollständige Rangliste aller Risiken. Die vollständige Katalogfilterung ist belegt, eine vollständige Recherche jeder Neuaufnahme oder jeder Schwachstelle ausserhalb KEV dagegen nicht. [1]

Für eine später separat autorisierte Artikelpflege sind Querbezüge zu Artikel 02 und 06 bei Outlook sowie zu Artikel 01, 07, 08 und 11 bei Patchpriorisierung, Wiederanlauf, Risikoregister und IT-Dienstleistern vorzumerken. Keine Artikeldatei, kein globales Manifest und kein CMS wurde verändert. Die verbindliche Wartungsbasis, Vorwochennews und Vorwochensperren wurden nur gelesen. Alle Fachmarker bleiben offen; Erreichbarkeit, Quelleninhalt und allgemeine Orientierung sind keine tatsächliche Fach-, Rechts-, Forensik-, Tenant- oder Produktprüfung und keine Veröffentlichungsfreigabe.

**Keine Schweizer Fristen ableiten:** Der Katalog nennt `dueDate` **24.11.2026** für Outlook und Chromium sowie **20.11.2026** für SonicWall. Diese US-Katalogdaten sind keine Schweizer gesetzlichen Fristen. Die geöffnete CISA-Meldung beschränkt BOD 26-04 ausdrücklich auf FCEB-Behörden. `knownRansomwareCampaignUse` ist bei allen drei ausgewählten CVEs **Unknown**; Ransomware-Nutzung ist damit nicht bestätigt. `forensicTriage: No` bei den drei Einträgen ist keine Schweizer Entwarnung oder Einzelfallentscheidung. Eine bereits erfolgte Kompromittierung wird durch einen Patch nicht ausgeschlossen. [1] [2]

## Quellen mit Abrufdatum, Aussage und Einschränkung

**[1] CISA-KEV-JSON:** Rückgabe 15.11.2026, **09:05:58 CET**; vollständig eingelesen **09:06:23 CET**. Original-URL: <https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json>. Belegt Katalogversion, Datensatzanzahl, zwölf Neuaufnahmen im Datumsfilter und CVE-Eigenschaften. Einschränkung: `dateAdded` hat nur Tagesauflösung; keine vollständige Ausnutzungsliste ausserhalb KEV und keine Schweizer Einzelfallprüfung.

**[2] CISA-Aufnahmemeldung vom 10.11.2026:** Rückgabe **09:06:24 CET**. Original-URL: <https://www.cisa.gov/news-events/alerts/2026/11/10/cisa-adds-six-known-exploited-vulnerabilities-catalog>. Belegt aktive Ausnutzung als Aufnahmegrund und sechs Einträge, darunter Outlook und Chromium; nennt FCEB-Geltung der BOD. Einschränkung: Keine Schweizer Vorfälle, keine Herstellerfixversionen.

**[3] Microsoft-CVE-Advisory:** Rückgabe **09:06:24 CET**. Original-URL: <https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-124194>. Release und Revision 1.0: **10.11.2026**. Belegt Ausnutzung, notwendiges Dateiöffnen, keinen Vorschauangriff und LTSC-Builds. Einschränkung: Kein Tenant-/Gerätebefund; Microsoft-365-Apps-Builds werden verlinkt statt direkt genannt.

**[4] Google-Desktoprelease:** Fetch-Rückgaben **09:06:24 und 09:06:42 CET**. Original-URL: <https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop_018223192.html>. Publikation: **09.11.2026**. Die Fetch-Extraktion zeigte Überschrift und Seitennavigation, aber keinen Artikelkörper. Der Artikelkörper wurde deshalb gezielt zusätzlich per direktem HTTP GET ohne Browser aus dem offiziellen HTML gelesen: **15.11.2026, 09:07:09.707839 CET, HTTP 200**. Belegt Chrome-Fixversionen, XML-Fehler und bestätigte Ausnutzung. Einschränkung: Gestaffelte Auslieferung und keine allgemeine Fixzusage für andere Chromium-Produkte. Das Datum und die Fixangaben wurden nicht aus Suchsnippets übernommen.

**[5] Microsoft-Office-Sicherheitsreleases:** Rückgabe **09:06:44 CET**; vollständiger gespeicherter Abschnitt inklusive Outlook-CVE-Zuordnung lokal gelesen **09:07:36 CET**. Original-URL: <https://learn.microsoft.com/en-us/officeupdates/microsoft365-apps-security-updates>. Belegt die Builds im Abschnitt **10.11.2026**, in dem CVE-2026-124194 genannt ist. Einschränkung: Sammelliste; tatsächlicher Produkt-, Kanal- und Installationsumfang ist gesondert zu bestätigen.

**[6] Chrome-CNA-Datensatz:** Rückgabe **09:07:05 CET**. Original-URL: <https://www.cve.org/CVERecord?id=CVE-2026-125350>. Veröffentlicht und aktualisiert **10.11.2026**. Belegt Versionsgrenze im Beschreibungstext und Codeausführung innerhalb der Sandbox. Einschränkung: Extrahierte Produktstatuszeile ist verkürzt/unklar; keine behauptete Sandbox-Flucht.

**[7] SonicWall-Advisory:** Rückgabe **09:06:45 CET**. Original-URL: <https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014>. Revision 1.1 und letzter Update-Tag **09.11.2026**. Belegt neuen Workaround und unveränderte Fix-/Plattformmatrix. Einschränkung: Initiale Datumsmetadaten weichen voneinander ab; Workaroundauswirkungen nicht konkret geprüft.

**[8] Microsoft-Edge-Sicherheitsreleases:** Rückgabe **09:07:05 CET**. Original-URL: <https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security>. Belegt explizite CVE-Fixes für Stable vom **09.11.2026** und Android vom **11.11.2026**. Einschränkung: Kein expliziter CVE-Beleg für iOS, Opera oder Extended Stable im verwendeten Abschnitt; neuere Stable-Zeile vom 13. November ist keine neu behauptete Erstbehebung.

**[9] WordPress-Versionsdokumentation:** Rückgabe **09:06:45 CET**. Original-URL: <https://wordpress.org/documentation/wordpress-version/version-7-1-4/>. Belegt bekannten Release **28.10.2026** und dokumentierte Backports. Einschränkung: «Last updated» ohne auslesbaren Datumswert; kein umfassender Nichtfund neuer Revisionen.

**[10] Apple-Sicherheitsübersicht:** Rückgabe **09:06:47 CET**. Original-URL: <https://support.apple.com/en-us/100100>. Belegt vorhandene Releasezeilen vom **09.–13.11.2026**. Einschränkung: Releaseübersicht allein belegt weder aktive Ausnutzung noch eine materielle Revision der Vorwochen-CVE; keine vierte News daraus erstellt.

**[11] Apple-Safari-Original:** Rückgabe **09:07:10 CET**. Original-URL: <https://support.apple.com/en-us/120896>. Release **13.05.2024**, Seitenpublikation **15.01.2025**. Belegt weiterhin den historischen CVE-2024-27834-Fix. Einschränkung: Nur dieses historische Apple-CVE-Advisory erneut geöffnet; kein vollständiger Apple-Revisionsvergleich.

**[12] Alpine-Original:** Rückgabe **09:06:24 CET**. Original-URL: <https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/>. Publikation **05.11.2026**. Belegt Konfigurationsvoraussetzungen, distributionsspezifische Fixpakete und notwendigen `sshd`-Neustart. Einschränkung: Keine Verallgemeinerung auf alle Linux-/OpenSSH-Systeme; nur Vormerkung.

**[13] OpenSSH-Releasenotes:** Rückgabe **09:06:47 CET**, vollständiger Sicherheitsabschnitt lokal gelesen **09:07:36 CET**. Original-URL: <https://www.openssh.org/releasenotes.html>. Belegt Release **10.6p2 vom 05.11.2026**, musl/PAM-Abgrenzung und Upstreambehebung. Einschränkung: Alter Patchtag liegt vor dem Newsfenster; neue Entwicklung ist allein die KEV-Aufnahme vom 9. November.

**[14] CISA-Aufnahmemeldung vom 09.11.2026:** Rückgabe **09:07:36 CET**. Original-URL: <https://www.cisa.gov/news-events/alerts/2026/11/09/cisa-adds-four-known-exploited-vulnerabilities-catalog>. Belegt die vier Aufnahmen, darunter OpenSSH, aufgrund aktiver Ausnutzung. Einschränkung: Keine eigene Herstellerfixmatrix und keine vierte priorisierte Meldung dieses Berichts.

## References

[1]: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json "CISA – offizieller vollständiger KEV-JSON"
[2]: https://www.cisa.gov/news-events/alerts/2026/11/10/cisa-adds-six-known-exploited-vulnerabilities-catalog "CISA – sechs KEV-Aufnahmen vom 10. November 2026"
[3]: https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-124194 "Microsoft – CVE-2026-124194"
[4]: https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop_018223192.html "Google – Chrome Desktop Stable vom 9. November 2026"
[5]: https://learn.microsoft.com/en-us/officeupdates/microsoft365-apps-security-updates "Microsoft – Office-Sicherheitsreleases"
[6]: https://www.cve.org/CVERecord?id=CVE-2026-125350 "Chrome-CNA – Originaldatensatz CVE-2026-125350"
[7]: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014 "SonicWall – SNWLID-2026-0014, Revision 1.1"
[8]: https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security "Microsoft – Edge-Sicherheitsreleases"
[9]: https://wordpress.org/documentation/wordpress-version/version-7-1-4/ "WordPress – Version 7.1.4 und Backports"
[10]: https://support.apple.com/en-us/100100 "Apple – Sicherheitsrelease-Übersicht"
[11]: https://support.apple.com/en-us/120896 "Apple – Sicherheitsinhalt Safari 17.5"
[12]: https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/ "Alpine – OpenSSH-Passwortauthentifizierungsumgehung"
[13]: https://www.openssh.org/releasenotes.html "OpenSSH – Releasenotes 10.6p2"
[14]: https://www.cisa.gov/news-events/alerts/2026/11/09/cisa-adds-four-known-exploited-vulnerabilities-catalog "CISA – vier KEV-Aufnahmen vom 9. November 2026"
