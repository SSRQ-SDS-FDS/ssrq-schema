# Abréviations

## Règles générales

Les abréviations fréquentes et qui reviennent dans un ou dans plusieurs documents 
sont laissées telles quelles. Voir la [liste des abréviations](abbreviation-list.fr.md)

Les abréviations sont balisées avec [`<abbr>`](abbr.fr.md) et intégrées dans 
un répertoire d’abréviations, dans lequel elles sont développées. 
Aucun point d’abréviation n’est utilisé, car les abréviations sont déjà 
signalées comme telles avec la balise.

Les sigles (Kürzel) sont systématiquement laissés 
tels quels et balisés avec [`<abbr>`](abbr.fr.md).

## Développement des abréviations

=== "Règles générales"

    Dans l’édition imprimée, les développements d’abréviations pour lesquels 
    subsiste un doute ont été mises entre crochets ; dans l’édition numérique, 
    ils sont balisés avec 
    [`<choice>`](choice.fr.md) en combinaison avec [`<abbr>`](abbr.fr.md) et
    [`<expan>`](expan.fr.md).
    
    Les abréviations présentes dans l’original sont développées, 
    si c’est possible et pertinent. 

    Les habitudes orthographiques du scribe sont respectées sans balisage particulier. 
    Certaines abréviations (par ex. « Ao » = « anno »), ainsi que les terminaisons, 
    sont résolues sans mention explicite (voir [normalisation](normalization.fr.md)).
    
    Dans certains cas ambigus, il est préférable de reproduire l’abréviation 
    telle quelle, sans la développer.

    Exemples :  
    fr. « sr » = « sieur » ou « seigneur » ?  
    fr. « monsr » = « monsieur » ou « monseigneur » ?  
    fr. « me » = « maître ou « messire » ?

    Pour développer les abréviations, il convient de privilégier autant que possible 
    les formes attestées sans ambiguïté dans d'autres parties du texte édité. 
    À défaut, on utilisera la forme classique (notamment en latin). 
    Dans tous les cas, il faut rester cohérent.

=== "Textes latins"

    Les abréviations latines courantes sont résolues sans mention particulière, 
    sauf s’il existe un doute sur la résolution correcte.

    La résolution se fait sur la base d’un dictionnaire de latin médiéval, 
    sauf en cas de pratique différente du scribe.

## Abréviations des mesures et monnaies

Les abréviations de mesures et de monnaies ne sont pas résolues 
(sauf dans les paratextes éditoriaux tels que les commentaires ou notes) 
et apparaissent dans la liste des abréviations.

Les [caractères spéciaux](special.fr.md) correspondants sont utilisés.

Les unités monétaires de mesure et de poids sont balisées avec [`<measure>`](measure.fr.md)
et, le cas échéant, avec [`<measureGrp>`](measureGrp.fr.md).
