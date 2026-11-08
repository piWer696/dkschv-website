---
status: "Entwurf – nicht freigegeben"
slug: "/wissen/microsoft-365-mfa-passkeys"
meta_title: "Microsoft 365: MFA und Passkeys 2026/2027 | DKSchV"
meta_description: "Microsoft Entra ID: Passkey-Rollout für Schweizer KMU mit Pilot, Conditional Access, Wiederherstellung und aktuellen Herstellerterminen."
hauptkeyword: "Microsoft 365 MFA"
suchintention: "Informational – Passkey- und MFA-Rollout in Microsoft Entra ID planen"
zielgruppe: "Geschäftsleitungen und IT-Verantwortliche Schweizer KMU"
autor: "DKSchV Redaktion"
veröffentlichungsdatum: "29.10.2026"
stand: "1. November 2026"
quellenpruefung_umfang: "16/16 eindeutige, in Artikel und Arbeitsmittel zitierte externe Quellenreferenzen stateless im Original abgerufen; zusätzlich Fedlex-Chronologie und amtliche XML-Fassung sowie die BACS-Vormerkung vom 20. Oktober 2026 geprüft"
quellenpruefung_status: "16/16 zitierte Referenzen am 1. November 2026, 09:05–09:07 CET im Original abgeglichen. Fedlex Art. 8 über amtliche Chronologie und XML-Fassung Stand 7. Juli 2025 bestätigt; Microsoft dokumentiert CYOT seit 30. Oktober 2026 als allgemein verfügbar für Entra-ID-Workforce-Tenants in global Azure. Keine Fach-, Rechts-, Tenant-, Lizenz-, Provider-, Verfügbarkeits- oder Publikationsfreigabe."
fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
---

# Microsoft 365 MFA und Passkeys für Schweizer KMU: Rollout zu den Microsoft-Terminen 2027

**Kurzantwort:** Schweizer KMU sollten jetzt erfassen, welche Entra-ID-Benutzer noch SMS oder Sprachanruf für die Mehrfaktor-Authentisierung (MFA) verwenden, und diese Gruppen kontrolliert auf phishing-resistente Verfahren umstellen. Microsoft aktiviert seit dem 1. September 2026 Passkeys für die betroffenen Benutzer und zieht seine SMS-/Sprachtelefonie für die meisten Benutzer am 1. Februar 2027 zurück. Beginnen Sie mit Administratoren und einem repräsentativen Pilot. Prüfen Sie Conditional Access zuerst im Berichtsmodus, definieren Sie Wiederherstellung und Notfallzugänge vor der Durchsetzung und kommunizieren Sie pro Benutzergruppe klar. Für eine belegte Ausnahme mit SMS oder Sprache ist «Choose Your Own Telephony Provider» (CYOT) laut aktueller Microsoft-Dokumentation seit 30. Oktober 2026 für Workforce-Tenants in global Azure allgemein verfügbar; die konkrete Tenant-, Provider- und Schweiz-Eignung bleibt aber vor einem Einsatz zu prüfen. Warten Sie nicht auf eine blockierende Registrierung beim Anmelden. [1] [15] [16]

*Stand der Produktinformationen: 1. November 2026. Dieser Beitrag bezieht sich auf Microsoft Entra ID in der Public Cloud. **[FACHPRÜFUNG ERFORDERLICH]** Vor einer Veröffentlichung und vor jedem produktiven Schritt müssen die Herstellertermine, der Geltungsbereich, die Lizenzen, die konkrete CYOT-Providerabdeckung und die Tenant-Einstellungen durch eine Microsoft-Entra-Fachperson gegen die aktuelle Herstellerdokumentation geprüft werden.*

## Die Termine: Was Microsoft ändert – und was bis Februar erledigt sein muss

**Microsoft Entra ID** ist der Identitäts- und Zugriffsservice hinter Microsoft 365. MFA verlangt beim Anmelden mindestens zwei unterschiedliche Nachweise, beispielsweise ein Passwort und einen Besitz- oder Biometrienachweis. Sie reduziert das Risiko gestohlener Passwörter, ist aber nicht automatisch gegen Phishing geschützt.

