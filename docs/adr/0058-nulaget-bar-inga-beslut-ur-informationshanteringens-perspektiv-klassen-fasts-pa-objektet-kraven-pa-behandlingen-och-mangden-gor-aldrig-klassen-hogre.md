# Nuläget bär inga beslut ur informationshanteringens perspektiv, klassen fästs på objektet, kraven på behandlingen, och mängden gör aldrig klassen högre

Beslutat av Nicklas 18 november 2026, när beslut 57 hade sagt att klassen är densamma i varje beteende och det skavde för tillgängligheten, för samlingar och för känslighet som uppstår i en koppling.

## Sammanhang

Katalogen sade att informationsägaren (`C-167`) sätter klassen på informationsobjektet (`C-060`) som typ, i fyra klasser, och att klassen är densamma i varje verksamhetsbeteende (`C-157`) som använder objektet (beslut 31, 35, 40 och 57). Lagringsytan (`C-165`) fick det högst klassade objektets krav i alla fyra klasserna, och lagret bar nivåerna (beslut 31).

Ärendet #177 ställde fem delfrågor. Beror tillgänglighet och spårbarhet på användningen? Är det samlingen som är känslig? Kan informationsägaren klassa utan att känna den framtida användningen? Vem följer klassningen, typens ägare eller den som svarar för förekomsterna? Och var sitter klassen när känsligheten uppstår först i kopplingen mellan två objekt?

Ett underlag prövade frågorna mot lagar, föreskrifter, metoder och granskningar: `docs/research/informationsklassning-var-klassen-sitter.md`. Fyra fynd vägde tyngst. Kontinuitetsmetoderna sätter avbrottstiden på aktiviteten, inte på informationen. De bindande svenska reglerna har tre aspekter, och spårbarhet står bara i ett allmänt råd. Säkerhetspolisen skiljer en samling av många likadana uppgifter från en samling som ger en ny uppgift. Och ingen läst källa höjer två objekt för att kopplingen mellan dem är känslig.

Grillningen gick fem rundor och avgjorde varje fråga på ett fall ur de två exempelorganisationerna. Nicklas ändrade utfallet på en punkt. När delfrågorna var besvarade frågade han om arkitekturen över huvud taget ska bära klassningen. Arkitekturen ska vara ett stöd för informationssäkerhet, dataskydd, offentlighet och informationsförsörjning, men inte lösningen. Den frågan blev beslutets första punkt.

## Beslut

### Vad nuläget bär

- **Nuläget bär inga beslut ur informationshanteringens fyra perspektiv.** Informationssäkerhet, dataskydd, offentlighet och arkiv, och informationsförsörjning läser kartan och fattar sina beslut i sina egna förteckningar. Kartan beskriver hur det är.
- **Klassen flyttar ut ur lagret.** Uthyrningschefen hos Brinkstadsbostäder klassar Hyresgäst i bolagets klassningsförteckning, och förteckningen pekar på objektet Hyresgäst på kartan. Klassen blir som ändamålet och gallringsfristen redan är: ett beslut i en förteckning, fäst på ett ankare i lagret. Det ändrar punkten "Klassen stannar i lagret" i beslut 31.
- **Ägaren står kvar på kartan.** Att uthyrningschefen är informationsägare för Hyresgäst är hur ansvaret är ordnat, och alla fyra perspektiven behöver veta vem de ska fråga. Kartan visar vem som beslutar, aldrig vad hen beslutade. Relationen ansvarar för (`C-208`) och de två ägarrollerna är orörda.
- **Katalogen säger var förteckningen fäster sina svar och hur de läses mot kartan.** Punkterna nedan står i begreppens anmärkningar och på sidan Informationskartläggning, som stöd för den som går igenom kartan. Lagret räknar ingenting. Datalagret hos Myndigheten för föreningsstöd: kartan visar att kopian av Företrädare ligger där och att analysfunktionen når den. Förteckningen ger nivåerna. Informationsägaren läser ihop dem och ser att datalagret inte räcker.
- **Det som genomgången kräver blir krav i målarkitekturen.** Chefen för Register- och tillsynsenheten beslutar att kopian av Företrädare ska bort ur datalagret. Beslutet skrivs som ett krav (`C-021`) på datalagret i målarkitekturen (`C-054`). Nuläget visar kopian tills den är borta.
- **Nuläget delar ett objekt först när verksamheten hanterar delen för sig.** Brinkstadsbostäder hanterar i dag alla hyresavtal lika. Vill informationsägaren att avtalen för hyresgäster med skyddade personuppgifter hanteras för sig, står Skyddat hyresavtal i målarkitekturen. Det flyttar till nuläget den dag uthyrningen gör så. Det skärper beslut 40: nuläget ändras av att verksamheten ändras, aldrig av att någon har beslutat att den borde.
- **Bedömning (`C-185`) står kvar som element.** Ett perspektivs eget beslut heter beslut i förteckningen, aldrig bedömning. Bedömningen är styrningens ord för att någon har värderat en ordning, och den är vägen från genomgången till målarkitekturen. Att Analysenhetens grupprum rymmer Riskindikator per förening är en sådan sak. Principen gäller de fyra perspektiven i informationshanteringen och inget annat i katalogen.

