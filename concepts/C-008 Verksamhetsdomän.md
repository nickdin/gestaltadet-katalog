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

Verksamhetsdomänen är både styrobjekt och arkitekturobjekt, samma sak sedd från styrningens respektive arkitekturens håll. Som styrobjekt är den det som styrningen av en domän avser. Den styrningen heter utvecklingsstyrning ([[C-043 Utvecklingsstyrning]]) sedd från utformningen och produktionsstyrning ([[C-215 Produktionsstyrning]]) sedd från produktionen. Som arkitekturobjekt står den på domännivå, under verksamheten ([[C-007 Verksamhet]]).

Varje verksamhetsdomän har en utformning och en produktion. Utformningen är domänens lösningar ([[C-055 Lösning]]): hur beteendet är ordnat, vilka roller som finns, hur informationen är uppbyggd och vilken teknik som används. Produktionen är de enskilda ärendena och de resurser ([[C-122 Resurs]]) som utför dem. Utveckling är att ändra utformningen. En rättning av lösningen är utveckling. Att rätta en enskild uppgift är registervård och produktion ([[0050-ett-beslut-fattas-av-den-som-har-bade-ram-och-mandat-ett-forum-beslutar-aldrig-aspekten-avgor-inga-enskilda-fall-och-domanens-agare-satter-losningens-ram|beslut 50]]). Det finns inte två sorters domän, en som utvecklar och en som producerar. Den som säger utvecklingsdomänen menar domänens utformning och ändringen av den, se utvecklingsstyrning ([[C-043 Utvecklingsstyrning]]). [[0047-en-sorts-verksamhetsdoman-med-utformning-och-produktion-losningen-innehaller-utformningen-allt-utforande-ar-produktion-och-leveransprodukten-ar-det-mottagaren-producerar-med|Beslut 47]].

En domän uppstår där någon har fått ett uppdrag delegerat ([[C-214 Delegation]]) med egen ram ([[C-210 Ram]]). Så ligger domäner i varandra. Rätten att besluta i enskilda ärenden skapar ingen domän. En domän är inte heller en organisationsenhet ([[C-121 Organisationsenhet]]). Enheten är aktören som utför produktionen, och den kan utföra beteende ur en lösning som hör hemma i en annan domän. [[0047-en-sorts-verksamhetsdoman-med-utformning-och-produktion-losningen-innehaller-utformningen-allt-utforande-ar-produktion-och-leveransprodukten-ar-det-mottagaren-producerar-med|Beslut 47]].

En lösnings hemdomän ska rymma den produktion som utför lösningens beteende. Beteendet som typ och dess förekomster är så tätt kopplade ([[C-211 Koppling]]) som två saker kan vara. Ligger de i var sin domän beslutar den ena ägaren om utformningen och den andra om bemanningen. Ingen av dem kan väga det ena mot det andra, och ingen kan bära ansvaret ([[C-209 Ansvar]]) för domänens mål. Avvägningen går då upp till den närmaste ägare som omsluter båda. Det är ofta högsta ledningen, men i en stor verksamhet kan det vara en chef längre ned.

Delningen visas alltid, men den väger olika tungt. Den vägs mot den närmaste ägare som håller båda halvorna. En bedömning ([[C-185 Bedömning]]) frågar efter fyra saker:

1. Hur många olika lägen kräver en avvägning? Olikheten räknas, inte mängden.
2. Hur långt är det från den som ser läget till den som väger?
3. Hur länge dröjer svaret?
4. Når det som produktionen ser den som äger utformningen?

Att leva med en delning som väger lätt är ett styrbeslut ([[C-019 Styrbeslut]]). [[0053-ordningen-i-verksamhetsstod-ar-inget-fynd-i-sig-samma-ordning-visas-i-tre-lagen-och-att-leva-med-ett-fynd-ar-ett-styrbeslut-pa-en-bedomning|Beslut 53]] och [[0070-produktionen-ska-ligga-i-losningens-hemdoman-men-behover-inte-spegla-formagorna-delningen-visas-alltid-och-vags-mot-den-narmaste-agare-som-haller-bada|70]].

Att hålla isär utformningen och produktionen har två fördelar. En utformning för flera enheter ger lika behandling. Ramen för ändring är också skyddad mot dagens tryck, för den som saknar folk i dag håller den inte. Fördelarna kommer av att rollerna är skilda. De kräver inte att ägaren ovanför är långt borta. Tre möter komplexiteten ([[C-219 Komplexitet]]). Den som utför arbetet möter läget. Linjechefen ([[C-207 Linjechef]]) möter belastningen. Lösningsägaren möter morgondagens lägen genom att ändra utformningen. De tre behöver inte vara samma person. Kravet gäller vägningen mellan dem: den ska landa hos en ägare som kan möta den. [[0070-produktionen-ska-ligga-i-losningens-hemdoman-men-behover-inte-spegla-formagorna-delningen-visas-alltid-och-vags-mot-den-narmaste-agare-som-haller-bada|Beslut 70]].

