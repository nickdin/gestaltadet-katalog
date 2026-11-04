---
id: C-208
term: ansvarar för
terms:
  - term: ansvarar för
    language: sv
    status: preferred
    source: concept new
definition: relationstyp som anger att en roll äger ett annat arkitekturelement och ytterst svarar för det
kind: relation-type
key: responsible_for
---
# C-208 ansvarar för

**Definition:** relationstyp som anger att en roll äger ett annat arkitekturelement och ytterst svarar för det

## Anmärkning

Relationen går från rollen till det den äger: informationsägaren ([[C-167 Informationsägare]]) till informationsobjektet ([[C-060 Informationsobjekt]]), processägaren ([[C-206 Processägare]]) till verksamhetsbeteendet ([[C-157 Verksamhetsbeteende]]). Den svarar på frågan vem som äger, och skiljer ägandet från utförandet: tilldelas ([[C-096 tilldelas]]) säger vem som utför. Härledningen nedåt (ADR 0030) och förteckningarna med ägare per behandling (ADR 0031) behöver det svaret.

Relationen är bara för ägarrollerna. Ett styrmedel eller en bärare ägs av den som fastställt det ([[C-183 fastställs av]]), och ett styrobjekt av den som har mandatet ([[C-189 Mandat]]) över det.

ArchiMates Assignment får inte gå från en roll till ett passivt objekt, så ArchiMate saknar motsvarighet och exporten får Association. Beslutet: ADR 0035.
