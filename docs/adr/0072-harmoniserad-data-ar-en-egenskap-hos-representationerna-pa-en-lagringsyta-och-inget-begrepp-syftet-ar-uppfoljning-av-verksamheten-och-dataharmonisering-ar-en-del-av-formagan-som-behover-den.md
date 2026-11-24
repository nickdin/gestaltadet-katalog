# Harmoniserad data är en egenskap hos representationerna på en lagringsyta och inget begrepp, syftet är uppföljning av verksamheten, och Dataharmonisering är en del av förmågan som behöver den

Beslutat av Nicklas 24 november 2026, när katalogen saknade ett ord för data som har hämtats in från flera källor och ordnats för fler frågor än en.

## Sammanhang

Datakategori (`C-201`) delar in informationsobjekt efter hur verksamheten håller och fångar dem. Den säger inget om hur färdig datan är för att användas. Sammanställning (`C-162`) sätts samman för ett bestämt ändamål. Datan i ett datalager ordnas i stället för att räcka även för frågor som ingen har ställt än. Arbetsnamnet var harmoniserad data, och förmågan som tar fram den kallades Dataharmonisering (#219).

Tre frågor behövde svar:

- Är harmoniserad data ett begrepp, och i så fall under vad?
- Hur går den ihop med dataskyddsförordningens krav på ett bestämt ändamål?
- Är harmoniseringen en egen förmåga?

Frågorna avgjordes på fallet Myndigheten för föreningsstöd, där Analysenheten läser Ansökan, Beslut och Utbetalning in i datalagret.

## Beslut

### Egenskapen

- **Inget i datalagret är namnlöst.** Beslut 68 säger att ansökningstabellen är samma Ansökan i en ny form: en representation (`C-085`) på en lagringsyta (`C-165`). Det som saknade ord var en egenskap hos tabellerna tillsammans.
- **Harmoniserad data är representationer på en lagringsyta som är ordnade för fler frågor än en.** Varje objekt hålls helt, varje objekt följer den definition dess ägare har gett det, och objekten går att koppla ihop.
- **Katalogen får inget nytt begrepp.** Harmoniserad data är inget eget slags informationsobjekt (`C-060`), ingen produkt (`C-014`) och ingen indelning bredvid datakategorin. Lagringsyta (`C-165`) förklarar ordet i sin anmärkning.
- **Tabellen med Förening är inte harmoniserad än.** Datalagret hämtar den ur Ärendesystemet och inte ur Föreningsregistret, som är källan. Antalet medlemmar skiljer sig därför ibland.

### Syftet

- **Harmoniserad data har ett syfte, och syftet är brett.** Vanligen är det uppföljning av verksamheten. Ansökningstabellen tjänar analysfunktionens uppföljning och räcker därför för frågor som ingen har ställt än. Katalogen skriver aldrig att sådan data saknar ändamål.
- **Lagen nämner syftet.** Patientdatalagen räknar upp ändamålet "administration, planering, uppföljning, utvärdering och tillsyn av verksamheten" (2 kap. 4 §). Myndighetsförordningen säger att ledningen ska se till att verksamheten "bedrivs effektivt" och att den "redovisas på ett tillförlitligt och rättvisande sätt" (3 §).
- **Skillnaden mot en sammanställning är att objekten hålls hela.** Utbetalningar per kommun väljer ut uppgifter för en fråga. Ansökningstabellen rymmer hela Ansökan.
- **För personuppgifter ska behovet finnas nu.** Personuppgifter ska vara "adekvata, relevanta och inte för omfattande i förhållande till de ändamål för vilka de behandlas" (dataskyddsförordningen, artikel 5.1 c). Ingen analys använder Företrädare, och kopian stannar därför utanför datalagret. Beslut 68 står kvar oförändrat.
- **Kravet på bevarande ger inte kopian något syfte.** Myndigheten bevarar ärendena och deras företrädare i Ärendesystemet och Föreningsregistret. Datalagret är inget arkiv.

### Förmågan

- **Dataharmonisering klarar provet för en förmåga.** Chefen för Analysenheten kan kräva att varje objekt i datalagret hämtas ur sin källa. Målet rör inte målet för rapporten till regeringen, och det står kvar om myndigheten byter analysplattform (beslut 65).
- **Exemplet delar Uppföljning och rapportering i Dataharmonisering och Analys.** Chefen för Analysenheten delar förmågan efter arkitektens bedömning om källan för Förening, för att kunna sätta målet.
- **Vem som behöver förmågan avgör var den sitter, inte om den finns.** Bara Uppföljning och rapportering behöver Dataharmonisering i dag, och därför är den en del av den förmågan. Behöver Tillsyn den också blir den en egen förmåga bredvid (beslut 69).
- **Dataharmonisering äger inga begrepp och inga informationsobjekt.** Den upprättar representationerna i datalagret.
- **Katalogen får inget begrepp för förmågan.** Dataharmonisering är en förmåga hos en organisation, alltså en förekomst av Verksamhetsförmåga (`C-069`).

## Övervägda alternativ

- **Harmoniserad data blir ett begrepp under informationsobjekt.** Ansökan i datalagret hade då varit ett annat objekt än Ansökan i Ärendesystemet, mot beslut 68. Avvisat.
- **Harmoniserad data blir en femte datakategori eller en indelning bredvid.** Kategorin säger hur verksamheten håller och fångar objektet, och objektet behåller sin kategori i datalagret. Avvisat.
- **Harmoniserad data definieras som data utan bestämt ändamål.** Tabellen med Företrädare hade då fått ligga kvar för att den kan behövas senare. Avvisat.
- **Kopian av Företrädare läggs tillbaka i datalagret, eftersom syftet rymmer framtida frågor.** Dataskyddsförordningen kräver att uppgifterna inte är fler än ändamålet behöver, och tre fynd i exemplet bygger på att kopian togs bort. Avvisat.
- **Kopian av Företrädare stannar för att ärendena ska bevaras.** Bevarandet sker i källan. Varje kopia av en bevarad handling hade annars fått ligga kvar överallt, mot beslut 68. Avvisat.
- **Dataharmonisering väntar tills fler än Analysenheten läser ur datalagret.** En förmåga prövas på om den kan få ett eget mål, inte på vem som använder den. Avvisat.

## Konsekvenser

- Ingen definition ändras, och inga begrepp eller relationer tillkommer.
- Lagringsyta (`C-165`), Sammanställning (`C-162`), Datakategori (`C-201`) och exemplet Myndigheten för föreningsstöd har fått text om detta.
- Exemplets förmåga Uppföljning och rapportering består av Dataharmonisering och Analys. Lösningen i domänen Uppföljning realiserar helheten, och ingen av delarna har en egen lösning.
- Fallet där en analys börjar använda Företrädare, så att kopian får ett behov, är inte skrivet. Det tas upp när exemplet behöver det.
