---
id: C-166
term: Informationstillgång
terms:
  - term: Informationstillgång
    language: sv
    status: preferred
    source: concept new
definition: resurs som bär, behandlar eller förmedlar information och som därför omfattas av informationssäkerhetsarbetet
generic: '[[C-122 Resurs]]'
associative:
  - concept: '[[C-060 Informationsobjekt]]'
    label: omfattar
  - concept: '[[C-071 Applikation]]'
    label: omfattar
  - concept: '[[C-165 Lagringsyta]]'
    label: omfattar
---
# C-166 Informationstillgång

**Definition:** resurs som bär, behandlar eller förmedlar information och som därför omfattas av informationssäkerhetsarbetet

## Anmärkning

Begreppet är vidare än informationsobjektet ([[C-060 Informationsobjekt]]). En myndighets riktlinje för informationsklassning använder ofta ordet för allt som ska klassas och skyddas: information, program, tjänster, fysiska tillgångar, människor med deras kompetens, och immateriella tillgångar som rykte. I lagret är informationstillgången en sorts resurs ([[C-122 Resurs]]) som omfattar informationsobjektet, applikationen ([[C-071 Applikation]]), lagringsytan ([[C-165 Lagringsyta]]) och representationen ([[C-085 Representation]]). Människor och rykte har inga egna begrepp i lagret och lämnas utanför.

Informationsägaren ([[C-167 Informationsägare]]) beslutar informationsklassningen. Klassningen har två klasser, konfidentialitet och riktighet, och båda sätts på informationsobjektet. Konfidentialiteten säger hur hemligt objektet måste vara, och riktigheten hur få fel det tål. Konfidentialitetens nivåer är öppen, intern och känslig. Klassen står i organisationens klassningsförteckning, som pekar på objektet. Lagret bär inga nivåer. En sådan riktlinje kräver klassning när en informationstillgång uppstår eller ändras, till exempel när något läggs till eller tas bort i ett verksamhetsbeteende, eller när nya krav eller risker uppstått. Beslut 58.

Processägaren ([[C-206 Processägare]]) ställer två krav på behandlingen ([[C-168 Behandling]]): tillgänglighet och spårbarhet. Tillgängligheten har två mått: hur länge beteendet klarar sig utan objektet, och hur mycket av objektet som får gå förlorat. Spårbarheten gäller vem som gjorde vad. Kraven fästs på paret beteende och objekt, där beteendet har åtkomst till ([[C-101 har åtkomst till]]) objektet. Hos Myndigheten för föreningsstöd behöver Pröva en ansökan objektet Förening samma dag, och analysfunktionen klarar en vecka utan det. Det andra måttet skiljer sig också per beteende och objekt. Anta att fastighetssystemet hos bostadsbolaget kraschar och återställs från nattens säkerhetskopia, så att dagens arbetsorder är borta. Åtgärda en felanmälan tål det, eftersom bovärdarna minns dem. Hyra tål inte att en enda inbetalning i Hyresfordran försvinner. Beslut 58 och 61.

Kontinuiteten är ett eget krav och hör inte till tillgängligheten. Den gäller hela beteendet och står i [[C-157 Verksamhetsbeteende]]. Ur kontinuitetskravet härleds återställningstiden, som är ett krav på applikationen eller lagringsytan ([[C-165 Lagringsyta]]). Beslut 61.

En sammanställning ([[C-162 Sammanställning]]) klassas för sig. Mängden gör aldrig klassen högre: förteckningen över alla föreningars företrädare har samma konfidentialitet som Företrädare. Högre blir klassen bara när sammanställningen ger en ny uppgift. Förteckningen över utsatta roller säger vilka anställda som är utsatta för hot, och det visar ingen enskild Yrkesroll. Lägre blir klassen när uppgiften inte längre finns kvar, som i en summering per enhet eller en avidentifiering. Uppgiften ([[C-161 Uppgift]]) ger golvet genom sekretess, känslig personuppgift och säkerhetsskyddsklass så länge den ingår.

Den som känner CIA-modellen (på engelska confidentiality, integrity, availability) känner igen konfidentialitet, riktighet och tillgänglighet. De tre är ISO 27000:s, och föreskrifterna för statliga myndigheter, MSBFS 2020:6, kräver klassning i samma tre. Spårbarhet är ett svenskt tillägg. Det står i metodstödet från Myndigheten för samhällsskydd och beredskap (MSB), och i föreskrifterna bara i ett allmänt råd.

Katalogen delar de fyra i två klasser och två krav efter vad skadan följer. Skadan av ett röjande följer uppgifterna vart de än tar vägen, så konfidentialiteten sitter på objektet. Objektet blir riktigt där det skapas, och kopiorna ärver felet, så riktigheten sitter också på objektet. Skadan av ett avbrott beror på vad beteendet ska göra just då, så tillgängligheten sitter på behandlingen. Spårbarheten gäller vad någon gjorde, inte uppgifterna, och sitter därför också på behandlingen. Beslut 58.

Klasserna och kraven uppfylls av åtgärder, och åtgärderna görs inte på informationen. De görs på lagringsytan ([[C-165 Lagringsyta]]), i applikationen ([[C-071 Applikation]]) och på representationen ([[C-085 Representation]]). Varje åtgärd tjänar en klass eller ett krav. Behörighet och märkning tjänar konfidentialiteten: behörigheten på lagringsytan och i applikationen, märkningen på representationen. Validering och signering tjänar riktigheten. Säkerhetskopiering, redundans och format tjänar tillgängligheten. Loggning tjänar spårbarheten. Samma objekt kan ligga på två ytor som ska klara olika tillgänglighet. Föreningsregistret ska klara dagen från Pröva en ansökan, och datalagret veckan från analysfunktionen.

Nivån i en klass måste hålla för den förekomst av typen som ställer störst krav: det värsta fallet gäller. Det gäller också när nivån beror på värdet i en uppgift. [[C-060 Informationsobjekt]] säger vad verksamheten gör när nivån då blir för hög för de övriga förekomsterna.

Lagret bär inga beslut ur regelverken. Klassen står i klassningsförteckningen. Ändamål, rättslig grund, bevarande och gallring ([[C-200 Gallring]]) står i sina förteckningar. Varje förteckning pekar på ett ankare i lagret (beslut 31 och 58). Lagret visar vem som beslutar, informationsägaren och processägaren, och var svaren fästs. Lagret räknar ingenting. Den som går igenom kartan läser ihop den med förteckningarna. Lagringsytans krav läses fram i fyra delar ([[C-165 Lagringsyta]]). Objektet får sin nivå genom en egen rad eller genom områdets rad ([[C-198 Informationsområde]]). Sammanställningen klassas för sig.

## Exempel

Föreningsregistret, förteckningen över alla företrädare, en enhets grupprum i SharePoint.

Åtgärda en felanmälan hos bostadsbolaget behöver Hyresgäst inom en timme vid en vattenläcka, för telefonnumrets skull. Teknisk chef ställer kravet som processägare. I fastighetssystemet uppfylls kravet av driftavtal och säkerhetskopiering. I en kopia i en handläggares Outlook uppfylls det inte alls.
