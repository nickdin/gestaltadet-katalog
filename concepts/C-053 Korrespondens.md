---
id: C-053
term: Korrespondens
terms:
  - term: Korrespondens
    language: sv
    source: catalogue
definition: "relation som anger hur arkitekturelement i en arkitekturvy hänger ihop med arkitekturelement i en annan vy av samma arkitekturbeskrivning"
associative:
  - concept: "[[C-052 Arkitekturvy]]"
    label: förbinder
---
# C-053 Korrespondens

**Definition:** relation som anger hur arkitekturelement i en arkitekturvy hänger ihop med arkitekturelement i en annan vy av samma arkitekturbeskrivning

UML:s «trace» mellan element i två modeller är en korrespondens, ingen relationstyp. ADR 0029.

## Exempel

en förmåga realiseras av en process; processen stöds av en applikation; applikationen hanterar ett informationsobjekt och körs på en plattform.

## Anmärkning

Korrespondenserna är det som gör beskrivningen till en och inte flera: utan dem är vyerna fristående dokument. De flesta arkitekturbeslut sitter i korrespondenserna, inte inuti en vy. ISO 42010: correspondence.
