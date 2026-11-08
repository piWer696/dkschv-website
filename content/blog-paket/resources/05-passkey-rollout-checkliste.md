---
status: "Arbeitsvorlage – nicht freigegeben"
slug: "/resources/05-passkey-rollout-checkliste"
titel: "Passkey-Rollout-Checkliste für Microsoft 365 und Entra ID"
meta_title: "Passkey-Rollout-Checkliste für Microsoft 365 | DKSchV"
meta_description: "Arbeitsvorlage für Inventar, Pilot, Conditional Access, Wiederherstellung und Kommunikation beim Entra-Passkey-Rollout."
suchintention: "Arbeitsmittel – Passkey-Rollout in Microsoft Entra ID planen"
zielgruppe: "IT-Verantwortliche und Geschäftsleitungen Schweizer KMU"
version: "Stand 1. November 2026"
quellenpruefung_umfang: "16/16 eindeutige, in Artikel und Arbeitsmittel zitierte externe Quellenreferenzen stateless im Original abgerufen; zusätzlich Fedlex-Chronologie und amtliche XML-Fassung sowie die BACS-Vormerkung vom 20. Oktober 2026 geprüft"
quellenpruefung_status: "16/16 zitierte Referenzen am 1. November 2026, 09:05–09:07 CET im Original abgeglichen. Fedlex Art. 8 über amtliche Chronologie und XML-Fassung Stand 7. Juli 2025 bestätigt; Microsoft dokumentiert CYOT seit 30. Oktober 2026 als allgemein verfügbar für Entra-ID-Workforce-Tenants in global Azure. Keine Fach-, Rechts-, Tenant-, Lizenz-, Provider-, Verfügbarkeits- oder Publikationsfreigabe."
bezug: "/wissen/microsoft-365-mfa-passkeys"
fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
---

# Passkey-Rollout-Checkliste für Microsoft 365 / Entra ID

**Arbeitsmittel zum Artikel:** [Microsoft 365 MFA und Passkeys für Schweizer KMU: Rollout zu den Microsoft-Terminen 2027](/wissen/microsoft-365-mfa-passkeys)  
**Version:** 1. November 2026  
**Status:** Arbeitsvorlage – nicht freigegeben; vor produktiver Durchsetzung **[FACHPRÜFUNG ERFORDERLICH]**

---

## Zweck

Diese Checkliste unterstützt Schweizer KMU dabei, die Ablösung von Microsoft-bereitgestellter SMS- und Sprachanruf-MFA in Microsoft Entra ID planbar vorzubereiten. Sie verbindet Inventar, Pilot, Conditional Access, Wiederherstellung und Benutzerkommunikation. Sie hilft, Auslassungen sichtbar zu machen, ersetzt aber weder die Prüfung des konkreten Entra-Tenants noch Herstellerdokumentation, Lizenzprüfung oder eine allfällig erforderliche rechtliche Fachprüfung.

Die Microsoft-Termine gelten nach Herstellerangaben für Entra ID in der Public Cloud: Seit 1. September 2026 werden Benutzer, die für SMS oder Voice aktiviert sind, für Passkeys automatisch aktiviert und können durch eine Registrierungskampagne angesprochen werden. Ab 1. Februar 2027 stellt Microsoft die bereitgestellte SMS-/Sprachübermittlung für alle Benutzer ausser globalen Administratoren und externen Benutzern ein; interne Gastbenutzer bleiben in dieser Februar-Gruppe. Für globale Administratoren und externe Benutzer gilt der 1. Juli 2027. Für einen belegten betrieblichen, regulatorischen oder technischen Bedarf an SMS oder Sprache dokumentiert Microsoft CYOT seit 30. Oktober 2026 als allgemein verfügbar für Workforce-Tenants in global Azure. Soprano, Telesign und Infobip nennt Microsoft als Anbieter. Das bestätigt weder die Berechtigung eines bestimmten Tenants noch regionale Zustellung in der Schweiz, ein verfügbares Angebot, Lizenzvoraussetzungen oder eine funktionierende Integration. **[FACHPRÜFUNG ERFORDERLICH]** Prüfen Sie Geltungsbereich, Termine, Lizenzen, Anbieterabdeckung, Azure-Voraussetzungen und Tenant-Konfiguration vor jeder produktiven Änderung erneut gegen die aktuelle Microsoft-Dokumentation. [1] [2] [8] [9] [10]