Microsoft hat am 1. September 2026 für Benutzer, die in der Authentication Methods Policy oder in den Legacy-MFA-Einstellungen für SMS oder Sprachanruf aktiviert waren, Passkeys automatisch als Methode aktiviert. Bei der nächsten MFA-Anmeldung kann die von Microsoft verwaltete Registrierungskampagne zur Passkey-Registrierung auffordern. Das ist **keine** automatische Registrierung eines Passkeys; Benutzer können die Aufforderung standardmässig aufschieben. [1] [2]

Für interne Benutzer und interne Gastbenutzer gilt ein wichtiger Stichtag: Ab **1. Februar 2027** stellt Microsoft die von Microsoft bereitgestellte Übermittlung von SMS und Sprachanrufen ein. Wer dann nur diese Methode hat, erhält beim Anmelden eine nicht überspringbare Aufforderung, einen Passkey zu registrieren, bevor der Zugriff weitergeht. Einen Verzicht auf diese Durchsetzung gibt es nicht. Globale Administratoren und externe Benutzer haben für die von Microsoft bereitgestellten Telekommunikationsdienste eine spätere Frist bis **1. Juli 2027**. Für die Betriebsstabilität ist es dennoch sinnvoll, auch diese Gruppen im Programm bis Februar 2027 einzuplanen. [1]

Die Termine gelten laut Microsoft nur für die **Public Cloud**. Azure AD B2C ist nicht betroffen; für Microsoft Entra External ID ist eine spätere separate Ankündigung vorgesehen. Für einen belegten betrieblichen, regulatorischen oder technischen Bedarf an SMS oder Sprache dokumentiert Microsoft am **1. November 2026** CYOT als seit **30. Oktober 2026** allgemein verfügbar – jedoch nur für Microsoft-Entra-ID-**Workforce-Tenants in global Azure**. Die am 30. Oktober aktualisierte Microsoft-FAQ nennt Soprano, Telesign und Infobip als wählbare Anbieter. Die ältere Übersichtsseite [14] beschreibt noch den vorherigen privaten Vorschauzustand mit Soprano und Telesign; für den aktuellen Bereitstellungsstand sind deshalb die neueren Quellen [15] und [16] massgeblich. [3] [14] [15] [16]

CYOT ist keine blosse Umschaltung des bisherigen SMS- oder Voice-Schalters: Das Unternehmen schliesst den Vertrag mit dem Anbieter über den Microsoft Security Store, stellt die Integration als Azure Function in seiner Azure-Subscription bereit und hinterlegt Endpunkt sowie Anwendungs-ID in der bestehenden SMS- oder Voice-Richtlinie. Microsoft empfiehlt zuerst den Evaluationsmodus und anschliessend eine schrittweise Produktionsumleitung. Sie dokumentiert zudem, dass der Betrieb die regionale Zustellung, Konditionen, Kosten, Sicherheit, Compliance und den Dienst überwacht. Aus der dokumentierten allgemeinen Verfügbarkeit folgt **nicht**, dass ein bestimmter Schweizer Tenant berechtigt ist, ein Angebot für die Schweiz abdeckt oder eine konkrete Konfiguration funktioniert: Das wurde für keinen Tenant, keine Subscription und keinen Anbieter geprüft. CYOT bleibt deshalb eine begründete Ausnahme mit eigener Beschaffungs-, Datenschutz-, Betriebs- und Fachprüfung, nicht der Standardpfad. Ein temporärer Opt-out kann die automatische Aktivierung und Kampagne verzögern, verschiebt aber die Durchsetzung nicht. [1] [14] [15] [16]

## Warum MFA allein nicht genügt

