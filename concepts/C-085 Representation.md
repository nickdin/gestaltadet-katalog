---
id: C-085
term: Representation
terms:
  - term: Representation
    language: sv
    source: catalogue
  - term: informationsbärare
    language: sv
    source: concept change
    status: admitted
  - term: handling
    language: sv
    source: concept change
    status: admitted
  - term: handlingstyp
    language: sv
    source: concept change
    status: admitted
definition: "konkret, ofta mänskligt läsbar form som ett informationsobjekt tar"
kind: element-type
associative:
  - concept: '[[C-060 Informationsobjekt]]'
    label: ger form åt
  - concept: '[[C-165 Lagringsyta]]'
    label: ligger på
---
# C-085 Representation

**Definition:** konkret, ofta mänskligt läsbar form som ett informationsobjekt tar

## Anmärkning

Motsvarar ArchiMates Representation. Informationsbärare i kartläggningens mening är representationen; stället den ligger på är lagringsytan ([[C-165 Lagringsyta]]), som aggregerar ([[C-100 aggregerar]]) den: samma representation kan ligga på flera ytor, och ytan finns kvar när representationen tas bort. En utskriven blankett eller en pappersakt är en representation, det fysiska som bär information. SDMN:s Document, ett dokument tryckt eller elektroniskt, är en representation, och dess Physical är det när saken bär information; utan informationssida är den ett verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]). Beslutet: ADR 0024.
