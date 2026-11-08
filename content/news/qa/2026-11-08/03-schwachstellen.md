# Aktiv ausgenutzte Schwachstellen – 08.11.2026, ISO-KW 45

Drei neue, für Schweizer KMU relevante KEV-Aufnahmen sind belegt: SonicWall CVE-2026-19868 am **06.11.2026**, Apple CVE-2024-27834 am **04.11.2026** und WordPress CVE-2026-119977 am **03.11.2026**. Die vollständige Filterung des direkt geöffneten offiziellen CISA-JSON nach `2026-11-01 <= dateAdded <= 2026-11-08` ergibt genau diese drei Einträge. Der Katalog nennt Version `2026.11.06`, Freigabe `2026-11-06T19:44:45.1797Z` und 1769 Einträge. Die neue Entwicklung ist jeweils die Aufnahme in den Katalog bekannter ausgenutzter Schwachstellen; daraus folgt kein Nachweis einer Kompromittierung einer konkreten KMU-Umgebung. [1]

**Newsfenster:** 01.11.2026, 09:00 bis 08.11.2026, 09:00 CET, Europe/Zurich. **Tatsächliche Prüfung:** Beginn laut Systemuhr am 08.11.2026, 09:04:06 CET; Quellenrückgaben zwischen 09:04:12 und 09:05:11 CET. Sämtliche Abrufe fanden nach 09:00 statt. Die Referenzen nennen die tatsächlich protokollierten Rückgabezeiten der Werkzeuge, nicht eine erfundene sekundengenaue Server-Abrufzeit. `dateAdded` enthält nur Kalendertage; ein exakter Wortlautstand um 09:00 ist nicht historisch bewiesen. Keiner der drei Einträge liegt auf einem der zeitlich mehrdeutigen Randtage 01. oder 08.11.

## 1. SonicWall: SSLVPN-Lücke kann SAML und dessen MFA umgehen

SonicWall veröffentlichte Advisory SNWLID-2026-0014 am 06.11.2026; letzter ausgewiesener Update-Tag und Revisionshistorie nennen ebenfalls den 06.11. Für **CVE-2026-19868** beschreibt der Hersteller, dass gültige Zugangsdaten einer alternativen Authentifizierungsmethode die SAML-Kontrollen und möglicherweise die durch SAML erzwungene Mehrfaktor-Authentifizierung umgehen können. Die Lücke betrifft den SonicOS-SSLVPN-Dienst **nur, wenn SAML für SSLVPN-Anmeldungen aktiviert ist**. Das ist keine pauschale unauthentifizierte Umgehung aller SonicWall-MFA-Konfigurationen. [2]

CISA nahm diese CVE am 06.11. in KEV auf. SonicWall selbst formuliert vorsichtiger und nennt einen untersuchten Bericht über **potenzielle** Ausnutzung. Die Nachricht über bekannte aktive Ausnutzung stützt sich deshalb auf KEV, nicht auf einen Proof of Concept oder auf eine stärkere Behauptung im Herstellertext. Die übrigen sechs CVEs im Sammeladvisory werden hier nicht als aktiv ausgenutzt ausgegeben. [1] [2]

### Hersteller-Fixmatrix

| Plattform | Betroffen laut Advisory | Behobene Version laut Advisory |
|---|---|---|
| Gen7 Hardware und aufgeführte Gen7 NSv | 7.3.3-7015 und ältere Versionen | **7.3.4-7013 und höher** |
| Gen8 Hardware und aufgeführte Gen8 NSv | 8.2.2-8015 und ältere Versionen | **8.2.3-8015 und höher** |

Die Gen7-Zeile umfasst TZ 270, 270W, 370, 370W, 470, 470W, 570, 570W, 570P, 670; NSa 2700, 3700, 4700, 5700, 6700; NSsp 10700, 11700, 13700, 15700 sowie NSv 270, 470, 870. Die Gen8-Zeile umfasst TZ 80, 280, 280W, 380, 380W, 480, 580, 680; NSa 2800, 3800, 4800, 5800 sowie NSv XS, S, M, L. Für die NSv-Plattformen nennt das Advisory ESX, KVM, HYPER-V, AWS und Azure. **Kein Workaround** wird genannt. Die Matrix ist nicht auf ungeprüfte Produktgenerationen oder andere SonicWall-Produkte übertragbar. [2]

