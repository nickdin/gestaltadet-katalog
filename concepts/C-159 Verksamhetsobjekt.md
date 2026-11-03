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
---
# C-159 Verksamhetsobjekt

**Definition:** det en verksamhetsprocess, en handläggning eller en verksamhetsfunktion hanterar och lämnar vidare

## Anmärkning

Motsvarar ArchiMates Business Object: flödesobjektet i ett verksamhetsbeteende ([[C-157 Verksamhetsbeteende]]), oavsett om det blir en produkt. Ett verksamhetsobjekt realiseras av ett eller flera informationsobjekt ([[C-060 Informationsobjekt]]), som är informationsperspektivets sida av samma sak. En produkt ([[C-014 Produkt]]) aggregerar de verksamhetsobjekt mottagaren får. Ett beteende når ett verksamhetsobjekt med relationen har åtkomst till ([[C-101 har åtkomst till]]); att det lämnas vidare till nästa beteende lagras inte som flödar till ([[C-097 flödar till]]), utan pilen härleds ur att det ena skriver och det andra läser (ADR 0014, ADR 0033). Ärendebeslutet ([[C-181 Ärendebeslut]]) är det verksamhetsobjekt en handläggning fattar och lämnar vidare. Ett verksamhetsobjekt består av ([[C-062 består av]]) sina tillstånd ([[C-182 Tillstånd]]), de lägen beteendet för det igenom, ritade i en tillståndsvy per objekt; informationsobjektet bär tillståndet som en uppgift. En fysisk sak processen hanterar utan informationssida, SDMN:s Physical, är ett verksamhetsobjekt; bär den information, den utskrivna blanketten, är den en representation ([[C-085 Representation]]). BPMN:s dataobjekt och CMMN:s ärendeakt (CaseFile, CaseFileItem) är verksamhetsobjekt. Beslutet: ADR 0016; ärendebeslutet ADR 0022; tillståndet som elementtyp och SDMN ADR 0024.

Motsvarar BusinessObject i Business Architecture Core Metamodel (BACM). Gränsen mot informationsobjektet dras i lagret efter roll, vad beteendet hanterar mot vad verksamheten håller som information, inte som i BACM efter påtaglighet, så ett ärende är ett verksamhetsobjekt här och en InformationItem där. En vara ([[C-191 Vara]]) är ett verksamhetsobjekt som lämnas över till mottagaren. ADR 0027.

Motsvarar BusinessItem i Value Delivery Modeling Language (VDML), allt som kan skapas eller skaffas och bär information, förpliktelse eller värde; det som används upp eller lånas i en aktivitet är en resurs ([[C-122 Resurs]]). ADR 0028.

I Unified Modeling Language (UML) är verksamhetsobjektet aktivitetsdiagrammets objekt (ObjectNode, Pin), det som flödar mellan två element (InformationItem) och den klass vars tillståndsmaskin ritas; klassen i klassdiagrammet är informationsobjektet som realiserar det. ADR 0029.

## Exempel

ett ärende, ett ärendebeslut, ett initiativ, en utgiftsprognos, verksamhetsplanen, en analysrapport.

