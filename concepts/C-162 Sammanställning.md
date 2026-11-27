---
id: C-162
term: Sammanställning
terms:
  - term: Sammanställning
    language: sv
    status: preferred
    source: concept new
definition: informationsobjekt som satts samman av uppgifter ur ett eller flera andra informationsobjekt för ett bestämt ändamål
generic: '[[C-060 Informationsobjekt]]'
associative:
  - concept: '[[C-161 Uppgift]]'
    label: sätter samman
---
# C-162 Sammanställning

**Definition:** informationsobjekt som satts samman av uppgifter ur ett eller flera andra informationsobjekt för ett bestämt ändamål

## Anmärkning

Ändamålet avgör vilka uppgifter ([[C-161 Uppgift]]) som ingår i sammanställningen. Ändamålet kommer från den behandling ([[C-168 Behandling]]) som gav upphov till sammanställningen: det är dess behandlingsändamål ([[C-163 Behandlingsändamål]]), dataskyddets ändamål, inte styrningens ([[C-022 Ändamål]]). Sammanställningen är innehållet och finns oavsett var den ligger. Samma sammanställning kan ha flera representationer ([[C-085 Representation]]), som en lista i Excel, i diariet och i ett mejl.

Ett begrepp, ingen elementtyp: en sammanställning registreras som ett informationsobjekt ([[C-060 Informationsobjekt]]) som aggregerar ([[C-100 aggregerar]]) de informationsobjekt den är gjord av. Relationen visar att den är en sammanställning. Sammanställningens uppgifter ([[C-161 Uppgift]]) pekar på samma begrepp som källobjektens ([[0024-tillstand-ar-en-elementtyp-uppgiften-ar-informationsmodellens-attribut-och-lagret-ar-den-delade-datamodell-sdmn-beskriver|beslut 24]]).

Den som gör en ny sammanställning ur en annans informationsobjekt har gjort en behandling. Den nya sammanställningen klassas för sig. Informationsägare ([[C-167 Informationsägare]]) till den nya sammanställningen är processägaren ([[C-206 Processägare]]) för det beteende som upprättade den, inte källornas ägare, om inget annat beslutats. Att läsa källorna är en behandling inom deras ägares beslut ([[0035-processagaren-ar-en-roll-linjechefen-ett-begrepp-agandet-skrivs-med-ansvarar-for-typerna-ags-och-forekomsterna-svarar-linjen-for-och-styrobjekten-ags-genom-mandat|beslut 35]]).

Två prov svarar på var sin fråga. Det första avgör om samlingen är ett eget informationsobjekt: verksamheten hanterar den som en enhet för ett ändamål ([[0023-regeln-anger-vad-som-ska-galla-kravet-ar-en-sorts-regel-katalogen-ar-organisationens-ordlista-och-sbvr-tas-in-med-faststalls-av-som-relationstyp|beslut 23]]). Det andra avgör om sammanställningen får högre konfidentialitet än sina delar: går det att säga vilken ny uppgift den ger? Förteckningen över alla föreningars företrädare klarar det första provet, eftersom Register- och tillsynsenheten hanterar den som en enhet. Den ger ingen ny uppgift och har samma konfidentialitet som Företrädare. Mängden gör aldrig klassen högre. Att uppgifterna är många höjer i stället kravet på lagringsytan ([[C-165 Lagringsyta]]) där förteckningen ligger. Lägre blir klassen när uppgiften inte längre finns kvar, som i en summering per enhet eller ett avidentifierat enkätutfall. [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|Beslut 58]].

En förteckning över utsatta roller är en sammanställning som aggregerar Yrkesroll eller Utsatt roll. Den säger vilka anställda som är utsatta för hot, och det visar ingen enskild Yrkesroll. Förteckningen ger alltså en ny uppgift. Den klassas för sig och får högre konfidentialitet än objekten den bygger på. En Excelfil är förteckningens representation ([[C-085 Representation]]): den ger form åt sammanställningen, inte åt Yrkesroll.

