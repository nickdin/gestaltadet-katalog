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

Ett begrepp, ingen elementtyp: ett informationsområde registreras som ett informationsobjekt ([[C-060 Informationsobjekt]]) som består av ([[C-062 består av]]) de informationsobjekt det samlar, och relationen visar att det är ett område. Varje informationsobjekt hör hemma i exakt ett område, det där förekomsterna skapas. Att en annan förmåga använder objektet är ett beroende, inte ett andra hem, och beroendet läses ur lagret: det beteende som har åtkomst till ([[C-101 har åtkomst till]]) objektet, och den lösning ([[C-055 Lösning]]) som aggregerar ([[C-100 aggregerar]]) området som en av sina komponenter. Förmågan ([[C-069 Verksamhetsförmåga]]) själv har ingen relation till informationen; förmågan är en möjlighet, lösningen gör och använder.

Området är den nivå informationsmodellen börjar på och den enhet ägaren och analysen arbetar med. Nivån får vara grov: dag ett kan ett område vara ett enda informationsobjekt med en ägare och en klass, och det förfinas genom att nya objekt läggs under det, aldrig genom att det delas. Informationsägaren ([[C-167 Informationsägare]]) och klassen ärvs nedåt som härledning till varje objekt som saknar egen; ett objekt med egen ägare eller egen klass behåller den.

Så dras gränsen, informationsmodelleringens praxis: en stark central entitet motiverar området; objekt som inte kan leva utan varandra, hänger ihop i en transaktion eller har samma livscykel ligger i samma område; en relation mellan två objekt hör till området med många-änden. Grupperingen är ett varv till över modellen, med ett nytt perspektiv. För allmänna områden, för grova områden, och två förmågor som båda skapar förekomster av samma objekt är fel i grupperingen, inte lägen att registrera.

Skillnaden mot sammanställningen ([[C-162 Sammanställning]]): sammanställningen sätts samman av uppgifter ur andra objekt för en behandlings ändamål och har representationer ([[C-085 Representation]]), en lista man kan skicka; området samlar hela objekt och har ingen egen representation. Får området en representation har det blivit en sammanställning eller ett vanligt objekt.

Ritas som en ram runt sina objekt, med relationerna mellan objekten som linjer; en ruta inuti ramen läses som att området består av rutan. Beslutet: ADR 0030.

## Exempel

Bidragsinformation hos myndigheten, med Ansökan, Redovisning, Beslut, Utbetalning och Återkrav under chefen för Bidragsenheten; Föreningsinformation, med Förening, Företrädare och Kontonummer, där Kontonummer hör hemma fast utbetalningen använder det; Fastighetsinformation hos bostadsbolaget, med Fastighet, Byggnad, Lägenhet, Lokal och Mätvärde, som uthyrningen använder för debitering men inte äger. Förteckningen över alla företrädare är inget informationsområde utan en sammanställning.
