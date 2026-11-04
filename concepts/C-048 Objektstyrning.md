---
id: C-048
term: Objektstyrning
terms:
  - term: Objektstyrning
    language: sv
    source: catalogue
definition: "objektbaserad styrning där styrobjektet är ett förvaltningsobjekt"
generic: '[[C-005 Objektbaserad styrning]]'
---
# C-048 Objektstyrning

**Definition:** objektbaserad styrning där styrobjektet är ett förvaltningsobjekt

## Anmärkning

Förvaltningsobjektet är en lösning ([[C-055 Lösning]]), inte en produkt: det som förvaltas och får en ram. I pm3 har det två objektägare; katalogens lösning har en ägare, lösningsägaren, den som har mandatet över den (ADR 0035). Det objektet tar fram är dess leveransprodukter ([[C-174 Leveransprodukt]]). ADR 0020.

pm3 delar ägandet längs komponentaxeln. En objektägare från verksamheten äger beteende och information, en från IT tekniken, och objektet är ett överlapp mellan dem. Då äger var och en sina komponenter, men det enda som gör dem till en lösning, att de hänger ihop, äger ingen. Överlappet är ett forum ([[C-156 Forum]]). Ett forum kan komma överens men inte besluta ensamt, och styrning förutsätter mandat ([[C-002 Styrning]]). Delat arbete inuti lösningen är inget problem; delat mandat över den gör den ostyrbar. Därför står en lösningsägare över processägaren, informationsägaren och systemägaren (ADR 0035).

Ett objekt som realiserar flera förmågor prövas mot förmågekartan (ADR 0020). Det som har ett eget uppdrag över flera lösningar är ingen grov lösning utan en verksamhetsdomän ([[C-008 Verksamhetsdomän]]). Den som då saknas i pm3 är domänägaren, som sätter målen på domänens förmågor och ställer kraven på objekten under.

Objektforumet är två olika saker, och snittet avgör vilken. Äger var sida en hel lösning är det ett kravforum: krav ([[C-021 Krav]]) åt ena hållet, leverans åt andra, och det de enas om är en överenskommelse ([[C-084 Överenskommelse]]). Möts två halvägare till samma lösning är det en kommitté som ersätter ett mandat som saknas. Vad ett reellt ansvar förutsätter står i Ansvar ([[C-209 Ansvar]]). ADR 0036.
