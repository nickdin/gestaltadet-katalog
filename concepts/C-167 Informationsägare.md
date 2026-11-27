---
id: C-167
term: Informationsägare
terms:
  - term: Informationsägare
    language: sv
    status: preferred
    source: concept new
definition: roll som ansvarar för ett informationsobjekt och beslutar hur det klassas och får behandlas
kind: element-type
generic: '[[C-074 Roll]]'
associative:
  - concept: '[[C-060 Informationsobjekt]]'
    label: ansvarar för
---
# C-167 Informationsägare

**Definition:** roll som ansvarar för ett informationsobjekt och beslutar hur det klassas och får behandlas

## Anmärkning

Informationsägaren äger informationsobjektet ([[C-060 Informationsobjekt]]) som typ: strukturen, klassen och besluten om vad som får göras med det. Processägaren ([[C-206 Processägare]]) äger beteendet som behandlar objektet, och linjechefen ([[C-207 Linjechef]]) svarar för förekomsterna, de faktiska uppgifterna. Riktighetskravet är informationsägarens genom klassen, kontrollen i beteendet processägarens och att uppgiften stämmer linjens. Ägarskapet skrivs med ansvarar för ([[C-208 ansvarar för]]) från rollen till objektet.

Utgångsläget är att informationsägaren är processägaren för objektets hem, det beteende där förekomsterna skapas ([[0030-informationsomradet-ar-ett-begrepp-utan-elementtyp-ett-informationsobjekt-som-bestar-av-sina-objekt-varje-objekt-har-ett-hem-och-nivan-far-vara-grov|beslut 30]]). Den som tar in eller skapar informationen sätter därför ramarna: klassen på objektet och ändamålet ([[C-163 Behandlingsändamål]]) på den insamlande behandlingen. Ett annat beteende som vill använda objektet behöver ägarens ja och sitt eget ändamål. En utsedd informationsägare som inte är hemmets processägare är undantaget, och regel för resursdata ([[C-202 Resursdata]]), som används brett. En myndighets anvisningar för informationsklassning ger ofta enhetscheferna rollen. De ansvarar för klassningen, utser dem som beskriver informationen och fastställer klassningen genom beslut, som ses över minst årligen.

Informationsägaren svarar för objektet inför ägaren till lösningen ([[C-055 Lösning]]) där objektet skapas. Det gäller också en utsedd informationsägare. Är Hyresgäst fel klassad vänder sig vd till uthyrningschefen som ägare till lösningen där Hyresgäst skapas. Där är uthyrningschefen också informationsägare, så de två leden syns först när rollerna skiljs åt. Definitionen säger därför ansvarar och inte ytterst ansvarar.

Klassen är konfidentialitet och riktighet. Informationsägaren sätter båda på objektet, och de är desamma i varje beteende som använder det. Skadan om hyresgästens namn och telefonnummer läcker är densamma hos uthyrningen som hos bovärden. Tre saker skiljer sig mellan beteendena. Den första är ändamålet, alltså vad beteendet får göra med objektet. Den andra är kraven på tillgänglighet och spårbarhet, som processägaren ställer för sin behandling. Den tredje är det beteendet självt skapar, som är ett eget objekt med egen klass. En lösning som får objektet från en annan lösning följer informationsägarens beslut som användare. Felanmälan får Hyresgäst från uthyrningschefens lösning, och teknisk chef håller sig till uthyrningschefens beslut om vad bovärdarna får se. Informationsägaren beslutar om sitt objekt och aldrig om den andra lösningen. Vill teknisk chef att bovärdarna ska se mer än uthyrningschefen tillåter avgör vd, som gav båda deras mandat. [[0057-en-agarroll-svarar-infor-en-losnings-agare-ordet-ytterst-stryks-ur-tre-definitioner-och-klassen-ar-densamma-i-varje-beteende|Beslut 57]] och [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|58]].

Klassen står i organisationens klassningsförteckning, som pekar på objektet i lagret. Lagret visar vem som är informationsägare, aldrig vad hen har beslutat. Riktigheten sätter informationsägaren efter den användning som tål minst fel. Ett fel i Kontonummer skickar pengarna till fel konto i Genomföra ansökningsomgången, och kopiorna ärver felet från källan. [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|Beslut 58]].

Informationsägaren klassar utan att känna den framtida användningen. Anta att en ny lösning hos bostadsbolaget om ett år vill skicka hyresavier som sms. Konfidentialiteten håller för all användning, och den nya lösningens processägare ställer sina egna krav på tillgänglighet och spårbarhet. Bara riktigheten kan behöva prövas om: avierna tål färre fel i telefonnumret än uthyrningen gör. Den nya lösningen ställer då ett krav ([[C-021 Krav]]) på uthyrningschefen, som beslutar om nivån höjs. [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|Beslut 58]].

Ägarskapet följer informationsobjektet, inte lagringsytan ([[C-165 Lagringsyta]]) eller applikationen ([[C-071 Applikation]]). Att en enhets uppgifter ligger i ett gemensamt system gör inte systemets objektansvarige till informationsägare. Den som hämtar en annans sammanställning och skickar den vidare blir inte ägare av det. En sammanställning ([[C-162 Sammanställning]]) som gjorts ur en annans informationsobjekt ägs av processägaren för det beteende som upprättade den, om inget annat beslutats ([[0035-processagaren-ar-en-roll-linjechefen-ett-begrepp-agandet-skrivs-med-ansvarar-for-typerna-ags-och-forekomsterna-svarar-linjen-for-och-styrobjekten-ags-genom-mandat|beslut 35]]). Ägaren till ett informationsområde ([[C-198 Informationsområde]]) är ägare till varje objekt i området som saknar egen; härledningen läses ur lagret och kopieras aldrig ([[0030-informationsomradet-ar-ett-begrepp-utan-elementtyp-ett-informationsobjekt-som-bestar-av-sina-objekt-varje-objekt-har-ett-hem-och-nivan-far-vara-grov|beslut 30]]).

Typ i verksamhetsperspektivet, en typ av roll ([[C-074 Roll]]). [[0035-processagaren-ar-en-roll-linjechefen-ett-begrepp-agandet-skrivs-med-ansvarar-for-typerna-ags-och-forekomsterna-svarar-linjen-for-och-styrobjekten-ags-genom-mandat|Beslut 35]].

## Exempel

chefen för Bidragsenheten för Ansökan, Villkorsbedömning, Bidragsberäkning, Beslut om bidrag, Utbetalning, Återkrav, Beslut om återkrav och Redovisning; uthyrningschefen i bostadsbolaget för Hyresgäst, Hyresavtal och Hyresfordran.
