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
---
# C-014 Produkt

**Definition:** varaktigt erbjudande av tjänster och/eller varor som levereras som en helhet till en mottagare och som utvecklas, vidmakthålls och avvecklas som en sammanhållen enhet

## Anmärkning

Motsvarar ArchiMates Product. Mellan den som tillhandahåller produkten och mottagaren finns en överenskommelse om vad som tillhandahålls ([[C-084 Överenskommelse]]). Den behöver inte vara undertecknad: den finns så snart en av parterna uttryckligen har beskrivit vad som tillhandahålls, och kan följa av lag lika väl som av ett avtal med en kund. Produkten är också ett styrobjekt ([[C-003 Styrobjekt]]), se produktstyrning ([[C-047 Produktstyrning]]). Produkten är erbjudandet, det mottagaren får; den aggregerar de verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]) som lämnas över, och realiseras av det verksamhetsbeteende som tar fram dem (ADR 0016).

Produkten specialiseras på två sätt som korsar varandra: efter var mottagaren finns, intern ([[C-118 Intern produkt]]) eller extern ([[C-119 Extern produkt]]), och efter vad produkten är för mottagaren: verksamhetsprodukten ([[C-173 Verksamhetsprodukt]]) fullgör ett uppdrag mot mottagaren, leveransprodukten ([[C-174 Leveransprodukt]]) blir en komponent i mottagarens lösning. Båda levereras av en lösning ([[C-055 Lösning]]), verksamhetsprodukten av den lösning verksamheten fullgör sitt uppdrag genom. Ingen av de fyra är en egen elementtyp; alla registreras som produkt. Förmågeprodukt är ordet när lösningen kallas förmågekonfiguration: det en förmågas lösning lämnar ut genom luckan i rummets vägg, vare sig det blir en verksamhetsprodukt eller en leveransprodukt. ADR 0020; axeln och termen Förmågeprodukt i ADR 0021.

Varorna i erbjudandet är varor ([[C-191 Vara]]), verksamhetsobjekt som blir mottagarens; tjänsterna är verksamhetstjänster ([[C-127 Verksamhetstjänst]]). Ingen sort säger vilketdera: en produkt blandar ofta, och innehållet syns i vad den aggregerar. ProductOffering i Business Architecture Core Metamodel (BACM), med MerchandiseOffering och ServiceOffering, mappas hit; villkoren BACM lägger i erbjudandet står i överenskommelsen, och det verksamheten själv köper in, BACM:s OutsourcedServiceOffering och ProcurementOffering, är en överenskommelse ([[C-084 Överenskommelse]]) med en aktör som är leverantör till ([[C-155 är leverantör till]]). ADR 0027.
