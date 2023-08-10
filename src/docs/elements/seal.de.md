---
title: seal
---



# `<seal/>`

## Beschreibung

Beschreibt ein Siegel.

## Erläuterung

Die Beschreibung der Siegel erfolgt von links nach rechts. Vgl. hierzu auch die Siegelbeschreibung unter Metadaten#Siegel. Der Siegler wird, wenn es sich um eine Person handelt, mit [`<persName/>`](persName.md)  und dem Attribut[@role](#role)  =`sigillant`  oder, wenn es sich um eine Institution handelt, mit [`<orgName/>`](orgName.md)  und dem gleichen Attribut erfasst. Wenn die Namen der Siegler auf der Plica oder dem Pergamentstreifen stehen, sollte innerhalb von[`<persName/>`](persName.md)  ein[`<orig/>`](orig.md)  den handschriftlichen Namen umfassen.

Bei unsicheren Siegelidentifikationen, wenn z. B. der Siegler in der Urkunde nicht genannt ist, werden kein [`<orgName/>`](orgName.md)  oder[`<persName/>`](persName.md)  angegeben. Wenn bei mehreren Siegeln die Siegler nicht sicher zugeordnet werden können, wird die Siegelidentifikation offen gelassen.

Die Siegel werden mit [@n](#n)  durchnummeriert. Wünschenswert wäre, wenn der Edition nicht nur ein Faksimile des Textes, sondern auch ein Foto des Siegels inkl. Masstab beigefügt würde. Wäre dies bei allen Siegeln der Fall, könnte auf[@extent](#extent)  verzichtet werden.

L. S. = Locus sigilli wird mit [`<figure/>`](figure.md)  erfasst. Wenn eine Urkunde ohne Siegel ausgestellt wurde, wird auch kein Siegel erfasst. Je nach Bedarf kann ein Kommentar zu den Siegeln verfasst werden.

Wichtig ist der Vergleich der Siegelankündigung im Text und die Besiegelung selber. 

- Haben alle angekündigten Siegler ihr Siegel an der Urkunde angebracht?
- Hängt ein Siegel eines nicht angekündigten Sieglers?
- Wurde evtl. ein Siegel gefälscht oder später angebracht?[@condition](#condition)  mit`absent`  anzumerken. Zudem ist in einer Anmerkung ([`<note/>`](note.md) ) zu beschreiben, weshalb wohl das Siegel fehlt bzw. weshalb die Urkunde unbesiegelt blieb.

Zu den Kaisersiegeln: Posse Otto: Die Siegel der deutschen Kaiser und Könige von 751-1806 und 1871-1913, 5 Bde. Dresden 1909–1913 (http://de.wikisource.org/wiki/Die_Siegel_der_Deutschen_Kaiser_und_K%C3%B6nige). 

## Inhaltsmodell

- **core**: [p](p.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md)

## Attribute

### @attachment

Beschreibt die Befestigungsart des Siegels

*Mögliche Werte*

- applied – *aufgedrückt*
- sealed_on_a_cord – *angehängt an einer Kordel*
- sealed_on_a_lace – *angehängt an Schnur*
- sealed_on_a_leather_tag – *angehängt an Lederstreifen*
- sealed_on_a_parchment_tag – *angehängt an Pergamentstreifen*
- sealed_on_a_ribbon – *angehängt an Band*
- sealed_on_laces – *angehängt an Fäden*
- slit – *nur Siegelschlitz vorhanden*
- wrapping-tie – *zum Verschluss aufgedrückt*

### @condition

Beschreibt den Erhaltungszustand und Schäden eines Siegels. 

*Mögliche Werte*

- absent – *fehlt*
- bound_in_linen – *in Leinensäckchen*
- chamfered – *bestossen*
- damaged – *beschädigt*
- ex_and_enclosed – *ab und beiliegend*
- fragmentary – *bruchstückhaft*
- in_a_box – *in verschlossener Holzkapsel*
- in_a_capsule – *in verschlossener Metallkapsel*
- polished – *abgeschliffen*
- well-preserved – *gut erhalten*

### @facs

Ordnet eine Textseite einem Faksimile oder einem faksimilierten Ausschnitt zu. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `[A-Za-z_\-\.0-9]+([1-9]|[rv])`

### @material

Beschreibt das Material eines Siegels

*Mögliche Werte*

- bulle – *Bulle*
- papered_seal – *Papierwachssiegel*
- sealing_wax – *Siegellack*
- wafer – *Oblatensiegel*
- wax – *Wachs*
- wax_in_a_box – *Wachs in Holzkapsel*
- wax_in_a_capsule – *Wachs in Metallkapsel*
- wax_with_margin – *Wachs in Schüssel*

### @n

Fortlaufende Zählung der Siegel von links nach rechts (anhand der Siegelschlitze bzw. der tatsächlich vorhandenen Siegel) 

*Mögliche Werte*

- Zahl

### @place

Beschreibt den Anbringungsort des Siegels

*Mögliche Werte*

- end – *am Ende der Urkunde*
- overleaf – *auf der anderen Seite des Blattes*

### @shape

Beschreibt die Form des Siegels

*Mögliche Werte*

- heart-shaped – *herzförmig*
- octangular – *achteckig*
- oval – *spitzoval*
- peltade – *schildförmig*
- round – *rund*
- triangular – *dreieckig*

## Beispiele

### Beispiel 1

Beispielhafte Erfassung eines Siegels

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <seal n="1" material="wax" shape="round" attachment="sealed_on_a_parchment_tag" condition="damaged">
        <persName role="sigillant" ref="per000271">Johannes von Belmont</persName>
    </seal>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [10.7.3.2. Seals](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msphse)