**KMU-Relevanz und Handlung:** Internet-erreichbare Fernzugänge können betroffen sein. Gerätegeneration, genaue Buildnummer und SAML-Nutzung am konkreten SSLVPN-Zugang erfassen und den passenden Herstellerfix mit dem IT-Dienstleister priorisieren. Bestehende MFA-Nutzung allein ist hier kein Beleg für Nichtbetroffenheit. Ein Update ersetzt keine Vorfallabklärung bei verdächtigen Zugängen und ist keine technische Freigabe durch diesen Bericht.

## 2. Apple: Neue KEV-Aufnahme für seit 2024 behobenen WebKit-Bypass

CISA nahm **CVE-2024-27834** am 04.11.2026 auf. Apples geöffnete Originaladvisories beschreiben einen WebKit-Fehler, durch den ein Angreifer mit bereits vorhandener beliebiger Lese- und Schreibfähigkeit Pointer Authentication umgehen kann. Die Voraussetzung muss ausdrücklich erhalten bleiben: Die CVE ist nicht als eigenständige voraussetzungslose Fernübernahme zu beschreiben. Apple nennt verbesserte Prüfungen als Behebung. Die hier geprüften Fix-Releases erschienen am **13.05.2024**; im Newsfenster ist die KEV-Aufnahme neu, nicht der Patch. [1] [4] [5] [6] [7] [8] [9]

### Direkt verifizierte CVE-Fixmatrix

| Produktlinie bzw. Komponente | Release mit CVE-2024-27834-Fix | Verfügbarkeit im CVE-Abschnitt des Originals |
|---|---|---|
| Safari auf macOS Monterey und Ventura | **Safari 17.5** | macOS Monterey und macOS Ventura [4] |
| iOS/iPadOS, ältere Geräte | **iOS 16.7.8 / iPadOS 16.7.8** | iPhone 8, 8 Plus, X; iPad 5. Generation; iPad Pro 9.7 Zoll und 12.9 Zoll 1. Generation [5] |
| tvOS | **tvOS 17.5** | Apple TV HD und Apple TV 4K, alle Modelle [6] |
| watchOS | **watchOS 10.5** | Apple Watch Series 4 und neuer [7] |
| macOS Sonoma | **macOS Sonoma 14.5** | macOS Sonoma [8] |
| iOS/iPadOS, neuere Geräte | **iOS 17.5 / iPadOS 17.5** | iPhone XS und neuer; iPad Pro 13 Zoll, 12.9 Zoll ab 2. Generation, 10.5 Zoll und 11 Zoll ab 1. Generation; iPad Air ab 3. Generation, iPad ab 6. Generation, iPad mini ab 5. Generation [9] |

Die Angaben sind **historische CVE-spezifische Fixstände**, keine Empfehlung, heute auf einem alten Release zu bleiben, und keine Aussage zur aktuellen Unterstützung jeder Gerätegeneration. Für Monterey/Ventura ist hier der Safari-Fix direkt belegt; es werden keine ungeprüften macOS-Buildnummern ergänzt. Die Apple-Seiten nennen als Seiten-Publikationsdatum 15.01.2025, bei Sonoma 16.05.2025; diese Metadaten werden nicht als neue Veröffentlichung im November 2026 missverstanden. [4] [5] [6] [7] [8] [9]

**KMU-Relevanz und Handlung:** Verwaltete und geschäftlich genutzte Apple-Geräte samt Safari-Version inventarisieren und den gerätespezifischen aktuellen Sicherheitsstand gegen die belegten Mindestfixes prüfen. Die Nachricht eignet sich als Anlass, alte Patchrückstände zu priorisieren, nicht als Behauptung eines neuen Apple-Zero-Days dieser Woche. Ein bekannter öffentlicher Demonstrationsangriff wäre allein kein Nachweis aktiver Ausnutzung; hier ist die neue KEV-Aufnahme der Nachweis.

