# DKSchV – Laufstatus vom 25. Oktober 2026

## Ausgeführter Umfang

Der 25.10.2026 ist **Sonntag der ungeraden ISO-Kalenderwoche 43**. Nach der heutigen Zeitumstellung gilt Europe/Zurich **CET, UTC+01:00**. Die [Sonntagsnews](2026-10-25_DKSchV_Branchennews.md) wurden aus fünf unabhängig geprüften Themenfeldern erstellt: Schweizer Behörden, Microsoft, aktiv ausgenutzte Schwachstellen, KI-Sicherheit und EU-Regulierung. Die Quellenbefunde liegen im [QA-Ordner](qa/2026-10-25/).

Heute erfolgte **keine vollständige turnusmässige Pflege** der zwölf Artikelpaare. Der gültige letzte Quellenpflegestand bleibt **18.10.2026**, nicht 25.10. Die Wochenrecherche ist keine neue Vollprüfung aller Artikelreferenzen. Die 24 Artikel-/Arbeitsmitteldateien sind nach [Hashvergleich](qa/2026-10-25/paket-hashes-nachher.txt) unverändert; SEO-Texte, ursprüngliche Termine und Fachmarker wurden nicht umgeschrieben. Auch Wartungs- und CMS-Importmanifest wurden nicht mit einem fiktiven neuen Quellenstand überschrieben.

Der [Paketvalidator](qa/2026-10-25/validator-ergebnis.txt) meldet **12 Artikel, 12 Arbeitsmittel, 12 Artikel-Slugs, 12 Arbeitsmittel-Slugs, 0 Fehler, 0 Warnungen**. Das ist eine formale Integritätsprüfung, keine Fach-, Rechts- oder Veröffentlichungsfreigabe.

## Live-Synchronisierung: blockiert

Der bekannte DKSchV-Webador-Projektweg wurde am 25.10. gegen **09:07 CET** im aktuellen Sandbox-Browser rein lesend geöffnet. Er leitete zur **Webador-Anmeldeseite** um. Die aktuelle Sitzung ist nicht authentifiziert. Die Konfigurationssuche fand keinen Webador-Connector. My Browser ist als Einstellung aktiviert, wurde aber nicht als verbundene oder authentifizierte Webador-Sitzung verwendet. Historische Logins ersetzen den heutigen Nachweis nicht. [CMS-Prüfprotokoll](qa/2026-10-25/cms-zugangsstatus.md).

Der öffentliche [Linkcheck](qa/2026-10-25/public-link-check.csv) ergab **28 Ziele: vier bestehende Service-/Kontaktziele HTTP 200, alle zwölf Artikel- und zwölf Arbeitsmittel-Ziele HTTP 404**. Lokale Paketverweise sind formal konsistent, ihre öffentlichen Zielseiten jedoch nicht vorhanden. Es wurde weder ein Import noch eine Editoränderung ausgeführt.

**Drei gemeinsame Veröffentlichungsblocker:** Der authentifizierte CMS-Zugang fehlt. Sämtliche Artikel enthalten ungelöste Fachprüfungsmarker. Die vorgesehenen öffentlichen Verweisziele fehlen. Jeder dieser Punkte muss vor einem Go-live tatsächlich gelöst sein; ein erreichtes Datum oder ein fehlerfreier Validator hebt keinen davon auf.

### Bereits terminlich fällige, aber weiterhin nicht freigegebene Beiträge

- **Artikel 01 – Ransomware-Erstreaktion, Termin 01.10.2026:** Vier Fachmarker bleiben vorhanden. Aus der letzten dokumentierten Prüfung sind insbesondere konkrete BACS-/DSG-Meldefragen, Beweissicherung, Wiederanlauf sowie Rechts-/Versicherungsfragen offen. [Einzelbericht 01](../reviews/2026-10-18/artikel-01-quellen-und-aenderungen.md).
- **Artikel 02 – CEO-Betrug/BEC, Termin 08.10.2026:** Zwei Fachmarker bleiben vorhanden. Offene Punkte betreffen Vorfall-/Personendatenbezug, allfällige Meldungen, Tenant-/Beweissicherung sowie konkrete Rollen, Schwellenwerte und Verifikationswege bei Zahlungen. [Einzelbericht 02](../reviews/2026-10-18/artikel-02-quellen-und-aenderungen.md).
- **Artikel 03 – Datenpanne, Termin 15.10.2026:** Vier Fachmarker bleiben vorhanden. Konkrete Art.-24-DSG-Risikoeinstufung, Betroffeneninformation, BACS-/CSV-Unterstellung, Angriffstatbestand und Entdeckungszeitpunkt sind nicht freigegeben. [Einzelbericht 03](../reviews/2026-10-18/artikel-03-quellen-und-aenderungen.md).
- **Artikel 04 – Ransomware-resistente Backups, Termin 22.10.2026:** Zwei Fachmarker bleiben vorhanden. Backup-/Object-Lock-/Schlüsselarchitektur, Aufbewahrung und Löschung, Datenschutz/Verträge, Berechtigungen sowie reale Wiederherstellungs- und Forensikentscheide verlangen eine konkrete Fachprüfung. [Einzelbericht 04](../reviews/2026-10-18/artikel-04-quellen-und-aenderungen.md).