Bei **phishing-resistenter Authentisierung** kann eine betrügerische Website den Anmeldenachweis nicht einfach entgegennehmen und an die echte Seite weiterreichen. NIST beschreibt dies als Schutz davor, dass Geheimnisse oder gültige Authenticator-Ausgaben einem vorgetäuschten Prüfdienst offengelegt werden. Ein manuell eingegebener Einmalcode erfüllt diese Eigenschaft gerade nicht, weil er an eine andere Sitzung weitergegeben werden kann. [4]

Das ist für Microsoft 365 keine theoretische Feinheit. Das BACS beschrieb im Februar 2026 eine SharePoint-Phishing-Welle, bei der Angreifer die Abfrage des zweiten Faktors in Echtzeit an eine Phishing-Seite weiterleiteten. So kann auch eine gewöhnliche Zwei-Faktor-Anmeldung ausgehebelt werden. [5]

Ein **Passkey** verwendet FIDO2-Standards und ein Schlüsselpaar: Der private Schlüssel bleibt beim Authenticator, während der Dienst nur den öffentlichen Schlüssel prüft. Die Anmeldung ist an die echte Website gebunden und verlangt eine lokale Entsperrung, etwa per PIN oder Biometrie. Microsoft ordnet Passkeys deshalb als phishing-resistente MFA ein. [2] Auch die CISA stuft FIDO/WebAuthn als den breit verfügbaren phishing-resistenten Ansatz ein; SMS und Sprache sind dagegen unter anderem gegenüber Phishing, SS7-Angriffen und SIM-Swaps verwundbar. [6]

Die Begriffe helfen bei einer pragmatischen Auswahl:

- **Synchronisierte Passkeys** liegen verschlüsselt in einem Plattform-Schlüsselbund, beispielsweise iCloud-Schlüsselbund oder Google Password Manager, und können auf den berechtigten Geräten des Benutzers verfügbar sein. Sie sind für viele Mitarbeitende praktikabel.
- **Gerätegebundene Passkeys** bleiben auf einem einzelnen Gerät, etwa in Microsoft Authenticator oder auf einem FIDO2-Sicherheitsschlüssel. Für privilegierte Rollen oder Umgebungen mit konkreten Vorgaben können sie passend sein.
- **Windows Hello for Business** und eine multifaktorielle zertifikatsbasierte Anmeldung sind weitere Verfahren, die Microsoft in der integrierten Stärke «phishing-resistant MFA» aufführt. [2] [7]

Die Wahl darf nicht allein eine Gerätefrage sein. Prüfen Sie pro Personengruppe, welche Endgeräte, Betriebssysteme, Arbeitsorte und Unterstützungsszenarien tatsächlich vorkommen. Attestierung kann bei bestimmten Sicherheitsanforderungen relevant sein; Microsoft weist jedoch darauf hin, dass synchronisierte Passkeys keine Attestierung unterstützen. [2]

## Zuerst Inventar und Risiken, dann Technik erzwingen

Ein belastbarer Umstieg beginnt mit einem begrenzten Bild der Ausgangslage. Exportieren Sie die Benutzer mit aktiver SMS- oder Sprachmethode mit dem von Microsoft beschriebenen Auswertungsweg und ordnen Sie sie nicht nur nach Abteilung, sondern nach Rolle und Zugriff ein. Separat zu kennzeichnen sind globale Administratoren, weitere privilegierte Entra-Rollen, IT-Provider mit Adminzugriff, Finanz- und Personalrollen, gemeinsam verwendete Geräte, Schichtmitarbeitende, Gäste sowie technische Konten. [1]

Prüfen Sie gleichzeitig, welche Anwendungen moderne Anmeldung unterstützen. Alte Protokolle oder Altanwendungen, die eine moderne Anmeldung nicht beherrschen, lösen sich nicht durch die Registrierung eines Passkeys. Sie brauchen einen dokumentierten Migrations-, Ersatz- oder Restrisikopfad. Die CISA empfiehlt, Systeme ohne MFA-Unterstützung zu identifizieren und den verbleibenden Risikoentscheid an die Leitung zu eskalieren. [6]

