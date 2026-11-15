# Prüfbericht – Artikel 05: Microsoft 365 MFA und Passkeys

**Prüfdatum:** 4. Oktober 2026; die tatsächlichen Quellenabrufe und Bearbeitung erfolgten nach 09:00 Uhr Europe/Zurich. **Berichts-Stichtag:** 09:00 Uhr.  
**Prüfzeitraum:** 20. September 2026 bis einschliesslich 4. Oktober 2026, 09:00 Uhr Europe/Zurich  
**Gegenstand:**

- Artikel: `blog-paket/articles/05-microsoft-365-mfa-passkeys.md`
- Zugehöriges Arbeitsmittel: `blog-paket/resources/05-passkey-rollout-checkliste.md`
- Wartungsgrundlage: `blog-paket/maintenance-manifest.md`, Eintrag zu `/wissen/microsoft-365-mfa-passkeys`

## Ergebnis in Kürze

Es liegt **eine materielle, belegte Korrektur** zur im Entwurf erwähnten Provideroption für SMS/Voice vor. Die Microsoft-Dokumentation wurde am **23. September 2026** zur Telekom-Providerdokumentation synchronisiert. Sie konkretisiert, dass die Auswahl und Konfiguration eines unterstützten Telekommunikationsanbieters im Microsoft Security Store **erst ab 30. Oktober 2026** verfügbar sein wird. Am Stichtag dieser Prüfung, dem 4. Oktober 2026, ist sie laut Microsoft ausdrücklich **noch nicht konfigurierbar**.

Der bisherige Text liess die Provideroption ohne diesen zeitlichen Vorbehalt als einrichtbar erscheinen. Das wurde im Artikel und in der Checkliste präzisiert. Die bestätigten Kerntermine und die Zielgruppen sind **unverändert**:

- automatische Passkey-Aktivierung und Registrierungshinweis für einschlägige SMS-/Voice-Benutzer seit **1. September 2026**;
- Ruhestand von Microsoft-bereitgestellter SMS-/Voice-Übermittlung ab **1. Februar 2027** für alle ausser globalen Administratoren und externen Benutzern; interne Gastbenutzer bleiben in dieser Februar-Gruppe;
- Ruhestand für globale Administratoren und externe Benutzer am **1. Juli 2027**;
- kein Opt-out von der Durchsetzung zum jeweils anwendbaren Stichtag.

Es gab im Prüfzeitraum **keine belegte Änderung** der im Manifest genannten Passkey- und Authentisierungsstärken-Dokumentationen.

## Geprüfte offizielle Primärquellen

Alle nachfolgend genannten URLs wurden über Suche zu den Microsoft-Originalseiten und anschliessenden Abruf geprüft. Ein erfolgreicher Abruf am Prüfzeitpunkt belegt nur die Abrufbarkeit zu diesem Zeitpunkt und ist keine Zusicherung künftiger URL-Erreichbarkeit.

| Quelle | Echte URL | Quellenstand / Befund am 4. Oktober 2026 | Ergebnis für den Entwurf |
|---|---|---|---|
| Microsoft Learn – *Passkeys by default and retirement of Microsoft-provided SMS and voice authentication* | https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement | Letzte Aktualisierung laut Seite: **23.09.2026**. Offizieller MicrosoftDocs-Commit vom 23.09.2026: https://github.com/MicrosoftDocs/entra-docs/commit/9f5847e4d8533127aa7d4abdb7375f36bf996467 | Termine, Gruppen, blockierende Registrierung und fehlender Durchsetzungs-Opt-out bestätigt. Neu bzw. konkretisiert: anfängliche Private-Preview-Provider Soprano und Telesign; Konfiguration ab 30.10.2026. |
| Microsoft Learn – *Frequently asked questions about SMS and voice retirement* | https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement-faq | Letzte Aktualisierung laut Seite: **23.09.2026**. Der genannte MicrosoftDocs-Commit erfasst auch diese FAQ. | Public Cloud; Azure AD B2C ausserhalb des Umfangs; External ID nicht von dieser Ankündigung betroffen; Fristen, interne Gastbenutzer und Opt-out-Aussage bestätigt. |
| Microsoft Learn – *Passkeys (FIDO2) authentication method in Microsoft Entra ID* | https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passkeys-fido2 | Metadaten der Seite: zuletzt aktualisiert **15.06.2026**. Die MicrosoftDocs-Commit-Abfrage für 20.09.–04.10.2026 lieferte keine Einträge. | Keine Änderung im Prüfzeitraum belegt. Bestehende Aussagen zu synchronisierten und gerätegebundenen Passkeys sowie fehlender Attestierung für synchronisierte Passkeys bleiben für diesen Quellenstand unverändert. |
| Microsoft Learn – *Conditional Access authentication strengths* | https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths | Letzte Aktualisierung laut Seite: **24.10.2025**. Die MicrosoftDocs-Commit-Abfrage für 20.09.–04.10.2026 lieferte keine Einträge. | Keine Änderung im Prüfzeitraum belegt. Bestehende Aussagen zu P1, den in «phishing-resistant MFA» enthaltenen Methoden und zur Auswertung nach der initialen Authentisierung bleiben für diesen Quellenstand unverändert. |
| Microsoft Learn – *Choose a telephony provider for SMS and voice authentication* | https://learn.microsoft.com/en-us/entra/identity/authentication/concept-phone-providers | Letzte Aktualisierung laut Seite: **23.09.2026**. Ergänzende offizielle Detailquelle für den in der Hauptquelle neu konkretisierten Providerpfad. | Konfiguration am 04.10.2026 noch nicht verfügbar; Verfügbarkeit ab 30.10.2026. Soprano und Telesign in privater Vorschau; weitere Provider erst bis General Availability angekündigt. |
| Microsoft Learn – *Frequently asked questions about telephony providers in Microsoft Entra ID* | https://learn.microsoft.com/en-us/entra/identity/authentication/phone-providers-faq | Letzte Aktualisierung laut Seite: **21.09.2026**. Ergänzende offizielle Detailquelle für Providerstatus und künftigen Ablauf. | Bestätigt Verfügbarkeit ab 30.10.2026, Private-Preview-Status sowie, dass pro Kanal ein Provider vorgesehen ist. Konkrete Konfigurationsanleitung erst bei Veröffentlichung angekündigt. |

