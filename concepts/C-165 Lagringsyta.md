---
id: C-165
term: Lagringsyta
terms:
  - term: Lagringsyta
    language: sv
    status: preferred
    source: concept new
definition: plats där representationer av information förvaras
kind: element-type
associative:
  - concept: '[[C-071 Applikation]]'
    label: tillhandahålls av
---
# C-165 Lagringsyta

**Definition:** plats där representationer av information förvaras

## Anmärkning

Lagringsytan är stället, inte formen. En representation ([[C-085 Representation]]) ligger på en lagringsyta, och samma fil flyttad till en annan mapp är samma representation på en ny lagringsyta. Behörighet, säkerhetskopiering och var uppgifterna fysiskt finns hör till lagringsytan; format och läsbarhet hör till representationen. Typen hör till applikationsperspektivet. Det är lagringsytan kartläggningens fråga "var lagras informationen" frågar efter.

En applikation ([[C-071 Applikation]]) tillhandahåller en digital lagringsyta, och den fysiska databäraren under den är en artefakt ([[C-081 Artefakt]]). Ett pappersarkiv eller ett skåp är en lagringsyta utan applikation, en fysisk plats. Så får frågan var handlingen förvaras samma svar för pappersakten som för mappen i ärendesystemet ([[0031-handlingen-ar-representationen-allman-handling-och-gallring-ar-begrepp-forteckningarna-bor-utanfor-lagret-och-lagringsytan-far-vara-fysisk|beslut 31]]). Lagringsytan klassas inte själv. Vad den måste klara läses fram ur objekten som ligger där och ur beteendena som når den, i fyra delar. Lagringsytan aggregerar ([[C-100 aggregerar]]) de representationer som ligger på den: en icke-exklusiv del, eftersom samma representation kan ligga på flera ytor och ytan finns kvar när den tas bort.

Ärendeakten som plats, ärendets mapp i ärendesystemet, är en lagringsyta. Det handläggningen hanterar är verksamhetsobjektet ([[C-159 Verksamhetsobjekt]]), och pappersakten som bär information är en representation. Diariet är en lagringsyta, och diarieposten, datum, diarienummer, avsändare och vad handlingen rör, är ett informationsobjekt ([[C-060 Informationsobjekt]]) vars representation ligger där. Diarienumret är ärendets identifierande uppgift ([[0031-handlingen-ar-representationen-allman-handling-och-gallring-ar-begrepp-forteckningarna-bor-utanfor-lagret-och-lagringsytan-far-vara-fysisk|beslut 31]]).

Lagringsytans krav läses fram i fyra delar:

- Konfidentialitet och riktighet: det högst klassade informationsobjektet på ytan gäller. Datalagret hos Myndigheten för föreningsstöd måste klara nivån för Företrädare så länge kopian ligger där.
- Tillgänglighet och spårbarhet: det strängaste kravet gäller bland de beteenden som når objektet på just den ytan. Datalagret får analysfunktionens vecka. Föreningsregistret får dagen från Pröva en ansökan.
- Mängden: många likadana uppgifter höjer ytans krav. De höjer aldrig objektets klass.
- Kopplingen: det som går att räkna ut ur objekten på ytan höjer ytans krav. Inget objekt höjs för det.

Lagret räknar ingenting. Nivåerna står i organisationens förteckningar, och den som går igenom kartan läser ihop dem med kartan. [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|Beslut 58]].

Tillgängligheten läses i två mått: hur länge beteendet klarar sig utan objektet, och hur mycket av objektet som får gå förlorat. I båda måtten gäller det strängaste kravet bland de beteenden som når objektet på ytan. Till tillgängligheten kommer återställningstiden: hur fort lagringsytan måste vara i bruk igen. Återställningstiden är ett krav ([[C-021 Krav]]) på lagringsytan. Den härleds ur kontinuitetskravet på de beteenden som använder ytan. Har beteendet en reservrutin, som säger hur det utförs när en resurs är borta, klarar det sig längre utan ytan. Återställningstiden blir då längre. När flera beteenden använder samma yta gäller den kortaste tiden. [[0061-kontinuitet-ar-ett-krav-pa-hela-beteendet-tillgangligheten-far-tva-matt-och-aterstallningstiden-harleds-till-resursen|Beslut 61]].

En reservrutin kan skapa en ny lagringsyta. Anta att teknisk chef hos bostadsbolaget beslutar att varje områdeskontor har en utskriven jourlista med hyresgästernas telefonnummer. Jourlistan är en representation av Hyresgäst på en ny lagringsyta, pärmen på kontoret. Pärmen måste klara konfidentialiteten för Hyresgäst. Kartan visar pärmen först när den finns. [[0061-kontinuitet-ar-ett-krav-pa-hela-beteendet-tillgangligheten-far-tva-matt-och-aterstallningstiden-harleds-till-resursen|Beslut 61]].