## 3. WordPress: Neu in KEV – Server-Codeausführung im Core-Upgradefenster

CISA nahm **CVE-2026-119977** am 03.11.2026 auf. Laut KEV können nicht authentifizierte Angreifer während eines vollständigen Core-Upgrades über vorhersagbare, web-erreichbare Zwischenablagepfade Code auf dem Server ausführen. WordPress bestätigt im Original eine Race Condition im Upgradeprozess mit möglicher Remote Code Execution und den Fix in **7.1.4**, veröffentlicht am **28.10.2026**. Die Freigabemeldung weist als letzte Änderung den 29.10. aus. Die neue Entwicklung dieser Woche ist die KEV-Aufnahme, nicht der bereits vor dem Newsfenster veröffentlichte Patch. [1] [3] [10]

### Liniengenaue Fixmatrix

Die offizielle Dokumentation zu 7.1.4 nennt auch die ausgelieferten älteren Sicherheitsreleases. Der zusätzlich direkt geöffnete, in KEV referenzierte Wordfence-Datensatz ordnet CVE-2026-119977 diesen Linien und Versionsgrenzen zu. Sein Veröffentlichungsdatum ist 28.10.2026, sein letzter ausgewiesener Update-Tag 31.10.2026. [10] [11]

| Linie | Betroffene Releases laut CVE-Datensatz | Release mit Fix |
|---|---|---|
| 7.1 | 7.1.0–7.1.3 | **7.1.4** |
| 7.0 | 7.0.0–7.0.7 | **7.0.8** |
| 6.9 | 6.9.0–6.9.10 | **6.9.11** |
| 6.8 | 6.8.0–6.8.11 | **6.8.12** |
| 6.7 | 6.7.0–6.7.10 | **6.7.11** |
| 6.6 | 6.6.0–6.6.10 | **6.6.11** |
| 6.5 | 6.5.0–6.5.13 | **6.5.14** |
| 6.4 | 6.4.0–6.4.13 | **6.4.14** |
| 6.3 | 6.3.0–6.3.13 | **6.3.14** |
| 6.2 | 6.2.0–6.2.14 | **6.2.15** |
| 6.1 | 6.1.0–6.1.15 | **6.1.16** |
| 6.0 | 6.0.0–6.0.17 | **6.0.18** |
| 5.9 | 5.9.0–5.9.19 | **5.9.20** |
| 5.8 | 5.8.0–5.8.18 | **5.8.19** |
| 5.7 | 5.7.0–5.7.20 | **5.7.21** |
| 5.6 | 5.6.0–5.6.22 | **5.6.23** |
| 5.5 | 5.5.0–5.5.23 | **5.5.24** |
| 5.4 | 5.4.0–5.4.24 | **5.4.25** |
| 5.3 | 5.3.0–5.3.26 | **5.3.27** |
| 5.2 | 5.2.0–5.2.29 | **5.2.30** |
| 5.1 | 5.1.0–5.1.27 | **5.1.28** |
| 5.0 | 5.0.0–5.0.30 | **5.0.31** |
| 4.9 | 4.9.0–4.9.34 | **4.9.35** |
| 4.8 | 4.8.0–4.8.33 | **4.8.34** |
| 4.7 | 4.7.0–4.7.38 | **4.7.39** |

**Quellenabweichung:** Die Freigabemeldung sagt noch, die Backports seien im Gang. Die geöffnete offizielle Versionsdokumentation nennt sie dagegen bereits als veröffentlicht. Damit ist eine pauschale Aussage «alle älteren Linien noch ungepatcht» nicht gerechtfertigt. Die Auslieferung an eine konkrete Website bzw. beim Hoster bleibt ungeprüft. WordPress betont, dass nur die jeweils jüngste Version aktiv unterstützt wird; ein Backport ist keine allgemeine Supportzusage. Versionen 4.6 und älter erhalten laut Dokumentation keine Sicherheitsupdates. [3] [10]

