# DKSchV – Laufstatus vom 22. November 2026, KW 47

**Keine Live-Änderung.** Die [Branchennews vom 22. November](2026-11-22_DKSchV_Branchennews.md) liegen als redaktioneller Entwurf vor. Die zwölf Artikel und zwölf Arbeitsmittel bleiben unverändert auf dem tatsächlichen Pflegestand **15. November 2026**. In dieser ungeraden ISO-Woche fand keine neue Vollpflege statt. Nächste vollständige Quellen- und Artikelpflege: **29. November 2026, KW 48**.

Autor: Manus AI. Der Nachrichtenzeitraum reicht vom 15. November, 09:00 Uhr, bis 22. November, 09:00 Uhr CET. Die dokumentierten Quellenabrufe erfolgten nach 09:00 Uhr; Befundzeiten stehen in den fünf Einzelrecherchen und sind keine historische Wortlautgarantie für den Redaktionsschluss.

## CMS und öffentlicher Zugriff

Der Sandbox-Browser leitete das bekannte Webador-Projekt um **09:04 CET** wieder auf die Anmeldeseite um. Es liegt kein authentifizierter Zugang zum passenden Editor vor. In dieser Ausführungsumgebung sind gespeicherte Anmeldereferenzen nicht zugreifbar; das bedeutet nicht, dass andernorts keine hinterlegt sind. Keine Anmeldung wurde eingereicht und keine Browserübernahme angefordert. Die vorhandene Sonntagsautomation und Verbindungseinstellungen wurden nicht verändert. Der [CMS-Zugangsbericht](qa/2026-11-22/cms-zugangsstatus.md) dokumentiert den Befund.

Der rein lesende [Pfadtest](qa/2026-11-22/public-link-check.csv) ergab **13 HTTP 200 und 12 HTTP 404**: alle zwölf Artikel-Slugs und die Kontaktadresse erreichbar, alle zwölf ursprünglichen Ressourcen-Slugs unter `/resources/` nicht gefunden. Die [separate Live-Zielzuordnung](qa/2026-11-22/public-target-map.csv) bestätigt dagegen alle zwölf tatsächlich verlinkten Arbeitsmittel unter `/wissen/resources/<Dateiname>.html` sowie drei Serviceziele im Website-Root mit **HTTP 200**. Die gegenüber der Vorwoche kleinere Pfadtestmenge folgt aus dem aktuellen lokalen Prüfumfang nach den Linkkorrekturen vom 15. November; sie belegt keine heutige Website-Reparatur. Die Tests liefen von 09:04:03 bis 09:04:42 CET.

**Der Schutzbefund bleibt offen:** Ein normaler GET ohne Cookies oder Credentials auf den Wiederherstellungsartikel lieferte um **09:04:49 CET** rund **26.800 Zeichen** lesbaren Text. Gleichzeitig sind Kunden-Login-/Mandantenhinweise, eine Fachprüfungswarnung und Wiederherstellungs-/Forensikmerkmale vorhanden. Ein wirksamer serverseitiger Schutz dieses ausgelieferten Inhalts ist weiterhin nicht nachgewiesen. Keine Sperre wurde umgangen; keine Passwortwerte oder Geheimnisse wurden untersucht. Das [bereinigte Prüfprotokoll](qa/2026-11-22/public-article-exposure.json) enthält nur unkritische Header und Inhaltsmerkmale.

Der Last-Modified-Header des Artikels nennt nun den **15. November 2026, 09:54:05 UTC** statt des zuvor erfassten 10. November. Das ist eine beobachtete Änderung, aber kein Nachweis ihrer Urheberschaft oder einer vollständigen Synchronisierung mit den lokalen Entwürfen. Die Zuordnung der öffentlichen Website zum historischen Webador-Projekt und das tatsächlich zuständige Hosting-/CMS-Ziel bleiben unverifiziert. Der heutige Lauf hat keine dieser Seiten veröffentlicht oder geändert.

## Termine und präzise Freigabeblocker

**Artikel 01–08 sind terminlich fällig**, Artikel 08 seit dem 19. November. **Artikel 09–12 sind noch nicht fällig**: 26. November, 3. Dezember, 10. Dezember und 17. Dezember. Dennoch antworten auch diese vier öffentlichen Artikel-Slugs mit HTTP 200. Daraus folgt weder eine Freigabe noch eine Zustimmung zur frühen Bereitstellung.

