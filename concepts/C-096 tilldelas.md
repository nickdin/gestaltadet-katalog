---
id: C-096
term: tilldelas
terms:
  - term: tilldelas
    language: sv
    source: catalogue
definition: relationstyp som anger att ett arkitekturelement utför ett annat arkitekturelements beteende
kind: relation-type
key: assigned_to
---
# C-096 tilldelas

**Definition:** relationstyp som anger att ett arkitekturelement utför ett annat arkitekturelements beteende

## Anmärkning

Relationen går från det utförande elementet till beteendet. Den säger vem som utför, inte vem som äger: ägandet är ansvarar för ([[C-208 ansvarar för]], beslut 35).

## Motsvarigheter

Motsvarar ArchiMates Assignment.

Motsvarar Deployment i Unified Modeling Language (UML), artefakten driftsatt på noden, och simbanan (ActivityPartition) som utför stegen i den. Beslut 29.
