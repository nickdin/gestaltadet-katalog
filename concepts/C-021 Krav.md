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

Objektet prövas mot kravet. Binärt. En sorts regel ([[C-020 Regel]]): regeln anger vad som ska gälla, kravet att det som ska gälla är en egenskap hos styrobjektet. SBVR skiljer inte kravet från regeln; lagret behåller ordet eftersom arkitekter säger krav och ArchiMate har Requirement. Krav kan härledas ur en princip via dess konsekvenser, eller komma direkt från lag och förordning. Inte ett systemkrav i kravhanteringens mening: kravet är ett styrmedel som styrobjektet prövas mot, inte en beskrivning av vad ett system ska göra. Beslutet: ADR 0023.

## Exempel

"Alla informationsutbyten ska ha en utpekad informationsägare."
