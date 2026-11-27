# Beteendet får ha åtkomst direkt till lagringsytan, och kartan visar då vilka beteenden som når varje yta

Beslutat av Nicklas 18 november 2026, när [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|beslut 58]] hade sagt att lagringsytans krav på tillgänglighet och spårbarhet kommer från de beteenden som når ytan, och lagret inte visade vilka de är.

## Sammanhang

[[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|Beslut 58]] läser fram lagringsytans (`C-165`) krav i fyra delar. En av delarna är tillgänglighet och spårbarhet: det strängaste kravet gäller bland de beteenden som når objektet på just den ytan. Hos Myndigheten för föreningsstöd behöver Pröva en ansökan objektet Förening samma dag och läser det i Föreningsregistret. Analysfunktionen klarar en vecka och läser kopian i datalagret.

Lagret visade att båda beteendena har åtkomst till (`C-101`) Förening och att Förening ligger på båda ytorna. Det visade inte vilket beteende som använder vilken yta. Den som gick igenom kartan kunde därför inte se att datalagret bara behöver klara veckan. [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|Beslut 58]] lämnade luckan till ärendet #179.

Åtkomsten fick gå till ett verksamhetsobjekt (`C-159`), ett informationsobjekt (`C-060`) eller en representation (`C-085`), men inte till en lagringsyta ([[0031-handlingen-ar-representationen-allman-handling-och-gallring-ar-begrepp-forteckningarna-bor-utanfor-lagret-och-lagringsytan-far-vara-fysisk|beslut 31]] och [[0034-beteendet-nar-informationsobjektet-genom-verksamhetsobjektet-och-direkt-atkomsten-foljer-realiseras-av-men-inte-aggregerar|34]]).

Frågan avgjordes i två rundor i #179, på två fall. Bovärden hos Brinkstadsbostäder utför Åtgärda en felanmälan med jourlistan i pärmen på områdeskontoret. Analysfunktionen hos Myndigheten för föreningsstöd läser Förening i datalagret. Första rundan gav ett villkor: kartan ska själv visa att ett beteende når en lagringsyta, också när ytan är en pärm.

## Beslut

- **Lagringsytan är ett fjärde mål för har åtkomst till (`C-101`).** Ett verksamhetsbeteende (`C-157`) får ritas med åtkomst direkt till en lagringsyta. Åtgärda en felanmälan ritas med åtkomst till pärmen på områdeskontoret. Analysfunktionen ritas med åtkomst till datalagret, och Pröva en ansökan med åtkomst till Föreningsregistret. Det ändrar punkten "Representationen är ett tredje mål" i [[0031-handlingen-ar-representationen-allman-handling-och-gallring-ar-begrepp-forteckningarna-bor-utanfor-lagret-och-lagringsytan-far-vara-fysisk|beslut 31]], som nu har ett fjärde bredvid sig.
- **Åtkomsten till ytan säger att beteendet använder ytan.** Den ritas alltid och härleds aldrig. En pil per beteende och yta räcker.
- **Beteendet når objektet på ytan när tre saker gäller.** Beteendet har åtkomst till objektet, beteendet har åtkomst till ytan, och en representation av objektet ligger på ytan. Analysfunktionen har åtkomst till Förening och till datalagret, och kopian av Förening ligger i datalagret. Alltså når analysfunktionen Förening där, och datalagret får veckan.
- **Når ett beteende två ytor som båda rymmer objektet, får båda ytorna beteendets krav.** Pröva en ansökan har åtkomst till både Ärendesystemet och Föreningsregistret, och Förening ligger på båda. Båda får dagen. Kartan säger hellre för strängt än för svagt.
- **Det gäller också en fysisk lagringsyta.** Pärmen har ingen applikation (`C-071`), och pilen går till pärmen på samma sätt som till datalagret.
- **Lagret räknar fortfarande ingenting.** Kartan visar vilka beteenden som når ytan. Förteckningen ger kraven. Den som går igenom kartan läser ihop dem, som i [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|beslut 58]].

## Övervägda alternativ

- **Kartan visar det inte, och genomgången frågar.** Informationsägaren hade då frågat varje processägare vilken yta beteendet använder, och svaret hade stått i förteckningen. Kartan hade aldrig svarat ensam. Avvisat.
- **Ytan läses genom applikationen.** Analysfunktionen använder analysplattformen, som tillhandahåller datalagret. Pärmen på områdeskontoret har ingen applikation, och en applikation med många grupprum säger inte vilket rum beteendet använder. Avvisat.
- **Beteendet ritas med åtkomst till representationen**, som ligger på ytan. Det är tillåtet sedan [[0031-handlingen-ar-representationen-allman-handling-och-gallring-ar-begrepp-forteckningarna-bor-utanfor-lagret-och-lagringsytan-far-vara-fysisk|beslut 31]] och säger exakt vilket objekt på vilken yta. Men varje objekt på varje yta måste då ritas som en egen representation, också Förening i datalagret, och kartan blir mycket större. Avvisat som vägen till ytan. Åtkomsten till representationen står kvar för det [[0031-handlingen-ar-representationen-allman-handling-och-gallring-ar-begrepp-forteckningarna-bor-utanfor-lagret-och-lagringsytan-far-vara-fysisk|beslut 31]] gav den.
- **Båda sätten efter behov**, pilen till ytan i vanliga fall och till representationen när det behöver vara exakt. Två kartor kan då rita samma läge olika. Avvisat.
- **Ett eget ärende med en egen grillning.** Lagringsyta (`C-165`) hade då väntat. Avvisat.

## Konsekvenser

- Ingen definition ändras, och inga begrepp eller relationstyper tillkommer. Definitionen av har åtkomst till (`C-101`) säger redan att ett arkitekturelement kan läsa eller skriva ett annat.
- Anmärkningarna i har åtkomst till (`C-101`) och Lagringsyta (`C-165`) säger det nya, och sidan Informationskartläggning får en följdfråga om vilka beteenden som har åtkomst till lagringsytan. Texterna skrivs in genom #179.
- Lagringsytan har ingen motsvarighet i ArchiMate (`mapping/archimate.yaml`). Åtkomsten till en yta följer därför inte med i en export dit.
- Om åtkomsten till ett objekt också når objektets representationer är fortfarande inte avgjort. Den frågan är ärende #35.
- De två ritningarna av analysfunktionens karta visar ännu inga pilar från beteendet till lagringsytorna. Det är ärende #185.
- [[0031-handlingen-ar-representationen-allman-handling-och-gallring-ar-begrepp-forteckningarna-bor-utanfor-lagret-och-lagringsytan-far-vara-fysisk|Beslut 31]] och [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|58]] har fått var sin not.
