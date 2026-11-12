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

## Anmärkning

En lösning känns igen på sitt ändamål och sina användare. Den realiserar exakt en verksamhetsförmåga och är vid varje tid den unika kombination av komponenter som gör förmågan möjlig. Förmågan kan ha flera lösningar, och lösningen är ett valt sätt att realisera den: den kan bytas mot ett annat utan att förmågan ändras. Lösningen består när en komponent byts. Ersätts en plattform av en annan visar lösningens beskrivning två sammansättningar, nuläget och målet, men det är en lösning hela vägen.

Perspektiv avgränsar inte en lösning. En plattform är en lösning om den har eget ändamål och någon som använder den. Dess målarkitektur ligger då på lösningsnivå, under domänens och verksamhetens, med alla vyer, även verksamhetsvyn som säger vem som använder plattformen till vad. Det som bara går att beskriva ur ett perspektiv är ingen lösning utan en arkitekturvy. Testet: går det att rita verksamhetsvyn och informationsvyn för en "teknikmålarkitektur"? Då är den en lösningsmålarkitektur under verksamhetens. Går det inte, är den teknikvyn i verksamhetens målarkitektur.

En komponent kan ingå i flera lösningar. Har komponenten eget ändamål och egna användare är den en egen lösning som de andra använder. Lönehanteringen är en lösning: HR:s rutiner, lönemodulen, bankfilen och löneinformationen. Bokföringen är en annan, och delar affärssystemet med lönehanteringen. På samma sätt kan en mindre lösning ingå i en större: det som ingår i exakt en större lösning är en del av den, det som flera använder är en egen lösning med eget hem.

Varje lösning hör hemma i exakt en verksamhetsdomän, den där den styrs, aldrig direkt i verksamheten. En gemensam lösning hör hemma i den domän som har i uppdrag att tillhandahålla den. Att lösningar i andra domäner använder dess leveransprodukter ([[C-174 Leveransprodukt]]) ändrar inte det: deras behov är intern påverkan, som lösningens ändamål uttolkas ur ([[C-022 Ändamål]]). En leverantör kan leverera hela lösningen, och den hör ändå hemma i den domän som beställer den ([[C-155 är leverantör till]]). Domänen själv är ingen lösning: den avgränsas av uppdrag och styrning och består medan dess lösningar byts. En lösning har ändamål men inget uppdrag ([[C-149 Uppdrag]]).

Lösningen är både styrobjekt och arkitekturobjekt. Som styrobjekt är den det som styrningen av förvaltning och utveckling avser; som arkitekturobjekt ligger den på lösningsnivå. Lösningsägaren har mandatet ([[C-189 Mandat]]) över lösningen som styrobjekt: en, aldrig två (beslut 35). Processägaren ([[C-206 Processägare]]) äger beteendena i lösningen och informationsägaren ([[C-167 Informationsägare]]) informationen. Lösningsägaren äger hur de och tekniken ska fungera ihop, nu och över tid, och fastställer ([[C-183 fastställs av]]) målarkitekturen ([[C-054 Målarkitektur]]). Arkitekturansvaret ([[C-117 Arkitekturansvar]]) tar fram målarkitekturen, och initiativ ([[C-012 Initiativ]]) i portföljen genomför den. Systemägaren äger applikationen ([[C-071 Applikation]]), inte lösningen.

Lösningsägaren svarar också för lösningens produkter, för en produkt har ingen egen ägare. När ett initiativ ändrar lösningen ställer lösningsägaren kraven på det initiativet lämnar och svarar för effekten. Initiativets ägare beslutar om arbetet. En lösningsägare får starta ett eget initiativ inom lösningens ram. Beslut 46.

En lösning som lämnar verksamhetsprodukter hör hemma i en produktionsdomän ([[C-010 Produktionsdomän]]), och dess ram sätts när verksamhetens ramar sätts. En lösning som lämnar leveransprodukter hör hemma i utvecklingsdomänen ([[C-009 Utvecklingsdomän]]), och dess ram sätts genom portföljen. Lämnar en lösning båda slagen är det ett fynd som prövas mot provet för ett snitt. Beslut 46.

