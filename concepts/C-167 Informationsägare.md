---
id: C-167
term: Informationsägare
terms:
  - term: Informationsägare
    language: sv
    status: preferred
    source: concept new
definition: roll som ytterst ansvarar för ett informationsobjekt och beslutar hur det klassas och får behandlas
kind: element-type
generic: '[[C-074 Roll]]'
associative:
  - concept: '[[C-060 Informationsobjekt]]'
    label: ansvarar för
---
# C-167 Informationsägare

**Definition:** roll som ytterst ansvarar för ett informationsobjekt och beslutar hur det klassas och får behandlas

## Anmärkning

Typ i verksamhetsperspektivet, en typ av roll ([[C-074 Roll]]). En myndighets anvisningar för informationsklassning ger ofta enhetscheferna rollen: de är ytterst ansvariga för klassningen, utser dem som beskriver informationen och fastställer klassningen genom beslut, som ses över minst årligen. Ägarskapet följer informationsobjektet ([[C-060 Informationsobjekt]]), inte lagringsytan ([[C-165 Lagringsyta]]) eller applikationen ([[C-071 Applikation]]): att en enhets uppgifter ligger i ett gemensamt system gör inte systemets objektansvarige till informationsägare, och den som hämtar en annans sammanställning och skickar den vidare blir inte ägare av det. En sammanställning ([[C-162 Sammanställning]]) som gjorts ur en annans informationsobjekt ägs av processägaren för det beteende som upprättade den, om inget annat beslutats (ADR 0035). Ägaren till ett informationsområde ([[C-198 Informationsområde]]) är ägare till varje objekt i området som saknar egen; härledningen läses ur lagret och kopieras aldrig (ADR 0030).

Informationsägaren äger informationsobjektet som typ: strukturen, klassen och besluten om vad som får göras med det. Beteendet som behandlar det äger processägaren ([[C-206 Processägare]]), och förekomsterna, de faktiska uppgifterna, svarar linjechefen ([[C-207 Linjechef]]) för: riktighetskravet är informationsägarens genom klassen, kontrollen i beteendet processägarens och att uppgiften stämmer linjens. Utgångsläget är att informationsägaren är processägaren för objektets hem, det beteende där förekomsterna skapas (ADR 0030); den som tar in eller skapar informationen sätter därför ramarna, klassen på objektet och ändamålet ([[C-163 Behandlingsändamål]]) på den insamlande behandlingen, och ett annat beteende som vill använda objektet behöver ägarens ja och sitt eget ändamål. En utsedd informationsägare som inte är hemmets processägare är undantaget, och regel för resursdata ([[C-202 Resursdata]]), som används brett. Ägarskapet skrivs med ansvarar för ([[C-208 ansvarar för]]) från rollen till objektet. Beslutet: ADR 0035.

## Exempel

chefen för Bidragsenheten för Ansökan, Redovisning, Beslut, Utbetalning och Återkrav; uthyrningschefen i bostadsbolaget för Hyresgäst, Hyresavtal och Hyresfordran.
