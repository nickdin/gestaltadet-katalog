---
id: C-130
term: Verksamhetsprocess
terms:
  - term: Verksamhetsprocess
    language: sv
    source: catalogue
definition: "process som aktörer i verksamheten utför"
kind: element-type
generic: "[[C-070 Process]]"
---
# C-130 Verksamhetsprocess

**Definition:** process som aktörer i verksamheten utför

## Anmärkning

En verksamhetsprocess har en början och ett slut, och namnet säger vad processen åstadkommer. Den namnges med ett verb i infinitiv följt av objektet: Ta fram årsredovisningen, Producera statistik, Göra dataskyddsbedömning. Det som inte går att namnge så är ingen process. Ett löpande ansvar är en verksamhetsfunktion ([[C-158 Verksamhetsfunktion]]), som namnges på samma sätt; typen bär skillnaden. [[0012-processer-namnges-med-verb-i-infinitiv-och-objekt|Beslut 12]], ändrat i [[0015-process-arende-och-funktion-ar-tre-verksamhetsbeteenden-av-samma-rang|beslut 15]].

En process är ett verksamhetsbeteende ([[C-157 Verksamhetsbeteende]]): den har en egen start, en händelse som sätter igång den, och ett eget resultat som någon utanför kedjan tar emot. Det som saknar endera är en verksamhetsaktivitet ([[C-175 Verksamhetsaktivitet]]) i någon annan process ([[0014-processerna-ar-organisationens-och-kartan-delas-per-process|beslut 14]]).

Resultatet är det verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]) processen lämnar ifrån sig. Den som tar emot det finns utanför processen själv. Resultat är inget eget begrepp och får ingen egen relation: det läses ur att processen skriver objektet ([[C-101 har åtkomst till]]). Ett resultat kan höra till en produkt ([[C-014 Produkt]]) eller sakna produkt. [[0045-resultatet-ar-verksamhetsobjektet-ett-beteende-lamnar-ifran-sig-produkten-ar-erbjudandet-vid-losningens-grans-och-ett-resultat-kan-sakna-produkt|Beslut 45]].

Arkivredovisningens klassificeringsstruktur läses ur verksamhetsbeteendena, inte bara ur processerna. Det står i Verksamhetsbeteende ([[C-157 Verksamhetsbeteende]], [[0067-arkivet-har-tva-enheter-handlingsslaget-lases-ur-verksamhetsbeteendet-och-handlingstypen-ar-representationen-redovisad-under-aktiviteten-dar-handlingen-kommer-in-eller-upprattas|beslut 67]]).

## Motsvarigheter

Motsvarar ArchiMates Business Process. I BPMN motsvarar den Process; stegen i den är verksamhetsaktiviteter och ritas i BPMN, och en delprocess är en process som processen rymmer ([[0022-aktivitet-och-beslutslogik-ar-elementtyper-bpmn-cmmn-och-dmn-tas-in-som-bestandsdelar-i-beteendet-med-egna-mappningstabeller|beslut 22]]).

Motsvarar Activity i Unified Modeling Language (UML) när aktörer i verksamheten utför den, med stegen som Action; tabellen speglar BPMN-tabellen rad för rad. [[0029-klassen-ar-informationsobjektet-tillstandsmaskinen-ar-tillstandsvyn-anvandningsfallet-ar-tjansten-vardemangd-ar-ett-begrepp-och-uml-tas-in-for-lasarnas-skull-utan-tveksamma-rader|Beslut 29]].
