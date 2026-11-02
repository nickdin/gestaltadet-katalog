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

Ett begrepp, ingen elementtyp: en sammanställning registreras som ett informationsobjekt ([[C-060 Informationsobjekt]]) som aggregerar ([[C-100 aggregerar]]) de informationsobjekt den är gjord av, och det är relationen som visar att den är en sammanställning. Ändamålet avgör vilka uppgifter ([[C-161 Uppgift]]) som ingår och vilka krav som gäller: en förteckning över alla föreningars företrädare är känsligare än varje företrädare för sig. Ändamålet är den behandlings ([[C-168 Behandling]]) behandlingsändamål ([[C-163 Behandlingsändamål]]) som gav upphov till sammanställningen, dataskyddets ändamål, inte styrningens ([[C-022 Ändamål]]). Sammanställningen är innehållet och finns oavsett var den ligger; samma sammanställning kan ha flera representationer ([[C-085 Representation]]), som en lista i Excel, i diariet och i ett mejl. Den som gör en ny sammanställning ur en annans informationsobjekt har gjort en behandling, och den nya sammanställningen klassas för sig: högre genom sammanställningseffekten, lägre när uppgiften inte längre finns kvar, som i en summering per enhet eller ett avidentifierat enkätutfall. Vem som är informationsägare ([[C-167 Informationsägare]]) till den nya sammanställningen är inte avgjort.

SDMN:s isCollection, flera av samma, är en sammanställning först när verksamheten hanterar samlingen som en enhet för ett ändamål, som förteckningen över alla företrädare; annars är "flera" bara många-änden på relationen mellan informationsobjekten (ADR 0023). Sammanställningens uppgifter ([[C-161 Uppgift]]) pekar på samma begrepp som källobjektens, och den aggregerar källobjekten (ADR 0024).

## Exempel

förteckningen över alla föreningars företrädare, månadsuppföljningen av hyresfordringar per område, distributionslistan för nyhetsbrevet.
