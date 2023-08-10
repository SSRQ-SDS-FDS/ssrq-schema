---
title: docImprint
---



# `<docImprint/>` (imprimer)

## Description

Contient, pour les imprimés, le lieu d'impression ([`<pubPlace/>`](pubPlace.md) ) et le nom de l'imprimerie ([`<publisher/>`](publisher.md) ).

## Modèle de contenu

- **core**: [pubPlace](pubPlace.md) [pubPlace](pubPlace.md) [publisher](publisher.md) [publisher](publisher.md)

## Exemples

### Exemple 1

Exemple d'empreinte avec lieu d'impression et imprimeur

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <docImprint>
        <pubPlace>Zürich</pubPlace>
        <publisher>Johann Heinrich Hamberger</publisher>
    </docImprint>
</egXML>
               
```

### Exemple 2

Exemple d'empreinte avec plusieurs lieux d'impression

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <docImprint>
        <pubPlace>Zürich</pubPlace>
        <pubPlace>Bern</pubPlace>
    </docImprint>
</egXML>
               
```

### Exemple 3

Exemple d'empreinte avec une imprimerie

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <docImprint>
        <publisher>Johann Heinrich Hamberger</publisher>
    </docImprint>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [4.6. Title Pages](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DSTITL)