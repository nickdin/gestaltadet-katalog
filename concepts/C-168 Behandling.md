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

Ett begrepp, ingen elementtyp: en behandling registreras inte som element, utan läses ur det verksamhetsbeteende som utför den och de informationsobjekt beteendet har åtkomst till ([[C-101 har åtkomst till]]), som ArchiMate gör; ändamål och rättslig grund står i beteendets beskrivning. Dataskyddsförordningens artikel 4.2: en åtgärd eller kombination av åtgärder beträffande personuppgifter, som insamling, registrering, lagring, bearbetning, användning, utlämning, sammanförande och radering. Här används begreppet för uppgifter ([[C-161 Uppgift]]) i allmänhet, inte bara personuppgifter. Behandlingen har behandlingsändamålet ([[C-163 Behandlingsändamål]]), och grundläggande bedömning och konsekvensbedömning görs per behandling och ändamål. Den utförs inom ett verksamhetsbeteende ([[C-157 Verksamhetsbeteende]]), som är det användningssammanhang en myndighets anvisningar för informationsklassning klassar utifrån. En behandling som sätter samman uppgifter ger upphov till en sammanställning ([[C-162 Sammanställning]]), som klassas för sig. Bearbetning är kartläggningens ord: att lägga till område i ekonomisystemets underlag eller kombinera två kolumner ur Föreningsregistret är en behandling som ger en ny sammanställning.

## Exempel

att dela upp listan över utbetalningar per handläggare och mejla den, att lägga till område i ekonomiunderlaget, att summera felanmälningarna per byggnad.
