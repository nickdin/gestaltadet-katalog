---
id: C-021
term: Krav
terms:
  - term: Krav
    language: sv
    source: catalogue
definition: regel som anger en egenskap som styrobjektet ska ha
kind: governance-type
associative:
  - concept: '[[C-018 Princip]]'
    label: kan härledas ur
generic: '[[C-020 Regel]]'
---
# C-021 Krav

**Definition:** regel som anger en egenskap som styrobjektet ska ha

## Anmärkning

Ett krav är en sorts regel ([[C-020 Regel]]): regeln anger vad som ska gälla, kravet att det som ska gälla är en egenskap hos styrobjektet. Styrobjektet prövas mot kravet, och prövningen är binär. Ett krav kan härledas ur en princip via dess konsekvenser, eller komma direkt ur påverkan ([[C-184 Påverkan]]): lag och förordning, eller den överordnade nivåns krav på styrobjekten under den. Ursprunget är regelns, och kravet ärver det. Det är inte ett systemkrav i kravhanteringens mening: kravet är ett styrmedel som styrobjektet prövas mot, inte en beskrivning av vad ett system ska göra. SBVR skiljer inte kravet från regeln; lagret behåller ordet för att arkitekter säger krav och ArchiMate har Requirement. Beslut 23.

## Exempel

"Alla informationsutbyten ska ha en utpekad informationsägare."