Alle zwölf Artikel und zwölf Ressourcen sind lokal weiterhin **nicht freigegebene Entwürfe**. Sämtliche `[FACHPRÜFUNG ERFORDERLICH]`-Marker bleiben erhalten. Einzelfallfragen zu Recht, Datenschutz, Meldepflicht, Forensik, Backup-/Restore-Architektur, Microsoft-Tenants und NIS2/DORA wurden nicht als gelöst ausgegeben. Die bisherigen Quellen- und Fachblocker stehen im [vollständigen Pflegebericht vom 15. November](../reviews/2026-11-15/DKSchV_Pflegebericht_KW46.md) und seinen zwölf Einzelberichten; diese Dokumentation wird durch die heutigen News nicht ersetzt.

Vor einer Veröffentlichung fehlen weiterhin der authentifizierte passende Editor, bestätigte Fachfreigaben und eine vollständige aktuelle Prüfung aller verwendeten Quellen, Fakten und Live-Links. Für als Kundeninhalt vorgesehene Seiten muss zudem die gewünschte Zugangspolitik tatsächlich serverseitig funktionieren. Normale Webador-Editoränderungen gehen sofort live; der öffentliche HTTP-Status allein legitimiert deshalb keine automatische Überschreibung.

**Live-Änderungsprotokoll dieses Laufs:** keine Einträge, kein erfolgreicher Import und keine Veröffentlichung.

## Vormerkungen für die Vollpflege am 29. November

Die folgenden Punkte sind Prüfaufträge, keine bereits eingearbeiteten Änderungen. Ihre datierten Quellen und Grenzen stehen in den Einzelrecherchen zu [Schweiz](qa/2026-11-22/news01.md), [Microsoft](qa/2026-11-22/news02.md), [CISA und Herstellern](qa/2026-11-22/news03.md), [KI und Standards](qa/2026-11-22/news04.md) sowie [EU-Regulierung](qa/2026-11-22/news05.md).

**01 – Ransomware-Erstreaktion:** Bei tatsächlichem ScreenConnect-/vCenter-Einsatz unabhängige Untersuchung, Sitzungsinvalidierung und Persistenznachweise mit den vorhandenen Passagen abgleichen. Die neue EU-Cyber-Sanktionslistung nur bei konkretem Zahlungs- oder Transaktionsbezug fachlich prüfen; DDoS nicht mit Ransomware gleichsetzen. Schweizer Übernahme und Ausnahmen sind nicht geklärt. [1]

**02 – CEO-Betrug/BEC:** Angebliche Sicherheitsupdates als Phishingköder und echte Personendaten als unzuverlässigen Echtheitsnachweis mit dem Verifizierungsabschnitt abgleichen. Den BACS-Fall nicht als belegten CEO-Betrug umdeuten und die ältere Datenpanne nicht auf November datieren.

**03 – Datenpanne:** Folgebetrugsrisiken und separate Betroffeneninformation prüfen. Die zuvor blockierte Lektüre der DSG-/DSV-Änderungslisten war heute möglich; diesen Quellenblocker im nächsten vollständigen Abgleich neu bewerten. Daraus folgt keine heute belegte neue allgemeine Meldefrist oder Bekanntmachungspflicht. Fedlex-AS-Novemberindex und verlässlich gefilterte EDÖB-Medienmeldungen bleiben unvollständig gesichtet.

**04 – Backups:** Synology-Produktlinie, passende Fixmatrix und Backupabhängigkeiten prüfen; Patchstatus ist keine ransomware-resistente Architektur. Den neuen ConnectWise-Cloud-Backup-Hinweis getrennt von ScreenConnect behandeln: Dienstewiederherstellung, allfällige Tenantneuautorisierung, erfolgreiche Snapshots und Untersuchungsabschluss sind verschiedene Nachweise.

**05 – MFA/Passkeys:** Die High-Assurance-Vorschau nach Geräteprofil, Lizenzierung, Providerdatenflüssen, Android-/iOS-Recovery und Notfallwegen prüfen. Sie ersetzt keine Tenantprüfung und ändert nicht die bereits gepflegten SMS-/Voice-Hauptfristen. PIM-/GCC-Retirement-FAQ und CYOT-Datierungen nicht als neue Wochenmeldung wiederholen.

**06 – Microsoft 365:** High-Assurance-Identitätsprüfung von Anmeldung und Zugriffsentscheidung trennen. Bei tatsächlichem Azure-/Arc-Scope die neue PIM-VM-Vorschau abgegrenzt prüfen; Rollen-Deaktivierung ist kein automatischer Sitzungsabschluss. ScreenConnect-Herstellerstatus und Cloud-Backup-Wiederherstellung getrennt aktualisieren, ohne Kundenentwarnung oder forensischen Abschluss zu behaupten.