### Två klasser på objektet

- **Ordet klass gäller bara det som fästs på objektet.** Klass och klassning betyder informationsägarens beslut om informationsobjektet, i två klasser: konfidentialitet och riktighet.
- **Konfidentialiteten fästs på objektet och är densamma i varje beteende.** Hyresgäst är känslig i delar: kontaktuppgifter, inkomstuppgifter och betalningshistorik. Bovärden ser bara namn och telefonnummer i Åtgärda en felanmälan. Klassen är ändå densamma som i uthyrningen, eftersom skadan av ett röjande följer uppgifterna. Vilka uppgifter beteendet får se styr ändamålet. Skälet i beslut 57 håller för konfidentialiteten.
- **Riktigheten fästs på objektet.** Ett fel i Kontonummer gör att pengarna går till fel konto i Genomföra ansökningsomgången. Samma fel i datalagret ger bara en felaktig rad i Utbetalningar per kommun. Skadan skiljer sig, men objektet blir riktigt där det skapas, och kopiorna ärver felet. Informationsägaren sätter därför nivån efter den användning som tål minst fel.
- **Klassen sitter på typen, aldrig på förekomsten.** Den som lägger upp en ny roll hos Brinkstadsbostäder väljer mellan Yrkesroll och Utsatt roll efter informationsägarens regel. Hen sätter aldrig en nivå själv. Linjechefen (`C-207`) svarar för att personalen hanterar varje förekomst efter klassen. Märkningen sitter på representationen (`C-085`), som förut.

### Två krav på behandlingen

- **Tillgänglighet och spårbarhet är krav på behandlingen, inte klasser.** Processägaren (`C-206`) ställer dem. Det ändrar punkten "Klassen sitter på objektet och är densamma i varje beteende" i beslut 57, som nu gäller konfidentialitet och riktighet.
- **Tillgängligheten beror på användningen.** Hos Myndigheten för föreningsstöd behöver Pröva en ansökan objektet Förening samma dag. Analysfunktionen klarar en vecka utan det. Chefen för Bidragsenheten anger dagen, chefen för Analysenheten veckan. Informationsägaren sätter ingen tillgänglighet på objektet. Skadan av ett avbrott beror på vad beteendet ska göra just då.
- **Spårbarheten beror på användningen.** Spårbarhet gäller vem som gjorde vad. Analysfunktionen ska kunna visa hur Riskindikator per förening räknades fram, eftersom den pekar ut föreningar. Utbetalningar per kommun kräver inte det.
- **Kraven fästs på paret beteende och objekt.** Åtgärda en felanmälan behöver hyresgästens telefonnummer inom en timme vid en vattenläcka. Samma beteende klarar flera dagar utan Hyresavtal. Kravet sitter därför där beteendet har åtkomst till objektet (`C-101`). Det paret är redan ankaret för behandlingen (`C-168`) och ändamålet (beslut 31).
- **Tillgängligheten är ett mått tills vidare**: hur länge beteendet klarar sig utan objektet. Skillnaden mellan tillgänglighet i vanlig drift och kontinuitet vid en kris får ett eget ärende.

