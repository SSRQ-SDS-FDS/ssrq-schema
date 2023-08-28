Drucke:
## 3 Druckfehler
Eindeutige Druckfehler werden mit [<choice/>](../../elements/choice.de.md), [<sic/>](../../elements/sic.de.md) und
[<corr/>](../../elements/corr.de.md) korrigiert.

Hss:
## 7 Behandlung von Lücken, Schäden und Mängeln in der Textvorlage

### 7.1 Lücken vom Schreiber

Vom Schreiber zwecks späterer Ergänzung bewusst gelassene Lücken (Auslassungen) wurden in analogen Bänden durch drei Auslassungspunkte ohne Klammer gekennzeichnet und in einer textkritischen Anmerkung unter Angabe der Grösse der Textlücke erläutert. In der digitalen Edition werden sie mit  [`<space/>`](../../elements/space.de.md)  getagt unter Angabe der Lückengrösse mit @unit und @quantity.

Referenzpunkte bzw. Reverenzpunkte vor Namen oder Amtsbezeichnungen wurden in der analogen Edition durch 2 Punkte ohne
Klammer wiedergegeben. In der digitalen Edition werden sie ebenfalls mit 2 Punkten ohne Klammer wiedergegeben.

### 7.2 Klammern in der Editionsvorlage

Vom Schreiber in (   ) gesetzte Textteile werden identisch wiedergegeben.

### 7.3 Weggelassene Textteile

Vom Schreiber irrtümlich weggelassene Textteile (z. B. beim Abschreiben übersprungene Zeile) wurden in der analogen Edition durch einen Ersatztext aus einer anderen originalen oder kopialen Quelle oder durch den Bearbeitenden selbst im Sinne einer sinngemässen Textwiedergabe in [ ]a ergänzt. Eine Anmerkung war notwendig.

In der digitalen Edition wird die Lücke mit [`<supplied/>`](../../elements/supplied.de.md) getaggt. Mit @reason wird der
Grund der Lücke und mit @resp das Kürzel des Bearbeitenden angegeben. Falls notwendig, kann eine
[`<note/>`](../../elements/note.de.md) gesetzt werden. Bei Ergänzungen anhand einer anderen Vorlage (2. Original, Kopie etc.)
wird mit @source auf diesen Textzeugen referenziert. Vgl. dazu auch [`<app/>`](../../elements/app.de.md).

Ein Textverlust infolge Mäusefrass, verblasster Tinte, Brand, Pilzbefall, Rissen, Löchern, Kassation usw. wird
mit [`<damage/>`](../../elements/damage.de.md) und [`<gap/>`](../../elements/gap.de.md) gekennzeichnet und falls möglich innerhalb
von  [`<damage/>`](../../elements/damage.de.md) mit [`<supplied/>`](../../elements/supplied.de.md) – oder bei Unsicherheit mit
[`<unclear/>`](../../elements/unclear.de.md) und @cert – ergänzt. Der Schaden wird innerhalb von
[`<damage/>`](../../elements/damage.de.md) mit @agent näher bezeichnet.

### 7.4 Irrtümliche Wiederholungen

Irrtümliche Wiederholungen von Silben, Wörtern und Satzteilen sollen mit [`<choice/>`](../../elements/choice.de.md) und
[`<sic/>`](../../elements/sic.de.md) angemerkt und mit [`<corr/>`](../../elements/corr.de.md) normalisiert werden.

### 7.5 Unsichere Lesung

Bei Wörtern mit unsicherer Lesung wurden bei der analogen Edition in einer textkritischen Anmerkung denkbare
Lesevarianten angeführt. Sie konnten zusätzlich mit [?] gekennzeichnet werden.
In der digitalen Edition werden unsichere Lesungen mit [`<unclear/>`](../../elements/unclear.de.md) getaggt. Die
Wahrscheinlichkeit der Lesung kann mit @cert angegeben werden. Falls dies nicht genügt, kann auch eine Anmerkung mit
[`<note/>`](../../elements/note.de.md) gemacht werden.

### 7.6 Schreib-, Sprach- und Stilfehler

Schreib-, Sprach- und Stilfehler werden im Text nicht korrigiert. In der analogen Edition wurden sie in einer textkritischen Anmerkung erläutert oder mit einem [!] gekennzeichnet.
In der digitalen Edition werden solche Fehler mit [`<sic/>`](../../elements/sic.de.md) gekennzeichnet und allenfalls  mit [`<choice/>`](../../elements/choice.de.md) zusammen mit [`<sic/>`](../../elements/sic.de.md) und [`<corr/>`](../../elements/corr.de.md) korrigiert.

