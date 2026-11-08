# CMS- und Verwaltungszugang – Befund vom 20.09.2026

- Die öffentliche Website liefert zahlreiche Assets von `primary.jwwb.nl` und `assets.jwwb.nl`; dies weist auf JouwWeb/Webador als Seitensystem hin.
- Die öffentliche Website verlinkt zusätzlich auf `https://admin.dkschv.ch`.
- `admin.dkschv.ch` läuft über eine Render-Anwendung. Beim Zugriff am 20.09.2026 blieb die Anwendung nach dem Aufwecken auf der Render-Zwischenseite „Application loading“ stehen.
- Der aktivierte Benutzerbrowser war während der Prüfung nicht verbunden; die Navigation lief deshalb im Sandbox-Browser. Ein authentifizierter Verwaltungszugang konnte noch nicht verifiziert werden.
- Vor einer automatisierten Veröffentlichung muss geklärt werden, ob Inhalte über JouwWeb direkt oder über die separate Render-Verwaltung gepflegt werden.
- Bis dahin werden alle Beiträge als CMS-fertige Markdown-Dateien mit Import-Manifest erstellt. Es wird nichts öffentlich veröffentlicht.

## Ergänzung nach Auswahl von Variante C

- Der offizielle JouwWeb-Login unter `https://www.jouwweb.nl/inloggen` wurde am 20.09.2026 erfolgreich im verbundenen Benutzerbrowser geöffnet.
- Die Seite zeigt die reguläre Anmeldung per E-Mail/Passwort sowie Google- oder Facebook-Anmeldung.
- Für den nächsten Schritt ist eine Anmeldung durch den Benutzer erforderlich. Zugangsdaten werden nicht durch Manus gelesen oder angefordert.
- Nach erfolgreicher Anmeldung wird zuerst geprüft, ob das DKSchV-Projekt im Konto vorhanden ist. Anschliessend wird ein nichtöffentlicher Testentwurf angelegt; eine öffentliche Veröffentlichung erfolgt erst nach Prüfung des genauen CMS-Ablaufs und der vorgesehenen Freigaberegeln.

## Authentifizierter CMS-Zugriff bestätigt

Am 20.09.2026 wurde der authentifizierte Webador-Zugang erfolgreich verifiziert. Das Konto enthält genau das Projekt **DKSchV Pro** mit der Domain `dkschv.ch`. Der Editor ist unter der Webador-Projekt-ID `6004383` erreichbar. Die Website ist im CMS derzeit als veröffentlicht gekennzeichnet.

Beim ersten Öffnen des Editors erschien jedoch die Meldung «Etwas scheint schief zu laufen! Seite neu laden.» und die Seitenvorschau blieb im Ladezustand. Vor Änderungen wird der Editor deshalb neu geladen und anschliessend zunächst die Seiten- und Blogstruktur geprüft. Es wurde noch kein Inhalt verändert oder veröffentlicht.

## Seiten- und Blogstruktur im CMS

Nach dem erneuten Laden funktioniert der Webador-Editor. Die verwaltete Seitenstruktur enthält **Home**, **Unsere Dienstleistungen** mit den Unterseiten **Sicherheitsanalyse**, **Risikomanagement**, **Notfallplanung** und **Test**, ausserdem **Häufige Fragen**, **Über uns**, **Kontakt**, **Blog**, **Anfrage** und **anfrage-test**. Die bestehende Blogseite ist als Unterseite von Kontakt angeordnet.

Die öffentliche Testseite und die Seite `anfrage-test` sind weiterhin im CMS vorhanden. Sie werden im Rahmen dieser Blogaufgabe nicht verändert. Als nächster Schritt wird die bestehende Blogseite geöffnet, um zu prüfen, ob Webador Entwürfe oder zeitgesteuerte Beiträge unterstützt. Es wurde weiterhin kein Inhalt verändert oder veröffentlicht.

## Bestehende Blogseite im Editor

Die Seite **Blog** ist im Webador-Editor unter der Seiten-ID `25868423` erreichbar. Nach erneutem Laden wird die Seite korrekt dargestellt. Sichtbar sind ein grosser Headerbereich, die Überschrift **«Blog-Informationen»**, ein Einführungstext sowie statische Inhaltsblöcke wie **«Aktuelle Sicherheitsfragen»**. Im unmittelbar sichtbaren Bereich ist noch keine Beitragsverwaltung oder Schaltfläche für einen neuen Blogbeitrag erkennbar.

Die linke Elementleiste enthält weiter unten das Webador-Element **Blog**. Vor dem Anlegen eines Testbeitrags wird geprüft, ob auf der bestehenden Seite bereits ein solches Blog-Element eingebunden ist und welche Entwurfs- oder Planungsoptionen es bietet. Es wurde kein Inhalt verändert.

## Blog-Element und Editor-Navigation

Durch Scrollen der linken Webador-Elementleiste wurde das Element **Blog** sichtbar. Der zentrale Vorschaubereich ist als eingebettete Editorfläche umgesetzt; ein gezielter Scrollversuch über die Browserautomation konnte dort keinen separaten scrollbaren Container erkennen. Deshalb wird als nächster risikoarmer Schritt das Blog-Element ausgewählt, um zu prüfen, ob Webador einen Einrichtungsdialog oder eine Beitragsverwaltung öffnet. Vor einer möglichen Einfügung wird beobachtet, ob die Aktion eine unmittelbare Seitenänderung auslösen würde.

## Sicherheitsentscheidung für den Testimport

