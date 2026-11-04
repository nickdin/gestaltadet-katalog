---
id: C-008
term: Verksamhetsdomän
terms:
  - term: Verksamhetsdomän
    language: sv
    source: catalogue
definition: "avgränsad del av verksamheten med eget uppdrag och egen styrning"
kind: architecture-object-type
architecture_level: domain
generic: "[[C-032 Arkitekturobjekt]]"
associative:
  - concept: "[[C-007 Verksamhet]]"
    label: ingår i
  - concept: "[[C-008 Verksamhetsdomän]]"
    label: kan ingå i
---
# C-008 Verksamhetsdomän

**Definition:** avgränsad del av verksamheten med eget uppdrag och egen styrning

## Anmärkning

En verksamhetsdomän ingår i verksamheten eller i en annan verksamhetsdomän, alltid i exakt en. Den domän som ingår i en annan har ändå eget uppdrag ([[C-149 Uppdrag]]) och egen styrning. En leverantör levererar aldrig en domän, bara dess lösningar ([[C-155 är leverantör till]]).

Verksamhetsdomänen är både styrobjekt och arkitekturobjekt, samma sak sedd från styrningens respektive arkitekturens håll. Som styrobjekt är den det som styrningen av en domän avser, till exempel utvecklingsstyrning ([[C-043 Utvecklingsstyrning]]). Som arkitekturobjekt står den på domännivå, under verksamheten ([[C-007 Verksamhet]]).
