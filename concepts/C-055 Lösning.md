---
id: C-055
term: Lösning
terms:
  - term: Lösning
    language: sv
    source: catalogue
  - term: Förmågekonfiguration
    language: sv
    source: catalogue
  - term: Förvaltningsobjekt
    language: sv
    source: concept change
definition: kombination av aktörer, processer, information och teknik som tillsammans realiserar en verksamhetsförmåga för ett eget ändamål
kind: architecture-object-type
architecture_level: solution
generic: "[[C-032 Arkitekturobjekt]]"
associative:
  - concept: "[[C-069 Verksamhetsförmåga]]"
    label: realiserar
  - concept: "[[C-122 Resurs]]"
    label: tar i anspråk
  - concept: "[[C-008 Verksamhetsdomän]]"
    label: hör hemma i
  - concept: "[[C-055 Lösning]]"
    label: kan ingå i
  - concept: '[[C-211 Koppling]]'
    label: avgränsas av
---
# C-055 Lösning

**Definition:** kombination av aktörer, processer, information och teknik som tillsammans realiserar en verksamhetsförmåga för ett eget ändamål

## Exempel

ett IT-system med sina processer och sin information; en teknisk plattform med sina användare; en tjänst.

## Anmärkning

Lösningen är två saker på en gång. Den är ett styrobjekt: det som styrningen av dess förvaltning och utveckling avser. Den är också ett arkitekturobjekt på lösningsnivå.

En lösning avgränsas av sitt ändamål och sina användare, inte av perspektiv. En plattform är en lösning om den har ett eget ändamål och någon som använder den. Då ligger dess målarkitektur på lösningsnivå, under domänens och verksamhetens, med alla vyer. Även verksamhetsvyn finns med, den som säger vem som använder plattformen till vad. Det som bara går att beskriva ur ett perspektiv är ingen lösning utan en arkitekturvy. Testet: går det att rita verksamhetsvyn och informationsvyn för en "teknikmålarkitektur"? Då är den en lösningsmålarkitektur och står under verksamhetens. Går det inte, är den teknikvyn i verksamhetens målarkitektur. ISO 42010 kallar det *system of interest*.

En lösning är ett valt sätt att realisera en verksamhetsförmåga. Den kan bytas mot ett annat sätt utan att förmågan ändras. En verksamhetsförmåga kan ha flera lösningar, men en lösning realiserar exakt en förmåga: den är vid varje tid den unika kombination av komponenter som gör förmågan möjlig. Lösningen känns igen på sitt ändamål och sina användare, och den består när en komponent byts. När en plattform ersätts av en annan visar lösningens beskrivning två sammansättningar, nuläget och målet. Det är ändå en lösning hela vägen. En komponent kan ingå i flera lösningar. Har komponenten eget ändamål och egna användare är den en egen lösning som de andra använder. Lönehanteringen är en lösning: HR:s rutiner, lönemodulen, bankfilen och löneinformationen. Bokföringen är en annan lösning, som delar affärssystemet med lönehanteringen. Lösning och förmågekonfiguration är samma begrepp, därav den andra termen. Det ordet betonar sammansättningen: lösningen sedd från det som bygger den.

En verksamhetsdomän är ingen lösning. Domänen avgränsas av uppdrag och styrning, och den består medan dess lösningar byts. En lösning hör hemma i exakt en verksamhetsdomän, den där den styrs, aldrig direkt i verksamheten. En gemensam lösning hör hemma i den domän som har i uppdrag att tillhandahålla den. Att flera domäner använder lösningen ändrar inte var den hör hemma. Deras behov är intern påverkan, som lösningens ändamål uttolkas ur ([[C-022 Ändamål]]). En mindre lösning kan ingå i en större. Det som ingår i exakt en större lösning är en del av den. Det som används av flera är en egen lösning med eget hem. En lösning har ändamål men inget uppdrag ([[C-149 Uppdrag]]). En leverantör kan leverera en lösning i sin helhet, och lösningen hör ändå hemma i den domän som beställer den ([[C-155 är leverantör till]]). I dagligt tal kallas en lösning av det här slaget ofta en funktion, till exempel arkitekturfunktionen.

