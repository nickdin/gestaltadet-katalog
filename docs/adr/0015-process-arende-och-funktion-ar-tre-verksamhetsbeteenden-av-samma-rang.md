# Process, ärende och funktion är tre verksamhetsbeteenden av samma rang

Beslutat av Nicklas 19 oktober 2026, när han frågade om process, ärende och funktion är tre företeelser av samma rang. Beslutet kom i samma samtal som beslut 14 och ändrar beslut 12:s led om löpande ansvar: ett löpande ansvar är ingen förmåga.

## Sammanhang

Nicklas frågade om funktion, ärende (i CMMN:s mening) och process är tre företeelser av samma rang, som alla kan realisera en förmåga. Beslut 12 hade sagt att ett löpande ansvar, det som inte går att namnge med verb och objekt, är en verksamhetsförmåga (`C-069`). `C-077 Funktion` hade sagt att verksamheten har förmågor, inte funktioner. Nicklas ifrågasatte det: en förmåga är vad verksamheten kan, en möjlighet, medan registerhållningen och tillsynen pågår. Samtidigt är Registerhållning och Tillsyn rimliga förmågor, realiserade av processer, ärenden och funktioner.

## Beslut

- Verksamhetsfunktion (`C-158`) är en elementtyp i verksamhetsperspektivet, ArchiMates Business Function: beteende utan början och slut, samlat efter kompetens eller resurs. Ett löpande ansvar är en verksamhetsfunktion. `C-077 Funktion` vidgas till familjebegrepp för verksamhets-, applikations- och teknikfunktion.
- Process, ärende och funktion är tre syskon av samma rang under familjebegreppet Verksamhetsbeteende (`C-157`). Ingen står över en annan. Det som skiljer dem är hur arbetet är ordnat: processen har start, slut och fast stegföljd; ärendet har start och slut, men stegen väljs efter hand; funktionen har varken start eller slut. Alla tre kan realisera en förmåga, har åtkomst till verksamhetsobjekt och kan utlösa och rymma varandra. Ärendet som typ blev handläggning (`C-160`) i beslut 17.
- Förmågan (`C-069`) är en möjlighet, och verksamhetsbeteenden realiserar den. Förmågor namnges med substantiv (Registerhållning, Tillsyn, Verksamhetsstyrning). Processer och funktioner namnges båda med verb i infinitiv plus objekt, så att typen bär skillnaden, inte namnet. Produkten är erbjudandet mottagaren får.
- "Arkitekturfunktionen är en lösning" står kvar i `C-077`: lösningen är ordningen av människor och verktyg, funktionen det den gör.

## Övervägda alternativ

- **Löpande ansvar är tjänster (`C-127`) när någon tar emot dem.** Internt löpande arbete, som att hålla riskregistret, får då ingen typ. Avvisat.
- **Löpande ansvar är processer som upprepas utan slut.** Det suddar ut just den skillnad kartan ska visa. Avvisat.
- **Funktionen som behållare, process och ärende som det som sker i den.** Det är ArchiMates vanliga bild, men den gör funktionen till organisation i förklädnad. Avvisat.
- **Egen namnform för funktioner.** Det ger krystade namn. Avvisat.

## Konsekvenser

- `C-157 Verksamhetsbeteende` (familjebegrepp), `C-158 Verksamhetsfunktion` (elementtyp, generisk `C-077`, täcks av `C-109`). Anmärkningarna i `C-069`, `C-077` och `C-130` är omskrivna. Beslut 12:s regel om namn står kvar, men dess led om löpande ansvar gäller inte längre.
- I `mapping/archimate.yaml` mappas Business Function till `C-158`. I `mapping/aris.yaml` förblir OT_FUNC omappat, eftersom en EPC-funktion är ett steg i en process, och `C-158` står under `unmapped-concepts`.
- Kartans löpande ansvar typas om till verksamhetsfunktioner: Hålla registret, Hantera risker och intern styrning och kontroll, Analysera omvärlden, Förmedla kunskap, Ge råd om säkerhet. Det är öppet vilka av dem som rymmer en årlig process.
- En förmågebild ritas med förmågorna och det som realiserar dem.
