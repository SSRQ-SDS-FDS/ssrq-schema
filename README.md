# SSRQ-Schema

Dieses Repository beinhaltet Quellcode und sonstige Dateien im Zusammenhang mit dem XML-Schema der Sammlung der Schweizerischen Rechtsquellen.

- [SSRQ-Schema](#ssrq-schema)
  - [Initiale Zielsetzung der Entwicklung](#initiale-zielsetzung-der-entwicklung)
  - [To-Dos](#to-dos)
    - [Inhaltlich](#inhaltlich)
    - [Technische Umsetzung](#technische-umsetzung)
  - [Dokumentation](#dokumentation)
    - [Versionierung](#versionierung)
    - [Aufbau](#aufbau)
    - [Was ist wo?](#was-ist-wo)
    - [Technisches Setup](#technisches-setup)
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

## To-Dos

### Inhaltlich

### Technische Umsetzung

## Dokumentation

### Versionierung

Die Versionierung des Schemas erfolgt gemäß Semantic Versioning. Dies erlaubt die eindeutige Zuordnung eines bestimmten Datenmodells zu einer bestimmten Version. Die Grundregel lautet:

```
MAJOR.MINOR.PATCH
```

Die Versionsnumer wird als Tag in der Git-History hinterlegt und ist zudem in der Datei `pyproject.toml` in der Tabelle `ssrq.schema.meta` hinterlegt. Die kompilierten Versionen des Schemas folgen dem Muster `tei-ssrq-schema-version.(rng|odd)` und verwenden die in dieser Projektkonfiguration hinterlegte Versionnumer.

### Aufbau

### Was ist wo?

ToDo

### Technisches Setup

**Verwendete Software / Technologien**:

- [TEI ODD](https://tei-c.org/guidelines/customization/getting-started-with-p5-odds/)
- [TEI Stylesheets](https://github.com/TEIC/Stylesheets)
- [pytest](https://docs.pytest.org/en/7.1.x/how-to/writing_plugins.html)
- [saxonche](https://pypi.org/project/saxonche/)
- [xmlformatter](https://pypi.org/project/xmlformatter/) (vakant!)
- [make](https://de.wikipedia.org/wiki/Make)
- ...

ToDo: Erläuterung Einrichtung, Entwicklung / Ausführen von Tests und Ausführung

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
