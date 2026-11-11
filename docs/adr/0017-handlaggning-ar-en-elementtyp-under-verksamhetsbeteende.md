# Handläggning är en elementtyp under verksamhetsbeteende, och ärendet är dess objekt

Beslutat av Nicklas 19 oktober 2026, när katalogen bara kunde beskriva arbete i ärenden som processer med fast stegföljd. Frågan kom från interlingua, programmet som läser katalogen. Beslutet väcker den typ beslut 14 sköt upp och fyller platsen beslut 15 lämnade öppen.

## Sammanhang

Svenska myndigheter arbetar i ärenden, men katalogen kunde bara beskriva dem som processer, med fast stegföljd. Beslut 15 gjorde process, ärende och funktion till tre verksamhetsbeteenden av samma rang, men lät ärendet som typ vänta. Beslut 14 ritade verkliga fall som processer, med raden "handläggs som ärende, utan fast stegföljd" bland osäkerheterna. Hos Myndigheten för föreningsstöd vore det att handlägga en ansökan om bidrag, att pröva ett återkrav och att granska en förening i tillsyn. Samma beslut sade att det enskilda ärendet är ett verksamhetsobjekt, och `C-159` nämnde ett ärende som sitt första exempel. Hade typen hetat Ärende hade samma ord stått för två saker: det som handläggs och handläggningen av det.

Interlingua självt behöver inget. Typen är ett begrepp, en rad i perspektivets `covers` och rader i mappningstabellerna, och programmet känner ingen processtyp vid namn (interlinguas beslut 6 och 11).

## Beslut

- Handläggning (`C-160`) är en elementtyp i verksamhetsperspektivet: verksamhetsbeteende kring ett enskilt ärende, med start och slut, där stegen väljs efter hand. Det är det CMMN kallar ett case. Den har generisk relation till `C-157 Verksamhetsbeteende`. Någon perspektivövergripande familj att peka på finns inte, eftersom ärenden bara finns i verksamheten.
- Ordet ärende står för objektet: det enskilda ärendet är ett verksamhetsobjekt (`C-159`) som handläggningen har åtkomst till. Definitionerna i `C-157` och `C-159` och anmärkningen i `C-069` säger handläggning där de sade ärende.
- Handläggningar namnges som processer och funktioner, med verb i infinitiv och objekt. Typen bär skillnaden (beslut 15).
- Stegen en handläggning väljer bland är processer och funktioner som den rymmer eller utlöser. `C-126 Aktivitet` förblir en del av en process och inget annat. Ett enskilt steg som inte är en process är text i elementet.
- `C-130` och `C-158` behåller sina generiska länkar till `C-070 Process` och `C-077 Funktion`, de perspektivövergripande familjer som applikations- och tekniktyperna delar. `C-157` är en familj i text; det är priset för att ett begrepp har en generisk länk.
- ArchiMate har inget case-element. Handläggning står som andra begrepp på raden Business Process, märkt tveksam. En export skriver en handläggning som Business Process, så att den syns i andras ArchiMate-ritningar; skillnaden går förlorad på vägen ut. En import läser varje Business Process som verksamhetsprocess, radens första begrepp. I ARIS står `C-160` under `unmapped-concepts`, eftersom en EPC har fast stegföljd.
- De fall som ritats som processer med raden om ärende får typen handläggning, och raden tas bort.

## Övervägda alternativ

- **Typen heter Ärende**, CMMN:s ord. Då måste exemplet i `C-159` och meningen i beslut 14 sluta kalla objektet ärende, annars står ett ord för både objekt och beteende. Avvisat.
- **Typen heter Ärendehantering**, beslut 14:s ord. Samma verkan som Handläggning, men ett längre ord. Avvisat.
- **Handläggning är en sorts process.** Avvisat av definitionerna: en process är en sekvens, och en handläggning har ingen.
- **Omappad i ArchiMate**, som Initiativ (beslut 10). Initiativets Work Package ligger utanför den kärna som tabellen täcker; här finns en närmaste typ. En handläggning som försvinner ur varje ritning andra ser är värre än en som ritas som process med en anmärkning. Avvisat.
- **Flytta `C-126 Aktivitet`:s helhet till `C-157`**, så att en handläggning kan rymma aktiviteter. Det skär av aktiviteten från applikations- och teknikprocesser, som också har aktiviteter. Avvisat.
- **Peka `C-130` och `C-158` på `C-157`.** Det bryter länken till Process och Funktion. Avvisat.

## Konsekvenser

- `C-160 Handläggning` (elementtyp, generisk `C-157`, täcks av `C-109`).
- `mapping/archimate.yaml`: Business Process är `[C-130, C-160]`, tveksam. `mapping/aris.yaml`: `C-160` under `unmapped-concepts`.
- Beslut 14:s "Ärendehantering som egen typ väcks inte nu" gäller inte längre.
- Interlingua, dess ordlista och exempellagret rörs inte. Frågan om förmågetjänst, som kom samma väg från interlingua, tas i ett eget beslut (beslut 21).
- Det en handläggning har som en process saknar, en milstolpe till exempel, är ett nytt ärende den dag en beskrivning behöver det.
