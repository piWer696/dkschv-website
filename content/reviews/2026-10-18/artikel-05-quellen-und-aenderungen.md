# Prüfbericht – Artikel 05: Microsoft 365 MFA und Passkeys

**Prüfdatum:** 18. Oktober 2026, ISO-Woche 42. Erstabrufe 09:04–09:11 Europe/Zurich; gezielte Fedlex-Endkorrektur gegen 09:15. Gegenstand sind der Artikel `articles/05-microsoft-365-mfa-passkeys.md` und das Arbeitsmittel `resources/05-passkey-rollout-checkliste.md`.

## Endergebnis und behobene Recherchelücke

Alle **14 eindeutigen externen Referenzen** beider Dateien sind erreichbar und inhaltlich gegen Originalquellen abgeglichen. Im ersten Prüfschritt war allein die Konsolidierung von DSG Art. 8 wegen des JavaScript-Zugangs unklar. Dieser technische Vorbehalt wurde am selben Tag gezielt geschlossen: Die amtliche [Chronologie](https://www.fedlex.admin.ch/eli/cc/2022/491/de/history) weist als jüngste Fassung die Berichtigung mit Inkrafttreten **7. Juli 2025** aus. Die dort ausdrücklich verlinkte [XML-Fassung](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml) bestätigt Art. 8 Abs. 1–3 und insbesondere die risikoadäquate Datensicherheit durch technische und organisatorische Massnahmen. Das ist ein überprüfter Quellenstand, **keine** Rechts- oder Tenant-Freigabe. Endstatus: **all_references_verified=true**; der frühere Teilstatus ist überholt.

## Geprüfte Originalreferenzen

1. [Microsoft: Passkeys und SMS/Voice Retirement](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement), Stand 23.09.2026, Abruf 09:04. Fristen 01.09.2026, 01.02.2027 und 01.07.2027 sowie Benutzerumfang, Registrierungskampagne und fehlender Enforcement-Opt-out bestätigt.
2. [Microsoft: Passkeys FIDO2](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passkeys-fido2), Stand 06.04.2026, Abruf 09:04. Schlüsselpaar, synchronisierte/gerätegebundene Passkeys und Attestierungsgrenze bestätigt.
3. [Microsoft: SMS/Voice FAQ](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement-faq), Stand 23.09.2026, Abruf 09:05. Public Cloud, B2C-Ausnahme, External-ID-Abgrenzung und Fristen bestätigt.
4. [NIST SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html), Abruf 09:05. Manuell eingegebene OTP-Ausgaben nicht phishing-resistent; kein seitenbezogenes Tagesänderungsdatum belegt.
5. [BACS: SharePoint-Phishing](https://www.bacs.admin.ch/de/26w5-de), veröffentlicht 03.02.2026, Abruf 09:05. Echtzeit-Weiterleitung des zweiten Faktors und Awareness-Hinweise bestätigt.
6. [CISA: Implementing Phishing-Resistant MFA](https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf), Dokument Oktober 2022, Abruf 09:10. Die aktuelle CISA-MFA-Seite verlinkt diese offizielle PDF; FIDO/WebAuthn und SMS/Voice-Risiken bestätigt.
7. [Microsoft: Authentication strengths](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths), Stand 24.10.2025, Abruf 09:05. P1-Bezug, integrierte phishing-resistente Methoden und Auswertung nach initialer Authentisierung bestätigt.
8. [Microsoft: Deploymentplanung](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-deploy-phishing-resistant-passwordless-authentication), MicrosoftDocs-Metadatum 26.03.2026, Abruf 09:05. Repräsentativer Pilot, Geräteprofile, Gruppe und Activity Report bestätigt.
9. [Microsoft: Conditional-Access-Planung](https://learn.microsoft.com/en-us/entra/identity/conditional-access/plan-conditional-access), MicrosoftDocs-Metadatum 01.06.2026, Abruf 09:06. Berichtsmodus, Protokolle, Pilot und kontrollierte Notfallzugänge bestätigt.
10. [Microsoft: Emergency access](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access), MicrosoftDocs-Metadatum 04.06.2026, Abruf 09:06. Mindestens zwei cloud-only Notfallkonten, privilegierte Rolle, phishing-resistente Anmeldung, Überwachung und Tests bestätigt. Ein Dateimetadatum ist nicht zwingend identisch mit dem sichtbaren Learn-Änderungsdatum.
11. [BACS: Grundschutz](https://www.bacs.admin.ch/de/grundschutz-unternehmen-behoerden), Abruf 09:06. Zusammenspiel technischer und organisatorischer Massnahmen sowie Führungsverantwortung bestätigt; kein vollständiges Seitenänderungsprotokoll.
12. [Microsoft: Temporary Access Pass](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-temporary-access-pass), MicrosoftDocs-Metadatum 04.03.2026, Abruf 09:06. Zeitlich begrenzter Registrierung-/Recoverycode und kontrollierte Ausgabe bestätigt.
13. [Fedlex: DSG Art. 8](https://www.fedlex.admin.ch/eli/cc/2022/491/de), HTML erstabgerufen 09:06; **amtliche Chronologie und XML gegen 09:15 verifiziert**, jüngste ausgewiesene Fassung Stand 07.07.2025. Kein verbleibender technischer Konsolidierungsblocker; konkrete Angemessenheit bleibt Fachfrage.
14. [Microsoft: Telephony provider](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-phone-providers), Stand 23.09.2026, Abruf 09:06. Konfiguration laut Hersteller **ab 30.10.2026**, am Prüftag noch nicht verfügbar; Soprano und Telesign als private Vorschau bestätigt.

Zusätzlich wurden BACS [Woche 40](https://www.bacs.admin.ch/de/26w40-de), [Oversharing vom 05.10.](https://www.bacs.admin.ch/de/csm26-s2-de) und [Im Fokus](https://www.bacs.admin.ch/de/im-fokus) geprüft. Daraus wurde keine neue MFA-/Passkey-Pflicht abgeleitet. Die für die verwendeten Learn-Dateien geprüfte MicrosoftDocs-Commit-Historie zeigte im Zeitraum 04.–18.10. keine neue Änderung; das ist keine Vollständigkeitsgarantie für nicht öffentliche Produktentwicklungen.

## Änderungen an Artikel und Arbeitsmittel

Der Quellenprüfstand wurde auf **18. Oktober 2026** gesetzt; die Reichweite und der endgültige Referenzstatus sind in den neuen Frontmatter-Feldern dokumentiert. Die Provider-Nichtverfügbarkeit ist nun auf den heutigen Prüftag statt auf 04.10. bezogen. Die CISA-PDF-Referenz wurde auf die von CISA selbst verlinkte aktuelle Speicheradresse `/2023-01/` korrigiert.

In den Abschnitten **«Wiederherstellung vor der Durchsetzung planen»** des Artikels und **«Grenzen»** der Checkliste wurde der zunächst neu eingefügte technische Fedlex-Vorbehalt nach erfolgreichem XML-/Chronologieabruf durch den belegten Fassungsstand ersetzt. **Alle Fachprüfungsmarker bleiben bestehen.** Es wurde kein `rechtsstand`, kein `fachlich_geprueft_am` und keine Freigabe gesetzt.

**Unverändert:** Original-Slugs, Artikeltermin 29.10.2026, H1/Kurzantwort, Struktur, Entwurfs-/Vorlagenstatus, Meta-Title und Meta-Description sowie interne relative Links. Die Metadatenänderung betrifft Prüfstand und Reichweite, nicht die SEO-Texte. Artikel besitzt weiterhin drei, Arbeitsmittel vier ursprüngliche Fachmarker.

## Konkrete verbleibende Fach- und Publikationsblocker

Die Eignung der Massnahmen nach DSG Art. 8 für den tatsächlichen Bearbeitungskontext ist nicht entschieden. Ebenso offen sind Tenant-Betroffenheit, Benutzer-/Gastklassifikation, Lizenzen, Conditional Access, TAP-Ausgabe, Geräteunterstützung, Recovery und Notfallzugänge. Ab 30.10. sind bei Bedarf Telefonieanbieter, regionale Abdeckung, Vertrag, Kosten, Datenschutz, Integration und Pilot separat zu prüfen. Keine Eignung eines Anbieters für die Schweiz oder diesen Tenant wird behauptet.

Beide Dateien bleiben **nicht freigegeben**. Vor Veröffentlichung braucht es echte Fachfreigabe, authentifizierten CMS-Zugang und erneute Prüfung sämtlicher öffentlicher Verweisziele. Die Quellenkorrektur hebt diese Sperren nicht auf; es fand kein CMS-Schreibvorgang statt.
