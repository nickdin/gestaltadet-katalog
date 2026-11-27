---
id: C-073
term: Aktör
terms:
  - term: Aktör
    language: sv
    source: catalogue
definition: "person, team eller organisation som kan agera inom eller mot verksamheten"
kind: element-type
associative:
  - concept: "[[C-032 Arkitekturobjekt]]"
    label: är leverantör till
---
# C-073 Aktör

**Definition:** person, team eller organisation som kan agera inom eller mot verksamheten

## Anmärkning

En aktör kan vara den som fastställer styrning ([[C-183 fastställs av]]): en namngiven person med delegation, en organisationsenhet.

## Motsvarigheter

Motsvarar ArchiMates Business Actor.

Aktören som fastställer styrning motsvarar SBVR:s authority ([[0023-regeln-anger-vad-som-ska-galla-kravet-ar-en-sorts-regel-katalogen-ar-organisationens-ordlista-och-sbvr-tas-in-med-faststalls-av-som-relationstyp|beslut 23]]).

I Unified Modeling Language (UML) är Actor en roll ([[C-074 Roll]]), inte aktören som spelar den. Aktören syns i UML som en simbana (ActivityPartition) döpt efter en organisation eller en enhet. [[0029-klassen-ar-informationsobjektet-tillstandsmaskinen-ar-tillstandsvyn-anvandningsfallet-ar-tjansten-vardemangd-ar-ett-begrepp-och-uml-tas-in-for-lasarnas-skull-utan-tveksamma-rader|Beslut 29]].

Motsvarar Actor och Person i Value Delivery Modeling Language (VDML). En automat som deltagare är där en Actor, här en applikation ([[C-071 Applikation]]) eller utrustning ([[C-090 Utrustning]]). [[0028-varde-ar-en-elementtyp-i-strategiperspektivet-dit-vardeerbjudandet-flyttar-arbetssatt-ar-ett-begrepp-svaret-heter-hjalp-och-vdml-tas-in-med-rakneverket-omappat|Beslut 28]].

## Exempel

en person, ett team, en organisationsenhet, en extern part.
