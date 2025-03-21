# SSRQ-Schema [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10040701.svg)](https://doi.org/10.5281/zenodo.10040701)

Dieses Repository beinhaltet Quellcode und sonstige Dateien im Zusammenhang mit dem XML-Schema 
der Sammlung der Schweizerischen Rechtsquellen.

- [SSRQ-Schema ](#ssrq-schema-)
  - [Initiale Zielsetzung der Entwicklung](#initiale-zielsetzung-der-entwicklung)
  - [Dokumentation](#dokumentation)
    - [Versionierung](#versionierung)
    - [Was ist wo?](#was-ist-wo)
      - [`src/docs`](#srcdocs)
      - [`src/schema`](#srcschema)
    - [Technisches Setup](#technisches-setup)
      - [Verwendete Software / Technologien](#verwendete-software--technologien)
      - [Einrichtung / Anforderungen an die Umgebung](#einrichtung--anforderungen-an-die-umgebung)
    - [Anpassung](#anpassung)
      - [Anpassung von Übersetzungen](#anpassung-von-übersetzungen)
      - [Anpassung von Inhaltstypen](#anpassung-von-inhaltstypen)
      - [Anpassung von Attributwerten](#anpassung-von-attributwerten)
      - [Anpassung / Erstellung von Tests](#anpassung--erstellung-von-tests)
      - [Links zwischen Bestandteilen des Schemas und der (übrigen) Dokuseite](#links-zwischen-bestandteilen-des-schemas-und-der-übrigen-dokuseite)
    - [Schema erzeugen](#schema-erzeugen)
      - [Erzeugung einer neuen Version und Upload](#erzeugung-einer-neuen-version-und-upload)
      - [Erzeugung der Dokumentation](#erzeugung-der-dokumentation)
        - [Befehle](#befehle)
        - [Datei- / Ordnerstruktur](#datei---ordnerstruktur)
  - [Autor:innen](#autorinnen)
  - [Lizenzierung](#lizenzierung)

## Initiale Zielsetzung der Entwicklung

1. Aktualisierung und Anpassung des bestehenden Schemas an Neuentwicklungen TEI-Guidelines
2. Aufarbeitung von Rück-/Misständen
3. Eindeutige Versionierung (Daten entsprechen einem Schema einer bestimmten Version)
4. Testbarkeit
5. Erzeugung einer Web-Dokumentation aus dem Schema heraus (ersetzt die Dokumentation im Wiki)
6. Erarbeitung von XSLT-Skripten (o.ä.) zur Migration zwischen Datenständen
7. Öffentlicher Zugriff auf vormals interne Dokumentation

## Dokumentation

### Versionierung

Die Versionierung des Schemas erfolgt gemäß Semantic Versioning. Dies erlaubt die eindeutige
Zuordnung eines bestimmten Datenmodells zu einer bestimmten Version. Die Grundregel lautet:

```
MAJOR.MINOR.PATCH
```

Die Versionsnummer wird als Tag in der Git-History hinterlegt und ist zudem in der Datei
`pyproject.toml` in der Tabelle `ssrq.schema.meta` hinterlegt. Die kompilierten Versionen des
Schemas folgen dem Muster `tei-ssrq-schema-version.(rng|odd)` und verwenden die in dieser
Projektkonfiguration hinterlegte Versionsnummer.

### Was ist wo?

Das Repository ist wie folgt aufgeteilt:

```
ssrq-schema/
├─ .github/
├─ src/
│  ├─ docs/
│  ├─ schema/
│  │  ├─ commons/
│  │  ├─ elements/
│  │  ├─ examples/
│  │  ├─ main.odd.xml
├─ utils/
│  ├─ commons/
│  ├─ docs/
│  ├─ schema/
├─ .gitignore
├─ .gitmodules
├─ CITATION.cff
├─ LICENSE
├─ mkdocs.yml
├─ poetry.lock
├─ pyproject.toml
├─ README.md
├─ Taskfile
```

1. `src`: hier befinden sich die Quelldateien des Schemas sowie Teile der Dokumentation (`.md`),
  die nicht Teil des ODDs sind
2. `tests`: der Name sagt es
3. `build`: dieser Ordner wird dynamisch generiert und steht nicht unter Versionskontrolle; hier
  befinden sich die kompilierten Schemadateien sowie die HTML-Doku

#### `src/docs`

Siehe [Erzeugung der Dokumentation](#erzeugung-der-dokumentation).

#### `src/schema`

- der Unterordner `elements` enthält die Schema-Deklarationen je Element; pro spezifizierten
  Element wird eine Datei nach dem Muster `name.odd.xml` erstellt – sofern verschiedene
  Spezifikationen für unt. Typen (Einleitung, Transkripte, etc.) festgelegt werden, wird der Typ
  mit `-type` an den Namen angehängt
- der Unterordner `commons` enthält Spezifikationen, die von verschiedenen Teilen des Schemas
  wiederverwendet werden
  - `classes.odd.xml`: Klassendefinitionen
  - `constrains.odd.xml`: globale Schematron-Regeln
  - `content.odd.xml`: Inhaltstypen
  - `datatypes.odd.xml`: Datentypen, die als Inhalt für Attribute oder Elemente verwendet werden
  - `modules.odd.xml`: SSRQ-spezifische Module in Ergänzung der TEI
  - `patterns.odd.xml`: sog. Patterns, die als Inhaltsmodelle an verschiedenen Stellen verwendet
    werden – bspw. das Muster für Personen-IDs
- konkrete Schemadeklrationen werden auf der obersten Ebene festgelegt; die benötigten Bestandteile
  werden hier eingebunden

#### `src/utils/schema/lib/tei_stylesheets`

Die Stylesheets der TEI werden als git submodule eingebunden. Um die Version der Stylesheets und 
damit auch die zugrunde liegende Version der TEI-Richtlinien zu aktualisieren kann man wie folgt
vorgehen:
git submodule set-branch -b <name-des-releases> utils/schema/lib/tei_stylesheets
git submodule sync
git submodule update --init --remote utils/schema/lib/tei_stylesheets

### Technisches Setup

#### Verwendete Software / Technologien

- [jing](https://github.com/relaxng/jing-trang)
- [mkdocs](https://www.mkdocs.org)
- [poetry](https://python-poetry.org)
- [pre-commit](https://pre-commit.com)
- [pydantic](https://pydantic.dev)
- [pytest](https://docs.pytest.org/en/7.1.x/how-to/writing_plugins.html)
- [saxonche](https://pypi.org/project/saxonche/)
- [TEI ODD](https://tei-c.org/guidelines/customization/getting-started-with-p5-odds/)
- [TEI Stylesheets](https://github.com/TEIC/Stylesheets)

#### Einrichtung / Anforderungen an die Umgebung

Das Repository wird regulär über `git clone` ausgecheckt. Für die vollständige Funktionalität
müssen dann noch die Git-Submodule initialisiert werden:

```sh
git submodule update --init --recursive
```

Für die Kompilierung des Schemas sowie die Ausführung der Tests ist es erforderlich, dass eine
`JAVA`-Laufzeitumgebung sowie `Python` in Version 3.11 auf dem System installiert ist. Ferner ist
es erforderlich, dass der Python-Paketmanager `poetry` installiert ist.

Alle weiteren Abhängigkeiten können dann über folgenden Befehl install werden

```sh
sh ./Taskfile install
```

Wiederholt ausgeführte Aufgaben (bspw. Ausführung der Tests) sind im sog. [Taskfile](Taskfile)
gebündelt. Für die einfachere Benutzung empfiehlt es sich in der lokalen Shell-Konfigurationen
einen Alias für das Taskfile nach dem Schema `alias run=./Taskfile` einzurichten, dann lassen
sich die diversen Aufgaben nach folgendem Muster ausführen:

```sh
run test
```

Weitere Parameter (bspw. `-s` um print-Statement immer anzuzeigen) können einfach übergeben werden:

```sh
run test -s
```

### Anpassung

#### Anpassung von Übersetzungen

Das Schema ist in vier verschiedene Sprachen übersetzt: de, fr (sowie z.T. en und it)

Beschreibungen von Elementen werden i.d.R. in Deutsch, Englisch und Franzözisch verfasst. Die
Spezifikation eines Element (siehe [/src/elements](/src/elements)) sollte immer ein Element `<desc/>` je
Sprache enthalten. Für das Element `<cell/>` sieht das bspw. so aus:

```xml
<desc xml:lang="de" versionDate="2023-03-03">Auszeichnung von Tabellenzellen.</desc>
<desc xml:lang="en" versionDate="2023-03-03">Table cell mark-up.</desc>
<desc xml:lang="fr" versionDate="2023-03-03">Balisage des cellules de tableau.</desc>
```

Neben der Sprache sollte das Attribut `@versionDate` verwendet werden.

Beschreibungen von Attributwerten werden in der z.T. in der digitalen Edition verwendet und müssen
in diesen Fällen **immer** in allen vier Sprachen angelegt werden. Dies kann folgendermaßen
aussehen:

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

Die im Schema festgelegten Regeln werden automatisch mit `pytest` überprüft. Hierfür müssen
Testfälle definiert werden. Tests werden im Unterordner [test](/test) erstellt. Es wird zwischen
Tests, die allgemeine Bedingungen des Schema prüfen, und elementspezifischen Tests unterschieden.
Allgemeine Tests befinden sich gemeinsam mit den Konfigurationsdateien (`conftest.py`) auf der
obersten Ebene. Elementspezifische Tests befinden sich in [test/element](/test/elements/). Nach Möglichkeit
sollten immer mehrere Fälle je Test überprüft werden -- siehe hierzu
[Parametrizing fixtures and test functions](https://docs.pytest.org/en/6.2.x/parametrize.html).

Im Testfile eines Elements müssen zunächst die benötigten Module importiert werden.

```python
import pytest
from ssrq_cli.validate.xml import RNGJingValidator

from main import Schema

from ..conftest import SimpleTEIWriter
```

Anschließend können die Tests erstellt werden. Hierbei wird zwischen Tests zum Prüfen von
RELAXNG- und Schematron-Regeln unterschieden (siehe bspw. [test_idno.py](/test/elements/test_idno.py)). Die Testdefinition
ist dabei weitestgehend an der Triple-A-Rule (Arrange-Act-Assert) orientiert und folgt
typischerweise folgendem Muster:

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

    # ACT & ASSERT innerhalb der generischen Funktion `test_element_with_rng`
    test_element_with_rng("text", name, markup, result, False)
```

Sollen nur die Tests eines Elements ausgeführt werden, dann kann dazu folgender Befehl
verwendet werden:

```sh
run test tests/src/schema/elements/test_cell.py
```

#### Links zwischen Bestandteilen des Schemas und der (übrigen) Dokuseite

Aus dem Schema wird statisch eine Dokumentationsseite erzeugt (siehe oben). Einige Bestandteile
dieser Seite liegen statisch als `.md`-Dateien vor. Verknüpfungen zwischen Schema und diesen
Einzeldateien (oder umgekehrt) können über direkten Verweis auf die jeweilige Datei vorgenommen
werden.

Aus dem Schema heraus:

```xml
<ref target="print.md"
````

Oder aus einer Markdown-Datei auf ein Element:

```md
Der Tag [TEI][tei.de.md]
```

Die relative Pfaden (von a zu b) werden während des Build-Prozesses automatisch aufgelöst und
müssen **nicht** händisch nachgeführt werden.

### Schema erzeugen

#### Erzeugung einer neuen Version und Upload

Die Version eines Schemas ist je Inhaltstyp in der Datei `pyproject.toml` festgelegt. Sieh
hierzu den Abschnitt [Versionierung](#versionierung). Der Befehl

```sh
run compile
```

erzeugt die jeweiligen Schemadateien. Je Inhaltstyp werden eine `.odd` sowie eine `.rng` im
Ordner `/build` gespeichert.

#### Erzeugung der Dokumentation

Die Dokumentation für das Schema zur Validierung der Transkriptionen der ‚Stücke‘
(der Quelldokumente) wird aus dem ODD selbst erzeugt. Mithilfe des Dokumentations-Frameworks
[mkdocs](https://www.mkdocs.org) wird eine statische HTML-Seite erzeugt. Diese beinhaltet sowohl die Dokumentation
der einzelnen Tags als auch erläuternde Texte zu philologischen Grundlagenentscheidungen.

##### Befehle

- `run serve-docs`: Erzeugt die Dokumentation und startet zugleich einen Webserver (gedacht 
  für die lokale Entwicklung)
- `run build-docs`: Generiert die statische Dokumentationsseite. Das Ergebnis wird im Ordner
  `/site` abgelegt.

##### Datei- / Ordnerstruktur

Die Quelldateien für die Dokumentation sind einerseits die einzelnen Elementdefinitionen, diese
befinden sich `/src/elements` und andererseits spezifische Dateien für die Dokuseite:

- `mkdocs.yml`: Konfigurationsdatei für `mkdocs`; enthält ebenso Übersetzungen für die Navigation
- `utils/docs/odd2md.py`: Python-Skript zur Umwandlung der ODD-Datei in einzelne Markdown-Dateien 
   je Element (Quelle ist ein kompiliertes ODD)
- `utils/docs/doc_hooks.py`: Hook (‚Event-Skript‘), welches von `mkdocs` beim Start aufgerufen 
   wird – der Hook bindet wiederum `odd2md.py` ein
- `src/docs`: grundlegende Quelldateien für die Dokuseite
  - `index.md`: Startseite (das Kürzel `.de` oder `.fr` verweist auf die jeweilige Sprachversion)
  - `assets`: CSS, Bilddateien usw.
  - `base`: Markdowndateien mit statischen Beschreibungstexten (bspw. Datierungsrichtlinien)
  - `elements`: leerer Ordner, in welchen die Markdowndateien je Element temporär gespeichert werden
  - `translations`: Übersetzungen für Bestandteile des UIs / des Inhalts

## Autor:innen

- [Bastian Politycki](https://github.com/Bpolitycki) – Swiss Law Sources
- [Christian Sonder](https://www.ssrq-sds-fds.ch/en/about-us/organisation/mitarbeitende/) – Swiss Law Sources
- [Pascale Sutter](https://www.ssrq-sds-fds.ch/en/about-us/organisation/mitarbeitende/) – Swiss Law Sources

## Lizenzierung

Siehe [LICENSE](./LICENSE).
