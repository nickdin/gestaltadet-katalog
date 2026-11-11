---
id: C-069
term: Verksamhetsförmåga
terms:
  - term: Verksamhetsförmåga
    language: sv
    source: catalogue
definition: "vad verksamheten kan göra, oberoende av hur och av vem det utförs"
kind: element-type
---
# C-069 Verksamhetsförmåga

**Definition:** vad verksamheten kan göra, oberoende av hur och av vem det utförs

## Anmärkning

En förmåga är något verksamheten kan. Den kan realiseras på flera sätt och finns kvar när lösningen byts. En förmåga är en möjlighet, inte något som pågår: den realiseras av verksamhetsbeteenden ([[C-157 Verksamhetsbeteende]]), processer, handläggningar och funktioner. Ett löpande ansvar är därför en verksamhetsfunktion ([[C-158 Verksamhetsfunktion]]), inte en förmåga. Förmågor namnges med substantiv: Analys, Säkerhetsrådgivning, Verksamhetsstyrning. Att flera lösningar eller flera organisationsenheter realiserar samma förmåga visar var arbetet är splittrat eller dubblerat.

Målet ([[C-017 Mål]]) sätts på förmågan, ramen på de lösningar ([[C-055 Lösning]]) som realiserar den. En lösning realiserar exakt en förmåga; en förmåga kan ha flera lösningar, och en komponent kan ingå i flera lösningar. Beslut 20.

Förmågan har ingen relation till informationen. Den information som hör till förmågan läses genom lösningen som realiserar den och de informationsområden ([[C-198 Informationsområde]]) lösningen aggregerar. Ett informationsområde hör hemma i förmågan där dess förekomster skapas; andra förmågor har beroenden till det, lästa ur sina lösningar och beteenden. Beslut 30.

Namnet säger att förmågan är verksamhetens; typen hör till strategiperspektivet.

## Motsvarigheter

ArchiMates Capability hör till strategilagret, utanför den kärna mappningstabellen för ArchiMate täcker; se unmapped-concepts.

Business Architecture Core Metamodel (BACM) definierar Capability på samma sätt: förmågan att producera ett utfall utan att säga hur. Dess CapabilityBehavior är det verksamhetsbeteende som realiserar förmågan, och dess CapabilityImplementation är lösningen. En värdeström ([[C-190 Värdeström]]) använder ([[C-095 använder]]) de förmågor dess steg förutsätter: förmågan är en möjlighet, det som pågår i steget är processen. Beslut 27.

Value Delivery Modeling Language (VDML) delar förmågan i tre. CapabilityDefinition, förmågan som sort, är verksamhetsförmågan. CapabilityOffer, en organisationsenhets förmåga med sina resurser, är lösningen ([[C-055 Lösning]]). CapabilityLibrary, samlingen av alla, är förmågekartan, en arkitekturvy och inget element. Beslut 28.
