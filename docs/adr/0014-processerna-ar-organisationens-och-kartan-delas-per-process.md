# Processerna är organisationens, och kartan delas i en översikt och en bild per process

Beslutat av Nicklas efter en grillning om varför en avdelnings processkarta blivit för mastig och vad på den som är process och vad som är aktivitet. Ersätter ADR 0013 i det som rör banden.

## Sammanhang

Kartan ritade ett trettiotal rutor i band efter ansvarsnivå, med avdelningen som den som driver varje process. Flera rutor var aktiviteter i någon större process, en tjänst och dess rapporter var samma sak, och en bedömning med egen start var en egen process. Processerna skulle dessutom beskrivas som organisationens, inte avdelningens, med de delar avdelningen verkar i eller driver. Organisationen hade ingen processkarta; det som tas fram är det som finns.

## Beslut

- En process har, utöver katalogens definition, en egen start, en händelse som sätter igång den, och ett eget resultat som någon utanför kedjan tar emot. Det som saknar endera är en aktivitet i någon annan process. Hos Myndigheten för föreningsstöd är att fördela ansökningarna på handläggare en aktivitet i ansökningsomgången, medan att göra en dataskyddsbedömning är en egen process.
- Processerna är organisationens. De namnges med verb plus objekt (ADR 0012) och får en ägare i organisationen. Avdelningens roll per process är driver, deltar eller normerar. En process organisationen utför per avdelning, som att styra en delportfölj, är en process med flera körningar, var och en driven av sin avdelning.
- En process där avdelningen bara deltar ritas som en ram med namn och ägare, inuti bara avdelningens steg och en grå ruta för övriga steg.
- Kartan delas: en översiktsbild som ritar bara processer, med avdelningens roll som markering och pilar som bär objektets namn, och en bild per process som avdelningen driver. Processer där avdelningen bara deltar får en rad i översikten. Banden försvinner; delegationsordningens rad står kvar under Ansvar på varje process, och de ställen där den och samtalen går isär står kvar som osäkerheter.
- Lagret lagrar åtkomsten mellan beteende och verksamhetsobjekt (`C-101 har åtkomst till`), inte flödet mellan processer. Pilen process till process i översikten är en slutsats ur åtkomsterna: A skapar X och B läser X ger pil A till B märkt X. Den ritas för hand tills interlingua härleder den. Produkten finns en gång i lagret, realiserad av processen, och ritas i bilden per process.
- Informationen samlas ur processerna: varje bild per process får verksamhetsobjekten vid stegen, och informationsmodellen blir en egen bild när några processer är ritade.
- Förmågorna får en egen bild som visar varje förmåga och det som realiserar den.
- Ärendehantering som egen typ väcks inte nu. Det som handläggs som ärende, utan fast stegföljd, ritas som process med den raden under osäkerheterna. Det enskilda ärendet är ett verksamhetsobjekt.
- Att styra verksamheten är en förmåga, inte en process.

## Övervägda alternativ

- **En bild per ansvarsband.** Behåller dagens struktur, men processerna är då fortfarande avdelningens. Avvisat.
- **En bild per verksamhetsområde.** Visar organisationen, vilket organisationsbilden redan gör. Avvisat.
- **Rita hela processen där avdelningen bara deltar.** Vi vet inte hur resten ser ut. Avvisat.
- **Lagra både flödet mellan processer och åtkomsten.** Samma sak sagd två gånger. Avvisat.
- **Väcka ärendetypen nu.** Kartan är till cheferna och väntar inte på en typ; typen grillas bättre med några verkliga fall framför sig. Avvisat tills vidare.

## Konsekvenser

- ADR 0013:s band och dess regel om vilka processer som är avdelningens egna gäller inte längre. Kvar från ADR 0013: organisationen är systemet, delegationsordningens rad under Ansvar, mottagare som relation.
- Översikten ritas om; bilderna per process blir nya vyer i beskrivningen.
- Kartans rutor sorteras om i processer, aktiviteter, funktioner (ADR 0015), verksamhetsobjekt (ADR 0016), produkter och förmågor. Rapporter utan process får en föreslagen process.
- Härledningen av pilen process till process är ett ärende hos interlingua.
- Ärendetypen väcktes kort därefter: ADR 0017.
