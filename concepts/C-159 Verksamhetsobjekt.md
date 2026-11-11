---
id: C-159
term: Verksamhetsobjekt
terms:
  - term: Verksamhetsobjekt
    language: sv
    status: preferred
    source: concept new
definition: det en verksamhetsprocess, en handläggning eller en verksamhetsfunktion hanterar och lämnar vidare
kind: element-type
associative:
  - concept: '[[C-060 Informationsobjekt]]'
    label: realiseras av
---
# C-159 Verksamhetsobjekt

**Definition:** det en verksamhetsprocess, en handläggning eller en verksamhetsfunktion hanterar och lämnar vidare

## Anmärkning

Verksamhetsobjektet är flödesobjektet i ett verksamhetsbeteende ([[C-157 Verksamhetsbeteende]]), oavsett om det blir en produkt. Ett verksamhetsobjekt realiseras av ett eller flera informationsobjekt ([[C-060 Informationsobjekt]]), som är informationsperspektivets sida av samma sak. En produkt ([[C-014 Produkt]]) aggregerar de verksamhetsobjekt mottagaren får. Ärendebeslutet ([[C-181 Ärendebeslut]]) är det verksamhetsobjekt en handläggning fattar och lämnar vidare.

Ett beteende når ett verksamhetsobjekt med relationen har åtkomst till ([[C-101 har åtkomst till]]). Att objektet lämnas vidare till nästa beteende lagras inte som flödar till ([[C-097 flödar till]]). Pilen härleds ur att det ena beteendet skriver och det andra läser (beslut 14, beslut 33). Beteendet som har åtkomst till verksamhetsobjektet har därmed åtkomst till de informationsobjekt som realiserar det, ett steg, härlett och inte ritat. Pröva ansökan har åtkomst till Ärende och når så Ansökan och Förening. Åtkomst direkt till ett informationsobjekt ritas bara där den inte följer av verksamhetsobjektet, och den följer inte aggregerar ([[C-100 aggregerar]]) (beslut 34).

Ett verksamhetsobjekt består av ([[C-062 består av]]) sina tillstånd ([[C-182 Tillstånd]]), de lägen beteendet för det igenom. Tillstånden ritas i en tillståndsvy per objekt, och informationsobjektet bär tillståndet som en uppgift. En fysisk sak processen hanterar utan informationssida är ett verksamhetsobjekt; bär den information, den utskrivna blanketten, är den en representation ([[C-085 Representation]]).

## Motsvarigheter

Motsvarar ArchiMates Business Object. Beslut 16; ärendebeslutet beslut 22; tillståndet som elementtyp och SDMN beslut 24.

Motsvarar BusinessObject i Business Architecture Core Metamodel (BACM). Lagret drar gränsen mot informationsobjektet efter roll: vad beteendet hanterar mot vad verksamheten håller som information. BACM drar den efter påtaglighet, så ett ärende är ett verksamhetsobjekt här och en InformationItem där. En vara ([[C-191 Vara]]) är ett verksamhetsobjekt som lämnas över till mottagaren. Beslut 27.

BPMN:s dataobjekt och CMMN:s ärendeakt (CaseFile, CaseFileItem) är verksamhetsobjekt. Beslut 16; ärendebeslutet beslut 22; tillståndet som elementtyp och SDMN beslut 24.

SDMN:s Physical är en fysisk sak processen hanterar utan informationssida. Beslut 24.

I Unified Modeling Language (UML) är verksamhetsobjektet aktivitetsdiagrammets objekt (ObjectNode, Pin), det som flödar mellan två element (InformationItem) och den klass vars tillståndsmaskin ritas. Klassen i klassdiagrammet är informationsobjektet som realiserar det. Beslut 29.

Motsvarar BusinessItem i Value Delivery Modeling Language (VDML): allt som kan skapas eller skaffas och bär information, förpliktelse eller värde. Det som används upp eller lånas i en aktivitet är en resurs ([[C-122 Resurs]]). Beslut 28.

## Exempel

ett ärende, ett ärendebeslut, ett initiativ, en utgiftsprognos, verksamhetsplanen, en analysrapport.
