# Metamodellen definierar typer, notationen är ett eget begrepp, en beskrivning följer en metamodell, och lagret rymmer bara katalogens

Beslutat av Nicklas 12 november 2026, när Metamodell (`C-039`) visade sig rymma både vad något är och hur det ritas.

## Sammanhang

Granskningen i #43 hade fyndet F26. Arkitekturbeskrivning (`C-035`) sade att varje vy följer perspektivets metamodell. Arkitekturvy (`C-052`) sade att perspektivet anger vilka metamodeller vyn använder. Den ena gav perspektivet en metamodell, den andra flera.

Beslut 37 sköt fyndet hit. Nicklas såg att frågan var större än en eller flera. Metamodell (`C-039`) definierades som en modell som definierar element, relationer och notation. Men samma notation kan läggas på olika metamodeller. Och katalogen beskriver genom sina begrepp redan en egen metamodell, byggd med de andra som källor (beslut 22).

Grillningen avgjorde varje fråga på ett fall ur de två exempelorganisationerna.

## Beslut

- **En metamodell definierar typer, inte notation.** Metamodell (`C-039`) är en modell som definierar vilka typer av arkitekturelement och relationer en arkitekturbeskrivning får använda. Begreppet är allmänt. Katalogen är GestaltaDets metamodell, och ArchiMate är en annan.
- **Metamodellen definierar typen, inte elementet.** Myndigheten för föreningsstöd har elementet Ärendesystemet, av typen Applikation (`C-071`). Katalogen definierar Applikation, inte Ärendesystemet. Arkitekturelement (`C-034`) är därför en beståndsdel av en arkitektur, av en typ som en metamodell definierar. Elementtyp och relationstyp blir inga egna begrepp.
- **En beskrivning följer exakt en metamodell.** Alla dess vyer följer samma. Perspektivet har ingen egen metamodell: det avgör vilka av metamodellens typer vyn täcker. Det avgör F26. Relationen `följer` går från Arkitekturbeskrivning (`C-035`), inte från Arkitekturvy (`C-052`). Relationen `anger` från Arkitekturperspektiv (`C-036`) är borttagen.
- **Lagret rymmer bara beskrivningar som följer katalogens metamodell.** Bostadsbolagets konsult ritar felanmälan i ArchiMate. Ritningen är en arkitekturbeskrivning, och den följer ArchiMate. Bolaget översätter den genom mappningstabellen innan den går in i målarkitekturen: Business Process blir Verksamhetsprocess (`C-130`). En beskrivning blandar aldrig två metamodeller.
- **Notation (`C-212`) är ett eget begrepp.** En notation är en uppsättning symboler, med regler för hur de används, som arkitekturelement och relationer ritas med i ett diagram. Notationen säger hur något ritas, metamodellen vad det är.
- **Notationen hör till diagrammet, inte till vyn.** Myndigheten ritar handläggningen av en bidragsansökan två gånger, med BPMN:s symboler och med ArchiMates. Vyn är densamma. Diagram (`C-106`) ritas med Notation (`C-212`). Ett diagram får blanda notationer.
- **En notation har en hemmetamodell.** Symbolerna står för hemmetamodellens typer. Notationen läggs på en annan metamodell genom en mappningstabell: Verksamhetsaktivitet (`C-175`) är BPMN:s Task och ritas därför som en rundad ruta.
- **En mappningstabell översätter mellan två metamodeller, typ för typ.** Den säger ingenting om symboler. Mappningstabell blir inget eget begrepp.
- **Katalogen har en egen notation.** Den är rutorna i draw.io-mallen. Den behöver ingen mappningstabell, eftersom symbolerna redan står för katalogens typer.
- **ISO 42010:s model kind rymmer både metamodellen och notationen.** Katalogen håller isär dem, och båda begreppen säger det.
- **Metamodellen avgör vad en organisation kan säga om sig själv.** Ett bostadsbolag som väljer en metamodell utan Beslutslogik (`C-178`) kan inte beskriva hur hyran bestäms som en regel bolaget återanvänder. Meningen står i anmärkningen till Metamodell (`C-039`).

## Övervägda alternativ

- **Pensionera Metamodell (`C-039`).** Katalogen är GestaltaDets enda metamodell och behöver inget ord för sig själv. Men då saknas ett ord för vad ArchiMate är när konsulten lämnar sin ritning. Avvisat.
- **Metamodell betyder bara katalogen.** Då är ArchiMate bara en källa, och mappningstabellerna översätter mellan en metamodell och något utan namn. Avvisat.
- **Arkitekturbeskrivning (`C-035`) betyder bara det som följer katalogen.** Då är konsultens ritning ett underlag utan namn, och relationen `följer` säger inget, eftersom svaret alltid är katalogen. Avvisat: begreppen är allmänna, och regeln om lagret står i anmärkningen.
- **Notationen kvar som egenskap hos metamodellen.** Det var utgångsläget. Det går inte ihop med att ArchiMates symboler kan läggas på katalogens typer. Avvisat.
- **Notationen hör till vyn.** Då hade samma vy inte kunnat ritas med två notationer. Avvisat.
- **Elementtyp och Relationstyp som egna begrepp.** Ordet typ räcker i texten. Avvisat för nu.
- **Mappningstabell som eget begrepp.** Den förklaras i anmärkningarna till Metamodell (`C-039`) och Notation (`C-212`). Avvisat.

## Konsekvenser

- Nytt begrepp: `C-212` Notation, med relationen `står för typerna i` → `C-039`.
- Ändrade definitioner: `C-039` och `C-034`.
- Ändrade relationer: `C-039` `definierar typerna av` → `C-034`, förut `definierar`. `C-035` `följer` → `C-039` är ny. `C-052` `följer` → `C-039` och `C-036` `anger` → `C-039` är borttagna. `C-106` `ritas med` → `C-212` är ny.
- Ändrade anmärkningar: `C-039`, `C-035`, `C-036` och `C-052`. `C-106` har fått en anmärkning. `C-039` har katalogen och BPMN bland exemplen.
- Meningen i beslut 38, att Arkitekturbeskrivning (`C-035`) följer metamodellen genom Arkitekturvy (`C-052`), gäller inte längre. Beskrivningen följer metamodellen själv.
- Två ritningar visar pilarna `följer` och `anger` som de var, och ingen visar Notation (`C-212`). Pilarna står kvar tills Nicklas värderat dem (#147).
- Interlinguas eget ord *metamodel kind* rörs inte. Det är programmets ord för typslagen.
- Två ärenden följer av grillningen: katalogens notation som mallar på gestaltadet.se (#148), och hur notationen ska se ut, klarspråk för diagram (#149).
- #72 stängs.
