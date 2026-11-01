---
id: C-135
term: Verksamhetshändelse
terms:
  - term: Verksamhetshändelse
    language: sv
    source: catalogue
definition: "händelse som inträffar i verksamheten eller dess omvärld"
kind: element-type
generic: "[[C-078 Händelse]]"
---
# C-135 Verksamhetshändelse

**Definition:** händelse som inträffar i verksamheten eller dess omvärld

## Anmärkning

Motsvarar ArchiMates Business Event. BPMN:s start-, mellan- och sluthändelser och CMMN:s EventListener är verksamhetshändelser, med sorten (meddelande, tid, fel, signal) i beskrivningen. CMMN:s milstolpe (Milestone), ett nåbart mål utan eget arbete, är den verksamhetshändelse en handläggning ([[C-160 Handläggning]]) eller en del av den utlöser när den är klar; händelsen utlöser ([[C-098 utlöser]]) det tillstånd ([[C-182 Tillstånd]]) ärendet då nått, och i en tillståndsvy ritas den så. Beslutet: ADR 0022; tillståndet som elementtyp ADR 0024.