Målet ([[C-017 Mål]]) sätts på förmågan, vad som ska vara möjligt, och ramen på var och en av lösningarna som realiserar den. Det lösningen levererar är produkter ([[C-014 Produkt]]), förmågeprodukter av båda slagen. Verksamhetsprodukter ([[C-173 Verksamhetsprodukt]]) levererar verksamheten genom lösningen till mottagaren, för att fullgöra sitt uppdrag. Leveransprodukter ([[C-174 Leveransprodukt]]) använder en annan förmågas lösning som komponent; så får en lösning vissa av sina komponenter, information till exempel, från andra lösningar. Leveransprodukterna realiseras av lösningen, och portföljen ([[C-011 Portfölj]]) prioriterar och finansierar dem. Lösningen själv står utanför portföljen men tar emot ramen. Beslut 20; lösningens beständighet och produktaxeln beslut 21.

Ett förvaltningsobjekt som realiserar flera förmågor är i katalogens ögon flera lösningar som delar komponenter, eller en lösning för en grövre förmåga. Förmågekartan visar vilket.

Andra ord för samma sak. Förmågekonfiguration är katalogens andra term: ordet betonar sammansättningen, lösningen sedd från det som bygger den. ISO 42010 kallar det *system of interest*. I dagligt tal kallas en lösning av det här slaget ofta en funktion, till exempel arkitekturfunktionen.

Provet för ett snitt, fyra delar. Samförändring: två lösningar ska kunna ändras var för sig. Måste de alltid ändras tillsammans är snittet fel. Förmågekartan visar var felet sitter: antingen är de en lösning, eller så hör de till två olika förmågor. Gränssnittet: gränsen går där kopplingen ([[C-211 Koppling]]) är lös. Lös betyder att det ena kan ändras utan att det andra måste ändras samtidigt. Det som korsar gränsen är en leveransprodukt ([[C-174 Leveransprodukt]]) med krav ([[C-021 Krav]]) och överenskommelse ([[C-084 Överenskommelse]]). Provet gäller komponenterna, beteende, information och teknik; resurser ([[C-122 Resurs]]), personal och kompetens, korsar fritt. Mandatet: ägaren kan besluta över varje komponent innanför och har ramen ([[C-210 Ram]]) att genomföra. Där ägaren inte kan det är gränsen fel eller mandatet. Delning: det flera använder bryts ut som egen lösning med egen ägare. Regeln är David Parnas (1972): varje modul döljer ett beslut som troligen ändras, så att ändringen stannar innanför gränsen. En organisation som antar provet gör det som arkitekturprincip ([[C-040 Arkitekturprincip]]) i sin referensarkitektur; katalogen definierar, organisationen fastställer.

När IT-avdelningen "äger systemen" i alla lösningar är det tre saker och aldrig en fjärde: arkitekturansvar ([[C-117 Arkitekturansvar]]) för teknik- och applikationsperspektivet, alltså vyerna; systemägare per applikation ([[C-071 Applikation]]) inuti varje lösning, under dess lösningsägare; och egna plattformslösningar i IT:s domän, som levererar leveransprodukter mot krav. Aldrig lösningsägare till verksamhetens lösning. Ansvar ([[C-209 Ansvar]]) som skärs på komponent utan någon som äger lösningen är ägarskap över vyer, och det som bara kan beskrivas ur ett perspektiv är ingen lösning. Beslut 36.

## Motsvarigheter

Motsvarar CapabilityImplementation i Business Architecture Core Metamodel (BACM), den samling resurser och utförare som implementerar en förmåga; lagrets skärpning är att en lösning realiserar exakt en förmåga. Beslut 27.

Motsvarar också CapabilityOffer i Value Delivery Modeling Language (VDML), en organisationsenhets förmåga med de resurser, metoder och personpooler som levererar den. Beslut 28.

Förvaltningsobjekt är det ord en förvaltningsmodell byggd på pm3 använder för lösningen som styrobjekt (objektstyrning, [[C-048 Objektstyrning]]). Där äger två objektet tillsammans, en objektägare från verksamheten och en från IT; katalogen har en ägare. pm3 kallar objektet i dag leveransområde, under byggstenen ansvarsområde, och kallade det tidigare objekt.

## Exempel

ett IT-system med sina processer och sin information; en teknisk plattform med sina användare; en tjänst.