## Änderungsanalyse

### Belegte materielle Änderung seit Quellenstand 20. September 2026

Die offizielle Änderung vom 23. September 2026 («Sync telephony provider documentation») ersetzt die zuvor generische bzw. angekündigte Beschreibung des Telekom-Pfads durch konkrete Angaben:

1. **Providerstatus:** Soprano und Telesign sind die anfänglichen Anbieter in einer privaten Vorschau.
2. **Konfigurationszeitpunkt:** Die Auswahl und Konfiguration eines Providers soll **ab 30. Oktober 2026** verfügbar werden.
3. **Folge am Stichtag:** Am 4. Oktober 2026 kann ein Tenant diese Funktion noch nicht konfigurieren. Ein Providerpfad kann daher zum Prüfzeitpunkt nur geplant und kommerziell bzw. technisch vorgeprüft, nicht jedoch produktiv eingerichtet werden.

Die Änderung ist relevant, weil der ursprüngliche Entwurf die Option als bereits einrichtbar formulierte. Sie betrifft weder die Ruhestandstermine noch die Durchsetzungslogik.

### Unveränderter, geprüfter Stand

Folgende Aussagen wurden gegen die vier Manifest-Primärquellen geprüft und im Prüfzeitraum nicht als geändert festgestellt:

- Die dynamische Passkey-Aktivierung und der Hinweis zur Registrierung seit 1. September 2026 betreffen Benutzer, die in der Authentication Methods Policy oder den Legacy-MFA-Einstellungen für SMS oder Voice aktiviert sind.
- Die Registrierungskampagne ist kein automatisch registrierter Passkey; der Hinweis kann standardmässig aufgeschoben werden.
- Interne Gastbenutzer fallen nicht in die spätere Juli-Gruppe, sondern unter den 1. Februar 2027.
- Nach dem jeweils massgeblichen Ruhestandstermin ist die Aufforderung zur Passkey-Registrierung für Benutzer, deren einzige MFA-Methode SMS oder Voice ist, blockierend; die Durchsetzung kann nicht abgewählt werden.
- Der temporäre Opt-out verschiebt die automatische Passkey-Aktivierung und Registrierungskampagne, nicht aber die spätere Durchsetzung.
- Die Public-Cloud-Einschränkung sowie die Aussage, dass Azure AD B2C nicht betroffen ist und für Microsoft Entra External ID eine separate spätere Ankündigung vorgesehen ist, bleiben bestätigt.
- Für Passkeys und Authentisierungsstärken wurde in der offiziellen MicrosoftDocs-Quellhistorie im Prüfzeitraum keine Änderung ausgewiesen.

## Durchgeführte Anpassungen

### Artikel

Datei: `blog-paket/articles/05-microsoft-365-mfa-passkeys.md`

- Metadatenfeld `stand` auf **4. Oktober 2026** gesetzt.
- Im einleitenden Standhinweis «20. September 2026» durch **«4. Oktober 2026»** ersetzt.
- Providerabschnitt präzisiert: Konfiguration unterstützter Anbieter erst ab **30. Oktober 2026**; am 4. Oktober 2026 noch nicht verfügbar; Soprano und Telesign als anfängliche Private-Preview-Anbieter genannt.
- Umstiegsplan bei der Telekom-Lösung um den erst ab 30. Oktober verfügbaren Konfigurationszeitpunkt ergänzt.
- Neue, direkt referenzierte Microsoft-Primärquelle als `[14]` ergänzt.

### Zugehöriges Arbeitsmittel

Datei: `blog-paket/resources/05-passkey-rollout-checkliste.md`

- Versionsmetadatum und sichtbare Version auf **4. Oktober 2026** gesetzt.
- Termin-/Geltungsbereichsabschnitt um den belegten Providerstatus und den Konfigurationszeitpunkt ab **30. Oktober 2026** ergänzt.
- Neue, direkt referenzierte Microsoft-Primärquelle als `[8]` ergänzt.

