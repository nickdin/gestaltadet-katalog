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

En myndighets riktlinje för informationsklassning använder ofta ordet för allt som ska klassas och skyddas: information, program, tjänster, fysiska tillgångar, människor med deras kompetens, och immateriella tillgångar som rykte. Begreppet är alltså vidare än informationsobjektet ([[C-060 Informationsobjekt]]). I lagret är det en sorts resurs ([[C-122 Resurs]]) som omfattar informationsobjektet, applikationen ([[C-071 Applikation]]) och lagringsytan ([[C-165 Lagringsyta]]); människor och rykte har inga egna begrepp i lagret och lämnas utanför. Informationsklassningen i konfidentialitet (öppen, intern, känslig) sätts på informationsobjektet och beslutas av informationsägaren ([[C-167 Informationsägare]]). En sammanställning ([[C-162 Sammanställning]]) klassas för sig: den kan bli högre än delarna, som förteckningen över alla föreningars företrädare, och lägre än det den sätts samman ur, som en summering per enhet eller en avidentifiering där uppgiften inte längre finns kvar. Uppgiften ([[C-161 Uppgift]]) ger golvet genom sekretess, känslig personuppgift och säkerhetsskyddsklass så länge den ingår; lagringsytan får kravet av det högst klassade som ligger där. Riktighet, tillgänglighet och spårbarhet har en klass var; de kraven gäller alltid och landar som åtgärder på lagringsytan och applikationen. En sådan riktlinje kräver klassning när en informationstillgång uppstår eller ändras, till exempel när något läggs till eller tas bort i ett verksamhetsbeteende, eller när nya krav eller risker uppstått.

Klassen är det enda av det regelverken vill veta som står i lagret: den är informationsägarens beslut om informationen själv, och lagret räknar med den, ytan får det högst klassade objektets krav, området ger klassen nedåt (ADR 0030), sammanställningen klassas för sig. Ändamål, rättslig grund, bevarande och gallring ([[C-200 Gallring]]) är beslut om vad som får göras med informationen och står i förteckningarna utanför lagret, med lagret som anker (ADR 0031).

## Exempel

Föreningsregistret, förteckningen över alla företrädare, en enhets grupprum i SharePoint.
