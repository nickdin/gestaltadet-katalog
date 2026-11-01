# Handläggning är en elementtyp under verksamhetsbeteende, och ärendet är dess objekt

Beslutat av Nicklas i en grillning av en fråga som kom från interlingua. Väcker den typ ADR 0014 sköt upp och fyller platsen ADR 0015 lämnade öppen.

## Sammanhang

Svenska myndigheter arbetar i ärenden, och katalogen kunde bara beskriva dem som processer, med fast stegföljd. ADR 0015 gjorde process, ärende och funktion till tre verksamhetsbeteenden av samma rang men lät ärendet som typ vänta. ADR 0014 ritade verkliga fall som processer med raden "handläggs som ärende, utan fast stegföljd" bland osäkerheterna; hos Myndigheten för föreningsstöd vore det att handlägga en ansökan om bidrag, att pröva ett återkrav och att granska en förening i tillsyn. Samma ADR sade att det enskilda ärendet är ett verksamhetsobjekt, och `C-159` nämnde ett ärende som sitt första exempel. Hade typen hetat Ärende hade samma ord stått för det som handläggs och för handläggningen av det.

Interlingua självt behöver inget: typen är ett begrepp, en rad i perspektivets `covers` och rader i mappningstabellerna, och programmet känner ingen processtyp vid namn (interlinguas ADR 0006 och 0011).

## Beslut

- Handläggning (`C-160`) är en elementtyp i verksamhetsperspektivet: verksamhetsbeteende kring ett enskilt ärende, med start och slut, vars steg väljs efter hand. Det är det CMMN kallar ett case. Generisk relation till `C-157 Verksamhetsbeteende`; det finns ingen perspektivövergripande familj att peka på, eftersom ärenden bara finns i verksamheten.
- Ordet ärende står för objektet: det enskilda ärendet är ett verksamhetsobjekt (`C-159`) som handläggningen har åtkomst till. Definitionerna i `C-157` och `C-159` och anmärkningen i `C-069` säger handläggning där de sade ärende.
- Handläggningar namnges som processer och funktioner, med verb i infinitiv och objekt; typen bär skillnaden (ADR 0015).
- Stegen en handläggning väljer bland är processer och funktioner den rymmer eller utlöser. `C-126 Aktivitet` förblir en del av en process och inget annat; ett enskilt steg som inte är en process är text i elementet.
- `C-130` och `C-158` behåller sina generiska länkar till `C-070 Process` och `C-077 Funktion`, de perspektivövergripande familjerna som applikations- och tekniktyperna delar. `C-157` är en familj i text, priset för att ett begrepp har en generisk länk.
- ArchiMate har inget case-element. Handläggning står som andra begrepp på raden Business Process, märkt tveksam: en export skriver en handläggning som Business Process så att den syns i andras ArchiMate-ritningar, med skillnaden förlorad på vägen ut, och en import läser varje Business Process som verksamhetsprocess, radens första begrepp. I ARIS står `C-160` under `unmapped-concepts`: en EPC har fast stegföljd.
- De fall som ritats som processer med raden om ärende typas om till handläggningar och raden tas bort.

## Övervägda alternativ

- **Typen heter Ärende**, CMMN:s ord. Då måste `C-159`:s exempel och ADR 0014:s mening sluta kalla objektet ärende, eller så står ett ord för både objekt och beteende. Avvisat.
- **Typen heter Ärendehantering**, ADR 0014:s ord. Samma verkan som Handläggning, ett längre ord. Avvisat.
- **Handläggning är en sorts process.** Avvisat av definitionerna: en process är en sekvens, en handläggning har ingen.
- **Omappad i ArchiMate**, som Initiativ (ADR 0010). Initiativets Work Package ligger utanför den kärna tabellen täcker; här finns närmaste typ, och en handläggning som försvinner ur varje ritning andra ser är värre än en som ritas som process med en anmärkning. Avvisat.
- **Flytta `C-126 Aktivitet`:s helhet till `C-157`** så att en handläggning kan rymma aktiviteter. Skär av aktiviteten från applikations- och teknikprocesser, som också har aktiviteter. Avvisat.
- **Peka `C-130` och `C-158` på `C-157`.** Bryter länken till Process och Funktion. Avvisat.

## Konsekvenser

- `C-160 Handläggning` (elementtyp, generisk `C-157`, täcks av `C-109`).
- `mapping/archimate.yaml`: Business Process är `[C-130, C-160]`, tveksam. `mapping/aris.yaml`: `C-160` under `unmapped-concepts`.
- ADR 0014:s "Ärendehantering som egen typ väcks inte nu" gäller inte längre.
- Interlingua, dess ordlista och exempellagret rörs inte. Frågan om förmågetjänst, som kom samma väg från interlingua, tas i ett eget beslut (ADR 0021).
- Vad en handläggning har som en process saknar, en milstolpe till exempel, är ett nytt ärende den dag en beskrivning behöver det.
