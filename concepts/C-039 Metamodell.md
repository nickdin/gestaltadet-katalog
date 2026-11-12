---
id: C-039
term: Metamodell
terms:
  - term: Metamodell
    language: sv
    source: catalogue
definition: modell som definierar vilka typer av arkitekturelement och relationer en arkitekturbeskrivning får använda
associative:
  - concept: '[[C-034 Arkitekturelement]]'
    label: definierar typerna av
---
# C-039 Metamodell

**Definition:** modell som definierar vilka typer av arkitekturelement och relationer en arkitekturbeskrivning får använda

## Exempel

katalogen själv, ArchiMate, TOGAF:s innehållsmetamodell, DIGG:s, BPMN:s.

## Anmärkning

Katalogen är GestaltaDets metamodell: dess elementtyper, dess relationstyper och vad varje perspektiv täcker. ArchiMate är en annan metamodell.

Lagret rymmer bara beskrivningar som följer katalogens metamodell. En beskrivning som följer en annan metamodell översätts genom en mappningstabell innan den tas in. Exempel: bostadsbolagets konsult ritar felanmälan i ArchiMate. Ritningen är en arkitekturbeskrivning som följer ArchiMate. När bolaget tar in den i sin målarkitektur blir Business Process en verksamhetsprocess ([[C-130 Verksamhetsprocess]]).

En mappningstabell översätter mellan två metamodeller, typ för typ. Den säger ingenting om symboler.

Metamodellen avgör vad en organisation kan säga om sig själv. Ett bostadsbolag som väljer en metamodell utan beslutslogik ([[C-178 Beslutslogik]]) kan inte beskriva hur hyran bestäms som en regel bolaget återanvänder.

Notationen ([[C-212 Notation]]) är ingen del av metamodellen. ISO 42010:s model kind rymmer både metamodellen och notationen, och katalogen håller isär dem. Beslut 42.
