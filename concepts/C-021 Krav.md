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
  - concept: "[[C-018 Princip]]"
    label: kan härledas ur
  - concept: "[[C-029 Extern påverkan]]"
    label: kan komma direkt ur
generic: '[[C-020 Regel]]'
---
# C-021 Krav

**Definition:** regel som anger en egenskap som styrobjektet ska ha

## Anmärkning

Ett krav är en sorts regel ([[C-020 Regel]]): regeln anger vad som ska gälla, kravet att det som ska gälla är en egenskap hos styrobjektet. Styrobjektet prövas mot kravet, och prövningen är binär. Ett krav kan härledas ur en princip via dess konsekvenser, eller komma direkt från lag och förordning. Det är inte ett systemkrav i kravhanteringens mening: kravet är ett styrmedel som styrobjektet prövas mot, inte en beskrivning av vad ett system ska göra. SBVR skiljer inte kravet från regeln; lagret behåller ordet för att arkitekter säger krav och ArchiMate har Requirement. Beslutet: ADR 0023.

## Exempel

"Alla informationsutbyten ska ha en utpekad informationsägare."