Die Markeranzahlen und Entwurfsstatus wurden heute aus den Dateien gelesen; die beschriebenen Fachfragen stammen aus den verlinkten **18.10.-Prüfberichten**, nicht aus einer neuen Einzelfallprüfung. Auch Artikel 05–12 bleiben nicht freigegeben; ihre genauen Passagen und Blocker sind im [KW42-Pflegebericht](../reviews/2026-10-18/DKSchV_Pflegebericht_KW42.md) dokumentiert.

**Live-Änderungsprotokoll:** Keine Einträge. Es wurden keine Artikel veröffentlicht und keine bereits öffentlichen Beiträge automatisch geändert. Deshalb gibt es keine neue Live-URL, keine geänderten Live-Abschnitte und keinen behaupteten Publikationszeitpunkt.

## Vormerkungen für die Quellenpflege am 1. November

Diese Punkte sind **Prüfaufträge für KW44**, keine heutigen Artikeländerungen oder Freigaben. Die bereits geöffneten Originalquellen stehen in den jeweiligen News-/Quellenbefunden; ihre Aktualität ist am nächsten Lauf erneut zu prüfen.

**Microsoft 365 und Agenten – Artikel 06 und 09:** Den Microsoft-Bericht vom 21.10. zu kompromittierten ConnectWise-Anwendungsidentitäten für einen klar abgegrenzten Abschnitt zu Enterprise Apps, Dienstprinzipalen und Lieferantenintegrationen prüfen. Bei der neuen Learn-Anleitung vom 22.10. widerrufene Anmeldeinformationen nicht mit vollständigem Ende sämtlichen Zugriffs gleichsetzen. Keine App deaktivieren, widerrufene Credentials reaktivieren oder Tenant-Freigabe simulieren. Die Agentenankündigung vom 19.10. nur mit aktueller Lizenz-/Verfügbarkeitsabgrenzung verwenden. [Microsoft-Quellenbefund](qa/2026-10-25/02-microsoft.md).

**KI-Verbrauch und Toolzugriff – Artikel 09, 08 und 11:** Die von CISA verlinkte Orientierung vom 22.10. auf angemessene Prüf-/Vorlagenpunkte zu Budgets, Monitoring, Verfügbarkeit und Ausweichabläufen auswerten. Zwei neue NVD-Agenten-CVEs haben unklare Herstellerfixnachweise; daraus keine belastbare Patch- oder aktive-Ausnutzungsbehauptung in die Artikel übernehmen. Allgemeine Tool-/Netzwerkberechtigungen nur kontextbezogen beurteilen. [KI-Quellenbefund](qa/2026-10-25/04-ki.md).

**Komponenten-/Lieferanteninventar – Artikel 08 und 11, ergänzend 01 und 07:** Die PHP-Warnung vom 21.10. und neuen KEV-/Herstellerhinweise auf Inventarisierung eingebetteter Komponenten, Betreiberbestätigungen und nachprüfbare Fixstände auswerten. Patchen beseitigt nicht automatisch Spuren oder Folgen einer vorherigen Kompromittierung; konkrete Forensik und Wiederanlauf gehören in Fachhände. [Schweizer Quellenbefund](qa/2026-10-25/01-schweiz.md) und [KEV-/Herstellerbefund](qa/2026-10-25/03-schwachstellen.md).

**Betrugsprävention – Artikel 02, gegebenenfalls 05:** Das BACS-Hotelbuchungsbeispiel vom 20.10. auf kontextbezogenes Phishing, unabhängige Zahlungsprüfung und Social Engineering eines zweiten Faktors auswerten. Keine Bank-, TWINT- oder Entra-spezifische Produktfreigabe daraus ableiten.

**Datenbearbeiter und Vorfallkommunikation – Artikel 03, 10 und 11:** Die EDÖB-Mitteilung vom 23.10. als Anlass für Rollen-/Datenklärung, erreichbare Lieferantenkontakte und faktengetrennte Kommunikation verwenden. Das hängige Verfahren ist kein abschliessender Verstossbefund und keine neue pauschale Meldefrist. [Schweizer Quellenbefund](qa/2026-10-25/01-schweiz.md).

**Bevorstehender Herstellertermin – Artikel 05:** Artikeltermin 29.10. und im letzten Quellenstand genannte Telefonieanbieter-Konfiguration ab 30.10. liegen vor dem nächsten Sonntagslauf. Das sind keine neuen Wochennews und keine Freigabe. Am 01.11. sind tatsächliche Bereitstellung, Geltungsbereich und Herstellertermine erneut gegen Microsoft zu prüfen; die heutige Recherche bestätigt keine produktive Verfügbarkeit. Der Beitrag bleibt wegen CMS-, Fach- und Linkblockern Entwurf.

Im EU-Regulierungsfeld wurde keine neue im Berichtsfenster wirksam gewordene materielle Änderung für die kompakte Ausgabe belegt. Die Kommissionsmitteilung vom 19.10. zu einem harmonisierten KI-Standard verweist auf einen bereits vor dem Fenster veröffentlichten Rechtsakt; sie wurde nicht als neue geltende Wochenpflicht ausgegeben. [EU-Quellenbefund](qa/2026-10-25/05-eu.md).

**Nächster Lauf:** Sonntag **01.11.2026, KW44**, mit News und vollständiger zweiwöchentlicher Blogpflege. Die heutigen Vormerkungen ergänzen das verbindliche Wartungsmanifest, ersetzen es aber nicht.
