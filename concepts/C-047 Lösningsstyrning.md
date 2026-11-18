---
id: C-047
term: Lösningsstyrning
terms:
  - term: Produktstyrning
    language: sv
    source: catalogue
    status: deprecated
  - term: Objektstyrning
    language: sv
    source: catalogue
    status: deprecated
  - term: Lösningsstyrning
    language: sv
    source: concept change
    status: preferred
definition: objektbaserad styrning där styrobjektet är en lösning
generic: '[[C-005 Objektbaserad styrning]]'
associative:
  - concept: '[[C-055 Lösning]]'
    label: avgränsas av
  - concept: '[[C-014 Produkt]]'
    label: ses från
---
# C-047 Lösningsstyrning

**Definition:** objektbaserad styrning där styrobjektet är en lösning

## Anmärkning

Lösningsstyrningen styr en lösning ([[C-055 Lösning]]): det som förvaltas och får en ram ([[C-210 Ram]]). Lösningen har en ägare, lösningsägaren. Lösningsägaren beslutar om lösningen, håller ramen och svarar för lösningen. Beslut 20 och 35.

Produktstyrning och objektstyrning är avrådda ord för lösningsstyrningen. De är samma styrning med samma ägare. Ordet objektstyrning ser lösningen från det som förvaltas, och ordet produktstyrning ser den från det som erbjuds. Katalogen döper styrningen efter styrobjektet, och styrobjektet är lösningen. Beslut 46 och 63.

Produkten ([[C-014 Produkt]]) är inget styrobjekt och har ingen egen ägare. Lösningsägaren beslutar om produkten och svarar för den. En produktägare vid sidan av lösningsägaren skulle svara för ett löfte utan att få besluta om det som uppfyller löftet. Det är samma fel som pm3:s två objektägare ger, se Motsvarigheter. Det lösningen tar fram är dess leveransprodukter ([[C-174 Leveransprodukt]]). Beslut 20 och 46.

Lösningsstyrning är inte produktionsstyrning ([[C-215 Produktionsstyrning]]). Produktionsstyrningen styr en verksamhetsdomän och ser den från dess produktion. Drift och support är produktion och ligger utanför lösningens ram. Beslut 47 och 48.

En lösning som realiserar flera förmågor prövas mot förmågekartan (beslut 20). Det som har ett eget uppdrag över flera lösningar är ingen grov lösning utan en verksamhetsdomän ([[C-008 Verksamhetsdomän]]).

Objektforumet är två olika saker, och snittet avgör vilken. Äger var sida en hel lösning är objektforumet ett kravforum. Krav ([[C-021 Krav]]) går åt ena hållet och leverans åt andra, och det sidorna enas om är en överenskommelse ([[C-084 Överenskommelse]]). Möts två halvägare till samma lösning är objektforumet en kommitté som ersätter ett mandat som saknas. Vad ett reellt ansvar förutsätter står i Ansvar ([[C-209 Ansvar]]). Beslut 36.

## Motsvarigheter

Förvaltningsobjektet i en förvaltningsmodell byggd på pm3 är en lösning, inte en produkt. Det pm3 kallar förvaltning är vidmakthållande och vidareutveckling inom lösningens ram. Orden förklaras i Initiativ ([[C-012 Initiativ]]). Beslut 20 och 46.

I pm3 har förvaltningsobjektet två objektägare. Katalogens lösning har en ägare, lösningsägaren, som har mandatet över lösningen (beslut 35). pm3 delar ägandet längs komponentaxeln. En objektägare från verksamheten äger beteende och information, en från IT äger tekniken, och objektet är ett överlapp mellan dem. Då äger var och en sina komponenter. Men det enda som gör komponenterna till en lösning är att de hänger ihop, och det äger ingen. Överlappet är ett forum ([[C-156 Forum]]). Ett forum kan komma överens men inte besluta (beslut 50), och styrning förutsätter mandat ([[C-002 Styrning]]). Delat arbete inuti lösningen är inget problem. Delat mandat över lösningen gör den ostyrbar. Därför står en lösningsägare över processägaren, informationsägaren och systemägaren (beslut 35).

pm3 saknar domänägaren. Domänägaren sätter målen på domänens förmågor och ställer kraven på lösningarna i domänen.

## Exempel

IT lämnar registersystemet med drift och support till registerlösningen. Det är IT:s leveransprodukt. Ägaren till IT:s lösning beslutar att supporten stänger tidigare på fredagar. Beslutet gäller vad produkten lovar, och det är den lösningens ägare som fattar det. Registerlösningens ägare ställer krav på supporten men beslutar inte om den. Supporten själv är produktion hos IT, och IT-chefen svarar som linjechef för varje supportärende. Beslut 50.
