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

Informationsägaren äger informationsobjektet ([[C-060 Informationsobjekt]]) som typ: strukturen, klassen och besluten om vad som får göras med det. Processägaren ([[C-206 Processägare]]) äger beteendet som behandlar objektet, och linjechefen ([[C-207 Linjechef]]) svarar för förekomsterna, de faktiska uppgifterna. Riktighetskravet är informationsägarens genom klassen, kontrollen i beteendet processägarens och att uppgiften stämmer linjens. Ägarskapet skrivs med ansvarar för ([[C-208 ansvarar för]]) från rollen till objektet.

Utgångsläget är att informationsägaren är processägaren för objektets hem, det beteende där förekomsterna skapas (ADR 0030). Den som tar in eller skapar informationen sätter därför ramarna: klassen på objektet och ändamålet ([[C-163 Behandlingsändamål]]) på den insamlande behandlingen. Ett annat beteende som vill använda objektet behöver ägarens ja och sitt eget ändamål. En utsedd informationsägare som inte är hemmets processägare är undantaget, och regel för resursdata ([[C-202 Resursdata]]), som används brett. En myndighets anvisningar för informationsklassning ger ofta enhetscheferna rollen. De är ytterst ansvariga för klassningen, utser dem som beskriver informationen och fastställer klassningen genom beslut, som ses över minst årligen.

Ägarskapet följer informationsobjektet, inte lagringsytan ([[C-165 Lagringsyta]]) eller applikationen ([[C-071 Applikation]]). Att en enhets uppgifter ligger i ett gemensamt system gör inte systemets objektansvarige till informationsägare. Den som hämtar en annans sammanställning och skickar den vidare blir inte ägare av det. En sammanställning ([[C-162 Sammanställning]]) som gjorts ur en annans informationsobjekt ägs av processägaren för det beteende som upprättade den, om inget annat beslutats (ADR 0035). Ägaren till ett informationsområde ([[C-198 Informationsområde]]) är ägare till varje objekt i området som saknar egen; härledningen läses ur lagret och kopieras aldrig (ADR 0030).

Typ i verksamhetsperspektivet, en typ av roll ([[C-074 Roll]]). Beslutet: ADR 0035.

## Exempel

chefen för Bidragsenheten för Ansökan, Redovisning, Beslut, Utbetalning och Återkrav; uthyrningschefen i bostadsbolaget för Hyresgäst, Hyresavtal och Hyresfordran.
