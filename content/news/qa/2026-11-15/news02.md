# Microsoft- und Identitätsnews – 15. November 2026, ISO-KW 46

**Drei neue Meldungen sind im begrenzten Lauf belegt:** der Outlook-Sicherheitsfix vom 10.11. mit bestätigter Ausnutzung, Microsofts SCKit-Bericht vom 13.11. zu Fernwartungs- und Technikersitzungen sowie nicht sicherheitsbezogene Windows-Server-Sonderupdates vom 13.11. Eine zusätzliche neue Entra-Veröffentlichung ist in den gezielt geprüften Quellen nicht belegt. Dies ist kein vollständiger Nichtfund.

**Autor:** Manus AI. **Newsfenster:** 08.11.2026 09:00 bis 15.11.2026 09:00 CET, Europe/Zurich. **Status:** Redaktioneller Entwurf, keine Freigabe. Die tatsächlichen Suchantworten und Originalabrufe erfolgten am 15.11.2026 zwischen 09:05:53 und 09:07:04 CET; relevante Teile gespeicherter Originalextraktionen wurden bis 09:07:22 CET gelesen. Diese Zeiten sind Rückgabe-/Lesezeiten des heutigen Laufs, keine erfundenen historischen Abrufzeiten. Ohne versionierte Historie ist der exakte Seitenwortlaut um 09:00 nicht rückwirkend belegt.

## 1. 10. November: Ausgenutzte Outlook-Lücke erhält Sicherheitsupdate

**Datum und Fakt:** MSRC datiert CVE-2026-124194 und Revision 1.0 auf den 10.11.2026. Microsoft markiert die Outlook-Spoofing-Lücke bereits in der Bewertung bei Erstveröffentlichung als «Exploited: Yes / Exploitation Detected». Ein Angreifer muss eine präparierte Datei zustellen und zum Öffnen in einer betroffenen Outlook-Version verleiten. Dadurch kann eine Verbindung zu einem angreiferkontrollierten Netzwerkziel ohne die übliche Warnung entstehen und ein NTLMv2-Hash offengelegt werden. Die Vorschau ist ausdrücklich kein Angriffsvektor. Die Einstufung «Moderate», CVSS 6.5, bedeutet hier nicht, dass keine reale Ausnutzung vorliegt.[1]

**Fixumfang:** Die geöffnete MSRC-Matrix führt sechs Produktzeilen für Microsoft 365 Apps for Enterprise, Office LTSC 2024 und Office LTSC 2021, jeweils 32-/64-bit, auf. Die ebenfalls geöffnete Office-Sicherheitsseite ordnet CVE-2026-124194 den Updates vom 10.11. zu. Für Current Channel nennt sie Version 2610, Build 20527.20196. Für Monthly Enterprise Channel sind 2610 / 20527.20194, 2609 / 20430.20264 und 2608 / 20326.20320 aufgeführt. Für den dort als «Semi-Annual Enterprise Channel, receives Monthly Enterprise Channel builds» bezeichneten Kanal nennt sie 2610 / 20527.20192, 2609 / 20430.20262 und 2608 / 20326.20318. Office LTSC 2024 Volume Licensed: 2408 / 17932.21140; Office LTSC 2021 Volume Licensed: 2108 / 14334.21048. Die LTSC-Builds stimmen mit den MSRC-Zeilen überein.[1] [2]

**KB/CVE/Katalogabgrenzung:** Für diese CVE verweist MSRC auf Office-Release-Notes und Buildstände, nicht auf eine einzelne numerische Outlook-KB. Eine solche wird nicht erfunden. CISA nahm dieselbe CVE am 10.11.2026 in KEV auf; diese Katalogaufnahme und Microsofts neue Patchveröffentlichung sind zwei unterschiedliche Ereignisse. Die CISA-Frist 24.11. ist keine hier festgestellte Schweizer KMU-Pflicht. «Known To Be Used in Ransomware Campaigns» steht auf «Unknown».[3]

**KMU-Relevanz und Prüfpunkt:** Mit dem zuständigen IT-Dienstleister installierte Office-Linie, Kanal und tatsächlich verteilten Build gegen die passende Herstellerzeile abgleichen. Bei verdächtigen Dateien oder Authentifizierungsvorgängen reicht ein Versionsabgleich nicht zur Entwarnung. Der Patchnachweis ist weder eine historische Nutzungsanalyse noch ein Nachweis, dass offengelegte Identitätsdaten nicht missbraucht wurden.

