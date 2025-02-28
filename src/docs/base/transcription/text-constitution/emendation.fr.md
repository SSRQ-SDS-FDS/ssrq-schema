# Interventions dans le texte

## Imprimes

Les fautes d’impression claires sont corrigées avec
[`<choice>`](choice.fr.md),[`<sic>`](sic.fr.md) et [`<corr>`](corr.fr.md).

## Textes manuscrits

### Parenthèses

Les parties de texte placées entre parenthèses par le scribe sont reproduites
à l’identique sans aucune intervention.

### Lacunes

Les espaces (espaces) délibérément laissés par le scribe pour des ajouts ultérieurs
étaient marqués dans les volumes analogiques par trois ellipses sans crochets et
expliqués dans une note critique du texte, indiquant la taille de l’espace dans le texte.
Dans l’édition numérique, ils sont étiquetés avec [`<space/>`](space.fr.md).

Les points de référence avant les noms ou titres officiels sont
représentés par deux points sans parenthèses.

### Parties du texte omises

Parties de texte omises par erreur par l’auteur, p. ex. les lignes oubliées 
lors de la copie du texte ont été complétées dans l’édition analogique par
un texte de remplacement provenant d’une autre source originale ou de copie
ou par l’éditeur lui-même dans le sens d’une reproduction appropriée du texte
entre crochets.
Un commentaire était nécessaire.
Dans l’édition numérique, le texte complété est étiqueté avec
[`<suppplied>`](supplied.fr.md). 
Si nécessaire, une note peut être ajoutée avec [`<note>`](note.fr.md).

Si des ajouts sont effectués à partir d’un autre modèle (deuxieme original,
copie, etc.), référence est faite à ce témoin de texte.
Voir aussi [`<app>`](app.fr.md).

La perte de texte due à des dommages tels que des dommages causés par la souris,
de l’encre fanée, un incendie, des champignons, des déchirures, des trous, une
cassation, etc. est enregistrée avec [`<damage>`](damage.fr.md) en combinaison
avec [`<gap/>`](gap.fr.md), [`<supplied>`](supplied.fr.md) ou [`<unclear>`](unclear.fr.md).

### Répétitions

Les répétitions erronées de syllabes, de mots et de parties de phrases (Dittographies)
doivent être normalisées avec [`<choice>`](choice.fr.md) en combinaison avec
[`<sic>`](sic.fr.md) et [`<corr>`](corr.fr.md).

### Lecture incertaine

Pour les mots dont la lecture est incertaine, des variantes de lecture imaginables
ont été répertoriées dans une note critique du texte dans l’édition analogique.
Ils pourraient également être marqués de `[?]`.
Dans l’édition numérique, les lectures incertaines sont étiquetées avec
[`<unclear>`](unclear.fr.md). Si cela ne suffit pas, vous pouvez aussi prendre
une note avec [`<note>`](note.fr.md).

### Erreurs d’écriture, de langage et de style

Les erreurs d’écriture, de langue et de style ne seront pas corrigées dans le texte.
Dans l’édition analogique, ils étaient expliqués dans une note critique du texte ou
marqués d’un `[!]`.
Dans l’édition numérique, ces erreurs sont marquées par [`<sic>`](sic.fr.md) et,
si nécessaire, corrigées par [`<choice>`](choice.fr.md) avec [`<sic>`](sic.fr.md) et
[`<corr>`](corr.fr.md).

### Omissions volontaires de texte par l’éditeur

Les omissions volontaires de texte de la part de l’éditeur (copie partielle) sont
signalées par `[...]` dans l’édition analogique et par
[`<gap Reason="irrelevant"/>`](gap.fr.md) est joué.
Cela devrait être évité si possible.

Si les ajouts ultérieurs ne sont pas modifiés par rapport à l’original, mais en tant
que pièce indépendante, les parties déjà modifiées dans un original antérieur peuvent
être omises avec [`<gap/>`](gap.fr.md).
Il est fait référence au document déjà édité.
Une note dans [`<note>`](note.fr.md) ou une note plus large dans [`<back>`](back.fr.md)
est nécessaire pour que le document soit référencé.

### Traitement des interventions éditoriales du scribe

=== "Règles générales"

    En principe, un texte transcrit doit être facile à lire et à comprendre,
    même s’il repose sur un modèle qui a été révisé plusieurs fois par
    différentes mains.
    L’éditeur doit choisir une variante de texte et marquer les variantes
    restantes avec des balises.
    Une attention particulière doit être portée aux suppressions ou aux
    rasages ainsi qu’aux ajouts.

=== "Suppressions"

    De simples corrections intervenues au cours du processus de rédaction
    ne sont mentionnées que dans des cas exceptionnels.

    Les suppressions étaient marquées par `a–...–a` dans la transcription
    analogique et répertoriées dans une note critique du texte.
    Dans l’édition numérique, les suppressions sont étiquetées avec [`<del>`](del.fr.md).

    Pour les suppressions complexes et inter-hiérarchies,
    [`<delSpan/>`](delSpan.fr.md) et [`<anchor/>`](anchor.fr.md) doivent être utilisés.

    Les passages de texte devenus illisibles en raison de suppressions étaient marqués d’un
    `[...]a` dans l’édition analogique et accompagnés d’une note.
    Dans l’édition numérique, ils sont marqués de [`<del>`](del.fr.md)
    et [`<gap/>`](gap.fr.md).

    Pour les passages de texte contenant des suppressions et des ajouts en combinaison,
    [`<subst>`](subst.fr.md) doit être utilisé.

=== "Copeaux"

    Dans l’édition analogique, les copeaux étaient traités de la même manière que
    les suppressions et une note critique du texte était requise.

    Dans l’édition numérique, un copeau est marqué de [`<del rend="rubbing">`](del.fr.md).
    Si rien n’est lisible après le copeau ou même après des caresses intenses,
    [`<gap/>`](gap.fr.md) est utilisé dans [`<del>`](del.fr.md).

=== "Ajouts"

    Les ajouts de première main ou ultérieurs doivent être inclus dans le texte
    et ont été expliqués dans une note critique du texte dans l’édition analogique.
    Dans l’édition numérique, la balise [`<add>`](add.fr.md) est utilisée.
    Le lieu de l’ajout doit et la main de la zone ajoutée peuvent être enregistrés.

    Pour les ajouts complexes entre hiérarchies, [`<addSpan/>`](addSpan.fr.md) et
    [`<anchor/>`](anchor.fr.md) doivent être utilisés.
