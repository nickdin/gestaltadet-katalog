# Nivån i en klass beror på värdet i en uppgift: värsta fallet gäller, eller delmängden blir ett eget informationsobjekt, och en förteckning i ett exemplar är ändå en typ

*[[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|Beslut 58]] skärper en punkt här. Nuläget visar delmängden som ett eget informationsobjekt först när verksamheten hanterar den för sig. Fram till dess står uppdelningen i målarkitekturen.*

Beslutat av Nicklas 3 november 2026, i ett samtal. Han avvisade att öppna uppgiften som elementtyp, eftersom det skulle riva upp [[0018-uppgift-sammanstallning-och-behandling-ar-begrepp-inte-elementtyper|beslut 18]], [[0024-tillstand-ar-en-elementtyp-uppgiften-ar-informationsmodellens-attribut-och-lagret-ar-den-delade-datamodell-sdmn-beskriver|24]] och [[0030-informationsomradet-ar-ett-begrepp-utan-elementtyp-ett-informationsobjekt-som-bestar-av-sina-objekt-varje-objekt-har-ett-hem-och-nivan-far-vara-grov|30]] utan att behövas.

## Sammanhang

Ett informationsobjekt har ibland en uppgift vars värde avgör hur känsliga förekomsterna är. Hos Brinkstadsbostäder har Yrkesroll uppgiften utsatt roll, ja eller nej. De roller som är utsatta för hot ställer andra krav än de övriga.

Katalogen svarade redan nej på frågan, men inte uttryckligen för det här fallet. Uppgiften är ett begrepp utan elementtyp ([[0018-uppgift-sammanstallning-och-behandling-ar-begrepp-inte-elementtyper|beslut 18]] och [[0024-tillstand-ar-en-elementtyp-uppgiften-ar-informationsmodellens-attribut-och-lagret-ar-den-delade-datamodell-sdmn-beskriver|24]]). Det som klassas, ägs eller regleras för sig är alltid ett eget objekt ([[0030-informationsomradet-ar-ett-begrepp-utan-elementtyp-ett-informationsobjekt-som-bestar-av-sina-objekt-varje-objekt-har-ett-hem-och-nivan-far-vara-grov|beslut 30]]). Informationsägaren sätter behovet på informationsobjektet. Inget sade vad som gäller när nivån beror på värdet i en uppgift.

## Beslut

- **Värsta fallet gäller.** Lagret ritar typer, och behovet sätts på typen. Nivån i varje klass måste hålla för varje förekomst, också de utsatta rollerna. Uppgiften utsatt roll är en vanlig uppgift med värdemängden ja och nej.
- **Blir nivån för hög för de övriga förekomsterna, blir delmängden ett eget informationsobjekt.** Utsatt roll specialiserar Yrkesroll, ärver dess uppgifter och lägger till sina egna uppgifter, som typ av hot, skyddsåtgärd och datum för senaste bedömning (exemplet Brinkstadsbostäder visar dem). Uppgiften utsatt roll står kvar i Yrkesroll, eftersom den skiljer objekten åt. Golvet i [[0030-informationsomradet-ar-ett-begrepp-utan-elementtyp-ett-informationsobjekt-som-bestar-av-sina-objekt-varje-objekt-har-ett-hem-och-nivan-far-vara-grov|beslut 30]] gäller: det som regleras för sig är ett eget objekt. Tydligast är fallet när rollen placeras i en säkerhetsskyddsklass.
- **Nivån sätts aldrig på uppgiften, och uppgiften blir aldrig ett eget element.**
- **En förteckning som finns i ett enda exemplar är ändå en typ.** Förteckningen över utsatta roller är en sammanställning som aggregerar Yrkesroll eller Utsatt roll. Den klassas för sig, oftast högre. Excelfilen är dess representation och ger form åt sammanställningen, inte åt Yrkesroll. Typen är det verksamheten talar om och ställer krav på. Förekomsten är listan som den ser ut just nu, skild från nästa version genom den identifierande uppgiften, versionsdatumet.

## Övervägda alternativ

- **Uppgiften som elementtyp.** Det skulle riva upp [[0018-uppgift-sammanstallning-och-behandling-ar-begrepp-inte-elementtyper|beslut 18]], [[0024-tillstand-ar-en-elementtyp-uppgiften-ar-informationsmodellens-attribut-och-lagret-ar-den-delade-datamodell-sdmn-beskriver|24]] och [[0030-informationsomradet-ar-ett-begrepp-utan-elementtyp-ett-informationsobjekt-som-bestar-av-sina-objekt-varje-objekt-har-ett-hem-och-nivan-far-vara-grov|30]] utan att behövas. Avvisat.

## Konsekvenser

- Anmärkningarna i Informationsobjekt (`C-060`), Informationstillgång (`C-166`) och Sammanställning (`C-162`) får texten om värsta fallet, delmängden som eget objekt och typen mot förekomsten. Inga definitioner, relationer eller begrepp ändras.
- Exempelorganisationen Brinkstadsbostäder får exemplet Yrkesroll, Utsatt roll och Förteckning över utsatta roller i `docs/exempel/brinkstadsbostader.md`.