**Unsicherheit:** Es ist keine Schweizer Organisation als betroffen geprüft. Die sechs MSRC-Zeilen begründen keine pauschale Aussage zu jedem Outlook-Produkt, jeder Altversion oder jedem Updatekanal. Die Monatsübersicht nennt beim heutigen Abruf 1094 Microsoft-CVEs, zeigt aber im Fuss «Released: Nov 15, 2026». Deshalb wird diese Gesamtzahl nicht als gesicherte Patch-Tuesday-Zahl vom 10.11. verwendet; das konkrete Datum dieser Meldung ist durch CVE-Revision und Office-Release-Notes belegt.[1] [2] [4]

**Vormerkung:** Artikelverbund 02 und 06: Dateiöffnungsrisiko, kanalgenaue Patchkontrolle und getrennte Identitäts-/Vorfallbeurteilung fachlich einordnen. Keine automatische Änderung der Artikel.

## 2. 13. November: SCKit zielt auf Fernwartungszugänge und Technikersitzungen

**Datum und Fakt:** Microsoft publizierte am 13.11.2026 eine Analyse der seit dem 11.11. von ConnectWise gemeldeten aktiven Kampagne. Microsoft bestätigt beobachteten Missbrauch von ScreenConnect zur Installation zusätzlicher, nicht autorisierter Fernzugangsclients und zur SCKit-Verteilung. Der analysierte Code zielt auf authentifizierte ScreenConnect-Websitzungen von Technikern; die erreichbaren weiteren Geräte hängen von deren Konsolenberechtigungen ab. RelayTrap ist zudem für die Übertragung vom Kundenendpunkt auf einen verbindenden Technikerclient ausgelegt.[5]

**Fixumfang und Aktualität:** Neu sind Kampagnenmeldung, Analyse und Herstellerhinweise, nicht der Clientpatch. Der beim Hersteller geöffnete Fix für CVE-2026-84869 stammt vom **08.09.2026**, Mindeststand ScreenConnect **26.6.5**. Er adressiert unautorisierte Dateiübertragung/-ausführung im Client während aktiver Sitzungen; laut Bulletin sind die Server von dieser CVE nicht betroffen. ConnectWise erklärt im aktuellen Advisory, dass 26.6.5 und spätere Clients den versuchten Endpunkt-zu-Techniker-Verbreitungsweg blockieren. Ein aktualisierter Cloudserver bestätigt nicht automatisch aktualisierte Technikerclients.[6] [7]

Der Herstellerhinweis mit sichtbarem Stand **13.11.2026, 21:15 UTC** nennt zusätzlich vorbeugend zu deaktivierende Drittanbietererweiterungen. Die ursprüngliche RMM+-Familie umfasst Labtech Plus, RMM Plus, RMM+, RMM Plus Password Link und RMM+ Password Link. Der aktuelle Stand ergänzt ITBoost Integration, RepairShopr Integration und Guest Session Starter. Das Clientupdate, die Erweiterungsrisiken und eine bereits bestehende Kompromittierung sind getrennte Sachverhalte.[7]

**KMU-Relevanz und Prüfpunkt:** Schweizer KMU mit MSP-Fernwartung sollten die verwendeten ScreenConnect-Instanzen, Erweiterungen und Clientstände durch den zuständigen Dienstleister bestätigen lassen. Bei Verdacht müssen Technikergeräte, Kundengeräte, zusätzliche Fernzugangsclients und exponierte ScreenConnect-/Identitätsanbieter-Sitzungen getrennt beurteilt werden. Passwortwechsel oder das Entfernen eines Clients allein belegen keine vollständige Bereinigung. Hier wird keine solche Untersuchung vorgenommen.[5] [7]

