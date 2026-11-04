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

**Definition:** information om en enskild egenskap hos en företeelse, den minsta enhet ett informationsobjekt består av

## Anmärkning

En uppgift är ett begrepp, ingen elementtyp. Den registreras inte som eget element och ritas inte som egen ruta. Den står i informationsobjektets ([[C-060 Informationsobjekt]]) lista över uppgifter och ritas inuti dess ruta, som attributen i en entitetstyp. Varje uppgift som ritas har sitt begrepp i katalogen, som informationsobjektet självt (ADR 0023). Raden i listan pekar på begreppet, kötid i Bostadssökande på begreppet Kötid, och det som återanvänds mellan två informationsobjekt är begreppet, definitionen, inget element. Interlingua har ännu inget fält för listan (interlingua #906); tills det finns står uppgifterna som en lista under en rubrik i informationsobjektets beskrivning.

Ett informationsobjekt består av uppgifter, och samma uppgift kan ingå i flera sammanställningar ([[C-162 Sammanställning]]). En uppgift som verksamheten hanterar som en enhet för sig, som personnumret, är ett eget informationsobjekt. Den identifierande uppgiften är hur en förekomst av ett informationsobjekt identifieras, ärendenumret, SBVR:s reference scheme (ADR 0023). Statusuppgiften bär verksamhetsobjektets tillstånd ([[C-182 Tillstånd]]): dess tillåtna värden är tillstånden. SDMN:s itemComponents, fälten i en ItemDefinition, är uppgifter. Beslutet: ADR 0018; attributet och listan ADR 0024.

Uppgift är förvaltningens och lagens ord, det personuppgiften, sekretessen och uppgiftsskyldigheten gäller, och därför det föredragna. Attribut är informationsmodelleringens ord för samma sak och är tillåten term. En personuppgift är en uppgift som direkt eller indirekt kan knytas till en levande person; det avgörs av uppgiften, inte av var den står.

Sekretessen är det tydligaste fallet av reglering för sig. Offentlighets- och sekretesslagen fäster sekretessen på uppgiften, ofta i ett sammanhang, "i ärende om bidrag, för uppgift om enskilds personliga förhållanden". En uppgift som omfattas av sekretess är därför ett eget informationsobjekt, med paragrafen i sin beskrivning. Sammanhanget läses ur det verksamhetsbeteende som har åtkomst till objektet. Sekretessen följer uppgiften vart den tar vägen och gäller inte handlingen; sekretessmarkeringen på handlingen är representationens ([[C-085 Representation]]) märkning (ADR 0031).

Motsvarar Property i Unified Modeling Language (UML), attributet i klassen. De värden uppgiften får anta är dess värdemängd ([[C-197 Värdemängd]]), och en DataType är uppgiftens format, text. ADR 0029.

## Exempel

en förenings organisationsnummer, ett hyresbelopp, datumet en ansökan kom in.
