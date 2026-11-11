---
id: C-031
term: Arkitektur
terms:
  - term: Arkitektur
    language: sv
    source: catalogue
definition: 'grundläggande utformning av ett arkitekturobjekt, beskriven eller inte: dess form och funktion och de principer som styr hur det realiseras och förändras'
associative:
  - concept: "[[C-041 Referensarkitektur]]"
    label: kan utformas enligt
  - concept: "[[C-054 Målarkitektur]]"
    label: realiseras enligt
  - concept: "[[C-032 Arkitekturobjekt]]"
    label: avser
  - concept: "[[C-033 Arkitekturnivå]]"
    label: gäller på
  - concept: "[[C-031 Arkitektur]]"
    label: kan ingå i
---
# C-031 Arkitektur

**Definition:** grundläggande utformning av ett arkitekturobjekt, beskriven eller inte: dess form och funktion och de principer som styr hur det realiseras och förändras

## Anmärkning

Varje arkitekturobjekt har exakt en arkitektur, beskriven eller inte. Processer körs, information flödar och beroenden finns oavsett om någon beskrivit dem; ett hus byggt utan ritning har en arkitektur, bara ingen artikulerad. Det arkitekturarbetet gör är att artikulera den: göra implicit utformning till beskriven arkitektur, så att den går att resonera om, styra och förändra. Avsikten bor i beskrivningarna. Nulägesarkitekturen ([[C-057 Nulägesarkitektur]]) uttrycker den faktiska utformningen, målarkitekturen ([[C-054 Målarkitektur]]) den avsedda, referensarkitekturen ([[C-041 Referensarkitektur]]) de allmänna valen, och gapanalysen ([[C-105 Gapanalys]]) skillnaden. En avsikt som ingen artikulerat finns inte i lagret. Beslut 37.

Arkitekturen har två sorters delar: arkitekturprinciperna ([[C-040 Arkitekturprincip]]), som är de allmänna valen, och arkitekturelementen med relationerna mellan dem, som uttrycker de bestämda valen. Referensarkitekturen uttrycker de allmänna valen och målarkitekturen de bestämda; tillsammans beskriver de en och samma arkitektur. Principerna styr de mer detaljerade valen i samma arkitektur, och arkitekturen som helhet styr arkitekturobjektet. En arkitektur som ingen artikulerat har inga principer. Mål och krav är inga delar: målen kommer ur ändamålet och kraven härleds ur principerna. Arkitekturen gäller på en arkitekturnivå, som följer av arkitekturobjektet, och domänens arkitektur är en del av verksamhetens.

ISO 42010 säger detsamma: varje system har en arkitektur, beskriven eller inte, och 2022 års definition, grundläggande begrepp och egenskaper samt styrande principer för realisering och utveckling, räknar principerna till arkitekturen. Den avsiktliga läsningen, där ett objekt byggt utan ritning har struktur men ingen arkitektur, övervägdes och avvisades i beslut 37.