**Unsicherheit:** Der initiale Einstieg und der Gesamtscope bleiben beim Hersteller in Untersuchung. Das Advisory vom 12.11. beschreibt eine gemeldete Authentifizierungsschwäche in RMM+ 1.0.31/1.0.32 bei nicht konfiguriertem Zugangsschlüssel. Das ist keine festgestellte neue ScreenConnect-Core-Lücke. Eine neue CVE-Zuordnung für die Drittanbietererweiterung ist kein Nachweis einer neuen Patchveröffentlichung; ein neuer Erweiterungs-Fixstand wird hier nicht behauptet. Die ungefähr 400 erwähnten Partnerumgebungen bezeichneten Installationen mit Erweiterungen, nicht 400 bestätigte Kompromittierungen. Die damalige Drittanbieterbeobachtung meldete keine erfolgreich beobachtete Endpunkt-zu-Techniker-Ausbreitung; analysierte Verbreitungsfähigkeit und bestätigte Infektionskette werden deshalb nicht gleichgesetzt.[5] [7]

**Vormerkung:** Artikelverbund 02, 06 und 11: privilegierte Fernwartungssitzungen, Lieferantenreichweite, getrennte Clientkontrolle und sichere Eskalation aufnehmen lassen. Keine Forensik- oder Produktfreigabe.

## 3. 13. November: Sonderupdates korrigieren Aktivierungsfehler nach November-Patches

**Datum und Fakt:** Microsoft veröffentlichte am 13.11.2026 kumulative, ausdrücklich **nicht sicherheitsbezogene Out-of-band-Updates** für Windows Server 2022 und 2025. Sie beheben Fehler **0x80041008**, «Invalid parameter», bei bestimmten Aktivierungs- und Lizenzoperationen mit slmgr.vbs, etwa KMS-Konfiguration oder Produktkey-Verwaltung. Bereits aktivierte Geräte bleiben laut Hersteller aktiviert; bestehende KMS-Konfigurationen ohne weitere betroffene Befehle sind nicht in gleichem Umfang betroffen.[8] [9]

**Fixumfang und KB-Abgrenzung:** Windows Server 2022: **KB5136487, OS Build 20348.5873**, enthält die vorherigen Fixes von **KB5131090 vom 10.11., OS Build 20348.5870**. Windows Server 2025, alle Editionen: **KB5136489, OS Build 26100.33828**, enthält die vorherigen Fixes von **KB5131080 vom 10.11.** Der geöffnete KB5131090-Stand dokumentiert das Aktivierungsproblem und nennt die Updates ab 13.11. als Lösung. Das ist eine neue Qualitätskorrektur, keine neue CVE, keine KEV-Aufnahme und kein Beleg für aktive Ausnutzung des Aktivierungsfehlers.[8] [9] [10]

**KMU-Relevanz und Prüfpunkt:** Für KMU mit eigenen Windows-Servern oder verwalteten Servern sind automatisierte Aktivierung, KMS und das Bereitstellen neuer Geräte der konkrete Bezug. Version, installierte November-KB, protokollierter Fehler und passende Sonder-KB mit dem Dienstleister abgleichen. Die Serverstände dürfen nicht auf Windows-Clients, andere Serverlinien oder Hotpatch-Varianten übertragen werden.

**Unsicherheit:** Der Lauf prüft nur diese beiden Serverlinien. Die geöffneten Sonder-KBs führen weiterhin eine Einschränkung bei WSUS-Synchronisierungsfehlerdetails aus älteren Updates auf; dies ist keine neue Meldung dieser Woche und kein Nachweis, dass die hier genannten Sonderupdates sämtliche bekannten Probleme lösen.[8] [9]

**Vormerkung:** Artikelverbund 06 und 08: Patchkontrolle um release- und buildgenaue Prüfung bekannter Probleme ergänzen lassen. Keine Installations- oder Betriebsfreigabe.

## Begrenzter Entra-Nichtfund und bestehende Vormerkungen

Die gezielt geöffnete Microsoft-Learn-Übersicht zeigt als obersten Monatsabschnitt Juni 2026; ihr Hinweis nennt monatliche Aktualisierung. Damit lässt sich keine neue Entra-Veröffentlichung im Wochenfenster belegen. Ein eingeschränkter oder veralteter Auslieferungsstand ist möglich. Zwei gezielte Suchläufe wurden zur Datums-/Identitätslücke verwendet; nach dem belegten Altstand erfolgte keine Wiederholungsschleife zur künstlichen Erzeugung einer neuen Meldung.[11]

