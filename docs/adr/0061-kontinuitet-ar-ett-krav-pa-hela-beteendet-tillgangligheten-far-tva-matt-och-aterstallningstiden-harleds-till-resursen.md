# Kontinuitet är ett krav på hela beteendet, tillgängligheten får två mått, och återställningstiden härleds till resursen

*[[0064-informationshanteringen-har-tre-perspektiv-informationsforsorjningen-ar-arkitekturarbete-och-varje-forteckning-halls-av-ett-perspektiv|Beslut 64]] lägger till en punkt här. Kontinuitetskravet och återställningstiden står i dokumentationen av kontinuiteten, på var sin rad.*

Beslutat av Nicklas 18 november 2026, när [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|beslut 58]] hade gjort tillgängligheten till ett enda mått och lämnat skillnaden mot kontinuitet till ett eget ärende.

## Sammanhang

[[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|Beslut 58]] gjorde tillgängligheten till ett krav som processägaren (`C-206`) ställer på paret beteende och informationsobjekt. Måttet var ett: hur länge beteendet klarar sig utan objektet. Ärendet #181 frågade om katalogen ska skilja tillgänglighet i vanlig drift från kontinuitet vid en kris.

Underlaget `docs/research/informationsklassning-var-klassen-sitter.md` visar hur kontinuitetsmetoderna gör. De sätter längsta tålbara avbrott på aktiviteten, återställningstiden på resursen och återställningspunkten på informationen. En av metoderna, BSI 200-4, skiljer dessutom tillgänglighet i vanlig drift från kontinuitet. Där får ett system hög tillgänglighet men inget kontinuitetskrav, eftersom verksamheten klarar sig utan det under en kris.

Måttet i [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|beslut 58]] är redan en avbrottstid, alltså kontinuitetsmetodernas sätt att mäta. Det som saknades var något annat: ett krav på att beteendet ska gå att utföra fast en resurs är borta.

Grillningen gick tre rundor och avgjorde varje fråga på ett fall hos Brinkstadsbostäder eller Myndigheten för föreningsstöd. Tiderna och reservrutinen i fallen är antaganden för grillningen. De står inte i exemplen.

## Beslut

### Två krav

- **[[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|Beslut 58]] står fast.** Processägaren ställer kravet, nivåerna står i en förteckning utanför lagret, och kartan bär inga nivåer. Det här beslutet säger att kraven är två och var det andra fästs.
- **Tillgänglighet och kontinuitet är två krav.** Anta att fastighetssystemet hos Brinkstadsbostäder ligger nere en hel dag och att en vattenläcka anmäls per telefon. Tillgängligheten säger att Åtgärda en felanmälan klarar en timme utan hyresgästens telefonnummer. Det är ett krav på att systemet ska finnas. Kontinuiteten säger att läckan ska åtgärdas fast systemet är nere. Det är ett krav på att processen ska gå att utföra utan systemet.
- **Tillgängligheten står kvar på paret beteende och objekt.** Den fästs där beteendet har åtkomst till objektet (`C-101`), som i [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|beslut 58]].
- **Kontinuiteten fästs på hela beteendet.** Kravet är den längsta tid verksamhetsbeteendet (`C-157`) får stå still. [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|Beslut 58]] avvisade krav på hela beteendet för tillgängligheten, eftersom ett beteende behöver olika objekt olika fort. Det skälet gäller inte beteendets eget stopp.
- **Kontinuiteten gäller vilken resurs som än faller bort.** Anta att halva bovärdsstyrkan på områdeskontoret i Åbrinken är sjuk i två veckor. Fastighetssystemet fungerar och varje informationsobjekt går att nå, men akuta fel blir ändå liggande. Det är samma fråga som när systemet ligger nere. Kontinuiteten omfattar personal, lokaler, applikationer och information.
- **Orden vanlig drift och kris skiljer inte kraven.** Anta att leverantören lägger in en uppdatering som går fel, och att fastighetssystemet är borta från klockan åtta till fyra. Det spelar ingen roll om det kallas en kris. Kraven skiljs av vad de ställs på, och båda gäller under samma åtta timmar.

### Vem som ställer kravet och vem som väger

- **Processägaren ställer kontinuitetskravet.** Teknisk chef hos Brinkstadsbostäder anger att akuta fel får bli liggande högst fyra timmar. Varken områdeskontorens chefer, som utför processen, eller uthyrningschefen, som äger Hyresgäst, anger tiden. Tiden står i en förteckning utanför lagret.
- **Avvägningen mellan två beteenden följer [[0050-ett-beslut-fattas-av-den-som-har-bade-ram-och-mandat-ett-forum-beslutar-aldrig-aspekten-avgor-inga-enskilda-fall-och-domanens-agare-satter-losningens-ram|beslut 50]].** Anta att bovärdarna inte räcker till både akuta fel och besiktningarna när hyresgäster flyttar ut. Den som har både ram och mandat beslutar, och här är det vd.
- **Prioritetsordningen är en princip.** Vd kan avgöra i förväg med en princip (`C-018`), som bolagets Akuta fel före planerat underhåll. Det som kontinuitetsmetoderna kallar prioritetsordning är en sådan princip och inget eget begrepp.

### De tre tiderna

Kontinuitetsmetodernas tre tider får inga egna begrepp. Kravet (`C-021`) räcker. Anta att fastighetssystemet kraschar klockan två och återställs från nattens säkerhetskopia.

