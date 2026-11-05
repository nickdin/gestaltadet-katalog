# Myndigheten för föreningsstöd

En påhittad statlig myndighet. Den finns för att katalogens exempel ur förvaltningen ska hämtas från ett och samma ställe. Exemplen: uppdrag, mål, portfölj, handläggning, ärendebeslut, beslutslogik, informationsägare och klassning. Allt här är uppfunnet. Det som liknar verkliga myndigheter är den allmänna förvaltningens, inte någon enskild myndighets.

## Vad den gör

Myndigheten fördelar statsbidrag till ideella föreningar, för register över föreningarna och deras företrädare och ser till att pengarna används som avsett. Den har omkring 120 anställda på en ort, och en generaldirektör leder den. Den har fyra enheter: Bidragsenheten, Register- och tillsynsenheten, Analysenheten och Verksamhetsstöd, där IT, ekonomi, juridik och kommunikation sitter.

## Uppdrag och styrning

Regeringen fastställer uppdraget i myndighetens instruktion. Den ger fyra uppdrag:

1. **Bidragsgivning**: att pröva ansökningar om och betala ut statsbidrag till ideella föreningar, i form av verksamhetsbidrag per år och projektbidrag för en avgränsad insats.
2. **Registerföring**: att föra ett register över bidragsberättigade föreningar och deras företrädare.
3. **Tillsyn**: att granska att bidrag använts enligt villkoren och att besluta om återkrav när de inte har det.
4. **Uppföljning**: att följa föreningslivets utveckling och rapportera till regeringen.

Regleringsbrevet ger varje år anslag, mål och återrapporteringskrav. Årets mål är till exempel att nio av tio ansökningar ska vara beslutade inom fyra månader och att andelen bidrag som återkrävs ska minska. Ett annat är att handläggningskostnaden per ärende ska redovisas. Förvaltningslagen styr hur varje ärende handläggs. Bidragsförordningen säger vem som kan få bidrag och hur det beräknas. Myndighetens egna principer är styrning som generaldirektören fastställer, till exempel att en förening alltid ska kunna sköta sitt ärende i e-tjänsten.

Utvecklingsarbetet samlas i en utvecklingsportfölj som generaldirektören prioriterar och finansierar. Just nu rymmer den två initiativ: en ny e-tjänst för redovisning och automatisk beräkning av verksamhetsbidraget.

## Förmågor

Fem förmågor säger vad myndigheten kan göra, oavsett vem som gör det eller med vilket system:

- **Bidragsprövning**: att avgöra om en förening har rätt till bidrag och hur mycket.
- **Utbetalning och återkrav**: att betala ut beviljat bidrag och kräva tillbaka det som inte använts rätt.
- **Registerhållning**: att veta vilka föreningar som finns, vem som företräder dem och vart pengarna ska.
- **Tillsyn**: att granska hur bidrag använts.
- **Uppföljning och rapportering**: att sammanställa och rapportera till regeringen.

## Processer och handläggningar

Den årliga **ansökningsomgången** är en process med fasta steg: utlysning öppnar, ansökningar kommer in, de fördelas på handläggare, beslut fattas, bidrag betalas ut, redovisning begärs in. **Handläggningen av en ansökan** inom den väljer sina steg efter hand. Myndigheten begär komplettering om något saknas och hämtar ett yttrande från registret om företrädaren är ny. Beslutet blir bifall, delvis bifall eller avslag. Varje beslut i ett enskilt ärende är ett ärendebeslut.

Återkravsärendet startar när en redovisning visar att pengar använts fel eller inte alls. Tillsynsärendet startar när en anmälan kommer in eller stickprovet pekar ut en förening. Registreringen av en ny företrädare är en kort handläggning med kontroll mot folkbokföringen.

Beslutslogiken är de regler som ger utfallet ur indata. Verksamhetsbidragets storlek beräknas ur antal medlemmar och antal lokalavdelningar. En förening är bidragsberättigad om den är demokratiskt uppbyggd, har funnits i två år och har minst tusen medlemmar. Reglerna står i bidragsförordningen och i myndighetens föreskrifter, och de används i varje ärende.

## Informationsobjekt

