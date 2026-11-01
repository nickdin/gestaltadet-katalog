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

Typ i informationsperspektivet, ArchiMates Data Object. Ett informationsobjekt är informationssidan av det verksamheten hanterar: ett verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]) realiseras av ett eller flera informationsobjekt. Begreppet som definierar det hör till katalogen, inte till arkitekturen: katalogen är organisationens ordlista, och begreppet ärende tas in där när arkitekturen namnger objektet Ärende (ADR 0023). Beslutet: ADR 0016.

Informationsklassningen i konfidentialitet sätts på informationsobjektet, inte på uppgiften eller lagringsytan; se [[C-166 Informationstillgång]].

Entitetstyp är informationsmodelleringens ord för samma sak: mallen, inte förekomsten. Person är en entitetstyp och ett informationsobjekt; en enskild företrädare i föreningsregistret är en entitet, ingen av delarna. Termen är tillåten så att katalogen svarar rätt när ordet används.

Ett informationsobjekt består av uppgifter ([[C-161 Uppgift]]), attributen, som ritas inuti rutan och inte som egna element; varje uppgift som ritas har sitt begrepp i katalogen, som objektet självt (ADR 0024). En uppgift blir ett eget informationsobjekt först när verksamheten hanterar den som en enhet för sig, klassar, äger eller reglerar den: personnumret är ett informationsobjekt, förfallodatumet är en uppgift i Faktura. Objektet som rymmer ett sådant fält aggregerar det ([[C-100 aggregerar]]), eftersom samma fält ingår i många objekt. Multipliciteten mellan två informationsobjekt, "ett ärende har exakt en sökande", står på relationen mellan dem, i dess beskrivning tills interlingua har fältet, och ritningarna visar den (ADR 0023). En sammanställning ([[C-162 Sammanställning]]) registreras som informationsobjekt och aggregerar det den är gjord av.

SDMN (Shared Data Model and Notation), den datamodell BPMN, CMMN och DMN delar, kallar samma sak DataItem och dess struktur ItemDefinition; båda är informationsobjektet, strukturen dess uppgifter. Lagret är den delade datamodellen: SDMN är ett utbytesformat mellan verktygen, inget verktyg för informationsmodellering, och ett sådant verktyg får sina dataelement från lagrets informationsobjekt. Informationsobjektet har inget eget tillstånd; verksamhetsobjektets tillstånd ([[C-182 Tillstånd]]) bärs av en uppgift, statusfältet. Beslutet: ADR 0024.

## Exempel

en ansökan, ett ärende, en person i ett register.
