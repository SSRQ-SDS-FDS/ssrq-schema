---
title: Startseite
---

# Transkriptionsrichtlinien und Dokumentation

![SSRQ Logo](ssrq-logo.svg)

## Hintergrund

Aufgrund des Medienwandels und der neuen Möglichkeiten im digitalen Zeitalter
werden die Editionen der Rechtsquellenstiftung des Schweizerischen
Juristenvereins sowohl in methodischer Hinsicht als auch in der Darstellung
angepasst.[^1]

Dazu setzt die Rechtsquellenstiftung auf den Einsatz der Auszeichnungssprache
Extensible Markup Language (XML) nach den Empfehlungen der Text Encoding
Initiative (TEI).

## Aufbau

Die folgenden Seiten sind eine Einführung in die Arbeitsweise der digitalen
Editionen der Rechtsquellenstiftung. Die Informationen in dieser Dokumentation
fungieren als «editorischer Bericht» und beschreiben sowohl philologische als
auch informationstechnologische Grundlagenentscheidungen.

Dazu zählen neben den allgemeinen Richtlinien zur Transkription und Datierung
der Texte auch ausführliche Erläuterungen zu allen im TEI-XML verwendeten
Elementen.

## Technologie und Standardisierung

### XML

> Die Extensible Markup Language (engl. für «erweiterbare
> Auszeichnungssprache»), abgekürzt XML, ist eine Auszeichnungssprache zur
> Darstellung hierarchisch strukturierter Daten in Form von Textdaten. XML
> wird u. a. für den Austausch von Daten zwischen Computersystemen eingesetzt,
> speziell über das Internet.[^2]

Der Fokus liegt bei XML auf einer strukturierten Erfassung der Daten und nicht
auf ihrer graﬁschen Präsentation, wie dies etwa bei gängigen Programmen zur
Textverarbeitung der Fall ist.

Aufgrund seiner Erweiterbarkeit hat es in XML unendlich viele Möglichkeiten,
die Daten zu erfassen und weiterzuverarbeiten.

Daher folgt die Rechtsquellenstiftung den Empfehlungen der international
anerkannten Text Encoding Initiative (TEI) zur Kodierung ihrer digitalen
Editionen.

### TEI

> «The Text Encoding Initiative» (TEI) is a consortium which collectively
> develops and maintains a standard for the representation of texts in digital
> form.
> Its chief deliverable is a set of Guidelines which specify encoding methods
> for machine-readable texts, chiefly in the humanities, social sciences and
> linguistics.[^3]

Der Vorteil der Empfehlungen der TEI ist, dass es für die meisten Phänomene,
welche bei der Edition historischer Texte auftreten, Definitionen und
Vorschläge zur Kodierung hat.
Dadurch wird erreicht, dass einzelne Editionsprojekte diese Phänomene nicht
mühsam selbst modellieren müssen und dass durch das Anwenden der Empfehlungen
viele Editionen miteinander vergleichbar und untereinander austauschbar werden.

Gleichzeitig bedeutet dies jedoch, dass die Empfehlungen der TEI sehr weit
gefasst sind, damit sie in möglichst vielen Projekten aus unterschiedlichen
Wissenschaften eingesetzt werden können.

Aus diesem Grund entwickelt die Rechtsquellenstiftung ein für ihre Zwecke
angepasstes TEI-XML-Schema,[^4] das nicht nur den Besonderheiten der
vielfältigen Quellentexte, sondern auch der Tradition der Sammlung
Schweizerischer Rechtsquellen gleichermassen Rechnung trägt.

[^1]:
    Vgl. Sahle, Patrick: Projektskizze zur elektronischen Bearbeitung und
    digitalen Edition von Zürcher Rechtsquellen (eRQZH) im Rahmen des
    Editionsunternehmens «Sammlung Schweizerischer Rechtsquellen (SSRQ)»,
    namens des Schweizerischen Juristenvereins herausgegeben von dessen
    Rechtsquellenstiftung. (Unpublizierte Projektskizze. Endfassung vom 9.
    September 2008.)
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
