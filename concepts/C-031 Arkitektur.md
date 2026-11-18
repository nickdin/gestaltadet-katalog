---
id: C-031
term: Arkitektur
terms:
  - term: Arkitektur
    language: sv
    source: catalogue
definition: 'grundläggande utformning av ett arkitekturobjekt, beskriven eller inte: dess form och funktion, vilka arkitekturobjekt det delas in i och de principer som styr hur det realiseras och förändras'
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

**Definition:** grundläggande utformning av ett arkitekturobjekt, beskriven eller inte: dess form och funktion, vilka arkitekturobjekt det delas in i och de principer som styr hur det realiseras och förändras

## Anmärkning

Varje arkitekturobjekt ([[C-032 Arkitekturobjekt]]) har exakt en arkitektur, beskriven eller inte. Ett hus som är byggt utan ritning har en arkitektur, fast ingen har beskrivit den. På samma sätt körs processer och flödar information i en verksamhet som ingen har beskrivit. Arkitekturarbetet beskriver utformningen, så att den går att resonera om, styra och förändra. Beslut 37.

Arkitekturen säger också vilka arkitekturobjekt objektet delas in i. Verksamhetens arkitektur säger vilka verksamhetsdomäner som finns. Domänens arkitektur säger vilka lösningar som finns i domänen. Varje del har en egen arkitektur, och den är en del av det omgivande objektets arkitektur. Att verksamheten själv finns säger ingen arkitektur. Arkitekturen gäller på en arkitekturnivå ([[C-033 Arkitekturnivå]]), som följer av arkitekturobjektet. Beslut 59.

Avsikten står i beskrivningarna. Nulägesarkitekturen ([[C-057 Nulägesarkitektur]]) uttrycker den faktiska utformningen och målarkitekturen ([[C-054 Målarkitektur]]) den avsedda. Referensarkitekturen ([[C-041 Referensarkitektur]]) uttrycker de allmänna valen, och gapanalysen ([[C-105 Gapanalys]]) visar skillnaden mellan nuläge och mål. En avsikt som ingen har beskrivit finns inte i lagret.

Arkitekturen har två sorters delar. Arkitekturprinciperna ([[C-040 Arkitekturprincip]]) är de allmänna valen. Arkitekturelementen ([[C-034 Arkitekturelement]]) och relationerna mellan dem är de bestämda valen. Referensarkitekturen uttrycker de allmänna valen och målarkitekturen de bestämda. Tillsammans beskriver de två en och samma arkitektur. Principerna styr de mer detaljerade valen i arkitekturen, och arkitekturen som helhet styr arkitekturobjektet. En arkitektur som ingen har beskrivit har inga principer. Mål och krav är inga delar av arkitekturen: målen kommer ur ändamålet, och kraven härleds ur principerna.

## Motsvarigheter

ISO 42010 säger detsamma: varje system har en arkitektur, beskriven eller inte. Standardens definition från 2022 räknar principerna till arkitekturen: grundläggande begrepp och egenskaper samt styrande principer för realisering och utveckling. Beslut 37 övervägde en annan läsning, där ett objekt som är byggt utan ritning har struktur men ingen arkitektur. Beslutet avvisade den.

## Exempel

Arkitekturen hos Myndigheten för föreningsstöd säger att myndigheten har fem verksamhetsdomäner under generaldirektören. Arkitekturen hos domänen Registerföring och tillsyn säger att registerlösningen är en egen lösning, eftersom två lösningar delar Föreningsregistret.
