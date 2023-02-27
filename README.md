# SSRQ-Schema

Dieses Repository beinhaltet Quellcode und sonstige Dateien im Zusammenhang mit dem XML-Schema der Sammlung der Schweizerischen Rechtsquellen.

- [SSRQ-Schema](#ssrq-schema)
  - [Initiale Zielsetzung der Entwicklung](#initiale-zielsetzung-der-entwicklung)
  - [To-Dos](#to-dos)
    - [Inhaltlich](#inhaltlich)
      - [Generelles](#generelles)
      - [Header](#header)
      - [Text](#text)
    - [Technische Umsetzung](#technische-umsetzung)
  - [Dokumentation](#dokumentation)
    - [Versionierung](#versionierung)
    - [Aufbau](#aufbau)
    - [Was ist wo?](#was-ist-wo)
    - [Technisches Setup](#technisches-setup)
      - [Verwendete Software / Technologien](#verwendete-software--technologien)
      - [Einrichtung / Anforderungen an die Umgebung](#einrichtung--anforderungen-an-die-umgebung)
    - [Anpassung](#anpassung)
      - [Anpassung von Übersetzungen](#anpassung-von-übersetzungen)
      - [Anpassung von Inhaltstypen](#anpassung-von-inhaltstypen)
      - [Anpassung von Attributwerten](#anpassung-von-attributwerten)
    - [Schema erzeugen](#schema-erzeugen)
      - [Erzeugung einer neuen Version und Upload](#erzeugung-einer-neuen-version-und-upload)
      - [Erzeugung der Dokuemtation](#erzeugung-der-dokuemtation)

## Initiale Zielsetzung der Entwicklung

1. Aktualisierung und Anpassung des bestehenden Schemas an Neuentwicklungen TEI-Guidelines
2. Aufarbeitung von Rück-/Misständen (siehe inhalt. To-Dos sowie die zugehörigen Projekte in Redmine)
3. Eindeutige Versionierung (Daten entsprechen einem Schema einer bestimmten Version)
4. Testbarkeit
5. Kopplung mit (Oxygen-)Templates
6. Erzeugung einer Web-Dokumentation aus dem Schema heraus (ersetzt die Dokumentation im Wiki)
7. XSLT-Skripte (o.ä.) zur Migration zwischen Datenständen

## To-Dos

### Inhaltlich

#### Generelles

- Kapselung in `<teiCorpus/>` [siehe #3035](https://histhub.ssrq-sds-fds.ch/redmine/issues/3035)
- Verweise ‚die alten Dateien‘ prüfen und bereinigen [#siehe 3036](https://histhub.ssrq-sds-fds.ch/redmine/issues/3036)

#### Header

- [ ] Speicherung der Archivsignatur / URL [siehe #1512](https://histhub.ssrq-sds-fds.ch/redmine/issues/1512?issue_count=24&issue_position=10&next_issue_id=1458&prev_issue_id=2548)
- [ ] `<settlement/>` zu `<msIdentifier/>` hinzufügen [#3033](https://histhub.ssrq-sds-fds.ch/redmine/issues/3033?issue_count=11&issue_position=1&next_issue_id=3032)
- [ ] Persitente Identifikatoren über UUIDs [siehe #2995](https://histhub.ssrq-sds-fds.ch/redmine/issues/2995)
- [ ] Content-Model für `<msItem/>` definieren [siehe #3007](https://histhub.ssrq-sds-fds.ch/redmine/issues/3007)
- [ ] Ergänzung von `<change/>`, um ‚Milestone‘-Änderungen zu verzeichnen [siehe #1441](https://histhub.ssrq-sds-fds.ch/redmine/issues/1441?issue_count=18&issue_position=10&next_issue_id=1424&prev_issue_id=2548)
- [ ] mehrere alternative Idenfikatoren erlauben [siehe #2880](https://histhub.ssrq-sds-fds.ch/redmine/issues/2880)
- [ ] sprachunabhängige Kodierung des Trägermaterials [siehe #2663](https://histhub.ssrq-sds-fds.ch/redmine/issues/2663)
- [ ] Werte für `<head/>` in Liste bibl. Angaben vereinheitlichen [siehe #2665](https://histhub.ssrq-sds-fds.ch/redmine/issues/2665)

#### Text

- [ ] Sauberes Content-Model für `tei:text` definieren [siehe #3031](https://histhub.ssrq-sds-fds.ch/redmine/issues/3031)
- [ ] Hashtags (Doppelkreuze...) nur noch für bestimmte Fälle (interne Verweise) erlauben [siehe #1458](https://histhub.ssrq-sds-fds.ch/redmine/issues/1458?issue_count=21&issue_position=10&next_issue_id=1441&prev_issue_id=2548)
- [ ] eine Ersetzung muss immer eine Löschung mit Inhalt enthalten [siehe #2548](https://histhub.ssrq-sds-fds.ch/redmine/issues/2548?issue_count=13&issue_position=6&next_issue_id=1361&prev_issue_id=2634)

### Technische Umsetzung

- [ ]: Aufteilung des Schemas bestimmen
- [ ]: Pipeline zur Erzeugung des Schemas erstellen
- [ ]: Benötigte Stylesheets aus den TEI-Stylesheets bestimmen und sinnvoll einbinden (Submodule?)
- [ ]: Welche Schritte sind notwendig, um die bestehenden Daten an das neue Schema anzupassen?

## Dokumentation

### Versionierung

Die Versionierung des Schemas erfolgt gemäß Semantic Versioning. Dies erlaubt die eindeutige Zuordnung eines bestimmten Datenmodells zu einer bestimmten Version. Die Grundregel lautet:

```
MAJOR.MINOR.PATCH
```

Die Versionsnummer wird als Tag in der Git-History hinterlegt und ist zudem in der Datei `pyproject.toml` in der Tabelle `ssrq.schema.meta` hinterlegt. Die kompilierten Versionen des Schemas folgen dem Muster `tei-ssrq-schema-version.(rng|odd)` und verwenden die in dieser Projektkonfiguration hinterlegte Versionnumer.

### Aufbau

ToDo

### Was ist wo?

ToDo

### Technisches Setup

#### Verwendete Software / Technologien

- [jing](https://github.com/relaxng/jing-trang)
- [poetry](https://python-poetry.org)
- [pytest](https://docs.pytest.org/en/7.1.x/how-to/writing_plugins.html)
- [saxonche](https://pypi.org/project/saxonche/)
- [taskipy](https://github.com/illBeRoy/taskipy)
- [TEI ODD](https://tei-c.org/guidelines/customization/getting-started-with-p5-odds/)
- [TEI Stylesheets](https://github.com/TEIC/Stylesheets)
- [xmlformatter](https://pypi.org/project/xmlformatter/) (vakant!)
- ...

#### Einrichtung / Anforderungen an die Umgebung

Das Repository wird regulär über `git clone` ausgecheckt. Für die vollständige Funktionalität müssen dann noch die Git-Submodule initialisiert werden:

```sh
git submodule update --init --recursive
```

Für die Kompilierung des Schemas sowie die Ausführung der Tests ist es erforderlich, dass eine `JAVA`-Laufzeitumgebung sowie `Python` in Version 3.11 auf dem System installiert ist. Ferner ist es erforderlich, dass der Python-Paketmanager `poetry` installiert ist.

Alle weiteren Abhängigkeiten können dann über folgenden Befehl install werden

```sh
poetry install
```

### Anpassung

#### Anpassung von Übersetzungen

ToDo

#### Anpassung von Inhaltstypen

ToDo

#### Anpassung von Attributwerten

Todo

### Schema erzeugen

#### Erzeugung einer neuen Version und Upload

ToDo

#### Erzeugung der Dokuemtation

Todo
