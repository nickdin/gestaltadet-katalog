---
id: C-054
term: Målarkitektur
terms:
  - term: Målarkitektur
    language: sv
    source: catalogue
definition: "arkitekturbeskrivning som avser tidsperspektivet målläge och uttrycker den avsedda arkitekturen hos ett arkitekturobjekt"
generic: "[[C-035 Arkitekturbeskrivning]]"
associative:
  - concept: "[[C-054 Målarkitektur]]"
    label: förfinar
  - concept: "[[C-054 Målarkitektur]]"
    label: prövas mot
---
# C-054 Målarkitektur

**Definition:** arkitekturbeskrivning som avser tidsperspektivet målläge och uttrycker den avsedda arkitekturen hos ett arkitekturobjekt

## Exempel

verksamhetens målarkitektur; målarkitekturen för en verksamhetsdomän; målarkitekturen för en lösning.

## Anmärkning

Ett arkitekturobjekt har högst en målarkitektur, och arkitekturen realiseras enligt den. På vägen dit har objektet noll eller flera transitionsarkitekturer. Domänens målarkitektur förfinar verksamhetens, prövas mot den och använder dess arkitekturelement; det binder nivåerna ihop.

Perspektiven är vyer i målarkitekturen, beskrivna var för sig och i relation till varandra genom korrespondenser. En vy kan saknas eller beslutas senare utan att det blir en annan målarkitektur. Det som finns per perspektiv är principer och referensarkitekturer.

Målarkitekturen skiljer sig från referensarkitekturen, som uttrycker de allmänna valen i samma arkitektur: målarkitekturen uttrycker de bestämda valen. Den beslutar inga principer, för där är valen redan gjorda. Den utformas enligt principer som redan är beslutade, prövas mot dem och hänvisar till dem.

Som dokument är målarkitekturen en bärare ([[C-016 Bärare]]): målen och kraven står i den. Principerna står i referensarkitekturen; mål och krav är ändå inga delar av arkitekturen.

Målbild och viljeinriktning används som synonymer. TOGAF: target architecture; finns inte i ISO 42010.
