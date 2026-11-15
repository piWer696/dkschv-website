# DKSchV CMS-Zugangsstatus – 15. November 2026

**Prüfung am 15.11.2026 gegen 09:05 CET, Europe/Zurich:** Der Sandbox-Browser wurde rein lesend auf `https://www.webador.de/v2/website/6004383/pages` geführt. Webador leitete auf `https://www.webador.de/anmelden?redirect=/v2/website/6004383/pages` um. Damit ist kein authentifizierter Zugang zum Projekt **DKSchV Pro** nachgewiesen.

Es wurden keine Anmeldedaten eingegeben, kein Editor geöffnet oder geändert, kein geschützter Import gestartet und kein Beitrag veröffentlicht. Die My-Browser-Einstellung ist aktiviert, wurde aber in diesem Lauf nicht als verbundene Webador-Sitzung verwendet. Die aktuelle Konfiguration enthält keinen passenden Webador-Connector. Gespeicherte Webador-Anmeldereferenzen sind in dieser Ausführungsumgebung nicht zugreifbar; dies behauptet nicht, der Benutzer habe nirgends welche gespeichert.

Der historische September-Login und die damals passwortgeschützte Testseite sind keine heutige Authentifizierungs- oder Schutzbestätigung. Auch der am 25. Oktober berichtete nicht ladende Browserübernahmeversuch belegt keinen späteren Importerfolg.

**Live-Synchronisierung: BLOCKIERT.** Normale Webador-Editoränderungen würden sofort live gehen. Ohne aktuellen Zugang und erfüllte Quellen-, Link- und Fachbedingungen werden deshalb nur lokale Entwürfe und Manifeste gepflegt. Offene Fachfragen bleiben in den zwölf Einzelberichten dokumentiert.

**Live-Änderungsprotokoll:** Keine Einträge; keine erfolgreiche Live-Änderung, kein neuer öffentlicher Beitrag und kein bestätigter geschützter Import.

## Öffentlicher Stand vom 15.11.2026

Der [HTTP-Linkchecker](public-link-check.csv) prüfte gegen 09:06 CET 28 Paket-/Serviceziele: **13 HTTP200, 15 HTTP404**. Dies unterscheidet sich vom403-Befund der Vorwoche. Ein200-Status allein ist keine Fachfreigabe, keine bewiesene Veröffentlichung durch diesen Agenten und kein Nachweis einer korrekt geschützten Kundenseite.

Der getrennte Inhaltsabruf von `https://www.dkschv.ch/wissen/backup-wiederherstellung-testen` gegen 09:06 CET lieferte ohne Anmeldung einen Artikel mit Quellenstand 1. November 2026 und Hinweisen «Mandanten-Bereich», «Kunden-Login erforderlich» und «Fachprüfung erforderlich». Gleichzeitig waren zahlreiche detaillierte Abschnitte und Quellen des Fachleitfadens in der Antwort auslesbar. Ein serverseitig wirksamer Zugriffsschutz für diesen Inhalt ist daher **nicht nachgewiesen**. Die blosse Login-Darstellung schützt den bereits ausgelieferten Text nicht vor direktem Abruf. Keine Zugangsdaten eingegeben und keine Sperre umgangen.

Die öffentliche Kontaktseite verwendet nun `.html`-Links und eine neue Gestaltung. Das aktuelle Hosting-/CMS-Ziel und die Zuordnung dieser öffentlichen Artikel zum bekannten Webador-Projekt sind damit nicht verifiziert. Ohne authentifizierten, passenden Editor sowie tatsächliche Fachfreigaben werden diese Seiten nicht automatisch überschrieben. Der Agent hat in diesem Lauf keinen der öffentlich gefundenen Artikel veröffentlicht oder live verändert.

## Tatsächlich verlinkte Ressourcen und Serviceziele

Die [rein lesende Zielzuordnung](public-target-map.csv) vom 15.11. gegen 09:08 CET fand alle zwölf Arbeitsmittel unter `https://www.dkschv.ch/wissen/resources/<Dateiname>.html`, jeweils HTTP200. Die drei Serviceadressen `sicherheitsanalyse.html`, `risikomanagement.html` und `notfallplanung.html` antworteten ebenfalls 200. Die 15 ursprünglichen Paket-/Servicepfade liefern weiterhin 404; dies ist eine Pfadabweichung und nicht der Nachweis, dass die entsprechenden Inhalte nirgends existieren.

Alle zwölf ursprünglichen Artikeladressen unter `/wissen/<Slug>` liefern HTTP200. Für den Wiederherstellungsartikel bestätigt ein weiterer GET ohne Credentials den Zugriff auf rund 22.200 Zeichen Text, einschliesslich Login-Hinweis, Fachprüfungswarnung, Wiederanlauf- und Forensikabschnitten sowie neun externen Quellenlinks. Der [strukturierte Befund](public-article-exposure.json) hält nur Status, unkritische Header und Inhaltsmerkmale fest; keine Zugangsdaten oder Passwortwerte wurden untersucht. Die Antwort nennt Apache und Last-Modified 10.11.2026; dies allein identifiziert weder die Deployment-Verantwortung noch ein bestimmtes CMS.

 **Zusätzliche Freigabeblocker:** Ein serverseitig wirksamer Schutz des als Mandanteninhalt bezeichneten Artikels ist nicht nachgewiesen; Fachmarker bleiben offen. Artikel 08–12 sind bereits mit HTTP 200 erreichbar, obwohl ihre vorgesehenen Veröffentlichungstermine am 15.11. noch nicht erreicht sind. Eine frühere Bereitstellung durch diesen Agenten wird nicht behauptet. Für konkrete Herkunft, Freigaben und gewünschte Zugangspolitik fehlt ein bestätigter CMS-/Hosting-Zugriff. Die lokale Pflege ist keine Zustimmung zu dieser öffentlichen Bereitstellung.