Der Microsoft-Entra-Blogbeitrag zu SSPR stammt vom **08.06.2026**, sichtbare Revision **04.08.2026, Version 4.0**. Er kündigt an, dass ab **09.11.2026** nur ausdrücklich registrierte Authentifizierungsmethoden für SSPR akzeptiert werden; reine Verzeichnis-Telefonnummern oder -E-Mail-Adressen genügen nicht. Der Termin liegt im Wochenfenster, die Veröffentlichung nicht. Deshalb ist er eine **bestehende Termin-Vormerkung, keine neue Wochenmeldung** und kein Beleg einer hier getesteten Tenantdurchsetzung. Die Kurzliste enthält «Oct 65» als offensichtlichen Datumsfehler, während der ausführliche Abschnitt «Oct 5» nennt; der Registrierungsbeginn wird daher nicht als neu verifizierte News übernommen.[12]

Die App-Secrets- und Q3-E-Mail-Berichte vom 05.11. sowie der vorgegebene Entra-Cloudfix vom 05.11. gehören zur Vorwoche und wurden nicht als neue Meldungen verwendet. Historische Secret-Nutzung, App-Berechtigungen und Sicherheitsausnahmen bleiben Vormerkungen aus den Eingabedateien. CYOT-GA vom 30.10. und der NIST-Agentenidentitätsvorschlag vom 27.10. sind ebenfalls keine neuen Wochenmeldungen. Diese älteren Details wurden in diesem Newsfeld nicht erneut fachlich geprüft.

## Quellenstatus und tatsächliche Abrufe

Alle folgenden Zeiten beziehen sich auf den **15.11.2026, CET**. Die Original-URLs stehen vollständig in den Referenzen. Suchsnippets wurden ausschliesslich zur Quellenauswahl verwendet, nicht als tragende Belege. Es handelt sich um eine begrenzte Auswahl, nicht um eine Vollerhebung aller Microsoft-CVEs oder Identitätsveröffentlichungen.

- **[1], 09:06:20:** MSRC-Einzel-CVE, veröffentlicht/revidiert 10.11.2026. Belegt Ausnutzung bei Erstveröffentlichung, Mechanismus, sechs Produktzeilen und LTSC-Builds. Grenze: keine organisationsbezogene Betroffenheit und keine pauschale Outlook-Gesamtmatrix.
- **[2], 09:06:34:** Office-Sicherheitsupdates, Abschnitt und «Last updated» 10.11.2026; Outlook-Zuordnung in gespeicherter Extraktion um 09:07:05 gelesen. Belegt Herstellerbuilds und CVE-Zuordnung. Grenze: ein Releaseblock ersetzt keine individuelle Kanal-/Produktprüfung.
- **[3], 09:06:32:** CISA-KEV, Outlook-Eintrag hinzugefügt 10.11.2026. Belegt Katalogaufnahme, nicht Herstellerpatch; Ransomware-Nutzung unbekannt. Keine Schweizer Einzelfall-Rechtseinordnung.
- **[4], 09:05:58:** MSRC-November-Release-Notes, sichtbares Fussdatum 15.11.2026. Belegt heutigen Monatsstand und hervorgehobene Outlook-CVE. Grenze: unklarer historischer Monatsstand zum 10.11.; keine gesicherte damalige Gesamtzahl.
- **[5], 09:06:20:** Microsoft Security Blog, Beitrag 13.11.2026. Relevante Analyse und Mitigationen lesbar; Gesamtextraktion länger als Inline-Ausgabe. Grenze: Toolkitdesign nicht mit bestätigter vollständiger Verbreitungskette gleichsetzen.
- **[6], 09:06:31:** ConnectWise-Bulletin, Datum 08.09.2026. Belegt Clientfix 26.6.5 und betroffene ältere Clients. Grenze: alter Patch, kein neuer Novemberfix und keine Bereinigungsgarantie.
- **[7], 09:06:52:** ConnectWise-Advisories, jüngster Kopfstand 13.11.2026, 21:15 UTC; Kopf und jüngste Ergänzungen in gespeicherter Originalextraktion um 09:07:05 gelesen. Belegt erweiterte vorbeugende Hinweise und getrennte Client-/Erweiterungsrisiken. Grenze: Einstieg und Gesamtscope offen; installierte Erweiterung nicht gleich Kompromittierung.
- **[8] und [9], je 09:07:04:** Microsoft-Sonder-KBs, beide Release 13.11.2026. Belegen nicht sicherheitsbezogene Qualitätsfixes und genaue Builds. Grenze: nur Server 2022 und 2025 geprüft.
- **[10], 09:06:51:** Microsoft KB5131090, Release 10.11.2026, beim Abruf um Hinweise zum Fix ab 13.11. ergänzt; relevante Abschnitte lokal um 09:07:22 gelesen. Grenze: aktuelle Auflösung des bekannten Problems, kein unveränderter historischer KB-Wortlaut am 10.11.
- **[11], 09:05:58:** Microsoft Learn, oberster Abschnitt Juni 2026. Belegt nur den ausgelieferten Altstand. Grenze: kein vollständiger Nachweis fehlender November-Entra-Neuigkeiten.
- **[12], 09:06:32:** Microsoft Entra Blog, Erstpublikation 08.06.2026 und sichtbare Revision 04.08.2026. Belegt alten SSPR-Stichtag. Grenze: Terminankündigung, kein neuer Beitrag oder Tenanttest; widersprüchlicher Oktober-Kurztext.
- **[13], 09:05:58:** Microsoft-Security-Blogindex mit Beiträgen bis 13.11.2026. Belegt Auswahlhinweise und Datumsnavigation, nicht allein die Einzelbehauptungen.