Diese Inventur gehört in die bestehende [Sicherheitsanalyse](/unsere-dienstleistungen/sicherheitsanalyse) und ins [Risikomanagement](/unsere-dienstleistungen/risikomanagement): Nicht jeder Zugang hat denselben Schadenfall, aber ein kompromittiertes Administratorkonto kann die Durchsetzung selbst verändern. Das BACS ordnet MFA als Teil technischer **und** organisatorischer Grundschutzmassnahmen ein und betont die Führungsverantwortung für Sicherheitsrisiken. [11]

> **Hypothetisches Praxisbeispiel:** Ein KMU mit Aussendienst, Büro und externem IT-Provider stellt fest, dass nur ein Teil der Belegschaft SMS nutzt. Die IT priorisiert zuerst die privilegierten Rollen und die Personen, die auf Finanz- oder Personaldaten zugreifen. Eine kleine Pilotgruppe deckt iPhone, Android, Windows-Notebook und gemeinsam genutzten Arbeitsplatz ab. Erst nachdem Registrierung, Supportfall und Rückkehr nach Geräteverlust getestet sind, folgt der Rollout nach Benutzergruppen. Dieses Beispiel ist hypothetisch und keine Aussage über ein Kundenprojekt.

## Passkey-Pilot: klein genug zum Lernen, breit genug für die Realität

Microsoft empfiehlt, Test- und Pilotbenutzer nach unterschiedlichen Benutzerprofilen und unterstützten Gerätetypen auszuwählen, nicht nur Administratoren. Legen Sie eine eigene Entra-Gruppe an und grenzen Sie ihre Authentisierungsmethoden zunächst auf diese Gruppe ein. Messen Sie Registrierung und Nutzung mit dem Authentication Methods Activity Report und dokumentieren Sie Rückmeldungen sowie Ausnahmen. [8]

Für die Pilotabnahme sollten Sie mindestens diese Fragen verbindlich beantworten:

1. Kann jede Pilotperson den vorgesehenen Passkey auf ihrem realen Arbeitsgerät registrieren und sich an Microsoft 365 sowie den kritischen Anwendungen erneut anmelden?
2. Ist für jede Person festgelegt, ob ein synchronisierter oder ein gerätegebundener Passkey vorgesehen ist, und weshalb?
3. Funktioniert ein zweiter, kontrollierter Weg nach Verlust, Defekt oder Gerätewechsel, ohne dass der Helpdesk die Identität bloss aufgrund einer eingehenden E-Mail annimmt?
4. Können IT und Support in den Protokollen erkennen, welche Richtlinie und welche Methode bei einer fehlgeschlagenen Anmeldung wirksam waren?
5. Sind noch SMS-/Voice- oder Altanwendungs-Ausnahmen vorhanden, mit Eigentümer, Begründung, Ablaufdatum und Entscheid?

Beginnen Sie typischerweise mit privilegierten Rollen, aber nur nachdem deren Wiederherstellung und Notfallzugang getestet sind. Danach folgen Gruppen, die technisch bereit sind und von einer klaren Umstellung profitieren. Das senkt die Zahl gleichzeitiger Sonderfälle und schafft belastbare Unterlagen für die nächste Welle. [6] [8]

## Conditional Access in Stufen einführen

**Conditional Access** sind Entra-Regeln, die den Zugriff aufgrund von Benutzer, Anwendung, Gerät, Ort oder Risiko steuern. Eine **Authentisierungsstärke** schränkt darin ein, welche Methoden eine Anforderung erfüllen dürfen. Für sensible Ressourcen kann die integrierte Stärke «phishing-resistant MFA» verlangt werden. Sie umfasst laut Microsoft Windows Hello for Business bzw. Plattform-Anmeldedaten, FIDO2-Sicherheitsschlüssel und multifaktorielle zertifikatsbasierte Authentisierung. Für Conditional Access ist eine Microsoft Entra ID P1-Lizenz erforderlich. [7]

