---
id: C-060
term: Informationsobjekt
terms:
  - term: Informationsobjekt
    language: sv
    source: catalogue
  - term: entitetstyp
    language: sv
    source: concept change
    status: admitted
definition: "avgränsad mängd information som verksamheten hanterar som en enhet"
kind: element-type
generic: "[[C-122 Resurs]]"
---
# C-060 Informationsobjekt

**Definition:** avgränsad mängd information som verksamheten hanterar som en enhet

## Anmärkning

Ett informationsobjekt är informationssidan av det verksamheten hanterar: ett verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]) realiseras av ett eller flera informationsobjekt. Det är en typ i informationsperspektivet, ArchiMates Data Object. Begreppet som definierar objektet hör till katalogen, inte till arkitekturen: katalogen är organisationens ordlista, och begreppet ärende tas in där när arkitekturen namnger objektet Ärende (ADR 0023). Beslutet: ADR 0016.

Ett informationsobjekt består av uppgifter ([[C-161 Uppgift]]), attributen. Uppgifterna ritas inuti rutan, inte som egna element, och varje uppgift som ritas har sitt begrepp i katalogen, som objektet självt (ADR 0024). Informationsobjektet har inget eget tillstånd: en uppgift, statusfältet, bär verksamhetsobjektets tillstånd ([[C-182 Tillstånd]]) (ADR 0024). Multipliciteten mellan två informationsobjekt, "ett ärende har exakt en sökande", står på relationen mellan dem, i dess beskrivning tills interlingua har fältet, och ritningarna visar den (ADR 0023).

Nivån i informationsmodellen väljs efter vad verksamheten behöver tala om och vad dess beteenden hanterar. Den får vara grov och förfinas över tid: nya objekt läggs under det grova, som då är ett informationsområde ([[C-198 Informationsområde]]). Klassning, ägande och reglering är skäl bland flera, men ett golv: det som klassas, ägs eller regleras för sig är alltid ett eget objekt. Personnumret är ett informationsobjekt, förfallodatumet en uppgift i Faktura (ADR 0030). Objektet som rymmer ett sådant fält aggregerar det ([[C-100 aggregerar]]), eftersom samma fält ingår i många objekt. Informationsklassningen i konfidentialitet sätts på informationsobjektet, inte på uppgiften eller lagringsytan; se [[C-166 Informationstillgång]].

En sammanställning ([[C-162 Sammanställning]]) registreras som informationsobjekt och aggregerar det den är gjord av. Ett informationsområde ([[C-198 Informationsområde]]) registreras som informationsobjekt och består av ([[C-062 består av]]) de objekt det samlar. Varje informationsobjekt hör hemma i exakt ett område (ADR 0030).

Ett informationsobjekt kan ha en datakategori ([[C-201 Datakategori]]): resursdata ([[C-202 Resursdata]]), referensdata ([[C-203 Referensdata]]), transaktionsdata ([[C-204 Transaktionsdata]]) eller händelsedata ([[C-205 Händelsedata]]). Kategorin är frivillig och högst en, så att en informationsmodell kan färgas efter den och informationsägaren lista sina resursdata. Kategorin sitter på informationsobjektet, inte på verksamhetsobjektet det realiserar; ett informationsområde och en sammanställning har ingen. Tills interlingua bär kategorin som ett fält på elementet står den som en mening i beskrivningen. ADR 0032.

Entitetstyp är informationsmodelleringens ord för samma sak: mallen, inte förekomsten. Person är en entitetstyp och ett informationsobjekt; en enskild företrädare i föreningsregistret är en entitet, ingen av delarna. Termen är tillåten så att katalogen svarar rätt när ordet används.

SDMN (Shared Data Model and Notation), den datamodell BPMN, CMMN och DMN delar, kallar samma sak DataItem och dess struktur ItemDefinition; båda är informationsobjektet, strukturen dess uppgifter. Lagret är den delade datamodellen: SDMN är ett utbytesformat mellan verktygen, inget verktyg för informationsmodellering, och ett sådant verktyg får sina dataelement från lagrets informationsobjekt. Beslutet: ADR 0024.

Motsvarar Class i Unified Modeling Language (UML): klassdiagrammet är informationsmodellen, attributen (Property) uppgifter och en Enumeration en värdemängd ([[C-197 Värdemängd]]). Klassen i klassdiagrammet är alltid informationsobjektet. Den klass vars tillståndsmaskin ritas är det verksamhetsobjekt informationsobjektet realiserar, och aktivitetsdiagrammets objekt är verksamhetsobjektet. ADR 0029.

## Exempel

en ansökan, ett ärende, en person i ett register.