## Unveränderte Grenzen

Nur dieser Einzelbericht wurde geschrieben. Artikeldateien, Wartungsbasis und globale Manifeste bleiben unangetastet. Es erfolgten keine CMS-/Browseroperationen, keine Nutzung von Zugangsdaten und keine Fach-, Rechts-, Forensik-, Tenant- oder Produktfreigabe. Erreichbarkeit, Inhalt und allgemeine Orientierung sind keine tatsächliche Einzelfallprüfung. Weder vollständige Patchabdeckung noch konkrete Betroffenheit oder Nichtbetroffenheit eines Schweizer KMU sind festgestellt.

## References

[1]: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-124194 "Microsoft MSRC: CVE-2026-124194, Outlook Spoofing Vulnerability"
[2]: https://learn.microsoft.com/en-us/officeupdates/microsoft365-apps-security-updates "Microsoft Learn: Release notes for Microsoft Office security updates"
[3]: https://www.cisa.gov/known-exploited-vulnerabilities-catalog "CISA: Known Exploited Vulnerabilities Catalog, Outlook-Eintrag"
[4]: https://msrc.microsoft.com/update-guide/releaseNote/2026-Nov "Microsoft MSRC: November 2026 Security Updates"
[5]: https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/ "Microsoft: SCKit abuses ScreenConnect to deploy remote access and target technician sessions"
[6]: https://www.connectwise.com/company/trust/security-bulletins/2026-09-08-screenconnect-bulletin "ConnectWise: ScreenConnect 26.6.5 Security Patch vom 8. September 2026"
[7]: https://www.connectwise.com/company/trust/advisories "ConnectWise: Latest Advisories, ScreenConnect Security Investigation Update"
[8]: https://support.microsoft.com/en-us/servicing/os/windows-server/2026/11/kb5136487-windows-server-2022-update "Microsoft: KB5136487, Windows Server 2022 OOB vom 13. November 2026"
[9]: https://support.microsoft.com/en-us/servicing/os/windows-server/2026/11/kb5136489-windows-server-2025-update "Microsoft: KB5136489, Windows Server 2025 OOB vom 13. November 2026"
[10]: https://support.microsoft.com/help/5131090 "Microsoft: KB5131090, Windows Server 2022 vom 10. November 2026"
[11]: https://learn.microsoft.com/en-us/entra/fundamentals/whats-new "Microsoft Learn: Microsoft Entra releases and announcements"
[12]: https://techcommunity.microsoft.com/blog/microsoft-entra-blog/microsoft-entra-id-security-updates-what-organizations-need-to-do-now/4522024 "Microsoft Entra: Security updates, bestehende SSPR-Ankündigung"
[13]: https://www.microsoft.com/en-us/security/blog/ "Microsoft Security Blog: Originalindex"
