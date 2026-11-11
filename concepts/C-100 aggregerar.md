---
id: C-100
term: aggregerar
terms:
  - term: aggregerar
    language: sv
    source: catalogue
definition: "relationstyp som anger att ett arkitekturelement har ett annat arkitekturelement som en icke-exklusiv del"
kind: relation-type
key: aggregates
aggregation: true
---
# C-100 aggregerar

**Definition:** relationstyp som anger att ett arkitekturelement har ett annat arkitekturelement som en icke-exklusiv del

## Anmärkning

Relationen går från det hela elementet till delen, som [[C-062 består av]] men utan exklusivitet. Motsvarar ArchiMates Aggregation.

Motsvarar Aggregation i Unified Modeling Language (UML), en association med aggregationen shared; det yttre beteendet aggregerar det beteende ett CallBehaviorAction anropar. Beslut 29.
