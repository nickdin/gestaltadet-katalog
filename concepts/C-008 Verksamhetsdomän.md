---
id: C-008
term: Verksamhetsdomän
terms:
  - term: Verksamhetsdomän
    language: sv
    source: catalogue
definition: "avgränsad del av verksamheten med eget uppdrag och egen styrning"
kind: architecture-object-type
architecture_level: domain
generic: "[[C-032 Arkitekturobjekt]]"
associative:
  - concept: "[[C-007 Verksamhet]]"
    label: ingår i
  - concept: "[[C-008 Verksamhetsdomän]]"
    label: kan ingå i
---
# C-008 Verksamhetsdomän

**Definition:** avgränsad del av verksamheten med eget uppdrag och egen styrning

## Anmärkning

En verksamhetsdomän ingår i verksamheten eller i en annan verksamhetsdomän, alltid i exakt en. Den domän som ingår i en annan har ändå eget uppdrag ([[C-149 Uppdrag]]) och egen styrning. En leverantör levererar aldrig en domän, bara dess lösningar ([[C-155 är leverantör till]]).

Verksamhetsdomänen är både styrobjekt och arkitekturobjekt, samma sak sedd från styrningens respektive arkitekturens håll. Som styrobjekt är den det som styrningen av en domän avser, till exempel utvecklingsstyrning ([[C-043 Utvecklingsstyrning]]). Som arkitekturobjekt står den på domännivå, under verksamheten ([[C-007 Verksamhet]]).

Varje verksamhetsdomän har en utformning och en produktion. Utformningen är domänens lösningar ([[C-055 Lösning]]): hur beteendet är ordnat, vilka roller som finns, hur informationen är uppbyggd och vilken teknik som används. Produktionen är de enskilda ärendena och de resurser ([[C-122 Resurs]]) som utför dem. Utveckling är att ändra utformningen. Det finns inte två sorters domän, en som utvecklar och en som producerar. Den som säger utvecklingsdomänen menar domänens utformning och ändringen av den, se utvecklingsstyrning ([[C-043 Utvecklingsstyrning]]). Beslut 47.

En domän uppstår där någon har fått ett uppdrag delegerat ([[C-214 Delegation]]) med egen ram ([[C-210 Ram]]). Så ligger domäner i varandra. Rätten att besluta i enskilda ärenden skapar ingen domän. En domän är inte heller en organisationsenhet ([[C-121 Organisationsenhet]]). Enheten är aktören som utför produktionen, och den kan utföra beteende ur en lösning som hör hemma i en annan domän. Beslut 47.

Inom domänens ram finns två slags ram: lösningarnas, för att ändra utformningen, och produktionens. Domänens ägare kan väga dem mot varandra. Det som inte ryms går upp till ägaren av det som omsluter domänen. En domän har högst en portfölj ([[C-011 Portfölj]]), och portföljen väger det som ändrar utformningen. Beslut 47.

En domän med en del av organisationens uppdrag ([[C-149 Uppdrag]]) är kärnverksamhet. En domän med ett inre uppdrag från ledningen är stödverksamhet: den lämnar det de andra behöver för att producera ([[C-174 Leveransprodukt]]). IT är stödverksamhet på samma sätt som HR. Beslut 47.

## Exempel

Bidragsgivningen hos Myndigheten för föreningsstöd, som chefen för Bidragsenheten äger. Utformningen är lösningen Ansökningshandläggningen. Produktionen är årets 4 000 ansökningar och handläggarna som prövar dem. HR är en annan domän: utformningen är lösningen för rekrytering, och produktionen är varje rekrytering.
