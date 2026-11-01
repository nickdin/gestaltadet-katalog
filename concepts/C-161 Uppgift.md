---
id: C-161
term: Uppgift
terms:
  - term: Uppgift
    language: sv
    status: preferred
    source: concept new
  - term: attribut
    language: sv
    source: concept change
    status: admitted
definition: information om en enskild egenskap hos en företeelse, den minsta enhet ett informationsobjekt består av
partitive: '[[C-060 Informationsobjekt]]'
---
# C-161 Uppgift

## Anmärkning

Ett begrepp, ingen elementtyp: en uppgift registreras inte som eget element och ritas inte som egen ruta, utan står i informationsobjektets ([[C-060 Informationsobjekt]]) lista över uppgifter och ritas inuti dess ruta, som attributen i en entitetstyp. Attribut är informationsmodelleringens ord för samma sak och är tillåten term; uppgift är förvaltningens och lagens ord, det personuppgiften, sekretessen och uppgiftsskyldigheten gäller, och därför det föredragna. Varje uppgift som ritas har sitt begrepp i katalogen, som informationsobjektet självt (ADR 0023): raden i listan pekar på begreppet, kötid i Bostadssökande på begreppet Kötid, och det som återanvänds mellan två informationsobjekt är begreppet, definitionen, inget element. Interlingua har ännu inget fält för listan (interlingua #906); tills det finns står uppgifterna som en lista under en rubrik i informationsobjektets beskrivning.

Ett informationsobjekt består av uppgifter, och samma uppgift kan ingå i flera sammanställningar ([[C-162 Sammanställning]]). En uppgift som verksamheten hanterar som en enhet för sig, som personnumret, är ett eget informationsobjekt. En personuppgift är en uppgift som direkt eller indirekt kan knytas till en levande person; det avgörs av uppgiften, inte av var den står. Hur en förekomst av ett informationsobjekt identifieras, ärendenumret, SBVR:s reference scheme, är den identifierande uppgiften (ADR 0023). Statusuppgiften bär verksamhetsobjektets tillstånd ([[C-182 Tillstånd]]): dess tillåtna värden är tillstånden. SDMN:s itemComponents, fälten i en ItemDefinition, är uppgifter. Beslutet: ADR 0018; attributet och listan ADR 0024.

## Exempel

en förenings organisationsnummer, ett hyresbelopp, datumet en ansökan kom in.
