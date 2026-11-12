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

Produkten är erbjudandet, det mottagaren får. Den aggregerar de verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]) som lämnas över, och realiseras av det verksamhetsbeteende som tar fram dem (beslut 16). Mellan den som tillhandahåller produkten och mottagaren finns en överenskommelse om vad som tillhandahålls ([[C-084 Överenskommelse]]). Den behöver inte vara undertecknad: den finns så snart en av parterna uttryckligen har beskrivit vad som tillhandahålls, och kan följa av lag lika väl som av ett avtal med en kund. Produkten är inget styrobjekt ([[C-003 Styrobjekt]]) och har ingen egen ägare. Ägaren till lösningen som realiserar produkten beslutar om den och svarar för den, se produktstyrning ([[C-047 Produktstyrning]]). Beslut 46.

Produkten specialiseras på två sätt som korsar varandra. Efter var mottagaren finns är den intern ([[C-118 Intern produkt]]) eller extern ([[C-119 Extern produkt]]). Efter vad produkten är för mottagaren är den en verksamhetsprodukt ([[C-173 Verksamhetsprodukt]]), som fullgör ett uppdrag mot mottagaren, eller en leveransprodukt ([[C-174 Leveransprodukt]]), som blir en komponent i mottagarens lösning. Båda levereras av en lösning ([[C-055 Lösning]]), verksamhetsprodukten av den lösning verksamheten fullgör sitt uppdrag genom. Ingen av de fyra är en egen elementtyp; alla registreras som produkt. Förmågeprodukt är ordet när lösningen kallas förmågekonfiguration: det en förmågas lösning lämnar ut genom luckan i rummets vägg, vare sig det blir en verksamhetsprodukt eller en leveransprodukt. Beslut 20; axeln och termen Förmågeprodukt i beslut 21.

Varorna i erbjudandet är varor ([[C-191 Vara]]), verksamhetsobjekt som blir mottagarens; tjänsterna är verksamhetstjänster ([[C-127 Verksamhetstjänst]]). Ingen sort säger vilketdera: en produkt blandar ofta, och innehållet syns i vad den aggregerar.

Produkten är varaktig, resultatet finns per körning. Produkten Verksamhetsbidraget aggregerar verksamhetsobjektet Ärendebeslut. Bifallet till en viss förening är en leverans av produkten, inte en del av den. Ett avslag är också en leverans: föreningen har fått prövningen och beslutet, men inga pengar.

Produkten hör till lösningens gräns. Inte varje resultat som lämnar en lösning hör till en produkt. Provet har två led. Vem tar emot objektet över lösningens gräns? Är det till för just den mottagaren? Ett beslut om återkrav tas emot av föreningen men är inte till för den, och hör därför inte till någon produkt. Riktningen avgör aldrig: en produkt kan gå ut till en kund, in till en annan lösning eller upp till den som styr, som årsredovisningen till styrelsen. Den kan inte gå till den egna lösningen. Beslut 45.

En produkt erbjuds av exakt en lösning. Det andra lösningar bidrar med kommer till den lösningen som leveransprodukter ([[C-174 Leveransprodukt]]). Verksamhetsbidraget lovar en prövning, ett beslut och en utbetalning. Lösningen Ansökningshandläggningen erbjuder bidraget, och dess ägare svarar inför föreningen för hela löftet, även om en annan lösning betalar ut. Den lösningens ägare svarar i sin tur inför Ansökningshandläggningens ägare, mot krav och överenskommelse. Så finns det en som svarar på var sida om varje gräns. Två lösningar med var sin produkt kan använda samma utbetalning. Beslut 46.

## Motsvarigheter

Motsvarar ArchiMates Product.

ProductOffering i Business Architecture Core Metamodel (BACM), med MerchandiseOffering och ServiceOffering, mappas hit. Villkoren BACM lägger i erbjudandet står i överenskommelsen. Det verksamheten själv köper in, BACM:s OutsourcedServiceOffering och ProcurementOffering, är en överenskommelse ([[C-084 Överenskommelse]]) med en aktör som är leverantör till ([[C-155 är leverantör till]]). Beslut 27.
