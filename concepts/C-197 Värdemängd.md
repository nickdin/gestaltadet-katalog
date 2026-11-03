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

Ett begrepp, ingen elementtyp: värdemängden ritas inte som egen ruta utan står som text vid uppgiften ([[C-161 Uppgift]]) i informationsobjektets ([[C-060 Informationsobjekt]]) lista över uppgifter. Värdeförråd och kodverk är alternativa termer, kodverk när värdena är koder med en betydelse var; domän avråds, eftersom ordet i katalogen är verksamhetsdomänens ([[C-008 Verksamhetsdomän]]). Statusuppgiftens värdemängd är verksamhetsobjektets tillstånd ([[C-182 Tillstånd]]): varje värde där är ett läge i tillståndsvyn, och ingen annan värdemängd pekar på element. Motsvarar Enumeration i Unified Modeling Language (UML), vars literaler är värdena. ADR 0029.

En värdemängd som organisationen själv fastställer, äger eller ger egna uppgifter, som Stödform med villkor och giltighetstid, är ett informationsobjekt av datakategorin referensdata ([[C-203 Referensdata]]); den som bara räknas upp vid uppgiften förblir text. ADR 0032.

## Exempel

utrett, beslutat och avslutat för ärendets statusuppgift; kommunkoderna för uppgiften kommun; ja och nej för uppgiften medlem i riksorganisation.