### 7.7 Bewusste Auslassungen von Text durch den Bearbeitenden

Bewusste Auslassungen von Text durch den Bearbeitenden (Teilabdruck) werden in der analogen Edition mit [...] und in der
digitalen mit [`<gap/>`](../../elements/gap.de.md) @reason="irrelevant" wiedergegeben. Dies sollte, wenn möglich, vermieden
werden.

Werden spätere Nachträge nicht beim Original, sondern als eigenständiges Stück ediert, können die Teile, die bereits in
einem früheren Original ediert wurden, mit [`<gap/>`](../../elements/gap.de.md) weggelassen werden. Auf das bereits edierte
Stück wird mit @source verwiesen. Eine Anmerkung in [`<note/>`](../../elements/note.md) oder eine Bemerkung in
[`<back/>`](../../elements/back.de.md) ist nötig.

## 8 Behandlung redaktioneller Eingriffe des Schreibers

Grundsätzlich hat ein transkribierter Text, auch wenn er auf einer von verschiedenen Händen mehrfach überarbeiteten
Vorlage basiert, gut lesbar und verständlich zu sein. Der Bearbeitende muss sich für eine Textvariante entscheiden und
die übrigen Varianten mit tags auszeichnen. Zu beachten ist:

### 8.1 Streichungen

Auf einfache Korrekturen, die beim Schreibvorgang entstanden sind, wird nur in Ausnahmefällen hingewiesen.

Streichungen wurden in der analogen Transkription mit `a–...–a` gekennzeichnet und in einer textkritischen Anmerkung
aufgeführt.
In der digitalen Edition werden Streichungen mit [`<del/>`](../../elements/del.de.md) getaggt.

Bei mehrfach gestrichenen Texten müssen [`<delSpan/>`](../../elements/delSpan.de.md) und
[`<anchor/>`](../../elements/anchor.de.md) eingesetzt werden.

Durch Streichungen unlesbar gewordene Textstellen wurden in der analogen Edition mit `[...]a` gekennzeichnet und mit
einer Anmerkung versehen.
In der digitalen Edition werden sie mit [`<del/>`](../../elements/del.de.md) und einem leeren
[`<gap/>`](../../elements/gap.de.md) ausgezeichnet.
`todo: Beispiel aufnehmen und dann hier löschen: <del><gap unit="cm" quantity="4"/></del>`

Bei Textstellen, die mehrere Streichungen und/oder Hinzufügungen bzw. Kombinationen davon aufweisen, muss
[`<subst/>`](../../elements/subst.de.md) verwendet werden.

### 8.2 Zusätze oder Nachträge

Zusätze oder Nachträge von erster oder späterer Hand müssen in den Text aufgenommen werden und wurden in der analogen
Edition in einer textkritischen Anmerkung erklärt.
In der digitalen Edition wird der Tag [`<add/>`](../../elements/add.de.md) verwendet.

Der Ort der Ergänzung muss zwingend in `@place` und die Hand der ergänzten Stelle kann mit `@hand` festgehalten werden.

`to do: Beispiel mit @hand und Jahrhundert aufnehmen und hier anfügen <add hand=hand18c></add>`

`<to do: Beispiel hier anfügen add place="margin" hand="other hand"></add>`

### 8.3 Rasuren

Mit Rasuren wurde in der analogen Edition gleich verfahren wie mit Streichungen und eine textkritische Anmerkung war
erforderlich.
In der digitalen Edition wird eine Rasur mit  [`<del/>`](../../elements/del.de.md) und `@rend="rubbing"` ausgezeichnet.
Wenn bei Rasuren oder auch bei heftigen Streichungen gar nichts mehr lesbar ist, wird ein leeres
[`<gap/>`](../../elements/gap.de.md) innerhalb von [`<del/>`](../../elements/del.de.md) verwendet.

`<to do gutes Beispiel für Rubbing aufnehmen und hier verlinken del rend="rubbing"><unclear>unsichere Lesung wegen Rasur</unclear></del>`

`<to do gutes Beispiel für Rubbing mit gap aufnehmen und hier verlinkendel rend="rubbing"><gap unit="cm" quantity="1"/></del>`