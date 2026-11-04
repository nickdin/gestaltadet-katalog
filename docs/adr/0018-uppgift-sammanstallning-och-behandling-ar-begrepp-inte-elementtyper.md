# Uppgift, sammanställning och behandling är begrepp, inte elementtyper

Beslutat av Nicklas i en grillning av informationsperspektivet inför draw.io-mallen med en ruta per elementtyp.

ADR 0031 ersatte meningen om att ändamål och rättslig grund står i beteendets beskrivning: de står i registerförteckningen, och lagret ger ankaret.

## Sammanhang

Kartläggningen av en avdelnings verksamhetsinformation gav katalogen åtta begrepp på två dagar, fyra av dem som elementtyper: Uppgift (`C-161`), Sammanställning (`C-162`), Lagringsyta (`C-165`) och Behandling (`C-168`). Inget element av någon av dem hade registrerats, och ArchiMate saknar motsvarighet till tre. Mallen som skulle visa en box per typ gjorde skevheten synlig. Informationsperspektivet är definierat som strukturen hos den information verksamheten hanterar, men rymde en åtgärd, och fältet i ett informationsobjekt hade en egen box.

## Beslut

- Uppgift är ett begrepp, ingen elementtyp. Ett informationsobjekt består av uppgifter, och de står i objektets beskrivning. En uppgift som verksamheten hanterar som en enhet för sig, klassar, äger eller reglerar, som personnumret, är ett eget informationsobjekt. Objektet som rymmer den aggregerar den (`C-100`), eftersom samma fält ingår i många objekt.
- Sammanställning är ett begrepp, ingen elementtyp. En sammanställning registreras som informationsobjekt och aggregerar de informationsobjekt den är gjord av. Relationen visar att den är en sammanställning. Inte `C-064 härleds ur`: den säger "motiveras av" och är ett ord för mål och krav.
- Behandling är ett begrepp, ingen elementtyp. Behandlingen läses ur det verksamhetsbeteende som utför den och de informationsobjekt som beteendet har åtkomst till (`C-101`), som ArchiMate gör med Access. Ändamål och rättslig grund står i beteendets beskrivning. En informationsägare läser verksamhetsperspektivet; informationsperspektivet behöver ingen kopia av beteendet.
- Lagringsyta står kvar som elementtyp i applikationsperspektivet, och Representation i informationsperspektivet. Informationsperspektivet täcker därmed Informationsobjekt och Representation.
- Informationsobjekt (`C-060`) får entitetstyp som tillåten term: informationsmodelleringens ord för mallen, inte för förekomsten. Entitet tas inte in, eftersom det ordet betyder förekomsten för den som modellerar information.

## Övervägda alternativ

- **Behålla de tre som typer.** Varje ritning måste då välja mellan två boxar för samma slags sak, informationsobjekt eller sammanställning. Fältet får en box ingen ritar, och behandlingen dubblerar beteendet i verksamhetsperspektivet. Avvisat.
- **Behandling som typ i informationsperspektivet med vidgad definition.** Perspektivets ägare äger behandlingarna, men beteendet finns redan i verksamhetsperspektivet. En informationsägare ska läsa andra perspektiv, inte ha allt i sitt eget. Avvisat av Nicklas.
- **Behandling som verksamhetsbeteende bredvid process, handläggning och funktion.** Den drunknar bland processerna, och den är ingen fjärde sorts beteende utan en synvinkel på de tre. Avvisat.
- **Entitet som andraterm eller föredragen term.** Fällan är att kollegan hör "en rad". Avvisat; entitetstyp är tillåten i stället.
- **Två typer, entitet för det informationen handlar om och informationsobjekt för mängderna.** Samma gränsdragningsproblem som sammanställningen gav. Skillnaden är detaljeringsgrad, och den har lagret redan. Avvisat.

## Konsekvenser

- `C-161`, `C-162` och `C-168` står utan `kind`; anmärkningarna säger hur de används. `C-066` täcker `C-060` och `C-085`. `C-060` får termen entitetstyp och regeln om när ett fält blir ett eget objekt.
- `mapping/archimate.yaml` och `mapping/aris.yaml`: de tre raderna under `unmapped-concepts` tas bort; bara typer står där.
- Begreppsmodellen `layout/Verksamhetsinformation begreppsmodell.drawio.svg` ritar fortfarande de tre, som begrepp, och rörs inte.
- draw.io-mallen byggs om från katalogens täckningslistor, med typnamnet på varje box, ikon per sorts sak och grupperna Arkitekturobjekt och Styrmedel utanför perspektiven.
