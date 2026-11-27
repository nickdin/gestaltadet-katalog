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

Ett styrmedel kan byta bärare utan att ändra innehåll. Standarden är en bärare: den bär krav, och kraven är styrmedlen. En arkitekturbeskrivning som beslutar principer är deras bärare. Riskanalysen och omvärldsanalysen är bärare: de bär bedömningar ([[C-185 Bedömning]]) ([[0025-paverkan-och-bedomning-ar-elementtyper-strategin-ar-sammanhangande-styrbeslut-visionen-ar-ett-mal-utan-matt-och-bmm-tas-in-med-andamalet-som-katalogens-tillagg|beslut 25]], [[0037-arkitekturen-finns-alltid-bararen-bar-bedomningar-hallningen-ar-intern-paverkan-regeln-lamnar-inget-bedomningsutrymme-och-principen-star-i-en-barare-som-den-med-mandat-faststaller|beslut 37]]). Policyn är en bärare. Ordet namnger dokumentet och säger inget om vad som står i det. Bostadsbolagets uthyrningspolicy bär en regel, den som stått längst i kön går först. Den bär en princip, bolaget hyr hellre ut till den som saknar bostad än till den som vill byta. Och den bär ett mål, hyresgästerna ska vara nöjda. Varje mening prövas för sig ([[0043-en-princip-klarar-tre-fragor-innehallet-avgor-om-den-ar-en-arkitekturprincip-avvikelsen-ar-ett-eget-begrepp-och-policyn-ar-en-barare|beslut 43]]). Arbetsordningen, delegationsordningen, vd-instruktionen och attestordningen är bärare. De bär reglerna som delegerar ([[C-214 Delegation]]), och de skiljer sig i vilka regler de bär ([[0044-delegation-ar-ett-eget-begrepp-ett-delegerat-styrobjekt-tar-mandat-ansvar-och-ram-med-sig-och-beslutanderatt-i-arenden-flyttar-inget-ansvar|beslut 44]]). Ett dokument som varken bär styrmedel, ändamål eller bedömning är ingen bärare. Som databärare är det en artefakt ([[C-081 Artefakt]]), och dess läsbara innehåll är representationer ([[C-085 Representation]]).

Bäraren är det som fastställs. Relationen fastställs av ([[C-183 fastställs av]]) går från bäraren till den aktör eller roll som beslutat eller antagit den, och styrmedlen bäraren bär följer med. Ett styrmedel utan bärare får relationen själv ([[0023-regeln-anger-vad-som-ska-galla-kravet-ar-en-sorts-regel-katalogen-ar-organisationens-ordlista-och-sbvr-tas-in-med-faststalls-av-som-relationstyp|beslut 23]]). I lagret skrivs bär mellan ett bärarelement och det styrmedel det bär med relationstypen aggregerar ([[C-100 aggregerar]]): ett styrmedel kan byta bärare utan att ändra innehåll, så det är ingen exklusiv del ([[0019-malet-forblir-styrmedel-och-ritas-som-styrmedelselement-portfolj-ar-en-elementtyp|beslut 19]]).

**Nödvändighet:** Varje bärare bär minst ett styrmedel, ett ändamål eller en bedömning.

Informationshanteringsplanen är en bärare. Den bär reglerna om registrering, bevarande och gallring ([[C-200 Gallring]]) per handlingsslag och handlingstyp, och myndigheten fastställer den; Riksarkivets föreskrifter är den påverkan reglerna kommer ur. Arkivredovisningen likaså. Ordet informationshanteringsplan står inte i föreskrifterna. De kräver arkivredovisningen av statliga myndigheter, och i kommunerna heter planen dokumenthanteringsplan ([[0067-arkivet-har-tva-enheter-handlingsslaget-lases-ur-verksamhetsbeteendet-och-handlingstypen-ar-representationen-redovisad-under-aktiviteten-dar-handlingen-kommer-in-eller-upprattas|beslut 67]]). Registerförteckningen enligt dataskyddsförordningen bär inga regler och är ingen bärare ([[0031-handlingen-ar-representationen-allman-handling-och-gallring-ar-begrepp-forteckningarna-bor-utanfor-lagret-och-lagringsytan-far-vara-fysisk|beslut 31]]).
