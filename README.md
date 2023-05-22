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
      - [`doc`](#doc)
      - [`src`](#src)
    - [Technisches Setup](#technisches-setup)
      - [Verwendete Software / Technologien](#verwendete-software--technologien)
      - [Einrichtung / Anforderungen an die Umgebung](#einrichtung--anforderungen-an-die-umgebung)
    - [Anpassung](#anpassung)
      - [Anpassung von Übersetzungen](#anpassung-von-übersetzungen)
      - [Anpassung von Inhaltstypen](#anpassung-von-inhaltstypen)
      - [Anpassung von Attributwerten](#anpassung-von-attributwerten)
      - [Anpassung / Erstellung von Tests](#anpassung--erstellung-von-tests)
      - [Randnotiz Perfomance der Tests](#randnotiz-perfomance-der-tests)
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

- [ ] Verweise ‚die alten Dateien‘ prüfen und bereinigen [#siehe 3036](https://histhub.ssrq-sds-fds.ch/redmine/issues/3036)
- [x] Verwendung von `@rendition` verbieten [#siehe 3048](https://histhub.ssrq-sds-fds.ch/redmine/issues/3048)
- [x] Verwendung von `@corresp` verbieten
- [ ] Verwendung von `@rend` prüfen [#siehe 3051](https://histhub.ssrq-sds-fds.ch/redmine/issues/3051)
- [ ] Verwendung von `@cert` prüfen [#siehe 3052](https://histhub.ssrq-sds-fds.ch/redmine/issues/3052)
- [ ] Verwendung von `@resp` prüfen [#siehe 3053](https://histhub.ssrq-sds-fds.ch/redmine/issues/3053)
- [ ] Attribut `@source` nur eingeschränkt zulassen [#siehe 3056](https://histhub.ssrq-sds-fds.ch/redmine/issues/3056)
- [x] Verwendung aller Attributklassen prüfen

#### Header

- [ ] Speicherung der Archivsignatur / URL [siehe #1512](https://histhub.ssrq-sds-fds.ch/redmine/issues/1512?issue_count=24&issue_position=10&next_issue_id=1458&prev_issue_id=2548)
- [x] `<settlement/>` zu `<msIdentifier/>` hinzufügen [#3033](https://histhub.ssrq-sds-fds.ch/redmine/issues/3033?issue_count=11&issue_position=1&next_issue_id=3032)
- [x] Persitente Identifikatoren über UUIDs [siehe #2995](https://histhub.ssrq-sds-fds.ch/redmine/issues/2995)
- [ ] Content-Model für `<msItem/>` definieren [siehe #3007](https://histhub.ssrq-sds-fds.ch/redmine/issues/3007)
- [ ] Ergänzung von `<change/>`, um ‚Milestone‘-Änderungen zu verzeichnen [siehe #1441](https://histhub.ssrq-sds-fds.ch/redmine/issues/1441?issue_count=18&issue_position=10&next_issue_id=1424&prev_issue_id=2548)
- [ ] mehrere alternative Idenfikatoren erlauben [siehe #2880](https://histhub.ssrq-sds-fds.ch/redmine/issues/2880)
- [x] sprachunabhängige Kodierung des Trägermaterials [siehe #2663](https://histhub.ssrq-sds-fds.ch/redmine/issues/2663)
- [ ] Werte für `<head/>` in Liste bibl. Angaben vereinheitlichen [siehe #2665](https://histhub.ssrq-sds-fds.ch/redmine/issues/2665)
- [ ] `<resp/>` vereinheitlichen [siehe #3070](https://histhub.ssrq-sds-fds.ch/redmine/issues/3070)
- [ ] Content Model `<condition/>` klären [siehe #3079](https://histhub.ssrq-sds-fds.ch/redmine/issues/3079)
- [x] Werte / Content Model für `<damage/>` bestimmen [siehe #3080](https://histhub.ssrq-sds-fds.ch/redmine/issues/3080)
- [x] `<date/>` sollte innerhalb von `<publicationStmt/>` optional sein [siehe #3084](https://histhub.ssrq-sds-fds.ch/redmine/issues/3084)

#### Text

- [x] Sauberes Content-Model für `tei:text` definieren [siehe #3031](https://histhub.ssrq-sds-fds.ch/redmine/issues/3031)
- [ ] Hashtags (Doppelkreuze...) nur noch für bestimmte Fälle (interne Verweise) erlauben [siehe #1458](https://histhub.ssrq-sds-fds.ch/redmine/issues/1458?issue_count=21&issue_position=10&next_issue_id=1441&prev_issue_id=2548)
- [ ] eine Ersetzung muss immer eine Löschung mit Inhalt enthalten [siehe #2548](https://histhub.ssrq-sds-fds.ch/redmine/issues/2548?issue_count=13&issue_position=6&next_issue_id=1361&prev_issue_id=2634)
- [x] Werte von `@n` als Teil von `tei:pb` einschränken [siehe #3047](https://histhub.ssrq-sds-fds.ch/redmine/issues/3047)
- [x] Content-Model für `@scribe` überarbeiten [siehe #1311](https://histhub.ssrq-sds-fds.ch/redmine/issues/1311)
- [ ] Attribut `@place` für `tei:figure` erlauben [siehe #3049](https://histhub.ssrq-sds-fds.ch/redmine/issues/3049)
- [x] `tei:anchor` innerhalb der Zelle einer Tabelle erlauben [siehe #3006](https://histhub.ssrq-sds-fds.ch/redmine/issues/3006?issue_count=10&issue_position=1&next_issue_id=3005)
- [ ] Werte für `@medium` einschränken [siehe #3064](https://histhub.ssrq-sds-fds.ch/redmine/issues/3064)
- [ ] `@rend` im Falle von `tei:addSpan|tei:add` durch `@medium` ersetzen [siehe #3065](https://histhub.ssrq-sds-fds.ch/redmine/issues/3065)
- [x] Verwendung von `@wit` sowie Erfassung von Metadaten referenzierter Textzeugen klären [siehe #1360](https://histhub.ssrq-sds-fds.ch/redmine/issues/1360)
- [x] Attribut `@type` für `<text/>` mit den Werten summary oder transcript verpflichtend festlegen [siehe #3074](https://histhub.ssrq-sds-fds.ch/redmine/issues/3074)
- [ ] Klärung Content-Model `<row/>` [siehe #3076](https://histhub.ssrq-sds-fds.ch/redmine/issues/3076)

### Technische Umsetzung

- [ ] Aufteilung des Schemas bestimmen
- [x] Pipeline zur Erzeugung des Schemas erstellen
- [x] Benötigte Stylesheets aus den TEI-Stylesheets bestimmen und sinnvoll einbinden (Submodule?)
- [ ] Welche Schritte sind notwendig, um die bestehenden Daten an das neue Schema anzupassen?

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

Das Repository besteht aus vier verschiedenen Bereichen:

1. `doc`: hier befindet sich die Dokumentation, diese wird größtenteils dynamisch aus dem ODD generiert
2. `src`: hier befinden sich die Quelldateien des Schemas
3. `test`: der Name sagt es
4. `dist`: dieser Ordner wird dynamisch generiert und steht nicht unter Versionskontrolle; hier befinden sich die kompilierten Schemadateien

#### `doc`

ToDo

#### `src`

- der Unterordner `lib` enthält als git-Submodule die tei-Stylesheets; die verwendete Branch ist in der Datei `.gitmodules` definiert
- der Unterordner `elements` enthält die Schema-Deklarationen je Element; pro spezifizierten Element wird eine Datei nach dem Muster `name.odd.xml` erstellt – sofern verschiedene Spezifikationen für unt. Typen (Einleitung, Transkripte, etc.) festgelegt werden, wird der Typ mit `-type` an den Namen angehängt
- der Unterordner `common` enthält Spezifikationen, die von verschiedenen Teilen des Schemas wiederverwendet werden
  - `classes.odd.xml`: Klassendefinitionen
  - `constrains.odd.xml`: globale Schematron-Regeln
  - `content.odd.xml`: Inhaltstypen
  - `datatypes.odd.xml`: Datentypen, die als Inhalt für Attribute oder Elemente verwendet werden
  - `modules.odd.xml`: SSRQ-spezifische Module in Ergänzung der TEI
  - `patterns.odd.xml`: sog. Patterns, die als Inhaltsmodelle an verschiedenen Stellen verwendet werden – bspw. das Muster für Personen-IDs
- konkrete Schemadeklrationen werden auf der obersten Ebene festgelegt; die benötigten Bestandteile werden hier eingebunden

### Technisches Setup

#### Verwendete Software / Technologien

- [jing](https://github.com/relaxng/jing-trang)
- [poetry](https://python-poetry.org)
- [pytest](https://docs.pytest.org/en/7.1.x/how-to/writing_plugins.html)
- [saxonche](https://pypi.org/project/saxonche/)
- [TEI ODD](https://tei-c.org/guidelines/customization/getting-started-with-p5-odds/)
- [TEI Stylesheets](https://github.com/TEIC/Stylesheets)
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

Wiederholt ausgeführte Aufgaben (bspw. Ausführung der Tests) sind im sog. [Taskfile](Taskfile) gebündelt. Für die einfachere Benutzung empfiehlt es sich in der lokalen Shell-Konfigurationen einen Alias für das Taskfile nach dem Schema `alias run=./Taskfile` einzurichten, dann lassen sich die diversen Aufgaben nach folgendem Muster ausführen:

```sh
run test
```

Weitere Parameter (bspw. `-s` um print-Statement immer anzuzeigen) können einfach übergeben werden:

```sh
run test -s
```

### Anpassung

#### Anpassung von Übersetzungen

Das Schema ist in vier verschiedene Sprachen übersetzt: de, fr, en, it

Beschreibungen von Elementen werden auf deutsch, englisch und franzözisch verfasst. Die Spezifikation eines Element (siehe [/src/elements](/src/elements)) sollte immer ein Element `<desc/>` je Sprache enthalten. Für das Element `<cell/>` sieht das bspw. so aus:

```xml
<desc xml:lang="de" versionDate="2023-03-03">Auszeichnung von Tabellenzellen.</desc>
<desc xml:lang="en" versionDate="2023-03-03">Table cell mark-up.</desc>
<desc xml:lang="fr" versionDate="2023-03-03">Balisage des cellules de tableau.</desc>
```

Neben der Sprache sollte das Attribut `@versionDate` verwendet werden.

Beschreibungen von Attributwerten werden in der z.T. in der digitalen Edition verwendet und müssen in diesen Fällen **immer** in allen vier Sprachen angelegt werden. Dies kann folgendermaßen aussehen:

```xml
<valItem ident="Sack">
    <desc xml:lang="de" versionDate="2023-03-17">Sack</desc>
    <desc xml:lang="de" type="plural" versionDate="2023-03-17">Säcke</desc>
    <desc xml:lang="fr" versionDate="2023-03-17">sac</desc>
    <desc xml:lang="fr" type="plural" versionDate="2023-03-17">sacs</desc>
    <desc xml:lang="en" versionDate="2023-03-17">bag</desc>
    <desc xml:lang="en" type="plural" versionDate="2023-03-17">bags</desc>
    <desc xml:lang="it" versionDate="2023-03-17">sacchetto,</desc>
    <desc xml:lang="it" type="plural" versionDate="2023-03-17">sacchetti</desc>
</valItem>
```

#### Anpassung von Inhaltstypen

ToDo

#### Anpassung von Attributwerten

Todo

#### Anpassung / Erstellung von Tests

Die im Schema festgelegten Regeln werden automatisch mit `pytest` überprüft. Hierfür müssen Testfälle definiert werden. Tests werden im Unterordner [test](/test) erstellt. Es wird zwischen Tests, die allgemeine Bedingungen des Schema prüfen, und elementspezifischen Tests unterschieden. Allgemeine Tests befinden sich gemeinsam mit den Konfigurationsdateien (`conftest.py`) auf der obersten Ebene. Elementspezifische Tests befinden sich in [test/element](/test/elements/). Nach Möglichkeit sollten immer mehrere Fälle je Test überprüft werden -- siehe hierzu [Parametrizing fixtures and test functions](https://docs.pytest.org/en/6.2.x/parametrize.html).

Im Testfile eines Elements müssen zunächst die benötigten Module importiert werden.

```python
import pytest
from ssrq_cli.validate.xml import RNGJingValidator

from main import Schema

from ..conftest import SimpleTEIWriter
```

Anschließend können die Tests erstellt werden. Hierbei wird zwischen Tests zum Prüfen von RELAXNG- und Schematron-Regeln unterschieden (siehe bspw. [test_idno.py](/test/elements/test_idno.py)). Die Testdefinition ist dabei weitestgehend an der Triple-A-Rule (Arrange-Act-Assert) orientiert und folgt typischerweise folgendem Muster:

```python
# ARRANGE
@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-text",
            "<text xmlns='http://www.tei-c.org/ns/1.0'><body><div><p>foo</p></div></body></text>",
            True,
        ),
        (
            "valid-text",
            "<text xmlns='http://www.tei-c.org/ns/1.0'><body><div><p>bar</p></div></body><back><div><p>foo</p></div></back></text>",
            True,
        ),
        (
            "invalid-text-with-back-only",
            "<text xmlns='http://www.tei-c.org/ns/1.0'><back><div><p>foo</p></div></back></text>",
            False,
        ),
        (
            "invalid-text-with-attribute",
            "<text type='foobar' xmlns='http://www.tei-c.org/ns/1.0'><body><div><p>hallo welt!</p></div></body></text>",
            False,
        ),
        (
            "invalid-text-with-group",
            "<text xmlns='http://www.tei-c.org/ns/1.0'><group><body><div><p>hallo welt!</p></div></body></group></text>",
            False,
        ),
    ],
)
def test_text(
    element_schema: dict[str, str],
    writer: SimpleTEIWriter,
    name: str,
    markup: str,
    result: bool,
):
    validator = RNGJingValidator()
    writer.write(name, markup)

    # ACT
    validator.validate(
        sources=writer.parse_files(),
        schema=element_schema["text"],
        file_pattern=writer.construct_file_pattern(),
    )

    # ASSERT
    assert len(validator.get_invalid()) == (0 if result else 1)
```

Sollen nur die Tests eines Elements ausgeführt werden, dann kann dazu folgender Befehl verwendet werden:

```sh
run test test/elements/test_cell.py
```

#### Randnotiz Perfomance der Tests

Bevor die Tests erzeugt werden, wird ein neues RNG-Schema basierend auf den Quelldateien in `src` erzeugt. Die Erzeugung der Schemadatei hängt vom jeweiligen Netzwerk ab, da hier der Server des TEI-Consortiums angefragt bei. In der Praxis hat sich gezeigt, dass eine VPN-Verbindung zur Uni dies drastisch beschleunigen kann.

### Schema erzeugen

#### Erzeugung einer neuen Version und Upload

ToDo

#### Erzeugung der Dokuemtation

Todo
