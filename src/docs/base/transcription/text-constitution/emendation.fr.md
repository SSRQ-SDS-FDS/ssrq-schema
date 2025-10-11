# Interventions dans le texte

## Imprimés

Les fautes d’impression claires sont corrigées avec
[`<choice>`](choice.fr.md),[`<sic>`](sic.fr.md) et [`<corr>`](corr.fr.md).

## Textes manuscrits

### Parenthèses

Les passages placés entre parenthèses par le scribe sont reproduits 
à l’identique, sans intervention.

### Lacunes

Les lacunes (espaces vides) laissés délibérément libres par le scribe pour
des ajouts ultérieurs étaient marqués dans les volumes imprimés par trois
points de suspension sans parenthèses et expliqués dans une note critique,
indiquant la taille de la lacune. 
Dans l’édition numérique, elles sont balisées avec [`<space/>`](space.fr.md).

Les points de révérence (Reverenzpunkte) avant les noms ou titres officiels 
sont représentés par deux points sans parenthèses.

### Parties du texte omises

Les passages oubliés par erreur par l’auteur, p. ex. les lignes sautées 
lors de la copie d’un texte, ont été complétées dans l’édition imprimée 
à l’aide d’un texte de remplacement provenant d’une autre source originale, 
d’une copie ou par l’éditeur lui-même sous forme d’une restitution appropriée 
du texte, entre crochets. Une note était alors nécessaire. Dans l’édition 
numérique, le texte complété est balisé avec [`<supplied>`](supplied.fr.md). 
Si nécessaire, une note peut être ajoutée avec [`<note>`](note.fr.md).

Si des ajouts sont effectués à partir d’une autre source (deuxième original, 
copie, etc.), cette source est indiquée. Voir aussi [`<app>`](app.fr.md).

La perte de texte due à des détériorations tels que des morsures de souris, 
de l’encre effacée, un incendie, des moisissures, des déchirures, des trous, 
des destructions volontaires, etc., est balisée avec [`<damage>`](damage.fr.md) 
en combinaison  avec [`<gap/>`](gap.fr.md), [`<supplied>`](supplied.fr.md) ou [`<unclear>`](unclear.fr.md).

### Répétitions

Les répétitions erronées de syllabes, de mots et de parties de phrases (dittographies)
doivent être normalisées avec [`<choice>`](choice.fr.md) en combinaison avec
[`<sic>`](sic.fr.md) et [`<corr>`](corr.fr.md).

### Lecture incertaine

Pour les mots dont la lecture est incertaine, l’édition imprimée présentait dans 
une note critique différentes variantes de lecture possibles. 
Ces mots pouvaient également être accompagnés de `[?]`. 
Dans l’édition numérique, les lectures incertaines sont balisées avec
[`<unclear>`](unclear.fr.md). Si cela ne suffit pas, une note peut être ajoutée
avec [`<note>`](note.fr.md).

### Erreurs d’écriture, de langage et de style

Les erreurs d’écriture, de langue et de style ne sont pas corrigées dans le texte. 
Dans l’édition imprimée, elles étaient expliquées dans une note critique ou 
signalées par un `[!]`. 
Dans l’édition numérique, ces erreurs sont balisées avec [`<sic>`](sic.fr.md) et,
si nécessaire, corrigées par [`<choice>`](choice.fr.md) avec [`<sic>`](sic.fr.md) et
[`<corr>`](corr.fr.md).

### Omissions volontaires de texte par l’éditeur

Les omissions volontaires de texte de la part de l’éditeur (reproduction partielle)
sont signalées par `[…]` dans l’édition imprimée et par 
[`<gap reason="irrelevant"/>`](gap.fr.md) dans l’édition numérique. 
Cela devrait être évité dans la mesure du possible.

Si les ajouts ultérieurs ne sont pas édités avec l’original,
mais en tant que pièce indépendante, les parties déjà éditées dans un original
antérieur peuvent être omises avec [`<gap/>`](gap.fr.md).
Une référence au document déjà édité doit être faite.
Une [`<note>`](note.fr.md) ou une remarque avec [`<back>`](back.fr.md)
est nécessaire pour que le document soit référencé.

### Traitement des interventions éditoriales du scribe

=== "Règles générales"

    En principe, un texte transcrit doit être facile à lire et à comprendre, 
    même s’il repose sur un modèle ayant subi plusieurs révisions de différentes mains. 
    L’éditeur doit choisir une des variantes du texte et indiquer les autres
    avec des balises. Une attention particulière doit être portée aux suppressions
    ou éléments effacés ainsi qu’aux ajouts ou mentions postérieures.

=== "Suppressions"

    Les corrections simples effectuées au cours du processus de rédaction 
    ne sont mentionnées que dans des cas exceptionnels.

    Dans la version imprimée, les suppressions étaient marquées par `a–…–a` 
    et expliquées dans une note critique du texte. Dans l’édition numérique, 
    les suppressions sont balisées avec [`<del>`](del.fr.md).

    Pour les suppressions complexes et impliquant plusieurs niveaux de hiérarchie,
    [`<delSpan/>`](delSpan.fr.md) et [`<anchor/>`](anchor.fr.md) doivent être utilisés.

    Les passages de texte devenus illisibles en raison de suppressions étaient, 
    dans l’édition imprimée, marqués d’un `[…]a`et accompagnés d’une note. 
    Dans l’édition numérique, ils sont balisés avec [`<del>`](del.fr.md)
    et [`<gap/>`](gap.fr.md).

    Pour les passages de texte contenant à la fois des suppressions et des ajouts,
    [`<subst>`](subst.fr.md) doit être utilisé.

=== "Rasures"

    Dans l’édition imprimée, les rasures étaient traitées de la même manière que
    les suppressions et une note critique du texte était requise.

    Dans l’édition numérique, une rasure est balisée avec [`<del rend="rubbing">`](del.fr.md).
    Si des rasures ou des ratures importantes rendent la lecture impossible,
    [`<gap/>`](gap.fr.md) est utilisé à l’intérieur de [`<del>`](del.fr.md).

=== "Ajouts"

    Les ajouts de première main ou mentions postérieures doivent être inclus dans le texte. 
    Dans l’édition imprimée, ils étaient expliqués dans une note critique. 
    Dans l’édition numérique, la balise [`<add>`](add.fr.md) est utilisée.
    Les informations sur l’auteur de l’ajout et l’endroit de ce dernier doivent être indiquées.

    Pour les ajouts complexes touchant plusieurs niveaux hiérarchiques, on utilise 
    [`<addSpan/>`](addSpan.fr.md) et [`<anchor/>`](anchor.fr.md).
