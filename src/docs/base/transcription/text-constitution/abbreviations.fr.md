# Abréviations

## Règles générales

Les abréviations typiques qui reviennent dans le même document ou dans plusieurs
documents sont laissées. Voir la [liste des abréviations](abbreviation-list.fr.md)

Les abréviations sont étiquetées avec [`<abbr>`](abbr.fr.md) et incluses dans
un répertoire d’abréviations, où la résolution a lieu.
Aucun point d’abréviation n’est utilisé, car les abréviations sont déjà marquées 
comme telles dans le balisage.

Les abréviations sont systématiquement laissées sous forme d’abréviations et
marquées de [`<abbr>`](abbr.fr.md).

## Dissolution des abréviations

=== "Règles générales"

    Dans l’édition analogique, les résolutions ont été mises entre crochets en cas de
    doute ; dans l’édition numérique, elles sont étiquetées avec
    [`<choice>`](choice.fr.md) en combinaison avec [`<abbr>`](abbr.fr.md) et
    [`<expan>`](expan.fr.md).
    
    Les abréviations dans le modèle de texte sont résolues si possible et raisonnable.

    Les habitudes orthographiques du scribe sont prises en compte
    sans marquage particulier.
    Certaines abréviations telles que « Ao » = « anno » et les terminaisons
    sont résolues silencieusement (voir [normalisation](normalization.fr.md)).
    
    Dans certains cas ambigus, il est préférable de reproduire un
    mot abrégé tel quel.

    Exemples :  
    fr. « sr » = « sieur » ou « seigneur » ?  
    fr. « monsr » = « monsieur » ou « monseigneur » ?  
    fr. « me » = « maître ou « messire » ?

    Bei der Auflösung von Abkürzungen sollte so weit wie möglich auf
    Schreibweisen zurückgegriffen werden, die in anderen Teilen des
    bearbeiteten Textes eindeutig belegt sind, ansonsten ist die
    klassische Form zu bevorzugen (insbesondere für Latein).
    In jedem Fall sollte man konsequent bleiben.

=== "Textes latins"

    Les abréviations latines courantes sont résolues silencieusement,
    sauf s’il existe un doute sur la résolution correcte.

    La résolution est conforme au dictionnaire moyen latin, à moins que
    le scribe ne pratique différemment.

## Abréviations des noms de mesures et de pièces de monnaie

Les abréviations de mesures et de noms de pièces ne sont résolues que dans
les paratextes éditoriaux (commentaires, notes) et apparaissent dans la
liste des abréviations.

Il y aura les appropriés [caractères spéciaux](special.fr.md) utilisés.

Les devises, mesures et poids sont étiquetés avec [`<measure>`](measure.fr.md)
et, le cas échéant, avec [`<measureGrp>`](measureGrp.fr.md).
