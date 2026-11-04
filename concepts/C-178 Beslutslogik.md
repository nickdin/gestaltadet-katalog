---
id: C-178
term: Beslutslogik
terms:
  - term: Beslutslogik
    language: sv
    status: preferred
    source: concept new
definition: återanvändbar regel för hur ett utfall bestäms ur indata
kind: element-type
associative:
  - concept: '[[C-126 Aktivitet]]'
    label: används av
  - concept: '[[C-020 Regel]]'
    label: härleds ur
  - concept: '[[C-029 Extern påverkan]]'
    label: härleds ur
  - concept: '[[C-060 Informationsobjekt]]'
    label: har åtkomst till
---
# C-178 Beslutslogik

**Definition:** återanvändbar regel för hur ett utfall bestäms ur indata

## Anmärkning

Beslutslogik är det DMN (Decision Model and Notation) kallar Decision: att bestämma ett utfall ur indata med en logik som går att skriva ner, en beslutstabell, en formel eller ett regelverk. Logiken ger samma svar varje gång samma indata kommer. Logiken är verksamhetens vare sig en handläggare eller ett system kör den, och hör därför till verksamhetsperspektivet. Ett system som kör den är en applikationstjänst ([[C-128 Applikationstjänst]]) som realiserar den ([[C-094 realiseras av]]), DMN:s Decision Service. Vad logiken avgör är dess utdata, inte dess sort: hos en myndighet är det ofta ett ärendebeslut ([[C-181 Ärendebeslut]]), men beslutslogik finns lika väl i ett bostadsbolags hyressättning. Beslutslogiken är inte ett styrbeslut ([[C-019 Styrbeslut]]), som är innehållet i en fråga styrningen avgjort en gång.

En aktivitet ([[C-126 Aktivitet]]) använder ([[C-095 använder]]) beslutslogiken: BPMN:s Business Rule Task, CMMN:s DecisionTask, och vägskälet i ett flöde. DMN:s övriga byggstenar är relationer, inte typer. En Business Knowledge Model, beslutskunskap skriven för att återanvändas utan eget sammanhang, är en beslutslogik som en annan beslutslogik använder. Input Data är informationsobjekt ([[C-060 Informationsobjekt]]) som logiken har åtkomst till ([[C-101 har åtkomst till]]). Knowledge Source, auktoriteten bakom logiken, är den regel ([[C-020 Regel]]) eller externa påverkan ([[C-029 Extern påverkan]]) som logiken härleds ur ([[C-064 härleds ur]]). ArchiMate har ingen motsvarighet; logiken ritas i DMN. Beslutet: ADR 0022.

En definitionsregel i SBVR:s mening som avgör ett utfall för varje fall, till exempel när en ansökan är komplett, är en beslutslogik; en som bara alltid gäller står i begreppets anmärkning (ADR 0023).