- **Längsta tålbara avbrott är kontinuitetskravet.** Åtgärda en felanmälan får stå still högst fyra timmar.
- **Återställningstiden härleds och ställs på resursen.** Med en reservrutin klarar processen en dag utan fastighetssystemet. Utan den måste systemet vara uppe inom fyra timmar. Tiden blir ett krav på applikationen (`C-071`) eller lagringsytan (`C-165`). När flera beteenden använder samma resurs gäller den kortaste tiden.
- **Återställningspunkten blir ett andra mått i tillgängligheten.** Dagens arbetsorder är borta efter kraschen. Åtgärda en felanmälan tål det, eftersom bovärdarna minns dem. Hyra tål inte att en enda inbetalning i Hyresfordran försvinner. Kravet skiljer sig per beteende och objekt och fästs därför på paret. Tillgängligheten har alltså två mått: hur länge beteendet klarar sig utan objektet, och hur mycket av objektet som får gå förlorat. Det ändrar punkten "Tillgängligheten är ett mått tills vidare" i [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|beslut 58]].

### Reservrutinen

- **Rutinen är en bärare.** Anta att teknisk chef beslutar att varje områdeskontor har en utskriven jourlista med hyresgästernas telefonnummer. Rutinen som säger hur bovärden arbetar utan systemet är en bärare (`C-016`) som processägaren fastställer.
- **Beteendet är detsamma.** Bovärden utför Åtgärda en felanmälan med andra resurser. Reservrutinen blir inget eget beteende och inget eget begrepp.
- **Reservrutinen syns på kartan genom lagringsytan den skapar.** Jourlistan är en representation (`C-085`) av Hyresgäst på en ny lagringsyta, pärmen på kontoret. Pärmen måste klara konfidentialiteten för Hyresgäst. Kartan visar pärmen först när den finns.

### Två tider i samma beteende

- **Värsta fallet gäller för beteendet.** En vattenläcka får vänta högst fyra timmar och en droppande kran fem arbetsdagar. Båda är Åtgärda en felanmälan, och processen får fyra timmar. Det är samma regel som för klassen på informationsobjektet ([[0040-nivan-i-en-klass-beror-pa-vardet-i-en-uppgift-varsta-fallet-galler-eller-delmangden-blir-ett-eget-informationsobjekt-och-en-forteckning-i-ett-exemplar-ar-anda-en-typ|beslut 40]] och [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|58]]).
- **Nuläget delar beteendet först när verksamheten utför delen för sig.** Har bolaget en jour som egen process med egen ordning, står den som ett eget beteende med sin egen tid.

### Var kontinuiteten hör hemma

- **Kontinuitet blir inget eget begrepp.** Kontinuitetskravet är ett krav (`C-021`) på beteendet. Det beskrivs i anmärkningarna till Verksamhetsbeteende (`C-157`) och Processägare (`C-206`), på samma sätt som tillgängligheten beskrivs i en anmärkning.
- **Kontinuiteten är inget femte perspektiv i informationshanteringen.** Den gäller beteendet och alla dess resurser. Informationssäkerheten läser den del som rör information och applikationer.
- **Informationssäkerhetens fråga i steg 4 räknar in återställningstiden.** Anta att Genomföra ansökningsomgången hos Myndigheten för föreningsstöd får stå still högst en dag när pengarna ska betalas ut, och att det inte finns någon reservrutin. Föreningsregistret måste då vara uppe inom dagen. Den som går igenom kartan frågar redan om varje lagringsyta klarar det förteckningen kräver, och återställningstiden är ett sådant krav.
- **Lagringsytans krav i [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|beslut 58]] får ett tillägg.** Tillgängligheten läses i två mått, med det strängaste kravet bland de beteenden som når objektet på ytan. Till den kommer återställningstiden som härleds ur kontinuitetskravet.

## Övervägda alternativ

- **Ett enda mått, som i [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|beslut 58]].** Kravet på att läckan åtgärdas fast systemet är nere går då inte att skriva. Avvisat.
- **Två mått som skiljs av händelsens allvar**, vanlig drift och kris, som i BSI 200-4. Det kräver en gräns som ingen kan dra för uppdateringen som gick fel. Avvisat.
- **Tillgänglighet i vanlig drift fästs på objektet eller applikationen.** [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|Beslut 58]] avvisade tillgänglighet på objektet, eftersom den saknar en användning att mätas mot. Avvisat.
- **Kontinuiteten fästs på paret beteende och objekt.** Sjukdomen bland bovärdarna rör inget informationsobjekt. Avvisat.
- **Kontinuiteten fästs på applikationen eller lagringsytan.** Tiden för resursen beror på om beteendet har en reservrutin. Den härleds därför ur beteendets krav. Avvisat.
- **Egna begrepp för de tre tiderna.** Alla tre är krav, och kravet finns. Avvisat.
- **Återställningspunkten räknas till riktigheten.** Riktigheten är en klass på objektet som informationsägaren sätter. Hur mycket som får gå förlorat skiljer sig mellan beteendena. Avvisat.
- **Kontinuitet blir ett eget begrepp.** Varken tillgänglighet eller konfidentialitet är egna begrepp. Avvisat.
- **Reservrutinen blir ett eget beteende.** Bovärden utför samma process med andra resurser. Avvisat.
- **Kontinuiteten blir ett femte perspektiv i informationskartläggningen.** Den når längre än informationen. Avvisat.

## Konsekvenser

- Ingen definition ändras, och inga begrepp, relationer eller typer tillkommer. Kontinuitet och reservrutin är ord i texten, inte begrepp med id.
- Ordlistan `CONTEXT.md` har fått orden tillgänglighet, kontinuitet, återställningstid och reservrutin.
- Anmärkningarna i Verksamhetsbeteende (`C-157`), Processägare (`C-206`), Lagringsyta (`C-165`) och Informationstillgång (`C-166`) och sidan Informationskartläggning skrivs om i ett eget ärende, när #179 har fört in [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|beslut 58]].
- [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|Beslut 58]] har fått en not om tillgänglighetens två mått.
- Ärendet #181 stängs.
