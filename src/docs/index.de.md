---
title: Startseite
---

# Transkriptionsrichtlinien und Dokumentation

![SSRQ Logo](ssrq-logo.svg)

Willkommen auf der Dokumentationsseite der Sammlung Schweizerischer Rechtsquellen (SSRQ)
der Rechtsquellenstiftung des Schweizerischen Juristenvereins.
Auf dieser Seite finden Sie eine ausführliche Beschreibung der philologischen Grundlagen,
auf denen die Editionseinheiten der SSRQ basieren, sowie eine Dokumentation des verwendeten 
TEI-XML-Schemas in Form eine «Tag-Bibliothek». Diese Seiten können daher als eine Einführung 
in die Arbeitsweise der digitalen Editionen der Rechtsquellenstiftung gesehen werden und 
fungieren zugleich als «editorischer Bericht».

- Die digitale Edition der SSRQ mit allen TEI-XML-Dateien finden Sie in unserem Editionsportal 
[Editio](https://editio.ssrq-online.ch/).
- Die [retrodigitalisierte Sammlung](https://www.ssrq-sds-fds.ch/online/cantons.html) erschliesst
die analog erschienenen Bände als OCR-PDF.
- Die [Projektwebseite](https://www.ssrq-sds-fds.ch/home/) informiert über die
aktuell laufenden Editionsprojekte und gibt eine Übersicht über die Geschichte der
Sammlung seit den 1890er Jahren.

## Technologie und Standardisierung

Aufgrund des Medienwandels und der Möglichkeiten des digitalen Zeitalters werden die Editionen der 
SSRQ mithilfe der Extensible Markup Language (XML) nach den Empfehlungen der Text Encoding
Initiative (TEI) umgesetzt.

## XML

> Die Extensible Markup Language (engl. für «erweiterbare
> Auszeichnungssprache»), abgekürzt XML, ist eine Auszeichnungssprache zur
> Darstellung hierarchisch strukturierter Daten in Form von Textdaten. XML
> wird u. a. für den Austausch von Daten zwischen Computersystemen eingesetzt,
> speziell über das Internet.[^2]

Der Fokus liegt bei XML auf einer strukturierten Erfassung von Daten und nicht
auf ihrer graﬁschen Präsentation, wie dies etwa bei gängigen Office-Programmen zur
Textverarbeitung der Fall ist.

Durch seine Erweiterbarkeit bietet XML unendlich viele Möglichkeiten,
die Daten zu erfassen und weiterzuverarbeiten.

## TEI

Daher folgt die Rechtsquellenstiftung den Empfehlungen der international
anerkannten Text Encoding Initiative (TEI) zur Kodierung ihrer digitalen
Editionen.

> «The Text Encoding Initiative» (TEI) is a consortium which collectively
> develops and maintains a standard for the representation of texts in digital
> form.
> Its chief deliverable is a set of Guidelines which specify encoding methods
> for machine-readable texts, chiefly in the humanities, social sciences and
> linguistics.[^3]

Der Vorteil der Empfehlungen der TEI ist, dass sie für die meisten Phänomene,
welche bei der Edition historischer Texte auftreten, Definitionen und
Vorschläge zur Kodierung bieten.

Dadurch wird einerseits erreicht, dass einzelne Editionsprojekte diese Phänomene
nicht mühsam selbst modellieren müssen, und andererseits werden durch das Anwenden 
der Empfehlungen viele Editionen miteinander vergleichbar. 

Diese Standardisierung trägt dazu bei, dass die erstellten Daten nicht nur für die
Öffentlichkeit, sondern auch für andere wissenschaftliche Zwecke leicht zugänglich 
sind.

Gleichzeitig bedeutet dies jedoch, dass die Empfehlungen der TEI sehr weit
gefasst sind, damit sie in möglichst vielen Projekten aus unterschiedlichen
Wissenschaften eingesetzt werden können.

## Schema

Aus diesem Grund wurden die Richtlinien der TEI für die Zwecke der SSRQ in Form 
eines eigenen, fortlaufend entwickelten Schemas[^4] angepasst, welches nicht nur 
den Besonderheiten der vielfältigen Quellentexte, sondern auch der Tradition der 
Sammlung gleichermassen Rechnung trägt.

Das [vollständige, kompilierte Schema](https://schema.ssrq-sds-fds.ch/latest/TEI_Schema.rng) 
kann frei heruntergeladen und weitergenutzt werden. Seine Entwicklung erfolgt öffentlich 
einsehbar auf der Plattform [GitHub](https://github.com/SSRQ-SDS-FDS/ssrq-schema), es wird nachhaltig auf 
[Zenodo](https://zenodo.org/records/13379935) publiziert.

[^2]:
    Zit. nach Wikipedia: [Extensible Markup Language]
    (https://de.wikipedia.org/wiki/Extensible_Markup_Language).
    Vgl. auch die Internetseite des World Wide Web Consortium (W3C) zu
    [XML](https://www.w3.org/TR/xml/).
[^3]:
    Zit. nach [TEI](http://www.tei-c.org/index.xml).
[^4]:
    Unter einem XML-Schema versteht man die formale Beschreibung einer Menge
    von XML-Dokumenten mithilfe einer Schemasprache. Eine solche Beschreibung
    ermöglicht die Validierung eines XML-Dokuments (d. h. eine Überprüfung, ob
    ein XML-Dokument so aufgebaut ist, wie es die Regeln des Schemas vorsehen)
    und stellt so die Einheitlichkeit der XML-Dokumente innerhalb einer Edition
    sicher.