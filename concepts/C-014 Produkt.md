---
id: C-014
term: Produkt
terms:
  - term: Produkt
    language: sv
    source: catalogue
  - term: Förmågeprodukt
    language: sv
    source: concept change
definition: "varaktigt erbjudande av tjänster och/eller varor som levereras som en helhet till en mottagare och som utvecklas, vidmakthålls och avvecklas som en sammanhållen enhet"
kind: element-type
associative:
  - concept: "[[C-084 Överenskommelse]]"
    label: regleras av
  - concept: "[[C-073 Aktör]]"
    label: levereras till
partitive: '[[C-011 Portfölj]]'
---
# C-014 Produkt

**Definition:** varaktigt erbjudande av tjänster och/eller varor som levereras som en helhet till en mottagare och som utvecklas, vidmakthålls och avvecklas som en sammanhållen enhet

## Anmärkning

Produkten är erbjudandet, det mottagaren får. Den aggregerar de verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]) som lämnas över, och realiseras av det verksamhetsbeteende som tar fram dem (ADR 0016). Mellan den som tillhandahåller produkten och mottagaren finns en överenskommelse om vad som tillhandahålls ([[C-084 Överenskommelse]]). Den behöver inte vara undertecknad: den finns så snart en av parterna uttryckligen har beskrivit vad som tillhandahålls, och kan följa av lag lika väl som av ett avtal med en kund. Produkten är också ett styrobjekt ([[C-003 Styrobjekt]]), se produktstyrning ([[C-047 Produktstyrning]]).

Produkten specialiseras på två sätt som korsar varandra. Efter var mottagaren finns är den intern ([[C-118 Intern produkt]]) eller extern ([[C-119 Extern produkt]]). Efter vad produkten är för mottagaren är den en verksamhetsprodukt ([[C-173 Verksamhetsprodukt]]), som fullgör ett uppdrag mot mottagaren, eller en leveransprodukt ([[C-174 Leveransprodukt]]), som blir en komponent i mottagarens lösning. Båda levereras av en lösning ([[C-055 Lösning]]), verksamhetsprodukten av den lösning verksamheten fullgör sitt uppdrag genom. Ingen av de fyra är en egen elementtyp; alla registreras som produkt. Förmågeprodukt är ordet när lösningen kallas förmågekonfiguration: det en förmågas lösning lämnar ut genom luckan i rummets vägg, vare sig det blir en verksamhetsprodukt eller en leveransprodukt. ADR 0020; axeln och termen Förmågeprodukt i ADR 0021.

Varorna i erbjudandet är varor ([[C-191 Vara]]), verksamhetsobjekt som blir mottagarens; tjänsterna är verksamhetstjänster ([[C-127 Verksamhetstjänst]]). Ingen sort säger vilketdera: en produkt blandar ofta, och innehållet syns i vad den aggregerar.

Motsvarar ArchiMates Product.

ProductOffering i Business Architecture Core Metamodel (BACM), med MerchandiseOffering och ServiceOffering, mappas hit. Villkoren BACM lägger i erbjudandet står i överenskommelsen. Det verksamheten själv köper in, BACM:s OutsourcedServiceOffering och ProcurementOffering, är en överenskommelse ([[C-084 Överenskommelse]]) med en aktör som är leverantör till ([[C-155 är leverantör till]]). ADR 0027.
