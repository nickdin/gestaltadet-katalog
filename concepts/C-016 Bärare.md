---
id: C-016
term: Bärare
terms:
  - term: Bärare
    language: sv
    source: catalogue
definition: dokument eller artefakt som ett eller flera styrmedel, ändamål eller bedömningar står i
kind: governance-type
associative:
  - concept: "[[C-015 Styrmedel]]"
    label: bär
  - concept: "[[C-022 Ändamål]]"
    label: bär
  - concept: '[[C-185 Bedömning]]'
    label: bär
---
# C-016 Bärare

**Definition:** dokument eller artefakt som ett eller flera styrmedel, ändamål eller bedömningar står i

## Exempel

riktlinje, policy, anvisning, standard, plan, målarkitektur, verksamhetsplan, budget, informationshanteringsplan, arbetsordning, delegationsordning, vd-instruktion, attestordning.

## Anmärkning

Ett styrmedel kan byta bärare utan att ändra innehåll. Standarden är en bärare: den bär krav, och kraven är styrmedlen. En arkitekturbeskrivning som beslutar principer är deras bärare. Riskanalysen och omvärldsanalysen är bärare: de bär bedömningar ([[C-185 Bedömning]]) (beslut 25, beslut 37). Policyn är en bärare. Ordet namnger dokumentet och säger inget om vad som står i det. Bostadsbolagets uthyrningspolicy bär en regel, den som stått längst i kön går först. Den bär en princip, bolaget hyr hellre ut till den som saknar bostad än till den som vill byta. Och den bär ett mål, hyresgästerna ska vara nöjda. Varje mening prövas för sig (beslut 43). Arbetsordningen, delegationsordningen, vd-instruktionen och attestordningen är bärare. De bär reglerna som delegerar ([[C-214 Delegation]]), och de skiljer sig i vilka regler de bär (beslut 44). Ett dokument som varken bär styrmedel, ändamål eller bedömning är ingen bärare. Som databärare är det en artefakt ([[C-081 Artefakt]]), och dess läsbara innehåll är representationer ([[C-085 Representation]]).

Bäraren är det som fastställs. Relationen fastställs av ([[C-183 fastställs av]]) går från bäraren till den aktör eller roll som beslutat eller antagit den, och styrmedlen bäraren bär följer med. Ett styrmedel utan bärare får relationen själv (beslut 23). I lagret skrivs bär mellan ett bärarelement och det styrmedel det bär med relationstypen aggregerar ([[C-100 aggregerar]]): ett styrmedel kan byta bärare utan att ändra innehåll, så det är ingen exklusiv del (beslut 19).

**Nödvändighet:** Varje bärare bär minst ett styrmedel, ett ändamål eller en bedömning.

Informationshanteringsplanen är en bärare. Den bär reglerna om registrering, bevarande och gallring ([[C-200 Gallring]]) per verksamhetsprocess och handlingstyp, och myndigheten fastställer den; Riksarkivets föreskrifter är den påverkan reglerna kommer ur. Arkivredovisningen likaså. Registerförteckningen enligt dataskyddsförordningen bär inga regler och är ingen bärare (beslut 31).
