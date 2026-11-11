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

Begreppet är vidare än informationsobjektet ([[C-060 Informationsobjekt]]). En myndighets riktlinje för informationsklassning använder ofta ordet för allt som ska klassas och skyddas: information, program, tjänster, fysiska tillgångar, människor med deras kompetens, och immateriella tillgångar som rykte. I lagret är informationstillgången en sorts resurs ([[C-122 Resurs]]) som omfattar informationsobjektet, applikationen ([[C-071 Applikation]]) och lagringsytan ([[C-165 Lagringsyta]]). Människor och rykte har inga egna begrepp i lagret och lämnas utanför.

Informationsägaren ([[C-167 Informationsägare]]) beslutar informationsklassningen: behovet, som sätts på informationsobjektet. Konfidentialitetens nivåer är öppen, intern och känslig. En sammanställning ([[C-162 Sammanställning]]) klassas för sig. Den kan bli högre än delarna, som förteckningen över alla föreningars företrädare, och lägre än det den sätts samman ur, som en summering per enhet eller en avidentifiering där uppgiften inte längre finns kvar. Uppgiften ([[C-161 Uppgift]]) ger golvet genom sekretess, känslig personuppgift och säkerhetsskyddsklass så länge den ingår. En sådan riktlinje kräver klassning när en informationstillgång uppstår eller ändras, till exempel när något läggs till eller tas bort i ett verksamhetsbeteende, eller när nya krav eller risker uppstått.

Behovet sätts på informationsobjektet i alla fyra klasserna: konfidentialitet, riktighet, tillgänglighet och spårbarhet. Informationsägaren beslutar det. Vad informationen är avgör hur hemlig, hur riktig, hur snabbt nåbar och hur väl spårad den måste vara.

De tre första klasserna är ISO 27000:s konfidentialitet, riktighet och tillgänglighet. Spårbarhet är det svenska tillägget i MSB:s metodstöd och i SKR:s KLASSA. Den som kommer från CIA-modellen (på engelska confidentiality, integrity, availability) känner därför igen tre av de fyra.

Uppfyllandet skiljer sig mellan klasserna. Konfidentialiteten följer innehållet vart det än tar vägen, så den prövas mot objektet och mot den behandling ([[C-168 Behandling]]) som görs. Riktighet, tillgänglighet och spårbarhet har var sin nivå på objektet, och behoven gäller alltid. De uppfylls av åtgärder, och åtgärderna görs inte på informationen. De görs på lagringsytan ([[C-165 Lagringsyta]]), i applikationen ([[C-071 Applikation]]) och på representationen ([[C-085 Representation]]). Varje åtgärd tjänar en klass. Behörighet och märkning tjänar konfidentialiteten: behörigheten på lagringsytan och i applikationen, märkningen på representationen. Validering och signering tjänar riktigheten. Säkerhetskopiering, redundans och format tjänar tillgängligheten. Loggning tjänar spårbarheten. Samma objekt kan ligga på två ytor med olika tillgänglighet.

Lagringsytan får behovet av det högst klassade informationsobjektet som ligger där, i alla fyra klasserna och inte bara i konfidentialitet.

Klassen är det enda av det regelverken vill veta som står i lagret. Den är informationsägarens beslut om informationen själv, och lagret räknar med den: ytan får det högst klassade objektets krav, området ger klassen nedåt (beslut 30), sammanställningen klassas för sig. Ändamål, rättslig grund, bevarande och gallring ([[C-200 Gallring]]) är beslut om vad som får göras med informationen. De står i förteckningarna utanför lagret, med lagret som anker (beslut 31).

## Exempel

Föreningsregistret, förteckningen över alla företrädare, en enhets grupprum i SharePoint.

Hyresavtal hos bostadsbolaget har hög tillgänglighet som behov, satt av uthyrningschefen. I hyressystemet uppfylls behovet av driftavtal och säkerhetskopiering. I en kopia i en handläggares Outlook uppfylls det inte alls.
