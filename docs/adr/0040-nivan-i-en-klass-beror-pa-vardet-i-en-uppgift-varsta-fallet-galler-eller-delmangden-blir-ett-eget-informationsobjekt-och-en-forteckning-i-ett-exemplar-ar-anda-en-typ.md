# Nivån i en klass beror på värdet i en uppgift: värsta fallet gäller, eller delmängden blir ett eget informationsobjekt, och en förteckning i ett exemplar är ändå en typ

Beslutat av Nicklas 3 november 2026, i ett samtal, när han frågade om en uppgift måste bli ett eget element för att kunna klassas.

## Sammanhang

Ett informationsobjekt har ibland en uppgift vars värde avgör hur känsliga förekomsterna är. Hos Brinkstadsbostäder har Yrkesroll uppgiften utsatt roll, ja eller nej. De roller som är utsatta för hot ställer andra krav än de övriga.

Katalogen svarade redan nej på frågan, men inte uttryckligen för det här fallet. Uppgiften är ett begrepp utan elementtyp (beslut 18 och 24). Det som klassas, ägs eller regleras för sig är alltid ett eget objekt (beslut 30). Informationsägaren sätter behovet på informationsobjektet. Inget sade vad som gäller när nivån beror på värdet i en uppgift.

## Beslut

- **Värsta fallet gäller.** Lagret ritar typer, och behovet sätts på typen. Nivån i varje klass måste hålla för varje förekomst, också de utsatta rollerna. Uppgiften utsatt roll är en vanlig uppgift med värdemängden ja och nej.
- **Blir nivån för hög för de övriga förekomsterna, blir delmängden ett eget informationsobjekt.** Utsatt roll specialiserar Yrkesroll, ärver dess uppgifter och lägger till egna: typ av hot, skyddsåtgärd och datum för senaste bedömning. Uppgiften utsatt roll står kvar i Yrkesroll, eftersom den skiljer objekten åt. Golvet i beslut 30 gäller: det som regleras för sig är ett eget objekt. Tydligast är fallet när rollen placeras i en säkerhetsklass.
- **Nivån sätts aldrig på uppgiften, och uppgiften blir aldrig ett eget element.**
- **En förteckning som finns i ett enda exemplar är ändå en typ.** Förteckningen över utsatta roller är en sammanställning som aggregerar Yrkesroll eller Utsatt roll. Den klassas för sig, oftast högre. Excelfilen är dess representation och ger form åt sammanställningen, inte åt Yrkesroll. Typen är det verksamheten talar om och ställer krav på. Förekomsten är listan som den ser ut just nu, skild från nästa version genom den identifierande uppgiften.

## Övervägda alternativ

- **Uppgiften som elementtyp, så att den kan få en egen klass.** Det river upp beslut 18, 24 och 30 utan att behövas: delmängden går att hantera som ett eget informationsobjekt. Avvisat.
- **Klass på uppgiften, utan att den blir element.** Behovet sätts då på något som inte är en typ med ägare och förekomster, och informationsägaren kan inte besluta om det. Avvisat.
- **Dela alltid objektet i två, ett för de vanliga och ett för de särskilda förekomsterna.** Det ger fler objekt än verksamheten talar om. Avvisat: delningen görs bara när nivån annars blir för hög för de övriga.
- **Förteckningen i ett exemplar som en förekomst av Yrkesroll.** Förteckningen är något annat än en roll: den är det verksamheten ställer krav på. Avvisat.

## Konsekvenser

- Anmärkningarna i Informationsobjekt (`C-060`), Informationstillgång (`C-166`) och Sammanställning (`C-162`) får texten om värsta fallet, delmängden som eget objekt och typen mot förekomsten. Inga definitioner, relationer eller begrepp ändras.
- Exempelorganisationen Brinkstadsbostäder får exemplet Yrkesroll, Utsatt roll och Förteckning över utsatta roller i `docs/exempel/brinkstadsbostader.md`.