**KMU-Relevanz und Handlung:** Eigene oder durch Dienstleister betriebene WordPress-Websites erfassen und den tatsächlichen Core-Fixstand mit dem Hoster bestätigen. Version und Linie müssen zusammen geprüft werden; die Kurzform «alles unter 7.1.4 verwundbar» würde die Backports falsch behandeln. Verdächtige Upgradezeitpunkte und Veränderungen bei Bedarf fachlich untersuchen lassen. Ein Update allein schliesst eine frühere Kompromittierung nicht aus. Die dynamische Wordfence-Anzeige über in den vergangenen 24 Stunden blockierte Angriffe wird nicht ins historische Wochenfenster übernommen. [10] [11]

## Vorwochenausschluss und Grenzen

Die Vorwochenausgabe vom 01.11.2026 sowie das Wartungsmanifest wurden gelesen, nicht verändert. PHP, GitLab und Ivanti werden **nicht nochmals als neue Meldung** ausgegeben:

- **PHP CVE-2026-109618 / CVE-2026-109619:** Das Originalarchiv bestätigt den bereits bekannten Sicherheitsfix vom 21.10. in 8.5.12, 8.4.27, 8.3.36 und 8.2.35. Im neuen Fenster steht dort PHP 8.6.0 RC5 vom 05.11., ausdrücklich nur zum Testen und nicht für Produktion; dies ist keine belegte neue Entwicklung aktiver Ausnutzung der Vorwochen-CVEs. Die Windows-Neubauten mit `-1` wegen Brotli stammen vom 26.10. und liegen vor dem Fenster. [12]
- **GitLab CVE-2026-97229:** Das geöffnete Original nennt weiterhin den Patchrelease vom 12.10. und die Fixlinien 19.2.8, 19.3.5, 19.4.2 sowie bereits gepatchtes GitLab.com und Dedicated. Ein Abschnitt mit sechs Erkennungen für Angriffsversuche ist sichtbar, aber im geprüften Text ohne belastbaren Veröffentlichungs- oder Änderungszeitpunkt im Newsfenster. Deshalb wird er nicht als neue November-Entwicklung behauptet. KEV-`dateAdded` bleibt 29.10. [1] [13]
- **Ivanti CVE-2026-104935 / CVE-2026-111357 / CVE-2026-118527:** Das Original weist als letzte Änderung 29.10.2026, 16:45:24 ohne sichtbare Zeitzone aus. Für die beiden zusätzlichen CVEs bleiben 25.1.1.3 und 22.8R2.6 die genannten Fixes; die Produkt-/Hardwarepfade sind weiterhin relevant. Keine neue datierte materielle Änderung im Fenster belegt. KEV-`dateAdded` für die beiden Vorwochenaufnahmen bleibt 30.10. [1] [14]

CISA nennt für SonicWall `dueDate` 20.11., für Apple 18.11. und für WordPress 06.11.2026. Diese Katalogdaten und die BOD-26-04-/Forensikverweise werden **nicht als Schweizer gesetzliche Fristen oder Pflichten** übernommen. Der Katalogwert `forensicTriage` ist bei WordPress `Yes`, bei SonicWall und Apple `No`; auch daraus wird keine Schweizer Rechts- oder Einzelfallpflicht abgeleitet. Bei allen drei CVEs ist `knownRansomwareCampaignUse` **Unknown**: Eine Nutzung in Ransomware-Kampagnen ist damit nicht bestätigt. Die BOD-Seiten und die NVD-Verweise wurden nicht zusätzlich geöffnet und sind keine Belege dieses Berichts. [1]

Die Prüfung ist begrenzt und gezielt: offizieller KEV-Originalabruf, eine Websuche zur Orientierung, Herstelleradvisories und die drei relevanten Vorwochenquellen. Suchsnippets sind keine Tatsachenbelege. Es wird weder behauptet, dass ausserhalb KEV keine Ausnutzung existiert, noch dass sämtliche Herstelleränderungen umfassend überprüft wurden. Keine CMS- oder Browsernutzung, keine Veränderung des Blogpakets und keine Fach-, Rechts-, Produkt-, Patch-, Publikations- oder Tenant-Freigabe.

