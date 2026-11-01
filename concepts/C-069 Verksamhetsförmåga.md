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

ArchiMates Capability hör till strategilagret, utanför den kärna mappningstabellen för ArchiMate täcker; se unmapped-concepts. Namnet säger att förmågan är verksamhetens; typen hör till strategiperspektivet. En förmåga är något verksamheten kan; den kan realiseras på flera sätt och finns kvar när lösningen byts. En förmåga är en möjlighet, inte något som pågår: den realiseras av verksamhetsbeteenden ([[C-157 Verksamhetsbeteende]]), processer, handläggningar och funktioner. Ett löpande ansvar är därför en verksamhetsfunktion ([[C-158 Verksamhetsfunktion]]), inte en förmåga. Förmågor namnges med substantiv: Analys, Säkerhetsrådgivning, Verksamhetsstyrning. Att samma förmåga realiseras av flera lösningar eller i flera organisationsenheter visar var arbetet är splittrat eller dubblerat.

Målet ([[C-017 Mål]]) sätts på förmågan, ramen på de lösningar ([[C-055 Lösning]]) som realiserar den. En lösning realiserar exakt en förmåga; en förmåga kan ha flera lösningar, och en komponent kan ingå i flera lösningar. ADR 0020.

Business Architecture Core Metamodel (BACM) definierar Capability på samma sätt, förmågan att producera ett utfall utan att säga hur; dess CapabilityBehavior är det verksamhetsbeteende som realiserar förmågan och dess CapabilityImplementation är lösningen. En värdeström ([[C-190 Värdeström]]) använder ([[C-095 använder]]) de förmågor dess steg förutsätter: förmågan är en möjlighet, det som pågår i steget är processen. ADR 0027.
