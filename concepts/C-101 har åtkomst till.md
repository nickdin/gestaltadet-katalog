---
id: C-101
term: har åtkomst till
terms:
  - term: har åtkomst till
    language: sv
    source: catalogue
definition: "relationstyp som anger att ett arkitekturelement kan läsa eller skriva ett annat arkitekturelement"
kind: relation-type
key: accesses
access: true
---
# C-101 har åtkomst till

**Definition:** relationstyp som anger att ett arkitekturelement kan läsa eller skriva ett annat arkitekturelement

## Anmärkning

Relationen går från det åtkommande beteendeelementet till det åtkomna. Motsvarar ArchiMates Access.

Relationen bär fältet `access` med värdet `read`, `write` eller `read-write`, markeringen `access: true` på begreppet säger det. Ur två åtkomster till samma objekt, ett beteende som skriver och ett som läser, härleder programmet flödet mellan beteendena; det lagras aldrig som flödar till ([[C-097 flödar till]]). ADR 0014, ADR 0033.

Motsvarar en handlings läsning eller skrivning av ett objekt i Unified Modeling Language (UML) (StructuralFeatureAction, LinkAction). ADR 0029.
