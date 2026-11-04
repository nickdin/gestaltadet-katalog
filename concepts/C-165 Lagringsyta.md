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

En applikation ([[C-071 Applikation]]) tillhandahåller en digital lagringsyta, och den fysiska databäraren under den är en artefakt ([[C-081 Artefakt]]). Ett pappersarkiv eller ett skåp är en lagringsyta utan applikation, en fysisk plats. Så får frågan var handlingen förvaras samma svar för pappersakten som för mappen i ärendesystemet (ADR 0031). Lagringsytan klassas inte själv: den får kravet av det högst klassade informationsobjektet som ligger där ([[C-166 Informationstillgång]]). Lagringsytan aggregerar ([[C-100 aggregerar]]) de representationer som ligger på den: en icke-exklusiv del, eftersom samma representation kan ligga på flera ytor och ytan finns kvar när den tas bort. SDMN:s Folder, en mapp i ett dokumentsystem som rymmer dokument och andra mappar, är en lagringsyta, och dess Containment är den relationen (ADR 0024).

Ärendeakten som plats, ärendets mapp i ärendesystemet, är en lagringsyta. Det handläggningen hanterar, CMMN:s CaseFile, är verksamhetsobjektet ([[C-159 Verksamhetsobjekt]]), och pappersakten som bär information är en representation. Diariet är en lagringsyta, och diarieposten, datum, diarienummer, avsändare och vad handlingen rör, är ett informationsobjekt ([[C-060 Informationsobjekt]]) vars representation ligger där. Diarienumret är ärendets identifierande uppgift (ADR 0031).

Motsvarar DataStoreNode i Unified Modeling Language (UML). ADR 0029.

## Exempel

en enhets grupprum i SharePoint, diariet i Ärendesystemet, en brevlåda i Outlook.