### Bewusst nicht geändert

- Slugs, Veröffentlichungsdatum des Artikels, Status «Entwurf – nicht freigegeben» und Status des Arbeitsmittels wurden unverändert erhalten.
- Sämtliche vorhandenen Marker **[FACHPRÜFUNG ERFORDERLICH]** wurden erhalten.
- Keine andere Artikeldatei, kein zentrales Wartungsmanifest, kein Freigabestatus und kein CMS wurden geändert.
- Artikel 01 wurde nicht bearbeitet, nicht freigegeben und nicht veröffentlicht.

## Nicht verifizierte Punkte und Grenzen

1. **Tenant-spezifische Betroffenheit:** Aus den öffentlichen Herstellerinformationen kann nicht abgeleitet werden, welche Benutzer im konkreten Tenant SMS/Voice aktiviert haben, ob Legacy-MFA aktiv ist, welche Passkey-Profile greifen oder ob interne/externe Gastrollen korrekt klassifiziert sind. Dies muss im Tenant mit dem von Microsoft genannten Auswertungsweg und durch eine berechtigte Entra-Fachperson geprüft werden.
2. **Provideroption in der Schweiz:** Für Soprano und Telesign wurden weder Schweizer Abdeckung, Preise, Vertragsbedingungen, Datenschutz-/Auftragsbearbeitungsfragen noch konkrete technische Eignung für einen bestimmten Tenant verifiziert. Microsoft weist die Auswahl, regionale Abdeckung, Vertragsbeziehung, Konfiguration und Überwachung der Organisation zu.
3. **Produktivkonfiguration:** Am Prüfzeitpunkt existiert laut Microsoft noch keine nutzbare Konfigurationsoberfläche und keine veröffentlichte detaillierte Konfigurationsanleitung für Choose Your Own Telephony Provider. Eine Behauptung, die Providerlösung sei bereits eingerichtet, getestet oder für einen Tenant verfügbar, wäre nicht belegt.
4. **Aussagen ausserhalb des Manifest-Quellenumfangs:** Die in Artikel und Arbeitsmittel zusätzlich zitierten NIST-, BACS-, CISA-, Fedlex-, TAP-, Notfallzugangs- und Conditional-Access-Planungsquellen wurden in dieser gezielten Wartungsprüfung nicht erneut vollständig inhaltlich auditiert. Sie sind keine belegte neue Änderung im hier festgestellten Zeitraum und bleiben vor Veröffentlichung fachlich zu prüfen.
5. **Fachliche und rechtliche Einordnung:** Diese Quellenprüfung ersetzt weder eine Microsoft-Entra-Fachprüfung noch eine organisations-, lizenz-, datenschutz- oder branchenspezifische Beurteilung.

## Klare Blocker vor Veröffentlichung

1. **Keine fachliche Freigabe:** Artikel und Arbeitsmittel bleiben ausdrücklich nicht freigegeben; die vorhandenen **[FACHPRÜFUNG ERFORDERLICH]**-Marker sind kein Freigabeersatz.
2. **Tenant-Prüfung erforderlich:** Vor jeder Produktivsetzung müssen Geltungsbereich, Benutzergruppen, Authentisierungsmethoden, Lizenzen, Conditional-Access-Auswirkungen, TAP-Prozess, Notfallzugänge und Wiederherstellung im konkreten Tenant geprüft und getestet werden.
3. **Providerpfad am 4. Oktober 2026 blockiert:** Wer SMS/Voice über einen unterstützten Anbieter weiterbetreiben will, kann die angekündigte Funktion laut Microsoft erst ab 30. Oktober 2026 konfigurieren. Danach sind Providervertrag, regionale und regulatorische Eignung, technische Integration, Pilot und produktiver Rollout separat zu validieren.
4. **Nicht pauschal veröffentlichen:** Der Artikel darf nicht allein wegen der aktualisierten Quellenstände publiziert werden. Die Herstellertermin- und Produktprüfung unmittelbar vor Produktivsetzung bleibt erforderlich.
5. **Artikel 01:** Die terminliche Fälligkeit seit 1. Oktober 2026 begründet keine Freigabe. Für Artikel 01 wurde keine Freigabe erteilt; es wurde nichts veröffentlicht.

## Integritätskontrolle der bearbeiteten Dateien

- Artikelstatus, Artikel-Slug und Veröffentlichungsdatum blieben erhalten.
- Die Zahl der vorhandenen **[FACHPRÜFUNG ERFORDERLICH]**-Marker blieb im Artikel bei **3** und im Arbeitsmittel bei **4**.
- Überholte Body-Standangaben «20. September 2026» wurden in den zwei bearbeiteten Dateien durch den jeweiligen Stand vom 4. Oktober 2026 ersetzt.
- Die bearbeiteten Texte verwenden Schweizer Schreibweise ohne Eszett.

**CMS-Status:** Kein CMS-Zugriff und keine Veröffentlichung durchgeführt.
