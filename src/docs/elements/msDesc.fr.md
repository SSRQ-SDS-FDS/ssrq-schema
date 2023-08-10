---
title: msDesc
---



# `<msDesc/>` (description d'un manuscrit)

## Description

Décrit la pièce de source éditée avec le lieu de conservation, le matériau, la mise en page, le scribe, le sceau et la bibliographie sur la littérature secondaire (métadonnées). 

## Modèle de contenu

- **core**: [head](head.md)
- **msdescription**: [additional](additional.md) [history](history.md) [msContents](msContents.md) [msIdentifier](msIdentifier.md) [physDesc](physDesc.md)

## Exemples

### Exemple 1

Exemple de description textuelle d'un témoin

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <msDesc>
        <msIdentifier>
            <idno source="https://suche.staatsarchiv.djiktzh.ch/detail.aspx?ID=3737536" xml:lang="de">StAZH B III 2, S. 353-355
            </idno>
            <repository xml:lang="de">Staatsarchiv Zürich</repository>
        </msIdentifier>
        <head>Ordnung der Stadt Zürich für die Ausrichtung von Witwen sowie Erläuterung
            betreffend Erbrecht von Schwiegertöchtern
        </head>
        <msContents>
            <summary>
                <p xml:lang="de">Bürgermeister und Rat regeln die Auszahlung nachfolgend genannter
                    Erbteile an Ehefrauen, deren Männer verstorben sind: die Aussteuer, die
                    sie in Form von Fahrhabe in die Ehe eingebracht haben (1); die vom
                    Ehemann erhaltene Morgengabe (2; 3); das Eherecht sowie ein Drittel des
                    gemeinsamen Vermögens, sofern sie ihre Erbschaft anzutreten wünschen
                    (4); die Aussteuer, die in Form von liegenden Gütern in die Ehe
                    eingebracht wurde (5); die Anteile von Ehefrauen, deren Männer
                    verstorben sind, am Gut ihrer Schwiegereltern (6).
                </p>
            </summary>
            <msItem>
                <textLang xml:lang="de" />
            </msItem>
        </msContents>
        <physDesc>
            <objectDesc form="original">
                <supportDesc>
                    <support>
                        <material type="paper" />
                    </support>
                    <extent>
                        <dimensions type="leaves">
                            <height unit="cm" quantity="33.0" />
                            <width unit="cm" quantity="24.0" />
                        </dimensions>
                    </extent>
                </supportDesc>
            </objectDesc>
        </physDesc>
        <history>
            <origin>
                <origDate calendar="julian" from-custom="1498-01-01" to-custom="1522-12-31">1498-1522</origDate>
            </origin>
        </history>
        <additional>
            <listBibl type="literature">
                <bibl>
                    <ref target="http://permalink.snl.ch/bib/chbsg000137461">Ott, Rechtsquellen</ref>,
                    Teil 1, S. 95, Nr. 258 (Dipl. Nr. 168)
                </bibl>
            </listBibl>
        </additional>
    </msDesc>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.1. Overview](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msov)