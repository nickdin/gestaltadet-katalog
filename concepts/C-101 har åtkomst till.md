---
id: C-101
term: har åtkomst till
terms:
  - term: har åtkomst till
    language: sv
    source: catalogue
definition: "relationstyp som anger att ett arkitekturelement kan läsa eller skriva ett annat arkitekturelement"
kind: relation-type
key: accesses
access: true
---
# C-101 har åtkomst till

**Definition:** relationstyp som anger att ett arkitekturelement kan läsa eller skriva ett annat arkitekturelement

## Anmärkning

Relationen går från det beteendeelement som har åtkomsten till det element det läser eller skriver.

Från ett verksamhetsbeteende ([[C-157 Verksamhetsbeteende]]) får målet vara ett verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]), ett informationsobjekt ([[C-060 Informationsobjekt]]), en representation ([[C-085 Representation]], [[0031-handlingen-ar-representationen-allman-handling-och-gallring-ar-begrepp-forteckningarna-bor-utanfor-lagret-och-lagringsytan-far-vara-fysisk|beslut 31]]) eller en lagringsyta ([[C-165 Lagringsyta]], [[0062-beteendet-far-ha-atkomst-direkt-till-lagringsytan-och-kartan-visar-da-vilka-beteenden-som-nar-varje-yta|beslut 62]]). Åtkomsten följer realiseras av ([[C-094 realiseras av]]) ett steg: den som har åtkomst till ett verksamhetsobjekt har också åtkomst till informationsobjekten som realiserar det. Den åtkomsten ritas inte; ritas den ändå är den överflödig. Åtkomst direkt till ett informationsobjekt ritas där den inte följer av verksamhetsobjektet: ett uppslag i ett register, ett utlämnande, en sammanställning. Åtkomsten följer däremot inte aggregerar ([[C-100 aggregerar]]). Åtkomst till Företrädare ger ingen åtkomst till Personnummer, som Företrädare aggregerar, så en ritad åtkomst till Personnummer är inte överflödig. Om åtkomsten till ett objekt också når dess representationer är inte avgjort. [[0034-beteendet-nar-informationsobjektet-genom-verksamhetsobjektet-och-direkt-atkomsten-foljer-realiseras-av-men-inte-aggregerar|Beslut 34]].

Åtkomsten till en lagringsyta säger att beteendet använder ytan. Den ritas alltid och härleds aldrig. Åtgärda en felanmälan har åtkomst till pärmen på områdeskontoret, och analysfunktionen har åtkomst till datalagret. Beteendet når ett informationsobjekt på en lagringsyta när tre saker gäller: beteendet har åtkomst till objektet, beteendet har åtkomst till ytan, och en representation av objektet ligger på ytan. Så visar lagret vilka beteenden som når objektet på just den ytan. [[0062-beteendet-far-ha-atkomst-direkt-till-lagringsytan-och-kartan-visar-da-vilka-beteenden-som-nar-varje-yta|Beslut 62]].

Paret beteende och informationsobjekt är ankaret för behandlingen ([[C-168 Behandling]]). Förteckningarna utanför lagret fäster tre svar på paret: ändamålet, kravet på tillgänglighet och kravet på spårbarhet. Relationen bär inget av svaren. [[0031-handlingen-ar-representationen-allman-handling-och-gallring-ar-begrepp-forteckningarna-bor-utanfor-lagret-och-lagringsytan-far-vara-fysisk|Beslut 31]] och [[0058-nulaget-bar-inga-beslut-ur-informationshanteringens-perspektiv-klassen-fasts-pa-objektet-kraven-pa-behandlingen-och-mangden-gor-aldrig-klassen-hogre|58]].

Relationen bär fältet `access` med värdet `read`, `write` eller `read-write`; markeringen `access: true` på begreppet säger det. Ur två åtkomster till samma objekt, ett beteende som skriver och ett som läser, härleder programmet flödet mellan beteendena. Det flödet lagras aldrig som flödar till ([[C-097 flödar till]]). [[0014-processerna-ar-organisationens-och-kartan-delas-per-process|Beslut 14]], [[0033-flodet-mellan-tva-beteenden-harleds-ur-atkomsten-flodar-till-ar-for-det-som-inte-ar-ett-element-och-de-frammande-flodena-som-bar-ett-element-ar-atkomstparet|beslut 33]].

## Motsvarigheter

Motsvarar ArchiMates Access.

Motsvarar en handlings läsning eller skrivning av ett objekt i Unified Modeling Language (UML) (StructuralFeatureAction, LinkAction). [[0029-klassen-ar-informationsobjektet-tillstandsmaskinen-ar-tillstandsvyn-anvandningsfallet-ar-tjansten-vardemangd-ar-ett-begrepp-och-uml-tas-in-for-lasarnas-skull-utan-tveksamma-rader|Beslut 29]].
