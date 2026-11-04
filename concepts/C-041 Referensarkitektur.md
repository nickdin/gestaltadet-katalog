---
id: C-041
term: Referensarkitektur
terms:
  - term: Referensarkitektur
    language: sv
    source: catalogue
definition: "arkitekturbeskrivning som uttrycker arkitekturprinciper, ensamma eller tillämpade i ett återanvändbart mönster"
generic: "[[C-035 Arkitekturbeskrivning]]"
associative:
  - concept: "[[C-040 Arkitekturprincip]]"
    label: uttrycker
---
# C-041 Referensarkitektur

**Definition:** arkitekturbeskrivning som uttrycker arkitekturprinciper, ensamma eller tillämpade i ett återanvändbart mönster

## Anmärkning

Beskriver de allmänna valen i arkitekturen på sin nivå: principer och mönster som gäller alla val av en viss typ. Bara referensarkitekturen beslutar principer. Målarkitekturen beskriver de bestämda valen; tillsammans beskriver de en och samma arkitektur, och en referensarkitektur är aldrig samtidigt en målarkitektur.

Valen blir en del av arkitekturen när ett forum antar referensarkitekturen. En som inte är antagen, till exempel en som kommer utifrån, beskriver ingen bestämd arkitektur; därför beskriver en arkitekturbeskrivning noll eller en arkitektur. Referensarkitekturen har inget tidsperspektiv: allmänna val gäller från att de antas tills de ändras.

Referensarkitekturen gäller på en nivå och för ett eller flera perspektiv, som principen. Verksamheten eller en verksamhetsdomän antar den, på den lägsta nivå som har alla berörda lösningar under sig, och en lösnings arkitektur kan utformas enligt den. En referensarkitektur för en sorts lösning, till exempel dataprodukter, handlar om lösningar men antas alltså inte av en lösning. En referensarkitektur kan innehålla enbart principer; en sådan för hela verksamheten är det översta lagret av principer.
