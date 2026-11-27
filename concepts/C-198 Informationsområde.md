---
id: C-198
term: Informationsområde
terms:
  - term: Informationsområde
    language: sv
    status: preferred
    source: concept new
  - term: informationsgrupp
    language: sv
    source: concept change
    status: admitted
  - term: ämnesområde
    language: sv
    source: concept change
    status: admitted
definition: informationsobjekt som samlar de informationsobjekt som hör ihop och vars förekomster skapas i samma verksamhetsförmåga
generic: '[[C-060 Informationsobjekt]]'
associative:
  - concept: '[[C-069 Verksamhetsförmåga]]'
    label: hör hemma i
---
# C-198 Informationsområde

**Definition:** informationsobjekt som samlar de informationsobjekt som hör ihop och vars förekomster skapas i samma verksamhetsförmåga

## Anmärkning

Varje informationsobjekt hör hemma i exakt ett område, det där förekomsterna skapas. Att en annan förmåga använder objektet är ett beroende, inte ett andra hem. Beroendet läses ur lagret: det beteende som har åtkomst till ([[C-101 har åtkomst till]]) objektet, och den lösning ([[C-055 Lösning]]) som aggregerar ([[C-100 aggregerar]]) området som en av sina komponenter. Förmågan ([[C-069 Verksamhetsförmåga]]) själv har ingen relation till informationen: förmågan är en möjlighet, lösningen gör och använder.

Området är den nivå informationsmodellen börjar på och den enhet ägaren och analysen arbetar med. Nivån får vara grov. Dag ett kan ett område vara ett enda informationsobjekt med en ägare och en rad i klassningsförteckningen; det förfinas genom att nya objekt läggs under det. Ett område delas bara när dess förmåga delas. Bidragsprövning hos Myndigheten för föreningsstöd har två delar, och Bidragsinformation består därför av två områden: Bedömningsinformation och Beräkningsinformation. Har en förmåga delar ligger varje hem i en del, aldrig i helheten. Området för helheten får stå kvar och bära ägaren och raden i klassningsförteckningen. [[0071-ett-informationsomrade-delas-nar-dess-formaga-delas-hemmet-ligger-da-alltid-i-en-del-och-beslutet-om-bidrag-skapas-i-bedomningen|Beslut 71]]. Informationsägaren ([[C-167 Informationsägare]]) ärvs nedåt som härledning till varje objekt som saknar egen; ett objekt med egen ägare behåller den.

Klassen står inte i lagret. Den når objektet genom klassningsförteckningen: objektet har en egen rad, eller så gäller raden för dess område. Ett objekt med egen rad behåller den. Området bär också informationsägarens beslut om grundnivån till de objekt som saknar egen rad. Grundnivån är den nivå i en klass som organisationen har beslutat ska gälla det mesta. Chefen för Bidragsenheten säger att grundnivån räcker för Utbetalningsinformation, och Utbetalning får konfidentialiteten därifrån. Organisationen ger ingenting nedåt till ett objekt som helt saknar rad. Området skymmer inte heller det som avviker: Återkrav ligger i Utbetalningsinformation och är känsligare än Utbetalning. [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|Beslut 58]] och [[0060-grundnivan-i-klassningen-ar-ett-beslut-av-informationsagaren-aldrig-tystnad-och-den-nar-objektet-genom-egen-rad-eller-omradets-rad|60]].

Gränsen dras efter informationsmodelleringens praxis. En stark central entitet motiverar området. Objekt som inte kan leva utan varandra, hänger ihop i en transaktion eller har samma livscykel ligger i samma område. En relation mellan två objekt hör till området med många-änden. Grupperingen är ett varv till över modellen, med ett nytt perspektiv. För allmänna områden, för grova områden, och två förmågor som båda skapar förekomster av samma objekt är fel i grupperingen, inte lägen att registrera.

Skillnaden mot sammanställningen ([[C-162 Sammanställning]]): sammanställningen sätts samman av uppgifter ur andra objekt för en behandlings ändamål och har representationer ([[C-085 Representation]]), en lista man kan skicka. Området samlar hela objekt och har ingen egen representation. Får området en representation har det blivit en sammanställning eller ett vanligt objekt.

Ett begrepp, ingen elementtyp: ett informationsområde registreras som ett informationsobjekt ([[C-060 Informationsobjekt]]) som består av ([[C-062 består av]]) de informationsobjekt det samlar, och relationen visar att det är ett område. Ritas som en ram runt sina objekt, med relationerna mellan objekten som linjer; en ruta inuti ramen läses som att området består av rutan. [[0030-informationsomradet-ar-ett-begrepp-utan-elementtyp-ett-informationsobjekt-som-bestar-av-sina-objekt-varje-objekt-har-ett-hem-och-nivan-far-vara-grov|Beslut 30]]. Ett område har ingen datakategori ([[C-201 Datakategori]]); kategorin sitter på objekten i det ([[0032-datakategorin-ar-ett-begrepp-resursdata-referensdata-transaktionsdata-och-handelsedata-sitter-pa-informationsobjektet-hogst-en-och-frivillig-och-referensdata-ar-en-vardemangd-organisationen-sjalv-faststaller|beslut 32]]).

## Exempel

Bidragsinformation hos myndigheten, under chefen för Bidragsenheten. Den består av två områden, ett för varje del av förmågan Bidragsprövning. Bedömningsinformation rymmer Ansökan, Villkorsbedömning och Beslut om bidrag och hör hemma i Bedömning av rätt till bidrag. Beräkningsinformation rymmer Bidragsberäkning och hör hemma i Beräkning av bidrag. Bara en relation korsar gränsen: beslutet hänvisar till beräkningen för beloppet. Utbetalningsinformation, med Utbetalning, Återkrav, Beslut om återkrav och Redovisning, hör hemma i förmågan Utbetalning och återkrav. Föreningsinformation, med Förening, Företrädare och Kontonummer, där Kontonummer hör hemma fast utbetalningen använder det. Fastighetsinformation hos bostadsbolaget, med Fastighet, Byggnad, Lägenhet, Lokal och Mätvärde, som uthyrningen använder för debitering men inte äger. Förteckningen över alla företrädare är inget informationsområde utan en sammanställning.
