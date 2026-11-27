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
nesting_relation_type: composed_of
generic: "[[C-122 Resurs]]"
---
# C-060 Informationsobjekt

**Definition:** avgränsad mängd information som verksamheten hanterar som en enhet

## Anmärkning

Ett informationsobjekt är informationssidan av det verksamheten hanterar: ett verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]) realiseras av ett eller flera informationsobjekt. Det är en typ i informationsperspektivet. Begreppet som definierar objektet hör till katalogen, inte till arkitekturen: katalogen är organisationens ordlista, och begreppet ärende tas in där när arkitekturen namnger objektet Ärende ([[0023-regeln-anger-vad-som-ska-galla-kravet-ar-en-sorts-regel-katalogen-ar-organisationens-ordlista-och-sbvr-tas-in-med-faststalls-av-som-relationstyp|beslut 23]]). [[0016-verksamhetsobjekt-ar-en-elementtyp|Beslut 16]].

Ett informationsobjekt består av uppgifter ([[C-161 Uppgift]]), attributen. Uppgifterna ritas inuti rutan, inte som egna element, och varje uppgift som ritas har sitt begrepp i katalogen, som objektet självt ([[0024-tillstand-ar-en-elementtyp-uppgiften-ar-informationsmodellens-attribut-och-lagret-ar-den-delade-datamodell-sdmn-beskriver|beslut 24]]). Informationsobjektet har inget eget tillstånd: en uppgift, statusfältet, bär verksamhetsobjektets tillstånd ([[C-182 Tillstånd]]) ([[0024-tillstand-ar-en-elementtyp-uppgiften-ar-informationsmodellens-attribut-och-lagret-ar-den-delade-datamodell-sdmn-beskriver|beslut 24]]). Multipliciteten mellan två informationsobjekt, "ett ärende har exakt en sökande", står på relationen mellan dem, i dess beskrivning tills interlingua har fältet, och ritningarna visar den ([[0023-regeln-anger-vad-som-ska-galla-kravet-ar-en-sorts-regel-katalogen-ar-organisationens-ordlista-och-sbvr-tas-in-med-faststalls-av-som-relationstyp|beslut 23]]).

Nivån i informationsmodellen väljs efter vad verksamheten behöver tala om och vad dess beteenden hanterar. Den får vara grov och förfinas över tid: nya objekt läggs under det grova, som då är ett informationsområde ([[C-198 Informationsområde]]). Klassning, ägande och reglering är skäl bland flera, men ett golv: det som klassas, ägs eller regleras för sig är alltid ett eget objekt. Personnumret är ett informationsobjekt, förfallodatumet en uppgift i Faktura ([[0030-informationsomradet-ar-ett-begrepp-utan-elementtyp-ett-informationsobjekt-som-bestar-av-sina-objekt-varje-objekt-har-ett-hem-och-nivan-far-vara-grov|beslut 30]]). Objektet som rymmer ett sådant fält aggregerar det ([[C-100 aggregerar]]), eftersom samma fält ingår i många objekt. Informationsägaren sätter klassen på informationsobjektet, inte på uppgiften eller lagringsytan. Klassen är konfidentialitet och riktighet. Den står i organisationens klassningsförteckning, som pekar på objektet, och lagret bär inga nivåer. Tillgänglighet och spårbarhet är inga klasser. De är krav som processägaren ställer på behandlingen; se [[C-166 Informationstillgång]]. [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|Beslut 58]].

Lagret ritar typer, och informationsägaren sätter klassen på typen. Nivån i varje klass måste hålla för varje förekomst, också den som ställer störst krav: det värsta fallet gäller. Beror nivån på värdet i en uppgift, är uppgiften ändå en vanlig uppgift med en värdemängd ([[C-197 Värdemängd]]). Bostadsbolagets Yrkesroll har uppgiften utsatt roll med värdena ja och nej. Informationsägaren sätter nivån så att den håller för de utsatta rollerna.

