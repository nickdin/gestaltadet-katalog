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

Förmågan är inget styrobjekt ([[C-003 Styrobjekt]]), men någon ansvarar för den ([[C-209 Ansvar]]). Det är ägaren till den innersta verksamhetsdomän ([[C-008 Verksamhetsdomän]]) som rymmer alla lösningar som realiserar förmågan. Ägaren ansvarar för förmågans delar och helhet: hur den är skuren och vad den ska klara. Samma ägare håller domänens portfölj ([[C-011 Portfölj]]) och sätter förmågans mål. Chefen för Bidragsenheten ansvarar för Bidragsprövning. Har Bidragsprövning två lösningar hos två enhetschefer ansvarar generaldirektören, som sätter målet och fördelar det på de två lösningsägarna. Hamnar ansvaret hos högsta ledningen syns det att förmågan är delad på flera domäner. Ansvaret följer av var lösningarna hör hemma, och ingen ritar det i lagret. Beslut 65 och 66.

Förmågans mål säger vad utformningen ska klara, inte vad som blev gjort. Bidragsprövning ska klara ett beslut inom tre månader med normal bemanning. Att nio av tio ansökningar är beslutade i tid är domänens mål för produktionen. Tar chefen in två handläggare till når domänen sitt mål, men förmågan är densamma. Förmågan blir bättre först när utformningen ändras. Det gör ett initiativ ([[C-012 Initiativ]]) eller en ändring inom lösningens ram.

Provet för en förmåga: portföljens ägare kan sätta ett eget mål för den och veta när det är nått, utan att ändra målen för förmågorna bredvid. Beräkning av bidrag klarar provet. Generaldirektören kan kräva högst ett felräknat belopp på hundra beslut, vem eller vad som än räknar. Fördelning av ansökningar på handläggare klarar det inte. Ingen vill ha en bättre fördelning för dess egen skull, och delen försvinner om ansökningarna läggs i en gemensam kö. Den är en verksamhetsaktivitet ([[C-175 Verksamhetsaktivitet]]). Beslut 65.

Förmågan har ingen relation till informationen. Den information som hör till förmågan läses genom lösningen som realiserar den och de informationsområden ([[C-198 Informationsområde]]) lösningen aggregerar. Ett informationsområde hör hemma i förmågan där dess förekomster skapas; andra förmågor har beroenden till det, lästa ur sina lösningar och beteenden. Beslut 30.

Namnet säger att förmågan är verksamhetens; typen hör till strategiperspektivet.

## Motsvarigheter

ArchiMates Capability hör till strategilagret, utanför den kärna mappningstabellen för ArchiMate täcker; se unmapped-concepts.

Business Architecture Core Metamodel (BACM) definierar Capability på samma sätt: förmågan att producera ett utfall utan att säga hur. Dess CapabilityBehavior är det verksamhetsbeteende som realiserar förmågan, och dess CapabilityImplementation är lösningen. En värdeström ([[C-190 Värdeström]]) använder ([[C-095 använder]]) de förmågor dess steg förutsätter: förmågan är en möjlighet, det som pågår i steget är processen. Beslut 27.

Value Delivery Modeling Language (VDML) delar förmågan i tre. CapabilityDefinition, förmågan som sort, är verksamhetsförmågan. CapabilityOffer, en organisationsenhets förmåga med sina resurser, är lösningen ([[C-055 Lösning]]). CapabilityLibrary, samlingen av alla, är förmågekartan, en arkitekturvy och inget element. Beslut 28.
