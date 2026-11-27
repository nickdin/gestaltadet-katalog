---
id: C-197
term: Värdemängd
terms:
  - term: Värdemängd
    language: sv
    status: preferred
    source: concept new
  - term: värdeförråd
    language: sv
    source: concept change
    status: admitted
  - term: kodverk
    language: sv
    source: concept change
    status: admitted
  - term: domän
    language: sv
    source: concept change
    status: deprecated
definition: mängd av de värden en uppgift får anta
associative:
  - concept: '[[C-161 Uppgift]]'
    label: gäller en
  - concept: '[[C-182 Tillstånd]]'
    label: är statusuppgiftens
---
# C-197 Värdemängd

**Definition:** mängd av de värden en uppgift får anta

## Anmärkning

Värdemängden ritas inte som egen ruta utan står som text vid uppgiften ([[C-161 Uppgift]]) i informationsobjektets ([[C-060 Informationsobjekt]]) lista över uppgifter: ett begrepp, ingen elementtyp. Statusuppgiftens värdemängd är verksamhetsobjektets tillstånd ([[C-182 Tillstånd]]): varje värde där är ett läge i tillståndsvyn, och ingen annan värdemängd pekar på element. Värdeförråd och kodverk är alternativa termer, kodverk när värdena är koder med en betydelse var. Domän avråds, eftersom ordet i katalogen är verksamhetsdomänens ([[C-008 Verksamhetsdomän]]).

En värdemängd som organisationen själv fastställer, äger eller ger egna uppgifter, som Stödform med villkor och giltighetstid, är ett informationsobjekt av datakategorin referensdata ([[C-203 Referensdata]]). Den som bara räknas upp vid uppgiften förblir text. [[0032-datakategorin-ar-ett-begrepp-resursdata-referensdata-transaktionsdata-och-handelsedata-sitter-pa-informationsobjektet-hogst-en-och-frivillig-och-referensdata-ar-en-vardemangd-organisationen-sjalv-faststaller|Beslut 32]].

## Motsvarigheter

Motsvarar Enumeration i Unified Modeling Language (UML), vars literaler är värdena. [[0029-klassen-ar-informationsobjektet-tillstandsmaskinen-ar-tillstandsvyn-anvandningsfallet-ar-tjansten-vardemangd-ar-ett-begrepp-och-uml-tas-in-for-lasarnas-skull-utan-tveksamma-rader|Beslut 29]].

## Exempel

utrett, beslutat och avslutat för ärendets statusuppgift; kommunkoderna för uppgiften kommun; ja och nej för uppgiften medlem i riksorganisation.
