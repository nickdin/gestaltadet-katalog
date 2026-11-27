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

Relationen går från det hela elementet till delen, som [[C-062 består av]] men utan exklusivitet.

## Motsvarigheter

Motsvarar ArchiMates Aggregation.

Motsvarar Aggregation i Unified Modeling Language (UML), en association med aggregationen shared; det yttre beteendet aggregerar det beteende ett CallBehaviorAction anropar. [[0029-klassen-ar-informationsobjektet-tillstandsmaskinen-ar-tillstandsvyn-anvandningsfallet-ar-tjansten-vardemangd-ar-ett-begrepp-och-uml-tas-in-for-lasarnas-skull-utan-tveksamma-rader|Beslut 29]].
