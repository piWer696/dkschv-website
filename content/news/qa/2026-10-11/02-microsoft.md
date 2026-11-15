# QA-Quellennotizen – Microsoft 365 und Entra

**Berichtsfenster:** nach 04.10.2026 09:00 bis 11.10.2026 09:00 Europe/Zurich. Die Quellen wurden in dieser Ausführung am 11.10.2026 ab 09:02 Europe/Zurich abgerufen; es wird kein Abschluss genau um 09:00 behauptet.

**Abgrenzung:** Vorwochenausgabe vom 04.10.2026 und Wartungsmanifest gelesen. Der Vorwochenstand führte bereits Entra Connect (Microsoft-Learn-Seite zuletzt 29.09.2026), Passkeys/SMS/Voice (23.09.2026) und die Providerkonfiguration ab 30.10.2026. Das Manifest ordnet diese Prüfungen den Artikeln 05 und 06 zu. Keine Artikel, Arbeitsmittel, Manifeste oder CMS geändert.

## Ergebnis

Im abgegrenzten Zeitfenster wurde **keine neue, datierte und materiell verifizierte Microsoft-Meldung** gefunden, die gegenüber dem Vorwochenstand eine neue Frist, einen neuen Geltungsbereich oder eine neue sicherheitsrelevante Produktänderung belegt. Daher `items=[]`.

## Tatsächlich geöffnete Originalquellen

1. **Passkeys by default and retirement of Microsoft-provided SMS and voice authentication – Microsoft Entra ID**  
   URL: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement  
   Geprüfter Stand: `ms.date`/aktualisiert 23.09.2026. Inhalt: Passkeys ab 01.09.2026 standardmässig für betroffene SMS-/Voice-Nutzer; Microsoft-Telefonie ab 01.02.2027 für die meisten Nutzer und ab 01.07.2027 für Global Administrators/externe Nutzer; Providerwahl ab 30.10.2026. Alles lag vor dem Beginn dieses Berichtsfensters und war bereits in der Vorwochenausgabe abgegrenzt. Keine neue Änderung im Fenster belegt.

2. **Security improvements to Microsoft Entra Connect Sync autoupgrade and Microsoft Entra Connect Health alerts**  
   URL: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/security-updates-pks  
   Geprüfter Stand: Last updated 29.09.2026. Inhalt: Empfehlung/Mindestversionen bis 30.09.2026; zwingendes Upgrade auf Connect Sync 2.6.84.0 oder höher plus app-basierte Authentisierung bis 07.04.2027. Vor dem Fenster aktualisiert und bereits in der Vorwochenausgabe enthalten; keine neue materielle Änderung im Fenster belegt.

3. **Microsoft Entra Connect Sync version history**  
   URL: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history  
   Geprüft: Version 2.6.92.0, Released for download 23.09.2026, Hotfix mit Security fixes; Version 2.6.91.0 vom 16.09.2026. Die Releases liegen vor dem Fenster. Keine im Fenster datierte neue Version oder neue Frist belegt.

4. **Microsoft Entra releases and announcements**  
   URL: https://learn.microsoft.com/en-us/entra/fundamentals/whats-new  
   Geöffnet und auf MFA/Passkeys/Sicherheits- und Produktumfang geprüft. Die extrahierten Einträge enthalten keine belastbare Datierung einer neuen Meldung zwischen 04.10. und 11.10.2026; mehrere sichtbare Inhalte sind ältere Rollouts (unter anderem Juni 2026). Deshalb keine Snippet-only- oder undatierte Meldung als News übernommen.

5. **Archive for Microsoft Entra releases and announcements**  
   URL: https://learn.microsoft.com/en-us/entra/fundamentals/whats-new-archive  
   Geprüft auf PIM-API-Abschaltung und weitere Sicherheitsänderungen. Der Fund zur Abschaltung von Iteration-2-Beta-APIs ab 28.10.2026 nennt die Frist, liefert im abgerufenen Archiv jedoch keinen belastbaren Veröffentlichungszeitpunkt im Berichtsfenster; zudem ist das Archiv als ältere Inhalte beschrieben. Nicht als neue Wochenmeldung übernommen.

6. **Baseline security mode settings – Microsoft 365**  
   URL: https://learn.microsoft.com/en-us/microsoft-365/baseline-security-mode/baseline-security-mode-settings?view=o365-worldwide  
   Geprüfter Stand: Last updated 30.09.2026. Inhalt: Publisher wird ab Oktober 2026 nicht mehr Bestandteil von Microsoft 365; Blockierung als Sicherheitsmassnahme. Aktualisierung vor dem Fenster und kein Nachweis einer neuen Änderung nach 04.10.; daher ausgeschlossen.

## Ausschlüsse und Unsicherheiten

- Keine CVE oder Hersteller-Fixmeldung erfunden oder aus Such-Snippets übernommen.
- Generische Microsoft-Learn-Seiten ohne im Fenster verifizierbares Änderungsdatum wurden nicht als neue News gezählt.
- Tenant-, Lizenz-, Versions- und Schweizer Rechtswirkung wurde nicht unterstellt. Die Quellen zeigen Herstellerumfang; die konkrete Betroffenheit eines KMU-Tenants bleibt offen.
- Der nächste Review sollte die bereits bekannte Providerkonfiguration ab 30.10.2026 sowie Connect-Sync- und SMS/Voice-Fristen erneut prüfen. Betroffene Wartungsmanifest-Artikel nur als Hinweis: Artikel 05 (MFA/Passkeys) und Artikel 06 (Microsoft 365); keine Pflegeänderung vorgenommen.
