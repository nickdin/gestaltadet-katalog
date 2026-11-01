---
id: C-176
term: Applikationsaktivitet
terms:
  - term: Applikationsaktivitet
    language: sv
    status: preferred
    source: concept new
definition: avgränsat stycke arbete som en applikation utför som ett steg i ett applikationsbeteende
kind: element-type
generic: '[[C-126 Aktivitet]]'
partitive: '[[C-179 Applikationsbeteende]]'
---
# C-176 Applikationsaktivitet

**Definition:** avgränsat stycke arbete som en applikation utför som ett steg i ett applikationsbeteende

## Anmärkning

Ett steg i ett applikationsbeteende ([[C-179 Applikationsbeteende]]): i en applikationsprocess ([[C-131 Applikationsprocess]]) eller en applikationsfunktion ([[C-133 Applikationsfunktion]]), som rymmer den ([[C-100 aggregerar]]). Ett steg en applikation utför åt verksamheten, BPMN:s Service Task, är ingen applikationsaktivitet: det är en verksamhetsaktivitet ([[C-175 Verksamhetsaktivitet]]) som realiseras av ([[C-094 realiseras av]]) en applikationstjänst ([[C-128 Applikationstjänst]]). Applikationsaktiviteten är steget inuti applikationens egen process. ArchiMate har ingen aktivitetstyp: en export skriver den som Application Process, och en import läser varje Application Process som applikationsprocess. Beslutet: ADR 0022.