## Anwendung

Füllen Sie die Vorlage vor dem Pilot aus. Verwenden Sie je eine Ausgabe pro Tenant oder klar abgegrenztem Rollout. Kennzeichnen Sie einen Kontrollpunkt erst als abgeschlossen, wenn ein Nachweis vorhanden ist, zum Beispiel ein Protokollauszug, ein dokumentierter Test oder eine freigegebene Kommunikationsvorlage. Behandeln Sie jede Ausnahme als befristete Risikoentscheidung mit verantwortlicher Person.

| Organisation / Tenant | Verantwortliche Person | Datum der letzten Aktualisierung |
|---|---|---|
|  |  |  |

| Geplantes Durchsetzungsdatum | Fachliche Prüfung durch | Nächster Testtermin |
|---|---|---|
|  |  |  |

---

## 1. Ausgangslage und Entscheidungsrahmen

| Kontrollpunkt | Status (☐ / ☑ / n. a.) | Nachweis / Bemerkung | Eigentümer | Termin |
|---|---|---|---|---|
| Die Public-Cloud-Anwendbarkeit und die für unsere Benutzer geltende Microsoft-Frist sind geprüft. | ☐ |  |  |  |
| Benutzer mit SMS oder Sprachanruf sind mit dem Microsoft-Auswertungsweg identifiziert. | ☐ |  |  |  |
| Die betroffenen Benutzer sind nach Rollen, Gerätetypen und kritischen Anwendungen gruppiert. | ☐ |  |  |  |
| Privilegierte Rollen, IT-Provider, Finanz- und Personalrollen sowie interne und externe Gäste sind separat markiert. | ☐ |  |  |  |
| Legacy- oder Altanwendungen ohne moderne Anmeldung/MFA-Unterstützung sind erfasst. | ☐ |  |  |  |
| Für jede Ausnahme bestehen Begründung, Risiko, Eigentümer, Ablaufdatum und Entscheid. | ☐ |  |  |  |
| Für eine SMS-/Voice-Ausnahme ist dokumentiert, weshalb keine phishing-resistente Methode genügt. | ☐ |  |  |  |
| Bei geplanter CYOT-Nutzung sind Workforce-Tenant in global Azure, Anbieterangebot, regionale Abdeckung einschliesslich Schweiz, Vertrag, Kosten, Datenschutz und Azure-Subscription fachlich geprüft. | ☐ |  |  |  |
| Die Geschäftsleitung kennt die offenen Risiken und den Rolloutentscheid. | ☐ |  |  |  |

**Offene Risiken / Entscheide:**  

| Risiko oder Ausnahme | Geschäftsauswirkung | Entscheidung / Massnahme | Eigentümer | Ablauf / Review |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |

## 2. Passkey-Design und Pilot

Ein Passkey ist ein FIDO2-basierter Anmeldenachweis, bei dem der private Schlüssel beim Authenticator bleibt. Synchronisierte Passkeys können über einen Plattform-Schlüsselbund auf den berechtigten Geräten einer Person verfügbar sein; gerätegebundene Passkeys bleiben auf einem bestimmten Gerät, etwa einem FIDO2-Sicherheitsschlüssel. Die Auswahl muss zu Rolle, Gerät, Wiederherstellung und Risiko passen. [3]

