# Förmågeprodukt är produkten sedd från lösningen, förmågetjänst är verksamhetstjänsten i den; produkterna skiljs på vad de är för mottagaren

Beslutat av Nicklas i den tredje av grillningarna av de öppna frågorna inför draw.io-mallen. Rättat samma dag: termen Förmågeprodukt sattes först på Leveransprodukt och flyttades till Produkt efter Nicklas invändning att en verksamhetsprodukt lika gärna kommer ur en lösning.

## Sammanhang

Frågan kom från interlingua och hade stått parkerad: förmåga är vad verksamheten kan oavsett hur, av vem och med vad; förmågekonfiguration är en kombination av komponenter som realiserar en förmåga; öppet var om förmågetjänst är ett tredje begrepp och hur det förhåller sig till Tjänst (`C-075`). ADR 0020 gav utgångsläget: Lösning (`C-055`) har Förmågekonfiguration som andra term och realiserar exakt en förmåga, och ett förmågenära ord för leveransprodukten sköts hit.

Nicklas rumsliknelse från IRM:s kurs: förmågor är rum där roller rör sig emellan, och förmågetjänsten är en lucka där information lämnas över i stället för att någon går med den till ett annat rum. IT-stödet är ofta ett bra sätt att börja identifiera rummen.

Lösning (`C-055`) sade två saker på en gång: att lösningen avgränsas av ändamål och användare, och att den är den unika kombination av komponenter som gör förmågan möjlig. Scenariot som prövade det var ett förvaltningsobjekt som byter rapportplattform under ett år, med samma chef, ram, användare och ändamål.

Nicklas bild av hur produkterna hänger ihop, uttalad i grillningen: för att leverera en verksamhetsprodukt med vissa egenskaper behöver verksamheten en viss förmåga; förmågan realiseras av en kombination av komponenter ur perspektiven; vissa av komponenterna, information till exempel, tas fram och tillgängliggörs av andra kombinationer, alltså andra förmågors lösningar. Det stred mot ADR 0020:s axel, där verksamhetsprodukten levereras av verksamheten och leveransprodukten av en lösning: en lösning levererar båda.

## Beslut

- En lösning känns igen på sitt ändamål och sina användare och består när en komponent byts. Raden om den unika kombinationen står kvar med tillägget "vid varje tid": under övergångsåret är det en lösning, vars beskrivning visar två sammansättningar, nuläget och målet. Förmågekonfiguration står kvar som term på Lösning (`C-055`); ordet betonar sammansättningen, lösningen sedd från det som bygger den.
- Produktaxeln ritas om. Verksamhetsprodukt (`C-173`) och Leveransprodukt (`C-174`) skiljs på vad produkten är för mottagaren, inte på vem som levererar: verksamhetsprodukten fullgör ett uppdrag mot mottagaren, leveransprodukten blir en komponent i mottagarens lösning. Båda levereras av en lösning, verksamhetsprodukten av den lösning verksamheten fullgör sitt uppdrag genom. Intern och extern är fortfarande den andra axeln. Leveransproduktens definition ändras till "produkt som en lösning tar fram och vidmakthåller och som mottagaren använder som komponent i sin egen lösning". Detta ersätter ADR 0020 på den punkten; de fyra specialiseringarna är desamma.
- Förmågeprodukt blir en term på Produkt (`C-014`): det en förmågekonfiguration levererar, vare sig det blir en verksamhetsprodukt eller en leveransprodukt. Ordet följer Förmågekonfiguration; båda säger samma sak sett från lösningen. Förmågeprodukten är luckan: det en förmågas lösning lämnar ut genom rummets vägg, och om mottagaren är en annan lösning eller en kund är de andra axlarna. Varje produkt kommer ur någon lösning, så ett eget begrepp ovanför båda produkterna vore detsamma som Produkt, och därför är det en term på just Produkt.
- Förmågetjänst är inget eget begrepp. De tjänster en förmågeprodukt erbjuder ges av lösningen som helhet, människor, processer och system tillsammans, och registreras som verksamhetstjänst (`C-127`), vars anmärkning redan säger att den kräver processer och kompetens. Applikations- och tekniktjänster står på komponentnivå: förmågeprodukten Föreningsregistret erbjuder verksamhetstjänsten Tillhandahålla registeruppgifter, som realiseras av applikationstjänsten Slå upp förening och registerenhetens arbete. Rader i anmärkningarna på Tjänst (`C-075`), Verksamhetstjänst (`C-127`) och Leveransprodukt (`C-174`) säger detta, med IRM:s ord nämnt.
- Relationerna, utan nya relationstyper: förmågeprodukten realiseras av (`C-094`) sin lösning; den lösning som tar emot den, eller den komponent i den som behöver den, använder (`C-095`) förmågeprodukten.

## Övervägda alternativ

- **Två lösningar under övergångsåret**, en per sammansättning, med förvaltningsobjektet som en av dem. Då kan regeln om ändamål och användare inte skilja dem åt, och chefen förvaltar en sak hela året. Avvisat.
- **Förmågekonfiguration som eget begrepp**, en lösnings sammansättning vid en viss tid. Det är vad en beskrivning redan visar; ett begrepp till vore en beskrivning förklädd till sak, samma skäl som fällde canvasen i ADR 0020. Avvisat. **Termen struken.** Ordet är det frågan kom med. Avvisat.
- **Förmågetjänst som begrepp under Tjänst utan elementtyp**, registrerad som verksamhets-, applikations- eller tekniktjänst efter perspektiv. Avvisat av Nicklas: på applikations- och tekniknivå är det komponenter, inte den totala lösningen. **Som begrepp under Verksamhetstjänst** med eget C-id. Produktaxeln bär redan skillnaden; ett begrepp till på tjänstesidan säger samma sak en gång till. Avvisat. **Som fjärde elementtyp i strategiperspektivet.** Förmågan beter sig inte, och ArchiMate saknar motsvarigheten. Avvisat.
- **Förmågetjänst som det som leveransprodukten paketerar, bredvid produkten.** För nischat när produkt är det bredare begreppet; ordet lades på produkten i stället. Avvisat.
- **Förmågeprodukt som term på Leveransprodukt (`C-174`)**, luckan mellan rummen, valt i grillningens andra runda. Då får en verksamhetsprodukt inte kallas förmågeprodukt fast den kommer ur en lösning på samma sätt; luckan lämnar ut åt vem som helst utanför rummet. Avvisat av Nicklas samma dag. **Som föredragen term** på Leveransprodukt, med Leveransprodukt som andra. Arkitekter i förvaltningen kan pm3:s ord. Avvisat. **Termen struken.** Nicklas saknar då ett eget ord för det lösningen levererar. Avvisat.

## Konsekvenser

- `C-014 Produkt` med termen Förmågeprodukt; `C-174 Leveransprodukt` med ny definition; anmärkningar i `C-055`, `C-014`, `C-173`, `C-174`, `C-075` och `C-127`. Mappningstabellerna ändras inte.
- Inga nya elementtyper, relationstyper eller rutor: draw.io-mallen är oförändrad. Generatorn körs om ändå.
- ADR 0020:s skrivning att verksamhetsprodukten levereras av verksamheten och leveransprodukten av en lösning gäller inte längre; det ADR:et står kvar oförändrat.
- Nästa fråga är aktiviteten och OMG:s notationer (ADR 0022).
