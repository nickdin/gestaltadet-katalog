---
id: C-031
term: Arkitektur
terms:
  - term: Arkitektur
    language: sv
    source: catalogue
definition: "avsiktlig grundläggande utformning av ett arkitekturobjekt: valen om dess form och funktion som styr hur det realiseras och förändras"
associative:
  - concept: "[[C-041 Referensarkitektur]]"
    label: kan utformas enligt
  - concept: "[[C-054 Målarkitektur]]"
    label: realiseras enligt
  - concept: "[[C-032 Arkitekturobjekt]]"
    label: avser
  - concept: "[[C-033 Arkitekturnivå]]"
    label: gäller på
---
# C-031 Arkitektur

**Definition:** avsiktlig grundläggande utformning av ett arkitekturobjekt: valen om dess form och funktion som styr hur det realiseras och förändras

## Anmärkning

Arkitektur finns när avsikten är artikulerad och går att skilja från det byggda. Struktur finns alltid: processer körs, information flödar, beroenden finns, oavsett om någon beskrivit dem. Ett hus byggt utan ritning har struktur, inte arkitektur. Det är det arkitekturarbetet gör: gör implicit struktur till explicit arkitektur, så att den går att resonera om, styra och förändra. Därför har ett arkitekturobjekt noll eller en arkitektur.

Arkitekturen har två sorters delar: arkitekturprinciperna ([[C-040 Arkitekturprincip]]), som är de allmänna valen, och arkitekturelementen med relationerna mellan dem, som uttrycker de bestämda valen. Referensarkitekturen uttrycker de allmänna valen och målarkitekturen de bestämda; tillsammans beskriver de en och samma arkitektur. Principerna styr de mer detaljerade valen i samma arkitektur, och arkitekturen som helhet styr arkitekturobjektet. Mål och krav är inga delar: målen kommer ur ändamålet och kraven härleds ur principerna. Arkitekturen gäller på en arkitekturnivå, som följer av arkitekturobjektet, och domänens arkitektur är en del av verksamhetens.

ISO 42010 säger att varje system har en arkitektur, beskriven eller inte. 2022 års definition, grundläggande begrepp och egenskaper samt styrande principer för realisering och utveckling, rymmer ändå avsikten och räknar principerna till arkitekturen.

## Alternativ definition, att ta ställning till

**Definition:** grundläggande struktur hos ett arkitekturobjekt, uttryckt i dess arkitekturelement och relationerna mellan dem

Den ISO-trogna varianten: varje arkitekturobjekt har då exakt en arkitektur, beskriven eller inte, och arkitekturarbetet beskriver något som redan finns. Valet mellan de två avgör om ett arkitekturobjekt har 0..1 eller 1 arkitektur i modellen. Det avgör också om "arkitektur" kan sägas om en lösning som byggts utan avsikt, och var principerna står. En struktur består av element och relationer, så med den här varianten kan en princip inte vara en del av arkitekturen. Att principerna räknas dit förutsätter den gällande definitionen.
