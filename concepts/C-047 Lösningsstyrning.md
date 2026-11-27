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

Lösningsstyrningen styr en lösning ([[C-055 Lösning]]): det som förvaltas och får en ram ([[C-210 Ram]]). Lösningen har en ägare, lösningsägaren. Lösningsägaren beslutar om lösningen, håller ramen och svarar för lösningen. [[0020-forvaltningsobjektet-ar-en-losning-som-realiserar-en-formaga-verksamhetsprodukt-och-leveransprodukt-under-produkt|Beslut 20]] och [[0035-processagaren-ar-en-roll-linjechefen-ett-begrepp-agandet-skrivs-med-ansvarar-for-typerna-ags-och-forekomsterna-svarar-linjen-for-och-styrobjekten-ags-genom-mandat|35]].

Produktstyrning och objektstyrning är avrådda ord för lösningsstyrningen. De är samma styrning med samma ägare. Ordet objektstyrning ser lösningen från det som förvaltas, och ordet produktstyrning ser den från det som erbjuds. Katalogen döper styrningen efter styrobjektet, och styrobjektet är lösningen. [[0046-portfoljen-och-initiativet-har-var-sin-agare-produkten-har-ingen-ramen-ar-bara-resurserna-och-initiativets-agare-beslutar-om-arbetet|Beslut 46]] och [[0063-losningsstyrning-ersatter-produktstyrning-och-objektstyrning-och-portfoljen-vager-ramen-och-aggregerar-initiativet|63]].

Produkten ([[C-014 Produkt]]) är inget styrobjekt och har ingen egen ägare. Lösningsägaren beslutar om produkten och svarar för den. En produktägare vid sidan av lösningsägaren skulle svara för ett löfte utan att få besluta om det som uppfyller löftet. Det är samma fel som pm3:s två objektägare ger, se Motsvarigheter. Det lösningen tar fram är dess leveransprodukter ([[C-174 Leveransprodukt]]). [[0020-forvaltningsobjektet-ar-en-losning-som-realiserar-en-formaga-verksamhetsprodukt-och-leveransprodukt-under-produkt|Beslut 20]] och [[0046-portfoljen-och-initiativet-har-var-sin-agare-produkten-har-ingen-ramen-ar-bara-resurserna-och-initiativets-agare-beslutar-om-arbetet|46]].

Lösningsstyrning är inte produktionsstyrning ([[C-215 Produktionsstyrning]]). Produktionsstyrningen styr en verksamhetsdomän och ser den från dess produktion. Drift och support är produktion och ligger utanför lösningens ram. [[0047-en-sorts-verksamhetsdoman-med-utformning-och-produktion-losningen-innehaller-utformningen-allt-utforande-ar-produktion-och-leveransprodukten-ar-det-mottagaren-producerar-med|Beslut 47]] och [[0048-produktionsstyrning-ar-utvecklingsstyrningens-tvilling-malet-hor-till-domanen-och-en-losnings-hemdoman-ska-rymma-produktionen-som-utfor-dess-beteende|48]].

En lösning som realiserar flera förmågor prövas mot förmågekartan ([[0020-forvaltningsobjektet-ar-en-losning-som-realiserar-en-formaga-verksamhetsprodukt-och-leveransprodukt-under-produkt|beslut 20]]). Det som har ett eget uppdrag över flera lösningar är ingen grov lösning utan en verksamhetsdomän ([[C-008 Verksamhetsdomän]]).

Objektforumet är två olika saker, och snittet avgör vilken. Äger var sida en hel lösning är objektforumet ett kravforum. Krav ([[C-021 Krav]]) går åt ena hållet och leverans åt andra, och det sidorna enas om är en överenskommelse ([[C-084 Överenskommelse]]). Möts två halvägare till samma lösning är objektforumet en kommitté som ersätter ett mandat som saknas. Vad ett reellt ansvar förutsätter står i Ansvar ([[C-209 Ansvar]]). [[0036-losningen-skars-dar-kopplingen-ar-los-ansvar-ram-och-koppling-ar-begrepp-utan-elementtyp-ramen-foljer-mandatet-och-den-som-svarar-for-en-sak-beslutar-om-den|Beslut 36]].

## Motsvarigheter

Förvaltningsobjektet i en förvaltningsmodell byggd på pm3 är en lösning, inte en produkt. Det pm3 kallar förvaltning är vidmakthållande och vidareutveckling inom lösningens ram. Orden förklaras i Initiativ ([[C-012 Initiativ]]). [[0020-forvaltningsobjektet-ar-en-losning-som-realiserar-en-formaga-verksamhetsprodukt-och-leveransprodukt-under-produkt|Beslut 20]] och [[0046-portfoljen-och-initiativet-har-var-sin-agare-produkten-har-ingen-ramen-ar-bara-resurserna-och-initiativets-agare-beslutar-om-arbetet|46]].

I pm3 har förvaltningsobjektet två objektägare. Katalogens lösning har en ägare, lösningsägaren, som har mandatet över lösningen ([[0035-processagaren-ar-en-roll-linjechefen-ett-begrepp-agandet-skrivs-med-ansvarar-for-typerna-ags-och-forekomsterna-svarar-linjen-for-och-styrobjekten-ags-genom-mandat|beslut 35]]). pm3 delar ägandet längs komponentaxeln. En objektägare från verksamheten äger beteende och information, en från IT äger tekniken, och objektet är ett överlapp mellan dem. Då äger var och en sina komponenter. Men det enda som gör komponenterna till en lösning är att de hänger ihop, och det äger ingen. Överlappet är ett forum ([[C-156 Forum]]). Ett forum kan komma överens men inte besluta ([[0050-ett-beslut-fattas-av-den-som-har-bade-ram-och-mandat-ett-forum-beslutar-aldrig-aspekten-avgor-inga-enskilda-fall-och-domanens-agare-satter-losningens-ram|beslut 50]]), och styrning förutsätter mandat ([[C-002 Styrning]]). Delat arbete inuti lösningen är inget problem. Delat mandat över lösningen gör den ostyrbar. Därför står en lösningsägare över processägaren, informationsägaren och systemägaren ([[0035-processagaren-ar-en-roll-linjechefen-ett-begrepp-agandet-skrivs-med-ansvarar-for-typerna-ags-och-forekomsterna-svarar-linjen-for-och-styrobjekten-ags-genom-mandat|beslut 35]]).

pm3 saknar domänägaren. Domänägaren sätter målen på domänens förmågor och ställer kraven på lösningarna i domänen.

## Exempel

IT lämnar registersystemet med drift och support till registerlösningen. Det är IT:s leveransprodukt. Ägaren till IT:s lösning beslutar att supporten stänger tidigare på fredagar. Beslutet gäller vad produkten lovar, och det är den lösningens ägare som fattar det. Registerlösningens ägare ställer krav på supporten men beslutar inte om den. Supporten själv är produktion hos IT, och IT-chefen svarar som linjechef för varje supportärende. [[0050-ett-beslut-fattas-av-den-som-har-bade-ram-och-mandat-ett-forum-beslutar-aldrig-aspekten-avgor-inga-enskilda-fall-och-domanens-agare-satter-losningens-ram|Beslut 50]].
