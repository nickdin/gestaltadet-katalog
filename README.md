# GestaltaDet: begreppskatalogen

En begreppskatalog för verksamhetsarkitektur: ett begrepp, ett id, en definition, de termer som används för det, och relationerna mellan begreppen. Katalogen är skriven från svensk offentlig sektor, men begreppen gäller alla verksamheter. Den läses av programmet interlingua och publiceras på gestaltadet.se/katalog.

## Vad som finns här

- `CONTEXT.md`: ordlistan, de ord katalogen själv är byggd av, med hänvisning till begreppen.
- `concepts/`: begreppen, en fil per begrepp, med term, definition, typ och begreppsrelationer.
- `mapping/`: tabeller som säger vilket begrepp varje typ i ArchiMate, ARIS, BACM, BMM, BPMN, CMMN, DMN, SBVR och SDMN motsvarar.
- `layout/`: ritningarna, begreppsmodeller och scheman som draw.io-filer, redigerbara; publicerade på gestaltadet.se/ritningar. En ritning visar lagrets relationer mellan de begrepp den visar, med lagrets ord på pilen. Den får också visa en relation som begreppet ärver från sitt överordnade begrepp när det överordnade inte är med i ritningen; en ritning är ett urval och behöver inte visa alla relationer.
- Besluten bakom katalogen (`docs/adr/`): varför ett begrepp finns, var gränsen mot grannen går och vad som valdes bort. De publiceras som sidor i katalogen.
- Två exempelorganisationer som alla exempel utgår från: en påhittad statlig myndighet och ett påhittat kommunalt bostadsbolag.

## Frågor och ändringar

Frågor, invändningar och förslag är välkomna som ärenden. Katalogen är ett sätt att se på saker, så ändringarna gör upphovspersonen själv; en invändning som håller blir en ändring, och ofta en artikel.

## Licens

Creative Commons Erkännande 4.0 Internationell (CC BY 4.0), se `LICENSE`. Använd och bygg vidare, med GestaltaDet och Nicklas Grandin som källa.
