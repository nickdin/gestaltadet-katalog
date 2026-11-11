---
id: C-168
term: Behandling
terms:
  - term: Behandling
    language: sv
    status: preferred
    source: concept new
  - term: bearbetning
    language: sv
    source: concept change
    status: admitted
definition: åtgärd som utförs på uppgifter, som att samla in, sammanställa, ändra, lämna ut eller radera dem, för ett bestämt behandlingsändamål
associative:
  - concept: '[[C-161 Uppgift]]'
    label: behandlar
  - concept: '[[C-162 Sammanställning]]'
    label: ger upphov till
  - concept: '[[C-163 Behandlingsändamål]]'
    label: har
  - concept: '[[C-157 Verksamhetsbeteende]]'
    label: utförs inom
---
# C-168 Behandling

**Definition:** åtgärd som utförs på uppgifter, som att samla in, sammanställa, ändra, lämna ut eller radera dem, för ett bestämt behandlingsändamål

## Anmärkning

Dataskyddsförordningens artikel 4.2 beskriver behandling som en åtgärd eller kombination av åtgärder beträffande personuppgifter, som insamling, registrering, lagring, bearbetning, användning, utlämning, sammanförande och radering. Här används begreppet för uppgifter ([[C-161 Uppgift]]) i allmänhet, inte bara personuppgifter. Behandlingen har behandlingsändamålet ([[C-163 Behandlingsändamål]]), och grundläggande bedömning och konsekvensbedömning görs per behandling och ändamål. Behandlingen utförs inom ett verksamhetsbeteende ([[C-157 Verksamhetsbeteende]]), det användningssammanhang en myndighets anvisningar för informationsklassning klassar utifrån.

Ett begrepp, ingen elementtyp: en behandling registreras inte som element. Den läses ur det verksamhetsbeteende som utför den och de informationsobjekt beteendet har åtkomst till ([[C-101 har åtkomst till]]). Åtkomsten är ritad eller härledd. Härledd är den när beteendet har åtkomst till ett verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]) som informationsobjektet realiserar ([[C-094 realiseras av]]). Ritad direkt är den där den inte följer av verksamhetsobjektet. Pröva ansökan har åtkomst till Ärende och når så Ansökan och Förening, men behandlingen "samla in företrädarens personnummer" kräver en ritad åtkomst till Personnummer. Den följer inte av att handläggningen läser Företrädare, som aggregerar Personnummer, eftersom åtkomsten inte följer aggregerar ([[C-100 aggregerar]]). Läget, läser, skriver eller båda, står på åtkomsten (beslut 34).

Vem som svarar för en behandling läses ur lagret: informationsägaren för objektet, processägaren ([[C-206 Processägare]]) för beteendet och linjechefen ([[C-207 Linjechef]]) för förekomsterna (beslut 35). En behandling som sätter samman uppgifter ger upphov till en sammanställning ([[C-162 Sammanställning]]), som klassas för sig. Bearbetning är kartläggningens ord: att lägga till område i ekonomisystemets underlag eller kombinera två kolumner ur Föreningsregistret är en behandling som ger en ny sammanställning.

Förteckningarna upprättas ur kartan. Registerförteckningen enligt dataskyddsförordningens artikel 30 upprättas ur behandlingarna. Arkivredovisningen och informationshanteringsplanen upprättas ur handlingstyperna per process, paren av verksamhetsbeteende och representation ([[C-085 Representation]], [[C-200 Gallring]]). Ändamål och rättslig grund står i registerförteckningen, inte i lagret: lagret ger ankaret, paret beteende och informationsobjekt, och förteckningen säger vad som gäller för det (beslut 31, som på den punkten ersätter beslut 18). Innehållet per rad, ändamål, grund och frist, ändras av juridiska skäl utan att arkitekturen gör det. Därför bor det i förteckningen, och lagret bär ingen kopia. Informationshanteringsplanen och arkivredovisningen är bärare ([[C-016 Bärare]]) för de regler de fastställer; registerförteckningen är en förteckning utan regler. Att lämna ut en handling, ett registerutdrag eller uppgifter för dataportabilitet är behandlingen lämna ut, i det beteende som prövar begäran. Det som lämnas ut är en representation i begärd form (beslut 31).

## Motsvarigheter

Behandlingen läses ur det verksamhetsbeteende som utför den och de informationsobjekt beteendet har åtkomst till ([[C-101 har åtkomst till]]), som ArchiMate gör (beslut 34).

## Exempel

att dela upp listan över utbetalningar per handläggare och mejla den, att lägga till område i ekonomiunderlaget, att summera felanmälningarna per byggnad, att lämna ut en handling på begäran.
