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

riktlinje, anvisning, standard, plan, målarkitektur, verksamhetsplan, budget, informationshanteringsplan.

## Anmärkning

Ett styrmedel kan byta bärare utan att ändra innehåll. Standarden är en bärare: den bär krav, och kraven är styrmedlen. En arkitekturbeskrivning som beslutar principer är deras bärare. Riskanalysen och omvärldsanalysen är bärare: de bär bedömningar ([[C-185 Bedömning]]) (ADR 0025, ADR 0037). Ett dokument som varken bär styrmedel, ändamål eller bedömning är ingen bärare. Som databärare är det en artefakt ([[C-081 Artefakt]]), och dess läsbara innehåll är representationer ([[C-085 Representation]]).

Bäraren är det som fastställs. Relationen fastställs av ([[C-183 fastställs av]]) går från bäraren till den aktör, roll eller det forum som beslutat eller antagit den, och styrmedlen bäraren bär följer med. Ett styrmedel utan bärare får relationen själv (ADR 0023). I lagret skrivs bär mellan ett bärarelement och det styrmedel det bär med relationstypen aggregerar ([[C-100 aggregerar]]): ett styrmedel kan byta bärare utan att ändra innehåll, så det är ingen exklusiv del (ADR 0019).

**Nödvändighet:** Varje bärare bär minst ett styrmedel, ett ändamål eller en bedömning.

Informationshanteringsplanen är en bärare. Den bär reglerna om registrering, bevarande och gallring ([[C-200 Gallring]]) per verksamhetsprocess och handlingstyp, och myndigheten fastställer den; Riksarkivets föreskrifter är den påverkan reglerna kommer ur. Arkivredovisningen likaså. Registerförteckningen enligt dataskyddsförordningen bär inga regler och är ingen bärare (ADR 0031).