Die offizielle JouwWeb-Dokumentation bestätigt zwei wesentliche Punkte: Nach der ersten Website-Veröffentlichung werden normale Editor-Änderungen automatisch auf der Live-Website sichtbar. Blogbeiträge können dagegen ausdrücklich als **Konzept/Entwurf** gespeichert oder für ein Veröffentlichungsdatum geplant werden. Eine versteckte Seite ist weiterhin über einen direkten Link erreichbar; eine passwortgeschützte Seite ist im Pro-Paket verfügbar.

Für den Testimport wird daher keine sichtbare Änderung an der bestehenden Blogseite vorgenommen. Stattdessen wird eine separate Seite mit ausgeblendeter Navigation und Passwortschutz verwendet. Der Testbeitrag selbst bleibt zusätzlich als Blogentwurf gespeichert. Diese doppelte Absicherung verhindert eine unbeabsichtigte öffentliche Veröffentlichung während der Einrichtung.

## Dialog zum Anlegen der Testseite

Der Dialog **«Neue Seite»** wurde geöffnet. Die automatische Browserauslese konnte den Modalinhalt in diesem Zustand wegen eines Artefaktfehlers nicht erfassen. Deshalb werden vor der Eingabe die sichtbaren Formularfelder mit alternativen Browserwerkzeugen ausgelesen. Es wurde noch kein Seitenname eingegeben und keine Seite erstellt.

## Abbruch des ersten Testseiten-Dialogs

Der nicht zuverlässig auslesbare Dialog zum Erstellen einer neuen Seite wurde mit **Escape** geschlossen. Die Seitenliste ist unverändert; es wurde keine Testseite angelegt. Der nächste Versuch erfolgt nur, wenn die Formularfelder und Speichereinstellungen sicher identifiziert werden können.

## Testseite erstellt

Die Seite **DKSchV Blog Test** wurde unter der Webador-Seiten-ID `38420588` angelegt und im Editor geöffnet. Sie enthält derzeit automatisch generierte statische Inhalte mit der Überschrift **«Einblicke in unsere Sicherheitsberatung»** und mehreren Bild-/Textabschnitten. Ein Blog-Element ist im sichtbaren Bereich noch nicht vorhanden. Vor weiterer Nutzung werden Seitenschutz und Suchmaschinen-/Menüsichtbarkeit geprüft; erst danach wird die Seite für den Blog-Workflow angepasst.

## Schutz der Testseite verifiziert

Der öffentliche Abruf von `https://www.dkschv.ch/dkschv-blog-test` zeigt ausschliesslich die Seite **«Passwort erforderlich»**; die automatisch generierten Testinhalte sind ohne Passwort nicht sichtbar. Der Menüname der Testseite erscheint nicht in der öffentlichen Hauptnavigation. Damit ist die Testumgebung für die nächste Einrichtung ausreichend abgeschirmt. Der geöffnete Einstellungsdialog wurde ohne Änderungen geschlossen.

## Blog-Modul erfolgreich eingerichtet

Auf der passwortgeschützten Testseite ist nun ein Webador-Blog-Modul vorhanden. Es enthält die zwei von Webador automatisch angelegten Beispielentwürfe **«(Konzept) Dies ist ein Beitrag mit Bildern»** und **«(Konzept) Dies ist ein einfacher Artikel»**. Nach Auswahl des Moduls zeigt die Toolbar die Funktionen **Blog verwalten**, **+ Beitrag**, **Ansicht**, **Einstellungen** und **Optionen**.

Damit ist die geschützte Testumgebung funktionsfähig. Der nächste Schritt ist das Anlegen von Artikel 01 über **+ Beitrag**, wobei als Veröffentlichungsstatus ausdrücklich «Konzept/Entwurf» verwendet wird.

## Einschränkung der Browserautomation im Blog-Modul

Das Blog-Modul und seine Toolbar sind visuell korrekt geladen. Zwei gezielte Klickversuche auf **«+ Beitrag»** innerhalb der eingebetteten Editorfläche lösten jedoch keinen Dialog aus. Die Toolbar liegt in einem von Webador intern gerenderten Bereich, der in der Browser-Zugänglichkeitsstruktur nicht als klickbares Element verfügbar ist. Um unbeabsichtigte Live-Änderungen zu vermeiden, werden keine weiteren blinden Klicks ausgeführt.

## Direkter Editor-Frame-Zugriff

Im gespeicherten Editor-HTML wurde die interne Vorschau-Route `/v2/website/6004383/editor-frame/page/38420588` identifiziert. Ein direkter authentifizierter Aufruf leitet Webador jedoch wieder auf den vollständigen Editor zurück. Die iframe-interne Blog-Toolbar bleibt damit für die Browserautomation nicht semantisch zugänglich. Das Blog-Modul selbst bleibt unverändert und geschützt.

## Tastaturnavigation getestet

Ein Tastatur-Fokusversuch nach Auswahl des Blog-Moduls öffnete lediglich den Bearbeitungsmodus des vorhandenen Fusszeilentextes; die iframe-interne Blogtoolbar wurde nicht fokussiert. Es wurde kein Text eingegeben und kein Inhalt verändert. Die automatische Beitragsbearbeitung bleibt damit über den aktuellen Browserkanal technisch nicht zuverlässig möglich.

## Blog-Schaltfläche präzise lokalisiert

Nach erneuter Auswahl des Blog-Moduls wurde die Schaltfläche **«+ Beitrag»** exakt lokalisiert. Die Hover-Beschriftung **«Neuen Beitrag hinzufügen»** bestätigt, dass die korrekte Schaltfläche erreicht ist. Die früheren Klickversuche lagen wegen der vertikalen Editorverschiebung oberhalb der aktiven Toolbar.
