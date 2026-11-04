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

Lösningen är både styrobjekt, det som styrningen av dess förvaltning och utveckling avser, och arkitekturobjekt på lösningsnivå. Avgränsas av ändamål och användare, inte av perspektiv: en plattform är en lösning om den har ett eget ändamål och någon som använder den, och dess målarkitektur ligger då på lösningsnivå, under domänens och verksamhetens, med alla vyer, även verksamhetsvyn som säger vem som använder den till vad. Det som bara går att beskriva ur ett perspektiv är ingen lösning utan en arkitekturvy. Testet: går det att rita verksamhetsvyn och informationsvyn för en "teknikmålarkitektur" är den en lösningsmålarkitektur och står under verksamhetens; går det inte, är den teknikvyn i verksamhetens. ISO 42010: system of interest. En lösning är ett valt sätt att realisera en verksamhetsförmåga och kan bytas mot ett annat utan att förmågan ändras; en verksamhetsförmåga kan ha flera lösningar, men en lösning realiserar exakt en förmåga: den är vid varje tid den unika kombination av komponenter som gör förmågan möjlig. Lösningen känns igen på sitt ändamål och sina användare och består när en komponent byts; när en plattform ersätts av en annan visar lösningens beskrivning två sammansättningar, nuläget och målet, men det är en lösning hela vägen. En komponent kan ingå i flera lösningar; har den eget ändamål och egna användare är den en egen lösning som de andra använder. Lönehanteringen är en lösning, HR:s rutiner, lönemodulen, bankfilen och löneinformationen; bokföringen är en annan, som delar affärssystemet med den. Lösning och förmågekonfiguration är samma begrepp, därav den andra termen; ordet betonar sammansättningen, lösningen sedd från det som bygger den. En verksamhetsdomän är ingen lösning: den avgränsas av uppdrag och styrning och består medan dess lösningar byts. En lösning hör hemma i exakt en verksamhetsdomän, den där den styrs, aldrig direkt i verksamheten; en gemensam lösning hör hemma i den domän som har i uppdrag att tillhandahålla den. Att flera domäner använder lösningen ändrar inte var den hör hemma: deras behov är intern påverkan som lösningens ändamål uttolkas ur ([[C-022 Ändamål]]). En mindre lösning kan ingå i en större: det som ingår i exakt en större lösning är en del av den, det som används av flera är en egen lösning med eget hem. En lösning har ändamål men inget uppdrag ([[C-149 Uppdrag]]). En lösning kan levereras i sin helhet av en leverantör och hör ändå hemma i den domän som beställer den ([[C-155 är leverantör till]]). I dagligt tal kallas en lösning av det här slaget ofta en funktion, till exempel arkitekturfunktionen.

Förvaltningsobjekt är det ord en förvaltningsmodell byggd på pm3 använder för lösningen som styrobjekt (objektstyrning, [[C-048 Objektstyrning]]), med en objektägare från verksamheten och en från IT som tillsammans äger den; katalogen har en ägare per styrobjekt, lösningsägaren, den som har mandatet ([[C-189 Mandat]]) över lösningen (ADR 0035); pm3 kallar den i dag leveransområde, under byggstenen ansvarsområde, och kallade den tidigare objekt. Ett förvaltningsobjekt som realiserar flera förmågor är i katalogens ögon flera lösningar som delar komponenter, eller en lösning för en grövre förmåga; vilket, visar kartan. Målet ([[C-017 Mål]]) sätts på förmågan, vad som ska vara möjligt, och ramen på var och en av lösningarna som realiserar den. Det en lösning levererar är produkter ([[C-014 Produkt]]), förmågeprodukter, av båda slagen: verksamhetsprodukter ([[C-173 Verksamhetsprodukt]]), som verksamheten genom sin lösning levererar till mottagaren för att fullgöra sitt uppdrag, och leveransprodukter ([[C-174 Leveransprodukt]]), som en annan förmågas lösning använder som komponent; vissa av en lösnings komponenter, information till exempel, tas fram och tillgängliggörs så av andra lösningar. Leveransprodukterna realiseras av lösningen och prioriteras och finansieras av portföljen ([[C-011 Portfölj]]); lösningen själv står utanför portföljen men tar emot ramen. ADR 0020; lösningens beständighet och produktaxeln ADR 0021.

Lösningsägaren är den som har mandatet över lösningen som styrobjekt: en, aldrig två. Processägaren ([[C-206 Processägare]]) äger beteendena i lösningen och informationsägaren ([[C-167 Informationsägare]]) informationen; lösningsägaren äger hur de och tekniken ska fungera ihop, nu och över tid, och fastställer ([[C-183 fastställs av]]) målarkitekturen ([[C-054 Målarkitektur]]), som arkitekturansvaret ([[C-117 Arkitekturansvar]]) tar fram och initiativ ([[C-012 Initiativ]]) i portföljen genomför. Systemägare är inte lösningens ägare utan applikationens ([[C-071 Applikation]]). ADR 0035.

Provet för ett snitt, fyra delar. Samförändring: två lösningar ska kunna ändras var för sig. Måste de alltid ändras tillsammans är snittet fel. Förmågekartan visar var felet sitter: antingen är de en lösning, eller så hör de till två olika förmågor. Gränssnittet: gränsen går där kopplingen ([[C-211 Koppling]]) är lös. Lös betyder att det ena kan ändras utan att det andra måste ändras samtidigt. Det som korsar gränsen är en leveransprodukt ([[C-174 Leveransprodukt]]) med krav ([[C-021 Krav]]) och överenskommelse ([[C-084 Överenskommelse]]). Provet gäller komponenterna, beteende, information och teknik; resurser ([[C-122 Resurs]]), personal och kompetens, korsar fritt. Mandatet: ägaren kan besluta över varje komponent innanför och har ramen ([[C-210 Ram]]) att genomföra. Där ägaren inte kan det är gränsen fel eller mandatet. Delning: det flera använder bryts ut som egen lösning med egen ägare. Regeln är David Parnas (1972): varje modul döljer ett beslut som troligen ändras, så att ändringen stannar innanför gränsen. En organisation som antar provet gör det som arkitekturprincip ([[C-040 Arkitekturprincip]]) i sin referensarkitektur; katalogen definierar, organisationen fastställer.

När IT-avdelningen "äger systemen" i alla lösningar är det tre saker och aldrig en fjärde: arkitekturansvar ([[C-117 Arkitekturansvar]]) för teknik- och applikationsperspektivet, alltså vyerna; systemägare per applikation ([[C-071 Applikation]]) inuti varje lösning, under dess lösningsägare; och egna plattformslösningar i IT:s domän, som levererar leveransprodukter mot krav. Aldrig lösningsägare till verksamhetens lösning. Ansvar ([[C-209 Ansvar]]) som skärs på komponent utan någon som äger lösningen är ägarskap över vyer, och det som bara kan beskrivas ur ett perspektiv är ingen lösning. ADR 0036.

Motsvarar CapabilityImplementation i Business Architecture Core Metamodel (BACM), den samling resurser och utförare som implementerar en förmåga; lagrets skärpning är att en lösning realiserar exakt en förmåga. ADR 0027.

Motsvarar också CapabilityOffer i Value Delivery Modeling Language (VDML), en organisationsenhets förmåga med de resurser, metoder och personpooler som levererar den. ADR 0028.