| Kontrollpunkt | Status (☐ / ☑ / n. a.) | Nachweis / Bemerkung | Eigentümer | Termin |
|---|---|---|---|---|
| Für jede Benutzergruppe ist die vorgesehene Passkey-Variante festgelegt. | ☐ |  |  |  |
| Für privilegierte Rollen ist eine besondere Passkey- und Aufbewahrungsregel dokumentiert. | ☐ |  |  |  |
| Der Pilot umfasst repräsentative Benutzerprofile und tatsächlich eingesetzte Windows-, macOS-, iOS- und/oder Android-Geräte. | ☐ |  |  |  |
| Eine eigene Entra-Gruppe begrenzt Methoden- und Richtlinienumfang im Pilot. | ☐ |  |  |  |
| Pilotpersonen können Passkeys registrieren und sich an Microsoft 365 sowie an kritischen Anwendungen erneut anmelden. | ☐ |  |  |  |
| Der Einsatz von Passkeys auf gemeinsam genutzten Geräten ist ausdrücklich getestet oder ausgeschlossen. | ☐ |  |  |  |
| Pilotfeedback, Registrierungsquote, Fehlerfälle und daraus abgeleitete Anpassungen sind festgehalten. | ☐ |  |  |  |
| Die Pilotabnahme ist durch IT und verantwortliche Fachseite freigegeben. | ☐ |  |  |  |

**Pilotgruppe / Abnahmekriterien:**  

| Gruppe / Geräteprofil | Anzahl geplant | Kritische Anwendungen getestet | Ergebnis | Freigabe durch |
|---|---:|---|---|---|
|  |  | ☐ Ja ☐ Nein |  |  |
|  |  | ☐ Ja ☐ Nein |  |  |
|  |  | ☐ Ja ☐ Nein |  |  |

## 3. Conditional Access kontrolliert einführen

Conditional Access steuert den Zugriff nach Bedingungen wie Benutzergruppe und Anwendung. Die Microsoft-Authentisierungsstärke «phishing-resistant MFA» lässt nur definierte phishing-resistente Methoden zu. Regeln müssen zuerst in einer begrenzten Gruppe und im Berichtsmodus geprüft werden; eine aktiv geschaltete Fehlkonfiguration kann Zugänge blockieren. [4] [5]

| Kontrollpunkt | Status (☐ / ☑ / n. a.) | Nachweis / Bemerkung | Eigentümer | Termin |
|---|---|---|---|---|
| Jede Regel hat einen eindeutigen Namen, Zweck, Zielressourcen, einbezogene Gruppe und Ausnahmebegründung. | ☐ |  |  |  |
| Der Berichtsmodus ist aktiviert und Auswirkungen sind in Anmeldeprotokollen geprüft. | ☐ |  |  |  |
| Pilotbenutzer verfügen vor der Durchsetzung über die geforderte, registrierte Methode. | ☐ |  |  |  |
| Notfallzugangskonten sind von blockierenden oder einschränkenden Regeln ausgeschlossen. | ☐ |  |  |  |
| Kritische Geschäftsanwendungen und Administrationspfade sind mit der geplanten Regel getestet. | ☐ |  |  |  |
| Die aktive Durchsetzung erfolgt nur nach dokumentierter Pilotabnahme und Benutzerinformation. | ☐ |  |  |  |
| Nach der Aktivierung sind Anmeldeprotokolle und Supportfälle während der festgelegten Beobachtungszeit kontrolliert. | ☐ |  |  |  |

**Richtlinienübersicht:**

| Regelname | Zielgruppe / Ressource | Berichtsmodus geprüft am | Aktive Durchsetzung ab | Ausnahmegruppe | Eigentümer |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## 4. Wiederherstellung und Notfallzugang

Ein verlorenes oder defektes Gerät darf nicht zu improvisierter Identitätsprüfung führen. Microsoft beschreibt den Temporary Access Pass (TAP) als zeitlich begrenzten Code, mit dem Benutzer einen Passkey einrichten und nach Verlust einer starken Methode wieder in einen geordneten Zustand zurückkehren können. Der TAP-Wert ist nach dem Anzeigen nicht erneut abrufbar. [6]