## Vormerkungen für die Pflege am 15.11.2026

Den offiziellen KEV-JSON erneut direkt öffnen und neue `dateAdded`-Werte sowie Änderungen der drei hier aufgenommenen CVEs abgleichen. SonicWall-Advisoryrevisionen und die SAML-/Gerätegenerationsabgrenzung erneut prüfen. Bei WordPress den aktuellen offiziellen Backportstand und die Differenz zwischen Freigabemeldung und Versionsdokumentation beachten; keine tatsächliche Hoster-Auslieferung unterstellen. Apples neue KEV-Aufnahme nicht als neuen Patch oder aktuellen Support aller Altgeräte darstellen.

PHP, GitLab und Ivanti nur wieder aufnehmen, wenn eine **neue datierte materielle Änderung** belegt ist. Bei GitLab insbesondere die Änderungsdatierung des Erkennungsabschnitts klären, falls er redaktionell relevant wird. Nicht nur aufgrund eines anderen Sekundärartikel-Datums wiederholen.

Für das unveränderte Blogpaket sind bei einer später separat autorisierten Pflege vor allem Artikel 01, 04 und 07 zu Ransomware/Backup/Restore, Artikel 08 zum Risikoregister und Artikel 11 zu IT-Dienstleistern auf passende, sachlich begrenzte Querbezüge zu prüfen. Eine KEV-Aufnahme begründet weder eine neue Schweizer Meldepflicht noch einen eigenen Vorfall; alle bisherigen Fachmarker bleiben offen. Es werden hier lediglich Vormerkungen festgehalten, keine Pflegeänderungen oder Automationen angelegt.

## References

[1]: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json "CISA – offizieller KEV-JSON, Rückgabe 08.11.2026 09:04:14 CET"
[2]: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014 "SonicWall – SNWLID-2026-0014, Rückgabe 08.11.2026 09:04:22 CET"
[3]: https://wordpress.org/news/2026/10/wordpress-7-1-4 "WordPress – Freigabe 7.1.4, Rückgabe 08.11.2026 09:04:22 CET"
[4]: https://support.apple.com/en-us/120896 "Apple – Safari 17.5, Rückgabe 08.11.2026 09:04:22 CET"
[5]: https://support.apple.com/en-us/120898 "Apple – iOS und iPadOS 16.7.8, Rückgabe 08.11.2026 09:04:55 CET"
[6]: https://support.apple.com/en-us/120901 "Apple – tvOS 17.5, Rückgabe 08.11.2026 09:04:55 CET"
[7]: https://support.apple.com/en-us/120902 "Apple – watchOS 10.5, Rückgabe 08.11.2026 09:04:55 CET"
[8]: https://support.apple.com/en-us/120903 "Apple – macOS Sonoma 14.5, Rückgabe 08.11.2026 09:04:55 CET"
[9]: https://support.apple.com/en-us/120905 "Apple – iOS und iPadOS 17.5, Rückgabe 08.11.2026 09:04:57 CET"
[10]: https://wordpress.org/documentation/wordpress-version/version-7-1-4/ "WordPress – offizielle Versionsdokumentation und Backports, Rückgabe 08.11.2026 09:05:11 CET"
[11]: https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-core/wordpress-core-470-713-unauthenticated-upgrade-window-staged-installer-remote-code-execution "Wordfence – Originaldatensatz CVE-2026-119977, Rückgabe 08.11.2026 09:05:11 CET"
[12]: https://www.php.net/archive/2026.php "PHP – Originalarchiv 2026, Rückgabe 08.11.2026 09:04:57 CET"
[13]: https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/ "GitLab – Originalrelease 19.4.2, 19.3.5, 19.2.8, Rückgabe 08.11.2026 09:04:57 CET"
[14]: https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-CVE-2026-104935?language=en_US "Ivanti – Connect Secure Originaladvisory, Rückgabe 08.11.2026 09:04:55 CET"
