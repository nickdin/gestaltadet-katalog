---
id: C-182
term: Tillstånd
terms:
  - term: Tillstånd
    language: sv
    status: preferred
    source: concept new
definition: läge ett verksamhetsobjekt befinner sig i under sin livstid
kind: element-type
associative:
  - concept: '[[C-159 Verksamhetsobjekt]]'
    label: gäller ett
  - concept: '[[C-135 Verksamhetshändelse]]'
    label: nås genom en
---
# C-182 Tillstånd

**Definition:** läge ett verksamhetsobjekt befinner sig i under sin livstid

## Anmärkning

Ett tillstånd är det läge ett verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]) är i, som utrett, beslutat eller avslutat för ett ärende. Det är en typ i verksamhetsperspektivet. Tillståndet är verksamhetsobjektets: objektet består av ([[C-062 består av]]) sina tillstånd, de är dess inre och ingen annans. Informationsobjektet ([[C-060 Informationsobjekt]]) har inget eget tillstånd utan bär det som en uppgift ([[C-161 Uppgift]]), statusfältet, vars tillåtna värden är verksamhetsobjektets tillstånd. Representationen ([[C-085 Representation]]) har inte heller något tillstånd: att ärendet är arkiverat är verksamhetsobjektets läge, och arkiverad och gallrad hos handlingen är aktiviteter i arkivvården, inte lägen ([[C-200 Gallring]], beslut 31).

Tillståndsmodellen ritas i lagret som en tillståndsvy per verksamhetsobjekt. Ett tillstånd utlöser ([[C-098 utlöser]]) nästa, med det som får övergången att ske i relationens beskrivning. Den verksamhetshändelse ([[C-135 Verksamhetshändelse]]) som markerar att ett läge nåtts, CMMN:s milstolpe, utlöser tillståndet. Det är första gången ett elements inre ritas i lagret rad för rad: beslutstabellen lämnades i modelleringsverktyget (beslut 22), men lägena är saker andra element pekar på, händelserna heter efter dem och statusuppgiftens värden är de.

"Ansökan är komplett" är ett tillstånd som en beslutslogik ([[C-178 Beslutslogik]]) sätter: logiken avgör när, tillståndet att det är så. Beslut 24; begreppet beslut 22.

## Motsvarigheter

Tillståndet är utan motsvarighet i ArchiMate.

Outcome i Business Architecture Core Metamodel (BACM), det läge hos ett objekt som en förmåga producerar eller behöver, är ett tillstånd. Att hålla lägena utanför objektet, så att förmågorna kan peka på dem, är BACM:s skäl och tillståndsvyns. Förmågans produces och needs ritas inte som pilar från förmågan: övergångarna står i tillståndsvyn, drivna av det beteende som realiserar förmågan. Beslut 27.

BPMN:s dataState och CMMN:s livscykel för aktens delar ligger på beteendesidan, och det är därför tillståndet är verksamhetsobjektets. Beslut 24; begreppet beslut 22.

SBVR:s characteristic med ett led, "ärendet är avslutat", är ett tillstånd när ett verksamhetsbeteende driver övergången. En egenskap som inget beteende ändrar, "beslutet är gynnande", är en uppgift. En som ger egna regler eller eget beteende, "ärendet är ett omprövningsärende", är en specialisering ([[C-063 specialiserar]]). Characteristic beslut 23.

SDMN (Shared Data Model and Notation) har inget tillstånd. Beslut 24; begreppet beslut 22.

Motsvarar State i Unified Modeling Language (UML). Övergången (Transition) är utlöser, med vakten i relationens beskrivning; händelsen på övergången utlöser tillståndet; ett sammansatt tillstånd består av sina deltillstånd; och tillståndsmaskinen själv är tillståndsvyn. Statusuppgiftens värdemängd ([[C-197 Värdemängd]]) är tillstånden, så UML:s EnumerationLiteral är ett tillstånd när värdemängden är statusuppgiftens. Beslut 29.

## Exempel

utrett, beslutat, avslutat och arkiverat för ett ärende; obetald och betald för en faktura.