| Kontrollpunkt | Status (☐ / ☑ / n. a.) | Nachweis / Bemerkung | Eigentümer | Termin |
|---|---|---|---|---|
| Der Identitätsprüfprozess vor einer Wiederherstellung ist schriftlich festgelegt und geübt. | ☐ |  |  |  |
| Die TAP-Richtlinie, berechtigte Gruppen, Lebensdauer und Ausgabeberechtigungen sind festgelegt. | ☐ |  |  |  |
| Sichere Übergabe und Dokumentation eines TAP sind definiert. | ☐ |  |  |  |
| Der Ablauf «Gerät verloren», «Sicherheitsschlüssel verloren» und «Gerätewechsel» ist im Pilot getestet. | ☐ |  |  |  |
| Alte oder verlorene Authentisierungsmethoden werden nach erfolgreicher Wiederherstellung bereinigt. | ☐ |  |  |  |
| Mindestens zwei cloud-only Notfallzugangskonten bestehen und verwenden eine vom normalen Adminweg unabhängige phishing-resistente Methode. | ☐ |  |  |  |
| Notfallzugänge sind sicher, getrennt und für mehrere berechtigte Personen verfügbar verwahrt. | ☐ |  |  |  |
| Jede Nutzung von Notfallzugängen löst eine Überwachung aus; die Konten sind regelmässig getestet. | ☐ |  |  |  |
| Bei geplanter CYOT-Nutzung ist der Ausfall der SMS-/Voice-Zustellung im Wiederherstellungs- und Notfallablauf behandelt. | ☐ |  |  |  |

**Wiederherstellungs-Testprotokoll:**

| Szenario | Getestet am | Ergebnis | Festgestellte Lücke | Korrektur bis | Freigabe |
|---|---|---|---|---|---|
| Verlorenes Mobilgerät |  |  |  |  |  |
| Verlorener Sicherheitsschlüssel |  |  |  |  |  |
| Admin-Aussperrung / Notfallzugang |  |  |  |  |  |

## 5. Benutzerkommunikation und Support

Kommunizieren Sie in Wellen: zuerst das «Warum» und den Zeitrahmen, danach die konkrete Handlung pro Gerätetyp und schliesslich zielgruppenspezifische Erinnerungen. Die Nachricht muss einen verlässlichen Supportweg nennen und darf Benutzer nie auffordern, Passwort, Einmalcode oder Entsperrung eines Passkeys weiterzugeben. Microsoft empfiehlt Kommunikation entlang der Phasen Awareness, Action und Reminder. [1]

| Kontrollpunkt | Status (☐ / ☑ / n. a.) | Nachweis / Bemerkung | Eigentümer | Termin |
|---|---|---|---|---|
| Zielgruppen und Reihenfolge der Kommunikationswellen sind definiert. | ☐ |  |  |  |
| Die Erstaussendung erklärt Änderung, Termin, Nutzen, Handlung und verlässlichen Supportweg. | ☐ |  |  |  |
| Es bestehen geprüfte Kurzanleitungen für die tatsächlich unterstützten Gerätetypen. | ☐ |  |  |  |
| Die Kommunikation enthält eine Phishing-Warnung und keinen unerwarteten Anmeldelink. | ☐ |  |  |  |
| Der Support kennt Wiederherstellungsprozess, Eskalationsweg und Grenzen der Identitätsprüfung. | ☐ |  |  |  |
| Erinnerungen richten sich nur an Benutzer mit fehlender Registrierung oder fehlgeschlagenem Pilot. | ☐ |  |  |  |
| Supportfälle, wiederkehrende Fragen und Kommunikationsanpassungen sind ausgewertet. | ☐ |  |  |  |

**Kommunikationsplan:**

| Welle | Zielgruppe | Kernaussage / Handlung | Versanddatum | Supportkontakt | Ergebnis / Nachfassaktion |
|---|---|---|---|---|---|
| Awareness |  |  |  |  |  |
| Action |  |  |  |  |  |
| Reminder |  |  |  |  |  |

## 6. Rollout-Freigabe und Nachsteuerung

