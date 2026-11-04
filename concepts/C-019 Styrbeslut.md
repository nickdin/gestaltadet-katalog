---
id: C-019
term: Styrbeslut
terms:
  - term: Styrbeslut
    language: sv
    status: preferred
    source: concept change
  - term: Beslut
    language: sv
    status: admitted
    source: catalogue
definition: "styrmedel som anger vilket alternativ som valts i en enskild fråga"
kind: governance-type
generic: "[[C-015 Styrmedel]]"
associative:
  - concept: "[[C-018 Princip]]"
    label: fattas enligt
---
# C-019 Styrbeslut

**Definition:** styrmedel som anger vilket alternativ som valts i en enskild fråga

## Anmärkning

Styrbeslutet är innehållet som bestämts i det enskilda fallet, inte handlingen att besluta. Varje styrmedel tillkommer genom ett beslut, men bara det som gäller ett enskilt fall är ett beslut i modellens mening. Det fallet prövas mot beslutet, men beslutet säger inget om nästa fråga av samma slag. Beslutet fattas enligt de principer som gäller för valet ([[C-018 Princip]]) och behöver inget eget ändamål bakom sig.

Ett vägval kan härledas ur ([[C-064 härleds ur]]) en bedömning ([[C-185 Bedömning]]) och påverkar ([[C-102 påverkar]]) det mål det ska föra verksamheten mot. Flera vägval som hänger ihop är en strategi ([[C-188 Strategi]]), och Business Motivation Models Course of Action, Strategy och Tactic är alla styrbeslut (ADR 0025). Valet av arbetssätt ([[C-196 Arbetssätt]]) är ett styrbeslut (ADR 0028).

Myndighetsbeslut i ärenden avses inte. Beslutet i ett enskilt ärende är ett ärendebeslut ([[C-181 Ärendebeslut]]), ett verksamhetsobjekt, och regeln för hur det bestäms är en beslutslogik ([[C-178 Beslutslogik]]). Förledet styr- håller de tre isär; Beslut ensamt är tillåten term där sammanhanget är styrningens (ADR 0022). Ordet är det arkitekter redan använder: ett arkitekturbeslut är ett beslut som ingår i en arkitektur, där det syns som arkitekturelement och relationerna mellan dem, och ISO 42010:2022 har begreppet architecture decision.

**Avrådd term:** ställningstagande. I vardagsspråket är ett ställningstagande varje beslutad ståndpunkt, alltså alla styrmedel. Det SBVR kallar advice, rådet som bekräftar att en frihet finns, är ett styrbeslut när det alls skrivs ner: svaret på frågan om en regel ska finnas, när svaret blev nej (ADR 0023).

## Exempel

"Ärendehanteringen byggs på plattform X."