### Framtida användning

- **Informationsägaren klassar utan att känna den framtida användningen.** Anta att en ny lösning hos Brinkstadsbostäder om ett år vill skicka hyresavier som sms. Konfidentialiteten håller för all användning. Den nya lösningens processägare ställer sina egna krav på tillgänglighet och spårbarhet. Lösningen behöver uthyrningschefens ja och ett eget ändamål (beslut 35).
- **Bara riktigheten kan behöva prövas om.** Avierna tål färre fel i telefonnumret än uthyrningen gör. Den nya lösningen ställer då ett krav (`C-021`) på uthyrningschefen, som beslutar om nivån höjs. Är de oense avgör vd (beslut 57).

### Samlingar

- **Två prov svarar på var sin fråga.** Om en samling är ett eget informationsobjekt avgör beslut 23: verksamheten hanterar den som en enhet för ett ändamål. Om samlingen får högre konfidentialitet än sina delar avgör ett annat prov: går det att säga vilken ny uppgift samlingen ger?
- **Mängden gör aldrig klassen högre.** Förteckningen över alla föreningars företrädare är en sammanställning (`C-162`), eftersom Register- och tillsynsenheten hanterar den som en enhet. Den ger ingen ny uppgift och har samma konfidentialitet som Företrädare. Att den är många höjer kravet på lagringsytan där den ligger.
- **En ny uppgift ger en egen klass.** Förteckningen över utsatta roller säger vilka anställda som är utsatta för hot. Det visar ingen enskild Yrkesroll. Den klassas för sig, som förut.
- **Klassen på typen är klassen på en förekomst i värsta fall**, inte klassen på hela mängden (beslut 40).

### Känslighet i en koppling

- **Värdemängden (`C-197`) får aldrig klassen.** Anta att Brinkstadsbostäder anpassar lägenheter av hälsoskäl, och att Lägenhetsanpassning har uppgiften skäl med värden ur värdemängden Hälsotillstånd. Listan över hälsotillstånd är öppen.
- **Relationen får aldrig klassen.** Att hyresgäster bor i lägenheter är ingen hemlighet. Känslig är en enskild koppling, och den står som en uppgift i ett objekt.
- **Klassen sitter på objektet där kopplingen skapas**, med värsta fallet (beslut 40). Lägenhetsanpassning får nivån för uppgifter om hälsa. Hyresavtal får nivån som hyresgästen med skyddade personuppgifter kräver. Lägenhet och dess adress står kvar som öppna.
- **Det som bara uppstår på en lagringsyta hanteras på ytan.** Anta att Lägenhetsanpassning bara pekar på Lägenhet. Fastighetssystemet rymmer också Hyresavtal. Den som kommer åt båda kan räkna ut vem som har vilket hälsotillstånd, fast inget objekt säger det. Inget objekt höjs. Fastighetssystemet måste klara nivån för uppgifter om hälsa, och en utskrift av bara Lägenhetsanpassning har sin egen lägre nivå.
- **Om ett objekt är en personuppgift avgörs per lagringsyta och behandling, inte bara på typen.** Adressen till ett flerbostadshus pekar på många hushåll. Den blir en personuppgift på en yta där den går att knyta till en hyresgäst.

### Lagringsytans krav

Lagringsytans krav läses fram i fyra delar:

- **Konfidentialitet och riktighet:** det högst klassade objektet på ytan. Datalagret måste klara nivån för Företrädare så länge kopian ligger där.
- **Tillgänglighet och spårbarhet:** det strängaste kravet bland de beteenden som når objektet på just den ytan. Datalagret får analysfunktionens vecka. Föreningsregistret får dagen från Pröva en ansökan.
- **Mängden:** många likadana uppgifter höjer ytans krav.
- **Kopplingen:** det som går att räkna ut ur objekten på ytan höjer ytans krav.