Schalten Sie diese Steuerung nicht in einem Schritt für alle ein. Erstellen Sie Regeln mit eindeutigen Namen, Gruppen, Zielressourcen, Ausnahmegrund und verantwortlicher Person. Aktivieren Sie sie zunächst im **Berichtsmodus**. Die Entra-Anmeldeprotokolle zeigen dann pro Ereignis, welche Wirkung eine Regel gehabt hätte. Erst nach Auswertung, Pilot und Benutzerinformation wird eine Regel aktiv geschaltet. Microsoft empfiehlt genau diese Reihenfolge und verlangt vor dem breiten Einsatz unter anderem registrierte Methoden, getestete Pilotgruppen sowie vorbereitete Kommunikation. [9]

Wichtig ist eine technische Grenze: Eine Authentisierungsstärke wird erst nach der ersten Authentisierung ausgewertet. Sie verhindert daher nicht zwingend, dass ein Benutzer zuerst ein Passwort eingibt; für die Fortsetzung zu einer geschützten Ressource muss er aber eine erlaubte stärkere Methode verwenden. Testen Sie deshalb konkrete Anmeldungspfade statt nur die Richtlinienansicht. [7]

Microsoft empfiehlt mindestens zwei cloud-only Notfallzugangskonten, die dauerhaft die Rolle Global Administrator haben. Ob sie in Ihrem Tenant von welchen Conditional-Access-Regeln ausgenommen werden müssen, welche Authentisierung sie verwenden und wie sie verwahrt sowie überwacht werden, ist anhand der aktuellen Herstellerdokumentation und Ihres Notfallprozesses festzulegen. Das ist kein Hintertürchen für den Alltag, sondern ein kontrollierter Wiederherstellungsmechanismus. [10]

## Wiederherstellung vor der Durchsetzung planen

Ein Passkey-Rollout ist erst dann betriebsfähig, wenn der Verlust eines Telefons, eines Sicherheitsschlüssels oder eines Zugangs zu einem synchronisierten Schlüsselbund geordnet behandelt werden kann. Halten Sie dafür einen kurzen, geübten Ablauf fest: Identität prüfen, betroffenen Authenticator sperren oder entfernen, zeitlich befristeten Zugang ausstellen, neuen Passkey registrieren lassen, alte Methode bereinigen, Vorgang protokollieren und bei Auffälligkeiten eskalieren.

Der **Temporary Access Pass (TAP)** von Entra ist dafür ein mögliches Werkzeug. Es handelt sich um einen zeitlich begrenzten Code für einmalige oder mehrfache Nutzung, mit dem Benutzer passwortlose Methoden einrichten können; Microsoft nennt ihn ausdrücklich auch für die Wiederherstellung nach Verlust oder Vergessen einer starken Methode. Nur Benutzer im TAP-Richtlinienumfang können ihn verwenden. Der Code ist nach dem Anzeigen nicht mehr abrufbar. Damit verlangt die Ausgabe einen klaren Identitätsprüfprozess, sichere Übermittlung und getrennte Rollen. [12]

Verknüpfen Sie den Ablauf mit der [IT-Notfallplanung](/unsere-dienstleistungen/notfallplanung). Dort gehören Stellvertretung, Erreichbarkeit ausserhalb der Bürozeit, sichere Aufbewahrung der Notfallzugänge und ein Testtermin hinein. Art. 8 DSG verlangt geeignete technische und organisatorische Massnahmen für eine dem Risiko angemessene Datensicherheit. Der Wortlaut wurde am 1. November 2026 mit der amtlichen Fedlex-XML-Fassung und Chronologie abgeglichen; die jüngste dort ausgewiesene Fassung hat den Stand 7. Juli 2025. **[FACHPRÜFUNG ERFORDERLICH]** Ob Ihr konkretes Verfahren, die Protokollierung und allfällige Branchenvorgaben diese Anforderung erfüllen, muss fachlich und bei Bedarf rechtlich geprüft werden; die Quellenprüfung erteilt keine individuelle Rechtsfreigabe. [13]

