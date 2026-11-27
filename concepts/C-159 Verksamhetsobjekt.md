---
id: C-159
term: Verksamhetsobjekt
terms:
  - term: Verksamhetsobjekt
    language: sv
    status: preferred
    source: concept new
definition: det en verksamhetsprocess, en handläggning eller en verksamhetsfunktion hanterar och lämnar vidare
kind: element-type
associative:
  - concept: '[[C-060 Informationsobjekt]]'
    label: realiseras av
---
# C-159 Verksamhetsobjekt

**Definition:** det en verksamhetsprocess, en handläggning eller en verksamhetsfunktion hanterar och lämnar vidare

## Anmärkning

Verksamhetsobjektet är flödesobjektet i ett verksamhetsbeteende ([[C-157 Verksamhetsbeteende]]), oavsett om det blir en produkt. Det verksamhetsobjekt ett beteende lämnar ifrån sig, till någon utanför beteendet självt, är beteendets resultat ([[0045-resultatet-ar-verksamhetsobjektet-ett-beteende-lamnar-ifran-sig-produkten-ar-erbjudandet-vid-losningens-grans-och-ett-resultat-kan-sakna-produkt|beslut 45]]). Ett verksamhetsobjekt realiseras av ett eller flera informationsobjekt ([[C-060 Informationsobjekt]]), som är informationsperspektivets sida av samma sak. En produkt ([[C-014 Produkt]]) aggregerar de verksamhetsobjekt mottagaren får. Ärendebeslutet ([[C-181 Ärendebeslut]]) är det verksamhetsobjekt en handläggning fattar och lämnar vidare.

Ett beteende når ett verksamhetsobjekt med relationen har åtkomst till ([[C-101 har åtkomst till]]). Att objektet lämnas vidare till nästa beteende lagras inte som flödar till ([[C-097 flödar till]]). Pilen härleds ur att det ena beteendet skriver och det andra läser ([[0014-processerna-ar-organisationens-och-kartan-delas-per-process|beslut 14]], [[0033-flodet-mellan-tva-beteenden-harleds-ur-atkomsten-flodar-till-ar-for-det-som-inte-ar-ett-element-och-de-frammande-flodena-som-bar-ett-element-ar-atkomstparet|beslut 33]]). Beteendet som har åtkomst till verksamhetsobjektet har därmed åtkomst till de informationsobjekt som realiserar det, ett steg, härlett och inte ritat. Pröva en ansökan har åtkomst till Ärende och når så Ansökan och Förening. Åtkomst direkt till ett informationsobjekt ritas bara där den inte följer av verksamhetsobjektet, och den följer inte aggregerar ([[C-100 aggregerar]]) ([[0034-beteendet-nar-informationsobjektet-genom-verksamhetsobjektet-och-direkt-atkomsten-foljer-realiseras-av-men-inte-aggregerar|beslut 34]]).

Ett verksamhetsobjekt består av ([[C-062 består av]]) sina tillstånd ([[C-182 Tillstånd]]), de lägen beteendet för det igenom. Tillstånden ritas i en tillståndsvy per objekt, och informationsobjektet bär tillståndet som en uppgift. En fysisk sak processen hanterar utan informationssida är ett verksamhetsobjekt; bär den information, den utskrivna blanketten, är den en representation ([[C-085 Representation]]).

## Motsvarigheter

Motsvarar ArchiMates Business Object. [[0016-verksamhetsobjekt-ar-en-elementtyp|Beslut 16]]; ärendebeslutet [[0022-aktivitet-och-beslutslogik-ar-elementtyper-bpmn-cmmn-och-dmn-tas-in-som-bestandsdelar-i-beteendet-med-egna-mappningstabeller|beslut 22]]; tillståndet som elementtyp och SDMN [[0024-tillstand-ar-en-elementtyp-uppgiften-ar-informationsmodellens-attribut-och-lagret-ar-den-delade-datamodell-sdmn-beskriver|beslut 24]].

Motsvarar BusinessObject i Business Architecture Core Metamodel (BACM). Lagret drar gränsen mot informationsobjektet efter roll: vad beteendet hanterar mot vad verksamheten håller som information. BACM drar den efter påtaglighet, så ett ärende är ett verksamhetsobjekt här och en InformationItem där. En vara ([[C-191 Vara]]) är ett verksamhetsobjekt som lämnas över till mottagaren. [[0027-vardestrom-ar-en-elementtyp-i-strategiperspektivet-utfallet-ar-tillstandet-losningen-ar-formagans-implementation-och-bacm-tas-in-med-hinder-vinst-och-svar-som-begrepp-i-texten|Beslut 27]].

BPMN:s dataobjekt och CMMN:s ärendeakt (CaseFile, CaseFileItem) är verksamhetsobjekt. [[0016-verksamhetsobjekt-ar-en-elementtyp|Beslut 16]]; ärendebeslutet [[0022-aktivitet-och-beslutslogik-ar-elementtyper-bpmn-cmmn-och-dmn-tas-in-som-bestandsdelar-i-beteendet-med-egna-mappningstabeller|beslut 22]]; tillståndet som elementtyp och SDMN [[0024-tillstand-ar-en-elementtyp-uppgiften-ar-informationsmodellens-attribut-och-lagret-ar-den-delade-datamodell-sdmn-beskriver|beslut 24]].

SDMN:s Physical är en fysisk sak processen hanterar utan informationssida. [[0024-tillstand-ar-en-elementtyp-uppgiften-ar-informationsmodellens-attribut-och-lagret-ar-den-delade-datamodell-sdmn-beskriver|Beslut 24]].

I Unified Modeling Language (UML) är verksamhetsobjektet aktivitetsdiagrammets objekt (ObjectNode, Pin), det som flödar mellan två element (InformationItem) och den klass vars tillståndsmaskin ritas. Klassen i klassdiagrammet är informationsobjektet som realiserar det. [[0029-klassen-ar-informationsobjektet-tillstandsmaskinen-ar-tillstandsvyn-anvandningsfallet-ar-tjansten-vardemangd-ar-ett-begrepp-och-uml-tas-in-for-lasarnas-skull-utan-tveksamma-rader|Beslut 29]].

Motsvarar BusinessItem i Value Delivery Modeling Language (VDML): allt som kan skapas eller skaffas och bär information, förpliktelse eller värde. Det som används upp eller lånas i en aktivitet är en resurs ([[C-122 Resurs]]). [[0028-varde-ar-en-elementtyp-i-strategiperspektivet-dit-vardeerbjudandet-flyttar-arbetssatt-ar-ett-begrepp-svaret-heter-hjalp-och-vdml-tas-in-med-rakneverket-omappat|Beslut 28]].

## Exempel

ett ärende, ett ärendebeslut, ett initiativ, en utgiftsprognos, verksamhetsplanen, en analysrapport.