## Övervägda alternativ

- **Klassen står kvar i lagret**, som i beslut 31. Kartan visar då ensam vad en lagringsyta måste klara. Men kartan ändras då varje gång ett perspektiv ändrar ett beslut, och arkitekturen blir lösningen i stället för stödet. Avvisat.
- **Också reglerna flyttar ut**, så att katalogen bara säger var förteckningen fäster sina svar. Då tar katalogen inte ställning i det som skavde. Avvisat.
- **Informationssäkerheten stryks ur katalogen.** Då faller det fjärde perspektivet i Informationskartläggning (beslut 55). Avvisat.
- **Konfidentialiteten sätts per beteende**, hög i uthyrningen och låg i felanmälan. Det ger en klassning per åtkomst, och skadan av ett röjande följer uppgifterna. Avvisat, som i beslut 57.
- **Tillgängligheten står kvar på objektet som ett golv, och beteendet lägger till sitt krav.** Golvet har ingen användning att mätas mot. Avvisat.
- **Riktigheten sätts per beteende.** Kopiorna ärver felet från källan, så kravet måste hålla redan där. Avvisat.
- **Spårbarheten står kvar som en fjärde klass på objektet.** De bindande reglerna har tre aspekter, och spårbarhet gäller vad någon gjorde, inte uppgifterna. Avvisat.
- **Spårbarheten räknas till riktigheten**, som i två av de lästa metoderna. Då hamnar ett krav på beteendet på objektet. Avvisat.
- **Kraven fästs på hela beteendet.** Ett beteende behöver olika objekt olika fort. Avvisat.
- **Den som skapar förekomsten sätter nivån på den.** Uppdelningen i beslut 40 ger samma sak med typer. Avvisat.
- **Varje samling som hanteras som en enhet klassas högre.** Många likadana uppgifter ger inget nytt att röja. Avvisat.
- **Klassen sätts på relationen mellan två objekt.** Katalogen har ingen klass på relationer, och relationen mellan typerna är inte känslig. Avvisat.
- **Båda objekten höjs när kopplingen är känslig.** Ingen läst källa gör så, och Lägenhet hade blivit känslig för en enda hyresgästs skull. Avvisat.
- **Tillgängligheten delas i två mått nu**, vanlig drift och kontinuitet vid en kris. Katalogen saknar begrepp för kontinuitet. Uppskjutet till ett eget ärende.
- **En baslinje**, där bara det som avviker klassas. Frågan gäller om man klassar, inte var klassen fästs. Uppskjutet till ett eget ärende.

## Konsekvenser

- Inga definitioner ändras och inga begrepp, relationer eller typer tillkommer. Inget i begreppen, på sidorna eller i ritningarna är ändrat med det här beslutet. Ändringarna görs i ett eget ärende.
- Anmärkningarna i Informationsobjekt (`C-060`), Sammanställning (`C-162`), Lagringsyta (`C-165`), Informationstillgång (`C-166`), Informationsägare (`C-167`), Behandling (`C-168`) och Informationsområde (`C-198`) säger i dag fyra klasser, att lagret bär nivån eller att mängden gör klassen högre. De skrivs om.
- Sidan och ritningen Informationskartläggning säger att kartan bär nivån i varje klass. Huvudfrågan i informationssäkerheten blir: finns varje objekt på kartan i klassningsförteckningen, och klarar varje lagringsyta det förteckningen kräver? Steg 4 får följdfrågan vilka objekt på lagringsytan som går att koppla ihop till en ny uppgift.
- Lagret visar i dag att ett beteende har åtkomst till ett objekt och att objektets representation ligger på en lagringsyta. Det visar inte vilken yta beteendet använder. Den luckan avgörs i ändringsärendet.
- De två exempelorganisationerna beskriver klassningen efter den gamla ordningen och skrivs om.
- Beslut 31, 40 och 57 har fått var sin not om vad som ändras.
- Två frågor har egna ärenden: en baslinje för klassningen, och kontinuitet vid en kris.
- Ärendet #177 stängs.