Förvaltningsobjekt är det ord en förvaltningsmodell byggd på pm3 använder för lösningen som styrobjekt (objektstyrning, [[C-048 Objektstyrning]]). Där äger två objektet tillsammans: en objektägare från verksamheten och en från IT. Katalogen har en ägare per styrobjekt, lösningsägaren, den som har mandatet ([[C-189 Mandat]]) över lösningen (ADR 0035). pm3 kallar objektet i dag leveransområde, under byggstenen ansvarsområde, och kallade det tidigare objekt. Ett förvaltningsobjekt som realiserar flera förmågor är i katalogens ögon antingen flera lösningar som delar komponenter, eller en lösning för en grövre förmåga. Förmågekartan visar vilket. Målet ([[C-017 Mål]]) sätts på förmågan, alltså på vad som ska vara möjligt. Ramen sätts på var och en av lösningarna som realiserar förmågan.

Det en lösning levererar är produkter ([[C-014 Produkt]]), förmågeprodukter, av båda slagen. Verksamhetsprodukter ([[C-173 Verksamhetsprodukt]]) levererar verksamheten genom sin lösning till mottagaren, för att fullgöra sitt uppdrag. Leveransprodukter ([[C-174 Leveransprodukt]]) använder en annan förmågas lösning som komponent. Så tas vissa av en lösnings komponenter fram av andra lösningar, information till exempel. Leveransprodukterna realiseras av lösningen, och portföljen ([[C-011 Portfölj]]) prioriterar och finansierar dem. Lösningen själv står utanför portföljen men tar emot ramen. ADR 0020; lösningens beständighet och produktaxeln ADR 0021.

Lösningsägaren är den som har mandatet över lösningen som styrobjekt: en, aldrig två. Processägaren ([[C-206 Processägare]]) äger beteendena i lösningen, och informationsägaren ([[C-167 Informationsägare]]) äger informationen. Lösningsägaren äger hur de och tekniken ska fungera ihop, nu och över tid. Lösningsägaren fastställer ([[C-183 fastställs av]]) målarkitekturen ([[C-054 Målarkitektur]]). Arkitekturansvaret ([[C-117 Arkitekturansvar]]) tar fram den, och initiativ ([[C-012 Initiativ]]) i portföljen genomför den. Systemägaren äger inte lösningen utan applikationen ([[C-071 Applikation]]). ADR 0035.

Provet för ett snitt, fyra delar. Samförändring: två lösningar ska kunna ändras var för sig. Måste de alltid ändras tillsammans är snittet fel. Förmågekartan visar var felet sitter: antingen är de en lösning, eller så hör de till två olika förmågor. Gränssnittet: gränsen går där kopplingen ([[C-211 Koppling]]) är lös. Lös betyder att det ena kan ändras utan att det andra måste ändras samtidigt. Det som korsar gränsen är en leveransprodukt ([[C-174 Leveransprodukt]]) med krav ([[C-021 Krav]]) och överenskommelse ([[C-084 Överenskommelse]]). Provet gäller komponenterna, beteende, information och teknik; resurser ([[C-122 Resurs]]), personal och kompetens, korsar fritt. Mandatet: ägaren kan besluta över varje komponent innanför och har ramen ([[C-210 Ram]]) att genomföra. Där ägaren inte kan det är gränsen fel eller mandatet. Delning: det flera använder bryts ut som egen lösning med egen ägare. Regeln är David Parnas (1972): varje modul döljer ett beslut som troligen ändras, så att ändringen stannar innanför gränsen. En organisation som antar provet gör det som arkitekturprincip ([[C-040 Arkitekturprincip]]) i sin referensarkitektur; katalogen definierar, organisationen fastställer.

När IT-avdelningen "äger systemen" i alla lösningar är det tre saker och aldrig en fjärde: arkitekturansvar ([[C-117 Arkitekturansvar]]) för teknik- och applikationsperspektivet, alltså vyerna; systemägare per applikation ([[C-071 Applikation]]) inuti varje lösning, under dess lösningsägare; och egna plattformslösningar i IT:s domän, som levererar leveransprodukter mot krav. Aldrig lösningsägare till verksamhetens lösning. Ansvar ([[C-209 Ansvar]]) som skärs på komponent utan någon som äger lösningen är ägarskap över vyer, och det som bara kan beskrivas ur ett perspektiv är ingen lösning. ADR 0036.

Motsvarar CapabilityImplementation i Business Architecture Core Metamodel (BACM), den samling resurser och utförare som implementerar en förmåga; lagrets skärpning är att en lösning realiserar exakt en förmåga. ADR 0027.

Motsvarar också CapabilityOffer i Value Delivery Modeling Language (VDML), en organisationsenhets förmåga med de resurser, metoder och personpooler som levererar den. ADR 0028.