Fyra vägar finns ur en delning som väger tungt. Halvorna flyttas så att en domän rymmer båda. Lösningen skärs om så att beteendet följer produktionen. En ägare sätts över båda. Eller så fastställer den som omsluter båda en regel ([[C-020 Regel]]) som ger den som har produktionen rätt att besluta. Då stannar de flesta avvägningarna där de uppstår, fast delningen står kvar. Varje väg har ett pris, och exemplet Brinkstadsbostäder visar de fyra. [[0048-produktionsstyrning-ar-utvecklingsstyrningens-tvilling-malet-hor-till-domanen-och-en-losnings-hemdoman-ska-rymma-produktionen-som-utfor-dess-beteende|Beslut 48]] och [[0070-produktionen-ska-ligga-i-losningens-hemdoman-men-behover-inte-spegla-formagorna-delningen-visas-alltid-och-vags-mot-den-narmaste-agare-som-haller-bada|70]].

Det som får komma från en annan domän är en färdig leveransprodukt ([[C-174 Leveransprodukt]]): tekniken från IT, medarbetaren från HR. Leverantören har då sitt eget beteende och sina egna förekomster hemma hos sig. En domän inuti en annan kan ha egen bemanning utan egen lösning. Då rymmer den omslutande domänen båda, och dess ägare kan väga utformningen mot bemanningen. [[0048-produktionsstyrning-ar-utvecklingsstyrningens-tvilling-malet-hor-till-domanen-och-en-losnings-hemdoman-ska-rymma-produktionen-som-utfor-dess-beteende|Beslut 48]].

Inom domänens ram finns två slags ram: lösningarnas, för att ändra utformningen, och produktionens. Domänens ägare kan väga dem mot varandra, och sätter varje lösnings ram ur domänens ram för ändring. Det som inte ryms går upp till ägaren av det som omsluter domänen. Varje domän har en portfölj ([[C-011 Portfölj]]), och portföljen väger det som ändrar utformningen. Den finns också när ingen kallar den portfölj. [[0047-en-sorts-verksamhetsdoman-med-utformning-och-produktion-losningen-innehaller-utformningen-allt-utforande-ar-produktion-och-leveransprodukten-ar-det-mottagaren-producerar-med|Beslut 47]], [[0050-ett-beslut-fattas-av-den-som-har-bade-ram-och-mandat-ett-forum-beslutar-aldrig-aspekten-avgor-inga-enskilda-fall-och-domanens-agare-satter-losningens-ram|50]] och [[0051-verksamheten-och-varje-verksamhetsdoman-har-en-portfolj-portfoljerna-ligger-i-varandra-som-domanerna-och-portfoljen-vager-ramar-for-andring-och-initiativ|51]].

Domänens ägare svarar för domänens mål, också målen för produktionen. Linjechefen ([[C-207 Linjechef]]) svarar för varje ärende och för bemanningen. Oftast är det samma chef. Ligger utformningen och produktionen i var sin domän svarar ingen av de två ägarna för målet. Det gör den närmaste ägare som omsluter båda, på vilken nivå hen än sitter. [[0050-ett-beslut-fattas-av-den-som-har-bade-ram-och-mandat-ett-forum-beslutar-aldrig-aspekten-avgor-inga-enskilda-fall-och-domanens-agare-satter-losningens-ram|Beslut 50]] och [[0070-produktionen-ska-ligga-i-losningens-hemdoman-men-behover-inte-spegla-formagorna-delningen-visas-alltid-och-vags-mot-den-narmaste-agare-som-haller-bada|70]].

En domän med en del av organisationens uppdrag ([[C-149 Uppdrag]]) är kärnverksamhet. En domän med ett inre uppdrag från ledningen är stödverksamhet: den lämnar det de andra behöver för att producera ([[C-174 Leveransprodukt]]). IT är stödverksamhet på samma sätt som HR. [[0047-en-sorts-verksamhetsdoman-med-utformning-och-produktion-losningen-innehaller-utformningen-allt-utforande-ar-produktion-och-leveransprodukten-ar-det-mottagaren-producerar-med|Beslut 47]].

Livskraften ([[C-216 Livskraft]]) prövas på varje domän, också en domän inuti en annan. Provet står i Livskraft. Domäner bredvid varandra samordnar sig ([[C-217 Samordning]]) genom en överenskommelse eller en gemensam regel. [[0049-livskraft-ar-mattstocken-for-styrningen-samordning-granskning-komplexitet-och-centralisering-ar-nya-begrepp-kopplingen-rader-ocksa-mellan-ansvar-och-lagarna-far-en-egen-sida|Beslut 49]].

## Exempel

Bidragsgivningen hos Myndigheten för föreningsstöd, som chefen för Bidragsenheten äger. Utformningen är lösningen Ansökningshandläggningen. Produktionen är årets 4 000 ansökningar och handläggarna som prövar dem. HR är en annan domän: utformningen är lösningen för rekrytering, och produktionen är varje rekrytering.
