---
id: C-016
term: Bärare
terms:
  - term: Bärare
    language: sv
    source: catalogue
definition: "dokument eller artefakt som ett eller flera styrmedel eller ändamål står i"
kind: governance-type
associative:
  - concept: "[[C-015 Styrmedel]]"
    label: bär
  - concept: "[[C-022 Ändamål]]"
    label: bär
---
# C-016 Bärare

**Definition:** dokument eller artefakt som ett eller flera styrmedel eller ändamål står i

## Exempel

riktlinje, anvisning, standard, plan, målarkitektur, verksamhetsplan, budget, informationshanteringsplan.

## Anmärkning

Ett styrmedel kan byta bärare utan att ändra innehåll. Standarden är en bärare: den bär krav, och kraven är styrmedlen. En arkitekturbeskrivning som beslutar principer är deras bärare. Ett dokument som varken bär styrmedel eller ändamål är ingen bärare; som databärare är det en artefakt ([[C-081 Artefakt]]), och dess läsbara innehåll är representationer ([[C-085 Representation]]). Bäraren är det som fastställs: relationen fastställs av ([[C-183 fastställs av]]) går från bäraren till den aktör, roll eller det forum som beslutat eller antagit den, och styrmedlen den bär följer med; ett styrmedel utan bärare får relationen själv (ADR 0023).

**Nödvändighet:** Varje bärare bär minst ett styrmedel eller ett ändamål.

Informationshanteringsplanen är en bärare: den bär reglerna om registrering, bevarande och gallring ([[C-200 Gallring]]) per verksamhetsprocess och handlingstyp, fastställs av myndigheten, och Riksarkivets föreskrifter är den påverkan reglerna kommer ur; arkivredovisningen likaså. Registerförteckningen enligt dataskyddsförordningen bär inga regler och är ingen bärare (ADR 0031).
