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

En applikation ([[C-071 Applikation]]) tillhandahåller en digital lagringsyta, och den fysiska databäraren under den är en artefakt ([[C-081 Artefakt]]). Ett pappersarkiv eller ett skåp är en lagringsyta utan applikation, en fysisk plats. Så får frågan var handlingen förvaras samma svar för pappersakten som för mappen i ärendesystemet (beslut 31). Lagringsytan klassas inte själv. Vad den måste klara läses fram ur objekten som ligger där och ur beteendena som når den, i fyra delar. Lagringsytan aggregerar ([[C-100 aggregerar]]) de representationer som ligger på den: en icke-exklusiv del, eftersom samma representation kan ligga på flera ytor och ytan finns kvar när den tas bort.

Ärendeakten som plats, ärendets mapp i ärendesystemet, är en lagringsyta. Det handläggningen hanterar är verksamhetsobjektet ([[C-159 Verksamhetsobjekt]]), och pappersakten som bär information är en representation. Diariet är en lagringsyta, och diarieposten, datum, diarienummer, avsändare och vad handlingen rör, är ett informationsobjekt ([[C-060 Informationsobjekt]]) vars representation ligger där. Diarienumret är ärendets identifierande uppgift (beslut 31).

Lagringsytans krav läses fram i fyra delar:

- Konfidentialitet och riktighet: det högst klassade informationsobjektet på ytan gäller. Datalagret hos Myndigheten för föreningsstöd måste klara nivån för Företrädare så länge kopian ligger där.
- Tillgänglighet och spårbarhet: det strängaste kravet gäller bland de beteenden som når objektet på just den ytan. Datalagret får analysfunktionens vecka. Föreningsregistret får dagen från Pröva en ansökan.
- Mängden: många likadana uppgifter höjer ytans krav. De höjer aldrig objektets klass.
- Kopplingen: det som går att räkna ut ur objekten på ytan höjer ytans krav. Inget objekt höjs för det.

Lagret räknar ingenting. Nivåerna står i organisationens förteckningar, och den som går igenom kartan läser ihop dem med kartan. Beslut 58.

Tillgängligheten läses i två mått: hur länge beteendet klarar sig utan objektet, och hur mycket av objektet som får gå förlorat. I båda måtten gäller det strängaste kravet bland de beteenden som når objektet på ytan. Till tillgängligheten kommer återställningstiden: hur fort lagringsytan måste vara i bruk igen. Återställningstiden är ett krav ([[C-021 Krav]]) på lagringsytan. Den härleds ur kontinuitetskravet på de beteenden som använder ytan. Har beteendet en reservrutin klarar det sig längre utan ytan, och återställningstiden blir längre. När flera beteenden använder samma yta gäller den kortaste tiden. Beslut 61.

En reservrutin kan skapa en ny lagringsyta. Anta att teknisk chef hos bostadsbolaget beslutar att varje områdeskontor har en utskriven jourlista med hyresgästernas telefonnummer. Jourlistan är en representation av Hyresgäst på en ny lagringsyta, pärmen på kontoret. Pärmen måste klara konfidentialiteten för Hyresgäst. Kartan visar pärmen först när den finns. Beslut 61.

Lagret visar vilka beteenden som når ytan. Ett verksamhetsbeteende ([[C-157 Verksamhetsbeteende]]) ritas med har åtkomst till ([[C-101 har åtkomst till]]) direkt till lagringsytan. Åtgärda en felanmälan hos bostadsbolaget har åtkomst till pärmen på områdeskontoret, och analysfunktionen har åtkomst till datalagret. Beteendet når ett objekt på ytan när tre saker gäller: beteendet har åtkomst till objektet, beteendet har åtkomst till ytan, och en representation av objektet ligger på ytan. Når ett beteende två ytor som båda rymmer objektet, får båda ytorna beteendets krav. Beslut 62.

Åtgärderna som uppfyller kraven på ytan, och vilken klass eller vilket krav var och en tjänar, står i [[C-166 Informationstillgång]]. De skiljer sig från representationens åtgärder ([[C-085 Representation]]).

## Motsvarigheter

CMMN:s CaseFile är det handläggningen hanterar, verksamhetsobjektet ([[C-159 Verksamhetsobjekt]]).

SDMN:s Folder, en mapp i ett dokumentsystem som rymmer dokument och andra mappar, är en lagringsyta, och dess Containment är relationen aggregerar ([[C-100 aggregerar]]) (beslut 24).

Motsvarar DataStoreNode i Unified Modeling Language (UML). Beslut 29.

## Exempel

en enhets grupprum i SharePoint, diariet i Ärendesystemet, en brevlåda i Outlook.
