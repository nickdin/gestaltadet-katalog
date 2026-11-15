# Båda exemplen bär fynd med flit, varje exempel visar också en skillnad som inte är ett fynd, och exemplen byggs i tre steg från nuläge till målarkitektur

Beslutat av Nicklas 15 november 2026, när exempelorganisationerna skulle ritas och frågan kom upp om ritningarna visar läsaren några fynd.

## Sammanhang

Ritningarna i `layout/` visar bara katalogens begrepp. Ingen ritning visar ett exempel. Nicklas beställde ärendet #161 i grillningen för #157: ritningar och arkitekturbeskrivningar av exempelorganisationerna är en mycket viktig pusselbit för läsarna.

Exemplen hade ett enda fynd. Hos Brinkstadsbostäder äger teknisk chef lösningen Felanmälan, och bovärdarna arbetar på tre områdeskontor bredvid. Myndigheten för föreningsstöd var motbilden, där allt stämmer.

Grillningens första runda frågade vilka domäner exemplen har. Nicklas vände på frågan: exemplen ska visa fynden för en läsare, så domänerna och organisationen ska inte stämma överens överallt. Först bestäms vilka fynd läsaren ska se. Sedan byggs indelningen så att fynden uppstår.

## Beslut

- **Båda exemplen bär fynd med flit.** Myndigheten för föreningsstöd är inte längre den rena motbilden. Motbilden finns inuti varje exempel: en domän som håller bredvid en som inte gör det. Bidragsgivningen står kvar som domänen som håller.
- **Varje exempel visar också en skillnad som inte är ett fynd.** En verksamhetsdomän (`C-008`) är aldrig en organisationsenhet, så att de två inte sammanfaller är inget fynd i sig. Ett fynd är när skillnaden gör att ingen kan väga eller svara. Läsaren ska se båda slagen.
- **Myndigheten för föreningsstöd har fem domäner direkt under generaldirektören.** Bidragsgivning ägs av chefen för Bidragsenheten. Registerföring och tillsyn ägs av chefen för Register- och tillsynsenheten. Uppföljning ägs av chefen för Analysenheten. IT och HR har var sitt inre uppdrag direkt från generaldirektören.
- **Tillsyn är en domän inuti Registerföring och tillsyn.** En gruppchef har fått den med egen ram. Chefen för enheten omsluter både registret och tillsynen och kan väga dem mot varandra. Det är skillnaden som inte är ett fynd.
- **Verksamhetsstöd är en enhet men ingen domän.** Ingen chef håller en ram för hela enheten. Vill IT ha en tekniker till och HR en rekryterare till kan bara generaldirektören väga dem mot varandra. Det är myndighetens fynd. Ekonomi, juridik och kommunikation är grupper i enheten utan egen domän.
- **Brinkstadsbostäder har åtta domäner direkt under vd.** Teknik ägs av teknisk chef och rymmer underhåll, nyproduktion och lösningen Felanmälan. Uthyrning ägs av uthyrningschefen och rymmer lösningen Hyra. De tre områdeskontoren är var sin domän med var sin kontorschef. Ekonomi, IT och Kommunikation är stöddomäner.
- **Kundcenter är en grupp i Uthyrning.** Gruppen har en egen chef men ingen egen domän. Kundcenter tar emot felanmälan, så fyndet i Felanmälan berör fyra chefer: teknisk chef, uthyrningschefen, chefen för kundcenter och kontorschefen. Bara vd håller alla fyra.
- **Attesträtten är bostadsbolagets skillnad som inte är ett fynd.** Kontorschefen godkänner underhållskostnader upp till 100 000 kronor. Det är beslutanderätt inom en ram som styrelsen redan har satt.
- **Exemplen byggs i tre steg.** Steg ett är nuläget: organisationsschemat, domänindelningen och en gemensam ritning med fynden. Det är en nulägesarkitektur (`C-057`) sedd ur styrningen. Steg två är flytten: en målarkitektur (`C-054`) där ett fynd är löst och en gapanalys (`C-105`) som visar vad som tillkommer och upphör. Steg tre är ett fynd som ledningen väljer att leva med, och varför.
- **Felanmälan flyttas, och fyndet i Verksamhetsstöd accepteras.** Felanmälan kostar varje vecka på tre kontor. Hos myndigheten väger generaldirektören en tekniker mot en rekryterare några gånger om året, och det hinner hen med. Läsaren ser då att ett fynd inte alltid ska åtgärdas.
- **Varje fynd pekar på en fråga i provet för Livskraft (`C-216`).** Felanmälan är ett nej på fråga 1: domänen rymmer inte både utformningen och produktionen. Läsaren lär sig provet genom exemplen, och frågor som saknar exempel visar vilka fynd som fattas.
- **Ett fynd ritas som en numrerad markering med en rad under ritningen.** Raden säger fyndet i en mening. Skillnaden som inte är ett fynd får samma slags markering i en annan färg, med orden inget fynd. Färg och form avgörs i #149.
- **Ritningarna ritas för hand i draw.io, i mappen `layout/Exempel`.** Exemplens domäner och enheter skrivs inte in i lagret som element. Det gör exempellagret i #2.
- **Bostadsbolaget ritas först.** Fyndet där stod redan i texten.
- **Fynd blir inget begrepp i det här beslutet.** Frågan har ett eget ärende.

## Övervägda alternativ

- **Domänerna följer enheterna hos myndigheten.** Rekommendationen i första rundan, med en chef över Verksamhetsstöd som omsluter IT och HR. Ritningen hade då visat att allt stämmer och inget annat. Avvisat.
- **Myndigheten står kvar som ren motbild.** Läsaren hade behövt jämföra en myndighet med ett bolag för att se skillnaden mellan rätt och fel. Avvisat för motbilden inuti varje exempel.
- **Fyndet att bidraget beslutas hos Bidragsenheten och betalas ut hos ekonomi ritas nu.** Det föregriper #152, som avgör om en process får gå genom flera lösningar. Uppskjutet dit.
- **Exemplens element skrivs in i lagret, och ritningarna byggs ur dem.** Det är att börja på #2 bakvägen. Avvisat nu. Kostnaden är att en ändring i ett exempel görs på två ställen, i texten och i ritningen, tills #2 är byggt.
- **Fynd definieras som begrepp här.** En definition tillkommer bara i en egen grillning. Att acceptera ett fynd liknar dessutom avvikelse (`C-213`) och bedömning (`C-185`) utan att vara någon av dem. Uppskjutet.

## Konsekvenser

- `docs/exempel/myndigheten-for-foreningsstod.md` och `docs/exempel/brinkstadsbostader.md` har fått var sitt avsnitt Organisation och domäner.
- Inga begrepp, definitioner eller relationer är ändrade.
- En sak är inte avgjord. Provets fråga 6 frågar om den som beslutar hinner möta komplexiteten, och generaldirektören hinner. Vilken fråga fyndet i Verksamhetsstöd är ett nej på avgörs i steg tre.
- Ritningarna i steg ett byggs i egna ärenden under #161. Steg två, steg tre och frågan om Fynd som begrepp har egna ärenden.