**07 – Wiederherstellung:** Korrigierte Java-Laufzeiten in Restore-Images und Containern, NAS-/vCenter-Abhängigkeiten und vertrauenswürdigen Wiederanlauf berücksichtigen. Herstellerupdates und abgeschlossene Untersuchung beweisen keine Bereinigung. Der sichere Danfoss-Build für die sechs zusätzlichen CCB-Lücken ist weiterhin nicht belegt.

**08 – Sicherheitscheck:** Java distributions-, architektur- und prozessspezifisch erfassen; vCenter-/Synology-Befunde mit Hersteller-Matrixzeilen abgleichen. Für eingesetztes LiteLLM den Fixversionswiderspruch offen führen. Künstliche KI-Benchmarks, realitätsnahe Workflowtests und unabhängige Kontrollen getrennt nachweisen. NISTs TLS-Revisionsankündigung ist noch kein neuer Entwurf oder neue Schweizer Pflicht. CRA-Produktrisiken nicht mit der betrieblichen CSRM-Prüfung gleichsetzen.

**09 – Schatten-KI:** Realitätsnähe von KI-Sicherheitstests, Datenzugriff, Werkzeugrechte und Kontrollwege ausserhalb des Entra-Tokenpfads prüfen. LiteLLM nur bei tatsächlichem Einsatz berücksichtigen. Neu gefunden wurde zudem der bereits am **11. November** publizierte KI-Reallabor-Akt EU 2026/2487 mit Inkrafttreten am **1. Dezember**: Er lag ausserhalb des heutigen Newsfensters und wurde deshalb nicht als neue Wochenmeldung aufgenommen. Den begrenzten Vorwochen-Nichtfund entsprechend nachtragen; ein Reallabor ist keine Freigabe alltäglicher Schatten-KI. [2]

**10 – Krisenkommunikation:** Technische Eindämmung von fortbestehendem Folgebetrugs- und Informationsbedarf trennen. Die ältere Datenabflussinformation und spätere Phishingmails des BACS-Berichts korrekt datieren. Der Abschluss einer Herstelleruntersuchung ist keine pauschale Entwarnung für Betroffene.

**11 – Lieferantenrisiken:** Nachweise für eingebettetes Java, verwaltetes vCenter, Synology und gegebenenfalls LiteLLM einfordern. Technikerzugänge, Cloud-Backup-Snapshots, KI-Testrealitätsnähe und TLS-Abhängigkeiten konkret prüfen. Danfoss-Fixbuild, LiteLLM-Fixmetadaten und der bisherige Kanada-Quellenblocker bleiben offen. Der SonicWall-Workaround vom 9. November ist kein neuer Wochenhinweis. CRA-Normversionen und etwaige Amtsblattreferenzen nur bei tatsächlichem Produkt-/EU-Bezug einordnen.

**12 – NIS2/DORA:** CRA-Produktkonformität, Cyber-Sanktionen und organisatorische NIS2-/DORA-Pflichten getrennt halten. Konkrete nationale Umsetzung, EU-Präsenz, Dienstleistung und Kundenverträge bleiben einzelfallabhängig. Die nicht verbindliche ENISA-Akkreditierungsreferenz und ein SRP-Plattformupgrade sind keine neuen NIS2-/DORA-Gesetzesakte. Eine Vollprüfung aller Mitgliedstaaten und Folgeakte fand heute nicht statt.

## Lokaler Abschluss

Der [abschliessende Paketvalidator](qa/2026-11-22/validator-abschluss.txt) bestätigt **0 Fehler und 0 Warnungen**. Der [Hashvergleich](qa/2026-11-22/paket-hashes-nachher.txt) bestätigt alle **24 Inhaltsdateien unverändert** gegenüber dem Laufbeginn. Originale SEO-Felder, Slugs, Termine, Quellenstände und Fachmarker wurden nicht geändert. Das CMS-Importmanifest bleibt auf dem tatsächlichen Pflegestand vom 15. November; keine vorgetäuschte neue Quellenprüfung am 22. November.

Die sechs kompakten Nachrichten umfassen Java4Shell, vCenter, KI-Testforschung, personalisiertes Phishing, Entra-Passkey-Vorschau und CRA-Normen. Synology und weitere nachrangige Hinweise sind in den Pflegevormerkungen und Einzelrecherchen erhalten. Die technische Validierung ist keine Fach-, Schutz- oder Publikationsfreigabe.

## References

[1]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202602550 "EUR-Lex: Durchführungsverordnung EU 2026/2550, Cyber-Sanktionslistung vom 16. November 2026"
[2]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R2487 "EUR-Lex: Durchführungsverordnung EU 2026/2487 zu KI-Reallaboren"