Lagret visar vilka beteenden som når ytan. Ett verksamhetsbeteende ([[C-157 Verksamhetsbeteende]]) ritas med har åtkomst till ([[C-101 har åtkomst till]]) direkt till lagringsytan. Anta att bostadsbolaget har pärmen med jourlistan på områdeskontoret. Åtgärda en felanmälan har då åtkomst till pärmen. Hos Myndigheten för föreningsstöd har analysfunktionen åtkomst till datalagret. Beteendet når ett objekt på ytan när tre saker gäller: beteendet har åtkomst till objektet, beteendet har åtkomst till ytan, och en representation av objektet ligger på ytan. Når ett beteende två ytor som båda rymmer objektet, får båda ytorna beteendets krav. [[0062-beteendet-far-ha-atkomst-direkt-till-lagringsytan-och-kartan-visar-da-vilka-beteenden-som-nar-varje-yta|Beslut 62]].

Harmoniserad data är representationer på en lagringsyta som är ordnade för fler frågor än en. Tre saker gäller för dem: varje objekt hålls helt, varje objekt följer den definition dess ägare har gett det, och objekten går att koppla ihop. Harmoniserad är alltså en egenskap hos representationerna på ytan. Det är inget eget slags informationsobjekt ([[C-060 Informationsobjekt]]) och ingen datakategori ([[C-201 Datakategori]]). Ansökan i datalagret hos Myndigheten för föreningsstöd är samma Ansökan som i Ärendesystemet, i formen ansökningstabellen. Tabellen med Förening är inte harmoniserad än. Datalagret hämtar den ur Ärendesystemet, och antalet medlemmar skiljer sig ibland från Föreningsregistret, som är källan.

Harmoniserad data har ett syfte, och syftet är brett: vanligen uppföljning av verksamheten. En sammanställning ([[C-162 Sammanställning]]) har ett smalare ändamål, som väljer ut uppgifterna. Utbetalningar per kommun rymmer bara de uppgifter som den frågan behöver, medan ansökningstabellen rymmer hela Ansökan. Patientdatalagen räknar upp det breda ändamålet ordagrant: "administration, planering, uppföljning, utvärdering och tillsyn av verksamheten" (2 kap. 4 §). För en statlig myndighet står skyldigheten bakom i myndighetsförordningen. Ledningen ska se till att verksamheten "bedrivs effektivt" och att den "redovisas på ett tillförlitligt och rättvisande sätt" (3 §).

Det breda syftet räcker för frågor som ingen har ställt än, men det ger ingen rätt att läsa in allt. Personuppgifter ska vara "adekvata, relevanta och inte för omfattande i förhållande till de ändamål för vilka de behandlas" (dataskyddsförordningen, artikel 5.1 c). En kopia av Företrädare i datalagret behöver därför ett behov i uppföljningen nu, inte ett som kan komma. Kravet på att bevara ärendena är inget skäl att hålla kopian. Myndigheten bevarar ärendena i källan, och datalagret är inget arkiv. [[0068-en-kopierad-representation-ger-ingen-ny-handlingstyp-men-innehall-i-ny-form-med-nytt-syfte-i-ett-annat-beteende-gor-det|Beslut 68]] och [[0072-harmoniserad-data-ar-en-egenskap-hos-representationerna-pa-en-lagringsyta-och-inget-begrepp-syftet-ar-uppfoljning-av-verksamheten-och-dataharmonisering-ar-en-del-av-formagan-som-behover-den|72]].

Åtgärderna som uppfyller kraven på ytan, och vilken klass eller vilket krav var och en tjänar, står i [[C-166 Informationstillgång]]. De skiljer sig från representationens åtgärder ([[C-085 Representation]]).

## Motsvarigheter

CMMN:s CaseFile är det handläggningen hanterar, verksamhetsobjektet ([[C-159 Verksamhetsobjekt]]).

SDMN:s Folder, en mapp i ett dokumentsystem som rymmer dokument och andra mappar, är en lagringsyta, och dess Containment är relationen aggregerar ([[C-100 aggregerar]]) ([[0024-tillstand-ar-en-elementtyp-uppgiften-ar-informationsmodellens-attribut-och-lagret-ar-den-delade-datamodell-sdmn-beskriver|beslut 24]]).

Motsvarar DataStoreNode i Unified Modeling Language (UML). [[0029-klassen-ar-informationsobjektet-tillstandsmaskinen-ar-tillstandsvyn-anvandningsfallet-ar-tjansten-vardemangd-ar-ett-begrepp-och-uml-tas-in-for-lasarnas-skull-utan-tveksamma-rader|Beslut 29]].

## Exempel

en enhets grupprum i SharePoint, diariet i Ärendesystemet, en brevlåda i Outlook.
