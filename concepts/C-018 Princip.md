---
id: C-018
term: Princip
terms:
  - term: Princip
    language: sv
    source: catalogue
definition: "styrmedel som anger vilken riktning som ska väljas när flera alternativ är möjliga"
kind: governance-type
decided_by: [reference]
generic: "[[C-015 Styrmedel]]"
associative:
  - concept: "[[C-022 Ändamål]]"
    label: härleds ur
  - concept: '[[C-184 Påverkan]]'
    label: härleds ur
  - concept: '[[C-185 Bedömning]]'
    label: härleds ur
  - concept: '[[C-023 Konsekvens]]'
    label: anger
---
# C-018 Princip

**Definition:** styrmedel som anger vilken riktning som ska väljas när flera alternativ är möjliga

## Anmärkning

Principen är ett ställningstagande med generalitet: den gäller alla val av en viss typ, till skillnad från beslutet, som gäller ett enskilt fall. Valet prövas mot principen; riktningen är given men valet lämnas kvar. Principen härleds ur ett ändamål, en påverkan ([[C-184 Påverkan]]) eller en bedömning ([[C-185 Bedömning]]), anger sina konsekvenser, är prövbar men inte binär och kan behöva vägas mot andra principer.

Principen står i en bärare ([[C-016 Bärare]]) som den med mandat ([[C-189 Mandat]]) fastställer: affärsplanen, verksamhetsplanen, en riktlinje. En arkitekturprincip ([[C-040 Arkitekturprincip]]) beslutas genom att ingå i en antagen referensarkitektur, som är dess bärare; bland arkitekturbeskrivningarna är det bara referensarkitekturen som fastställer principer. Arkitekturprincipen tar beskrivningens nivå, har ingen detaljeringsgrad och anger de perspektiv den gäller. Beslut 37. Markeringen `decided_by: [reference]` på Princip och Arkitekturprincip är en spärr, ingen relation: bland arkitekturbeskrivningarna får bara en referensarkitektur fastställa en princip, och en målarkitektur, nulägesarkitektur eller transitionsarkitektur som listar den visar att den gäller utan att fastställa den. Verksamhetens princip fastställs genom sin bärare, utanför beskrivningarna.

Den som har mandat ([[C-189 Mandat]]) formulerar principen som svar på en bedömning ([[C-185 Bedömning]]) (beslut 23, beslut 25).

## Motsvarigheter

Principen är SBVR:s och Business Motivation Models business policy: styrning som inte är direkt prövbar, finns för att vägleda och som regler härleds ur.

## Exempel

"Utveckla för återanvändning."