| Freigabekriterium | Erfüllt (☐ / ☑) | Nachweis / Restpunkt | Freigabe durch | Datum |
|---|---|---|---|---|
| Pilot und Wiederherstellungsfälle sind erfolgreich getestet oder bekannte Grenzen als Risiko entschieden. | ☐ |  |  |  |
| Conditional-Access-Auswirkungen sind im Berichtsmodus geprüft und Ausnahmegruppen sind minimal. | ☐ |  |  |  |
| Notfallzugänge sind funktionsfähig, überwacht und getestet. | ☐ |  |  |  |
| Benutzerkommunikation und Supportbereitschaft sind bestätigt. | ☐ |  |  |  |
| SMS-/Voice-Restbestand und Ausnahmen sind vor der relevanten Microsoft-Frist aktiv entschieden. | ☐ |  |  |  |
| CYOT-Ausnahmen sind nur nach dokumentiertem Evaluations- und Produktionstest mit stufenweiser Verkehrsverlagerung freigegeben; bestehende SMS-/Voice-Zielgruppen wurden dabei nicht unbeabsichtigt geändert. | ☐ |  |  |  |
| Nachkontrolle von Registrierung, Anmeldung und Support ist terminiert. | ☐ |  |  |  |

**Rolloutentscheid:**  
☐ Freigabe für nächste Gruppe  
☐ Zurück in Pilot / Anpassung erforderlich  
☐ Ausnahme oder Verschiebung mit dokumentiertem Risikoentscheid  

**Entscheid, Begründung und Unterschrift / Freigabe:**  

---

## Grenzen

Diese Checkliste ist eine organisatorische Arbeitsvorlage. Sie garantiert weder eine unterbruchsfreie Anmeldung noch vollständigen Schutz vor Kontoübernahmen oder Phishing. Passkeys reduzieren bestimmte Phishing-Risiken, ersetzen aber nicht sichere Endgeräte, Berechtigungsmanagement, Protokollierung, Benutzeraufmerksamkeit und Incident Response. Herstellerfunktionen, Lizenzvoraussetzungen, unterstützte Geräte sowie Microsoft-Termine können sich ändern; prüfen Sie vor jedem produktiven Schritt die aktuelle Herstellerdokumentation.

Art. 8 DSG verlangt geeignete technische und organisatorische Massnahmen für eine dem Risiko angemessene Datensicherheit. Der Wortlaut wurde am 1. November 2026 anhand der amtlichen Fedlex-XML-Fassung und Chronologie geprüft; die jüngste dort ausgewiesene Fassung hat den Stand 7. Juli 2025. **[FACHPRÜFUNG ERFORDERLICH]** Ob die konkreten Einstellungen, Verfahren und allfälligen Branchenvorgaben Ihres Unternehmens genügen, muss fachlich und bei Bedarf rechtlich geprüft werden. Dieses Arbeitsmittel und die Quellenprüfung erteilen keine individuelle Rechtsfreigabe. [7]

## Quellen

[1]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement "Microsoft Learn – Passkeys by default and retirement of Microsoft-provided SMS and voice authentication"
[2]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement-faq "Microsoft Learn – Frequently asked questions about SMS and voice retirement"
[3]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passkeys-fido2 "Microsoft Learn – Authentication methods in Microsoft Entra ID: passkeys (FIDO2)"
[4]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths "Microsoft Learn – Conditional Access authentication strengths"
[5]: https://learn.microsoft.com/en-us/entra/identity/conditional-access/plan-conditional-access "Microsoft Learn – Plan a Conditional Access deployment"
[6]: https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-temporary-access-pass "Microsoft Learn – Configure Temporary Access Pass to register passwordless authentication methods"
[7]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz (DSG), Art. 8 Datensicherheit"
[8]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-phone-providers "Microsoft Learn – Choose a telephony provider for SMS and voice authentication"
[9]: https://learn.microsoft.com/en-us/entra/identity/authentication/phone-providers-faq "Microsoft Learn – Frequently asked questions about Choose Your Own Telephony Provider"
[10]: https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-set-up-sms-voice-api "Microsoft Learn – Set up SMS and voice with Choose Your Own Telephony Provider"
