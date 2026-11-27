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
  - concept: '[[C-213 Avvikelse]]'
    label: kan godta
---
# C-019 Styrbeslut

**Definition:** styrmedel som anger vilket alternativ som valts i en enskild fråga

## Anmärkning

Styrbeslutet är innehållet som bestämts i det enskilda fallet, inte handlingen att besluta. Varje styrmedel tillkommer genom ett beslut, men bara det som gäller ett enskilt fall är ett beslut i modellens mening. Det fallet prövas mot beslutet, men beslutet säger inget om nästa fråga av samma slag. Beslutet fattas enligt de principer som gäller för valet ([[C-018 Princip]]) och behöver inget eget ändamål bakom sig.

Ett styrbeslut kan gå emot en princip. Väger en annan princip tyngre i valet är beslutet ändå fattat enligt principerna. Bär ingen princip valet är det en avvikelse ([[C-213 Avvikelse]]). Beslutet att godta avvikelsen är ett eget styrbeslut, som anger sitt skäl och fattas ovanför den som är bunden av principen. [[0043-en-princip-klarar-tre-fragor-innehallet-avgor-om-den-ar-en-arkitekturprincip-avvikelsen-ar-ett-eget-begrepp-och-policyn-ar-en-barare|Beslut 43]].

Ett vägval kan härledas ur ([[C-064 härleds ur]]) en bedömning ([[C-185 Bedömning]]) och påverkar ([[C-102 påverkar]]) det mål det ska föra verksamheten mot. Flera vägval som hänger ihop är en strategi ([[C-188 Strategi]]). Valet av arbetssätt ([[C-196 Arbetssätt]]) är ett styrbeslut ([[0028-varde-ar-en-elementtyp-i-strategiperspektivet-dit-vardeerbjudandet-flyttar-arbetssatt-ar-ett-begrepp-svaret-heter-hjalp-och-vdml-tas-in-med-rakneverket-omappat|beslut 28]]).

Myndighetsbeslut i ärenden avses inte. Beslutet i ett enskilt ärende är ett ärendebeslut ([[C-181 Ärendebeslut]]), ett verksamhetsobjekt, och regeln för hur det bestäms är en beslutslogik ([[C-178 Beslutslogik]]). Förledet styr- håller de tre isär; Beslut ensamt är tillåten term där sammanhanget är styrningens ([[0022-aktivitet-och-beslutslogik-ar-elementtyper-bpmn-cmmn-och-dmn-tas-in-som-bestandsdelar-i-beteendet-med-egna-mappningstabeller|beslut 22]]). Ordet är det arkitekter redan använder: ett arkitekturbeslut är ett beslut som ingår i en arkitektur, där det syns som arkitekturelement och relationerna mellan dem, och ISO 42010:2022 har begreppet architecture decision.

**Avrådd term:** ställningstagande. I vardagsspråket är ett ställningstagande varje beslutad ståndpunkt, alltså alla styrmedel.

## Motsvarigheter

Business Motivation Models Course of Action, Strategy och Tactic är alla styrbeslut ([[0025-paverkan-och-bedomning-ar-elementtyper-strategin-ar-sammanhangande-styrbeslut-visionen-ar-ett-mal-utan-matt-och-bmm-tas-in-med-andamalet-som-katalogens-tillagg|beslut 25]]).

Det SBVR kallar advice, rådet som bekräftar att en frihet finns, är ett styrbeslut när det alls skrivs ner: svaret på frågan om en regel ska finnas, när svaret blev nej ([[0023-regeln-anger-vad-som-ska-galla-kravet-ar-en-sorts-regel-katalogen-ar-organisationens-ordlista-och-sbvr-tas-in-med-faststalls-av-som-relationstyp|beslut 23]]).

## Exempel

"Ärendehanteringen byggs på plattform X."