## Kommunikation ist eine Sicherheitskontrolle

Eine Anmeldung scheitert oft nicht an Kryptografie, sondern an einer unklaren Aufforderung im falschen Moment. Senden Sie die Information nicht an alle gleich, sondern an die aus dem Inventar bekannte Zielgruppe. Microsoft empfiehlt eine Folge aus Bewusstsein schaffen, Handlung erklären und erinnern. Teilen Sie dabei mit, was sich ändert, warum SMS und Sprachanruf abgelöst werden, bis wann die Person handeln soll, welches Verfahren sie nutzt und wo sie verlässliche Hilfe erhält. [1]

Eine gute Nachricht enthält einen echten Absender, keinen Anmeldelink aus einer unerwarteten E-Mail und eine klare Warnung: Der Support fragt nie nach Passwort, Einmalcode oder Passkey-Entsperrung. Verweisen Sie stattdessen auf eine bekannte interne Anlaufstelle und auf eine Schritt-für-Schritt-Anleitung pro Betriebssystem. Das passt zu den BACS-Empfehlungen, ungewöhnliche Nachrichten über einen alternativen Kanal zu verifizieren und Mitarbeitende fortlaufend über Phishing-Varianten zu informieren. [5]

Dokumentieren Sie für die Geschäftsleitung fortlaufend nur die entscheidungsrelevanten Werte: Benutzer im SMS-/Voice-Bestand, registrierte Passkeys, erfolgreiche Pilotanmeldungen, offene Ausnahmen, Wiederherstellungsfälle und getestete Notfallzugänge. Für Fragen zu den vereinbarten Kontaktwegen finden Sie die allgemeinen Angaben unter [Kontakt](/kontakt). Ergänzende technische Themen behandeln die Beiträge [CEO-Betrug und Business Email Compromise](/wissen/ceo-betrug-business-email-compromise) sowie [Microsoft 365 sicher konfigurieren](/wissen/microsoft-365-sicherheit-kmu).

## Typische Fehler, die Aussperrungen oder Scheinsicherheit erzeugen

Der erste Fehler ist, «MFA aktiviert» mit phishing-resistent gleichzusetzen. SMS, TOTP-Codes und Push-Freigaben können sinnvoller Übergangsschutz sein, schützen aber nicht wie ein Passkey vor Echtzeit-Phishing. Der zweite Fehler ist, die Microsoft-Aufforderung mit einer vollständigen Migration zu verwechseln. Eine aktivierte Methode und eine tatsächlich verwendete, getestete Methode sind zwei verschiedene Zustände.

Der dritte Fehler ist eine globale Conditional-Access-Regel ohne Berichtsmodus, Pilot und Ausschluss kontrollierter Notfallzugänge. Der vierte ist ein Wiederherstellungsprozess, der nur auf dem verlorenen Gerät, beim gleichen Provider oder bei einer einzelnen Person im IT-Team beruht. Der fünfte ist Kommunikation ohne Supportprozess: Dann suchen Benutzer unter Zeitdruck nach Hilfe und werden anfälliger für betrügerische Anweisungen.

## Umstiegsplan bis Februar 2027

