---
id: C-165
term: Lagringsyta
terms:
  - term: Lagringsyta
    language: sv
    status: preferred
    source: concept new
definition: plats som en applikation tillhandahåller och där representationer av information förvaras
kind: element-type
associative:
  - concept: '[[C-071 Applikation]]'
    label: tillhandahålls av
---
# C-165 Lagringsyta

## Anmärkning

Typ i applikationsperspektivet. Lagringsytan är stället, inte formen: en representation ([[C-085 Representation]]) ligger på en lagringsyta, och samma fil flyttad till en annan mapp är samma representation på en ny lagringsyta. Behörighet, säkerhetskopiering och var uppgifterna fysiskt finns hör till lagringsytan; format och läsbarhet hör till representationen. Lagringsytan tillhandahålls av en applikation ([[C-071 Applikation]]); den fysiska databäraren under den är en artefakt ([[C-081 Artefakt]]). Det är lagringsytan kartläggningens fråga "var lagras informationen" frågar efter. Lagringsytan klassas inte själv: den får kravet av det högst klassade informationsobjektet som ligger där ([[C-166 Informationstillgång]]). Lagringsytan aggregerar ([[C-100 aggregerar]]) de representationer som ligger på den: en icke-exklusiv del, eftersom samma representation kan ligga på flera ytor och ytan finns kvar när den tas bort. SDMN:s Folder, en mapp i ett dokumentsystem som rymmer dokument och andra mappar, är en lagringsyta, och dess Containment är den relationen (ADR 0024).

## Exempel

en enhets grupprum i SharePoint, diariet i Ärendesystemet, en brevlåda i Outlook.
