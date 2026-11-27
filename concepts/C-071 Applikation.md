---
id: C-071
term: Applikation
terms:
  - term: Applikation
    language: sv
    source: catalogue
definition: "avgränsad programvara som tillhandahåller funktionalitet åt verksamheten genom ett eget gränssnitt"
kind: element-type
generic: "[[C-122 Resurs]]"
---
# C-071 Applikation

**Definition:** avgränsad programvara som tillhandahåller funktionalitet åt verksamheten genom ett eget gränssnitt

## Anmärkning

Systemägare är vardagens ord för den som har mandat ([[C-189 Mandat]]) över en applikation. Systemägaren är skild från informationsägaren ([[C-167 Informationsägare]]) till det applikationen lagrar och från lösningsägaren ([[C-055 Lösning]]). Systemägare är inget begrepp ([[0035-processagaren-ar-en-roll-linjechefen-ett-begrepp-agandet-skrivs-med-ansvarar-for-typerna-ags-och-forekomsterna-svarar-linjen-for-och-styrobjekten-ags-genom-mandat|beslut 35]]).

Återställningstiden är ett krav ([[C-021 Krav]]) på applikationen: hur fort applikationen måste vara i bruk igen. Den härleds ur kontinuitetskravet på de verksamhetsbeteenden ([[C-157 Verksamhetsbeteende]]) som använder applikationen. Anta att Åtgärda en felanmälan hos bostadsbolaget får stå still högst fyra timmar. Anta också att en reservrutin säger hur processen utförs utan fastighetssystemet, och att processen då klarar en dag utan det. Utan reservrutinen måste fastighetssystemet vara i bruk inom fyra timmar. När flera beteenden använder samma applikation gäller den kortaste tiden. [[0061-kontinuitet-ar-ett-krav-pa-hela-beteendet-tillgangligheten-far-tva-matt-och-aterstallningstiden-harleds-till-resursen|Beslut 61]].

## Motsvarigheter

Motsvarar ArchiMates Application Component.

Motsvarar Component i Unified Modeling Language (UML), och Actor när aktören är ett annat system. Komponenterna inuti en applikation är dess insida och ritas inte i lagret ([[0026-omgs-ovriga-specifikationer-sorteras-i-tre-fack-bacm-vdml-och-uml-tas-in-sysml-ar-utanfor-och-utbytesspecifikationerna-ar-programmets-sak|beslut 26]]). Applikationen består av sina gränssnitt (Interface, Port), realiseras av sin artefakt (Manifestation) och använder det gränssnitt kopplingen (Connector) går till. [[0029-klassen-ar-informationsobjektet-tillstandsmaskinen-ar-tillstandsvyn-anvandningsfallet-ar-tjansten-vardemangd-ar-ett-begrepp-och-uml-tas-in-for-lasarnas-skull-utan-tveksamma-rader|Beslut 29]].
