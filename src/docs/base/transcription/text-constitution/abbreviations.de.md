# Abkürzungen

## Allgemeine Regeln

Typische, im selben Schriftstück oder in mehreren Schriftstücken 
wiederkehrende Abkürzungen werden stehen gelassen. Vgl. die 
[Liste von Abkürzungen](abbreviation-list.de.md)

Abkürzungen werden mit [`<abbr>`](abbr.de.md) getaggt und in ein Abkürzungsverzeichnis 
aufgenommen, wo die Auflösung erfolgt.
Es werden keine Kürzungspunkte verwendet, da die Abkürzungen durch die 
Auszeichnung bereits als solche gekennzeichnet sind.

Kürzel werden konsequent als Kürzel belassen und mit [`<abbr>`](abbr.de.md) ausgezeichnet.

## Auflösen von Abkürzungen

=== "Allgemeine Regeln"

    Auflösungen wurden in der analogen Edition in Zweifelsfällen in eckige
    Klammern gesetzt, in der digitalen Edition werden sie mit
    [`<choice>`](choice.de.md) in Kombination mit [`<abbr>`](abbr.de.md) und
    [`<expan>`](expan.de.md) getaggt.
    
    Abkürzungen in der Textvorlage werden aufgelöst, wenn es möglich und
    sinnvoll ist.

    Orthographische Gepflogenheiten des Schreibers werden ohne besondere
    Kennzeichnung berücksichtigt.
    Einige Abkürzungen wie z. B. «Ao» = «anno» sowie Endungen werden
    stillschweigend aufgelöst 
    (vgl. [Normalisierung](normalization.de.md)).
    
    In einigen mehrdeutigen Fällen ist es besser, ein abgekürztes Wort
    unverändert wiederzugeben.

    Beispiele:  
    frz. «sr» = «sieur» oder «seigneur»?  
    frz. «monsr» = «monsieur» oder «monseigneur»?  
    frz. «me» = «maître oder «messire»?

    Bei der Auflösung von Abkürzungen sollte so weit wie möglich auf
    Schreibweisen zurückgegriffen werden, die in anderen Teilen des
    bearbeiteten Textes eindeutig belegt sind, ansonsten ist die
    klassische Form zu bevorzugen (insbesondere für Latein).
    In jedem Fall sollte man konsequent bleiben.

=== "Lateinische Texte"

    Die gebräuchlichen lateinischen Abkürzungen werden stillschweigend
    aufgelöst, sofern nicht Zweifel an der korrekten Auflösung bestehen.

    Die Auflösung erfolgt gemäss mittellateinischem Wörterbuch, ausser
    bei abweichender Praxis des Schreibers.

## Abkürzungen von Mass- und Münzbezeichnungen

Abkürzungen von Mass- und Münzbezeichnungen werden ausser in editorischen
Paratexten (Kommentaren, Anmerkungen) nicht aufgelöst und erscheinen im 
Abkürzungsverzeichnis. 
Es werden die entsprechenden
[Sonderzeichen](special.de.md#code-tabelle-fur-sonderzeichen) verwendet.

Währungen, Masse und Gewichte werden mit [`<measure>`](measure.de.md) und
ggf. mit [`<measureGrp>`](measureGrp.de.md) getaggt.