| Zeitraum | Ergebnis | Verantwortlich |
|---|---|---|
| September–Oktober 2026 | SMS-/Voice-Bestand, Rollen, Geräteprofile, Anwendungen und Ausnahmen sind erfasst; Eigentümer und Risiko sind zugeordnet. | IT-Verantwortung mit Geschäftsleitung |
| Oktober–November 2026 | Passkey-Varianten, TAP-Ablauf, mindestens zwei Notfallzugänge und Kommunikationsmaterial sind im Pilot getestet. | Entra-Administration und Support |
| November–Dezember 2026 | Conditional-Access-Regeln laufen für Pilotgruppen im Berichtsmodus; Protokolle und Fehlerfälle sind ausgewertet. | Entra-Administration |
| Januar 2027 | Phishing-resistente Methoden sind für die priorisierten internen Benutzer aktiv durchgesetzt; offene Ausnahmen sind entschieden und dokumentiert. | Geschäftsleitung und IT-Verantwortung |
| Bis 1. Februar 2027 | Für interne Benutzer und interne Gäste im Geltungsbereich ist eine geeignete Anmeldemethode oder eine dokumentierte, geprüfte Telekom-Lösung eingerichtet. Für CYOT dokumentiert Microsoft seit 30. Oktober 2026 allgemeine Verfügbarkeit für Workforce-Tenants in global Azure; Anbieterangebot, regionale Abdeckung einschliesslich Schweiz, Azure-Voraussetzungen, Evaluations- und Produktionstest sind vor Nutzung belegt. Wiederherstellung und Notfallzugänge sind erneut getestet. [14] [15] [16] | IT-Verantwortung |

Dieser Plan ist absichtlich risikobasiert und kein Ersatz für die technische Prüfung Ihres Tenants. Bei wesentlichen Änderungen an Microsofts Zeitplan, Lizenzierung oder unterstützten Methoden muss die Umsetzung erneut gegen die aktuelle Herstellerdokumentation geprüft werden.

## Nächster Schritt

Verwenden Sie die [Passkey-Rollout-Checkliste](/resources/05-passkey-rollout-checkliste), um Pilot, Ausnahmen, Wiederherstellung und Freigaben nachvollziehbar zu dokumentieren. Für eine Anfrage zur [DKSchV-Sicherheitsanalyse](/unsere-dienstleistungen/sicherheitsanalyse) steht [Kontakt](/kontakt) zur Verfügung. Prüfen Sie Produktfunktionen, Lizenzen und Termine vor jeder produktiven Änderung erneut gegen Microsoft Learn.

## Quellen

[1]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement "Microsoft Learn – Passkeys by default and retirement of Microsoft-provided SMS and voice authentication"
[2]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passkeys-fido2 "Microsoft Learn – Authentication methods in Microsoft Entra ID: passkeys (FIDO2)"
[3]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement-faq "Microsoft Learn – Frequently asked questions about SMS and voice retirement"
[4]: https://pages.nist.gov/800-63-4/sp800-63b.html "NIST SP 800-63B – Digital Identity Guidelines: Authentication and Authenticator Management"
[5]: https://www.bacs.admin.ch/de/26w5-de "BACS – Woche 5: Weltweite SharePoint-Phishing-Welle – auch die Schweiz ist betroffen"
[6]: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf "CISA – Implementing Phishing-Resistant MFA"
[7]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths "Microsoft Learn – Conditional Access authentication strengths"
[8]: https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-deploy-phishing-resistant-passwordless-authentication "Microsoft Learn – Plan a phishing-resistant passwordless authentication deployment in Microsoft Entra ID"
[9]: https://learn.microsoft.com/en-us/entra/identity/conditional-access/plan-conditional-access "Microsoft Learn – Plan a Conditional Access deployment"
[10]: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access "Microsoft Learn – Manage emergency access accounts in Microsoft Entra ID"
[11]: https://www.bacs.admin.ch/de/grundschutz-unternehmen-behoerden "BACS – Grundschutz: Schützen Sie Ihr Unternehmen und Ihre Behörde"
[12]: https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-temporary-access-pass "Microsoft Learn – Configure Temporary Access Pass to register passwordless authentication methods"
[13]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz (DSG), Art. 8 Datensicherheit"
[14]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-phone-providers "Microsoft Learn – Choose a telephony provider for SMS and voice authentication"
[15]: https://learn.microsoft.com/en-us/entra/identity/authentication/phone-providers-faq "Microsoft Learn – Frequently asked questions about Choose Your Own Telephony Provider"
[16]: https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-set-up-sms-voice-api "Microsoft Learn – Set up SMS and voice with Choose Your Own Telephony Provider"