Blir nivån för hög för de övriga rollerna, hanterar verksamheten de utsatta rollerna för sig, och golvet för vad som blir ett eget informationsobjekt gäller ([[0030-informationsomradet-ar-ett-begrepp-utan-elementtyp-ett-informationsobjekt-som-bestar-av-sina-objekt-varje-objekt-har-ett-hem-och-nivan-far-vara-grov|beslut 30]]). Utsatt roll blir då ett eget informationsobjekt som specialiserar ([[C-063 specialiserar]]) Yrkesroll. Det ärver Yrkesrolls uppgifter och lägger till sina egna; exemplet Brinkstadsbostäder visar vilka. Uppgiften utsatt roll står kvar i Yrkesroll, eftersom den skiljer de två objekten åt. Tydligast är fallet när rollen placeras i en säkerhetsskyddsklass: då är den reglerad för sig.

En uppgift blir aldrig ett eget element för att den ska kunna klassas ([[0040-nivan-i-en-klass-beror-pa-vardet-i-en-uppgift-varsta-fallet-galler-eller-delmangden-blir-ett-eget-informationsobjekt-och-en-forteckning-i-ett-exemplar-ar-anda-en-typ|beslut 40]]).

En sammanställning ([[C-162 Sammanställning]]) registreras som informationsobjekt och aggregerar det den är gjord av. Ett informationsområde ([[C-198 Informationsområde]]) registreras som informationsobjekt och består av ([[C-062 består av]]) de objekt det samlar. Varje informationsobjekt hör hemma i exakt ett område ([[0030-informationsomradet-ar-ett-begrepp-utan-elementtyp-ett-informationsobjekt-som-bestar-av-sina-objekt-varje-objekt-har-ett-hem-och-nivan-far-vara-grov|beslut 30]]).

Ett informationsobjekt kan ha en datakategori ([[C-201 Datakategori]]): resursdata ([[C-202 Resursdata]]), referensdata ([[C-203 Referensdata]]), transaktionsdata ([[C-204 Transaktionsdata]]) eller händelsedata ([[C-205 Händelsedata]]). Kategorin är frivillig och högst en, så att en informationsmodell kan färgas efter den och informationsägaren lista sina resursdata. Kategorin sitter på informationsobjektet, inte på verksamhetsobjektet det realiserar; ett informationsområde och en sammanställning har ingen. Tills interlingua bär kategorin som ett fält på elementet står den som en mening i beskrivningen. [[0032-datakategorin-ar-ett-begrepp-resursdata-referensdata-transaktionsdata-och-handelsedata-sitter-pa-informationsobjektet-hogst-en-och-frivillig-och-referensdata-ar-en-vardemangd-organisationen-sjalv-faststaller|Beslut 32]].

Entitetstyp är informationsmodelleringens ord för samma sak: mallen, inte förekomsten. Person är en entitetstyp och ett informationsobjekt; en enskild företrädare i föreningsregistret är en entitet, ingen av delarna. Termen är tillåten så att katalogen svarar rätt när ordet används.

## Motsvarigheter

Informationsobjektet är ArchiMates Data Object.

SDMN (Shared Data Model and Notation), den datamodell BPMN, CMMN och DMN delar, kallar samma sak DataItem och dess struktur ItemDefinition; båda är informationsobjektet, strukturen dess uppgifter. Lagret är den delade datamodellen: SDMN är ett utbytesformat mellan verktygen, inget verktyg för informationsmodellering, och ett sådant verktyg får sina dataelement från lagrets informationsobjekt. [[0024-tillstand-ar-en-elementtyp-uppgiften-ar-informationsmodellens-attribut-och-lagret-ar-den-delade-datamodell-sdmn-beskriver|Beslut 24]].

Motsvarar Class i Unified Modeling Language (UML): klassdiagrammet är informationsmodellen, attributen (Property) uppgifter och en Enumeration en värdemängd ([[C-197 Värdemängd]]). Klassen i klassdiagrammet är alltid informationsobjektet. Den klass vars tillståndsmaskin ritas är det verksamhetsobjekt informationsobjektet realiserar, och aktivitetsdiagrammets objekt är verksamhetsobjektet. [[0029-klassen-ar-informationsobjektet-tillstandsmaskinen-ar-tillstandsvyn-anvandningsfallet-ar-tjansten-vardemangd-ar-ett-begrepp-och-uml-tas-in-for-lasarnas-skull-utan-tveksamma-rader|Beslut 29]].

## Exempel

en ansökan, ett ärende, en person i ett register.