- **Förening**: namn, organisationsnummer, säte, antal medlemmar. Öppen information.
- **Företrädare**: personuppgifter om styrelseledamöter och firmatecknare. Känslig: personuppgifter som kan användas för bedrägeri.
- **Kontonummer**: föreningens konto för utbetalning. Känslig.
- **Ansökan**, **Redovisning**: det föreningen lämnar in. Intern tills beslut.
- **Beslut**: bifall, delvis bifall, avslag, återkrav. Öppen när det är fattat, allmän handling.
- **Utbetalning**, **Återkrav**: beloppet och dess väg.
- **Tillsynsärende**: anmälan, granskning, utfall.

Chefen för Bidragsenheten är informationsägare för Ansökan, Redovisning, Beslut, Utbetalning och Återkrav. Chefen för Register- och tillsynsenheten är det för Förening, Företrädare, Kontonummer och Tillsynsärende. Informationsägaren beslutar klassningen och vad som får göras med informationen. Förteckningen över alla företrädare är känsligare än varje företrädare för sig.

Chefen för Bidragsenheten är också processägare för handläggningen av ansökan och linjechef för enheten som handlägger. Det är det vanliga fallet: de tre rollerna är samma person, och delningen mellan dem syns inte.

Analysenheten läser Ansökan, Beslut och Utbetalning in i ett datalager, en lagringsyta i myndighetens analysplattform. Den sätter samman Utbetalningar per kommun och räknar fram Riskindikator per förening. Chefen för analysenheten är processägare för analysfunktionen och informationsägare för de två objekt den upprättar. Läsningen av Bidragsenhetens objekt sker inom det Bidragsenhetens chef beslutat.

## System

- **Föreningsportalen**: e-tjänsten där föreningen ansöker, kompletterar och redovisar, med inloggning för företrädaren.
- **Ärendesystemet**: handläggarens arbetsyta och myndighetens diarium.
- **Föreningsregistret**: föreningar, företrädare och kontonummer; hämtar folkbokföringsuppgifter från Skatteverket.
- **Ekonomisystemet**: utbetalningar, återkrav och bokföring.
- **Beräkningstjänsten**: räknar ut verksamhetsbidraget ur registrets uppgifter, som Ärendesystemet anropar.

Alla fem körs på en gemensam plattform i myndighetens datahall, utom Föreningsportalen som en leverantör driftar.

Handläggningen av en ansökan är en lösning: processen, Bidragsenhetens handläggare, Ansökan, Beslut och Utbetalning, och Ärendesystemet. Bidragsenhetens chef är dess lösningsägare, håller ramen och svarar för målet att nio av tio ansökningar är beslutade inom fyra månader. Lösningen använder Föreningsregistret som leveransprodukt. Registerlösningen tar fram och vidmakthåller registret, handläggningen ställer krav på det, och de två kan ändras var för sig. Kopplingen är lös. Myndighetens referensarkitektur antar provet för ett snitt som arkitekturprincip: en lösning har en ägare med ram, och det två lösningar delar bryts ut som en egen lösning.

## Vem den finns för

Målgruppen är ideella föreningar och de människor som företräder dem, oftast ideellt och vid sidan av ett arbete. Deras behov är att få stöd till verksamheten utan att administrationen äter upp den. Resan de går igenom är att starta en förening, få den att växa och hålla den vid liv över åren. Myndigheten är en av flera parter i den, med Skatteverket, kommunen och banken. Värdeerbjudandet är ett bidrag som går att söka på en kväll och som betalas ut i tid.

## I katalogen

Myndigheten står för förvaltningens mekanik. Hämta härifrån exempel på:

- uppdrag (C-149), verksamhetsmål (C-169), portfölj (C-011) och initiativ (C-012)
- verksamhetsförmåga (C-069), verksamhetsprocess (C-130) och handläggning (C-160)
- ärendebeslut (C-181) och beslutslogik (C-178)
- informationsobjekt (C-060), uppgift (C-161) och sammanställning (C-162)
- informationsägare (C-167), processägare (C-206) och linjechef (C-207) i en och samma person
- lösning (C-055) med handläggningen och Föreningsregistret som leveransprodukt (C-174) i lös koppling (C-211)
- ansvar (C-209) och ram (C-210) hos Bidragsenhetens chef
- arkitekturprincip (C-040) med provet för ett snitt
- informationstillgång (C-166), applikation (C-071) och plattform (C-072)
- målgrupp (C-145), behov (C-146), resa (C-147) och värdeerbjudande (C-148)

Det fysiska, kunden i vardagen och tekniken i husen hämtas från bostadsbolaget.