Att förteckningen finns i ett enda exemplar gör den inte till en förekomst. Typen är det verksamheten talar om och ställer krav på. Förekomsten är listan som den ser ut just nu, och den skiljs från nästa version genom den identifierande uppgiften, versionsdatumet. Samma mönster gäller förteckningen över alla föreningars företrädare. Det gäller också en blankett: Ansökningsblankett är handlingstypen, den enskilda ansökan förekomsten ([[0040-nivan-i-en-klass-beror-pa-vardet-i-en-uppgift-varsta-fallet-galler-eller-delmangden-blir-ett-eget-informationsobjekt-och-en-forteckning-i-ett-exemplar-ar-anda-en-typ|beslut 40]]).

Ett datalager är en lagringsyta ([[C-165 Lagringsyta]]) som en applikation tillhandahåller, och det äger ingen information. Analysfunktionen som läser kärnprocessens objekt in i datalagret och sätter samman dem har en egen processägare. Den processägaren är informationsägare till sammanställningarna och till de nya informationsobjekt som räknas fram ur dem. Källornas klass är ingång till deras klass, som sätts för sig ([[0035-processagaren-ar-en-roll-linjechefen-ett-begrepp-agandet-skrivs-med-ansvarar-for-typerna-ags-och-forekomsterna-svarar-linjen-for-och-styrobjekten-ags-genom-mandat|beslut 35]]). Representationerna i datalagret är inga sammanställningar. De är samma informationsobjekt i en ny form, ordnade för fler frågor än en. [[C-165 Lagringsyta]] säger vad som gör dem till harmoniserad data ([[0072-harmoniserad-data-ar-en-egenskap-hos-representationerna-pa-en-lagringsyta-och-inget-begrepp-syftet-ar-uppfoljning-av-verksamheten-och-dataharmonisering-ar-en-del-av-formagan-som-behover-den|beslut 72]]).

Ett informationsområde ([[C-198 Informationsområde]]) samlar också informationsobjekt, men hela objekt, för att de hör ihop och ägs tillsammans, och utan egen representation. Sammanställningen är innehåll satt samman av uppgifter för ett ändamål. Får det som samlats en representation är det en sammanställning ([[0030-informationsomradet-ar-ett-begrepp-utan-elementtyp-ett-informationsobjekt-som-bestar-av-sina-objekt-varje-objekt-har-ett-hem-och-nivan-far-vara-grov|beslut 30]]). En sammanställning har ingen datakategori ([[C-201 Datakategori]]): de fyra kategorierna beskriver det verksamheten håller och fångar, inte det den sätter samman ([[0032-datakategorin-ar-ett-begrepp-resursdata-referensdata-transaktionsdata-och-handelsedata-sitter-pa-informationsobjektet-hogst-en-och-frivillig-och-referensdata-ar-en-vardemangd-organisationen-sjalv-faststaller|beslut 32]]).

Den potentiella handlingen i tryckfrihetsförordningen 2 kap. 6 §, en sammanställning av uppgifter som myndigheten kan göra med rutinbetonade åtgärder, är en sammanställning utan representation ännu. Ett registerutdrag och en fil för dataportabilitet är sammanställningar myndigheten upprättar på begäran, med formatkravet på representationen ([[C-085 Representation]]). Arkivredovisningen ordnar handlingen under den process som upprättade den, samma regel som ägandet ([[0031-handlingen-ar-representationen-allman-handling-och-gallring-ar-begrepp-forteckningarna-bor-utanfor-lagret-och-lagringsytan-far-vara-fysisk|beslut 31]], avgjort i [[0035-processagaren-ar-en-roll-linjechefen-ett-begrepp-agandet-skrivs-med-ansvarar-for-typerna-ags-och-forekomsterna-svarar-linjen-for-och-styrobjekten-ags-genom-mandat|beslut 35]]).

## Motsvarigheter

SDMN:s isCollection, flera av samma, är en sammanställning först när verksamheten hanterar samlingen som en enhet för ett ändamål, som förteckningen över alla företrädare; annars är "flera" bara många-änden på relationen mellan informationsobjekten ([[0023-regeln-anger-vad-som-ska-galla-kravet-ar-en-sorts-regel-katalogen-ar-organisationens-ordlista-och-sbvr-tas-in-med-faststalls-av-som-relationstyp|beslut 23]]).

## Exempel

förteckningen över alla föreningars företrädare, månadsuppföljningen av hyresfordringar per område, distributionslistan för nyhetsbrevet.
