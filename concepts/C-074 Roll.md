---
id: C-074
term: Roll
terms:
  - term: Roll
    language: sv
    source: catalogue
definition: "det en aktör agerar som inom organisationen, med det ansvar som hör till"
kind: element-type
associative:
  - concept: "[[C-125 Kompetens]]"
    label: kräver
---
# C-074 Roll

**Definition:** det en aktör agerar som inom organisationen, med det ansvar som hör till

## Anmärkning

En roll kräver kompetens ([[C-125 Kompetens]]), och kompetensen hämtas ofta ur en disciplin ([[C-124 Disciplin]]). Ett team eller en organisationsenhet kan verka i flera roller. En roll kan vara den som fastställer styrning ([[C-183 fastställs av]]), chefen för en organisationsenhet ([[0023-regeln-anger-vad-som-ska-galla-kravet-ar-en-sorts-regel-katalogen-ar-organisationens-ordlista-och-sbvr-tas-in-med-faststalls-av-som-relationstyp|beslut 23]]). Rollen bär också mandat ([[C-189 Mandat]]): befogenheten att fastställa styrning som följer av positionen ([[0025-paverkan-och-bedomning-ar-elementtyper-strategin-ar-sammanhangande-styrbeslut-visionen-ar-ett-mal-utan-matt-och-bmm-tas-in-med-andamalet-som-katalogens-tillagg|beslut 25]]).

Något ägs på tre sätt, och en regel säger när något får en ägarroll ([[0035-processagaren-ar-en-roll-linjechefen-ett-begrepp-agandet-skrivs-med-ansvarar-for-typerna-ags-och-forekomsterna-svarar-linjen-for-och-styrobjekten-ags-genom-mandat|beslut 35]]). Ett styrmedel eller en bärare ägs av den som fastställt det ([[C-183 fastställs av]]). Ett styrobjekt, verksamheten, en domän, en portfölj, en lösning, ägs av den som har mandatet ([[C-189 Mandat]]) över det. Ett arkitekturelement får en ägarroll som egen typ bara när ett regelverk utanför katalogen frågar vem som svarar per element: informationsobjektet har informationsägaren ([[C-167 Informationsägare]]), verksamhetsbeteendet processägaren ([[C-206 Processägare]]), båda skrivna med ansvarar för ([[C-208 ansvarar för]]). Allt annat ägs genom det som rymmer det. Linjechefen ([[C-207 Linjechef]]) är begreppet för förekomsterna, som katalogen inte ritar.

## Motsvarigheter

Motsvarar ArchiMates Business Role.

Motsvarar Actor i Unified Modeling Language (UML), som UML självt definierar som en roll en användare eller ett annat system spelar mot subjektet. Ett annat system är en applikation ([[C-071 Applikation]]), och aktören ([[C-073 Aktör]]) som spelar rollen ritas inte där. Simbanan (ActivityPartition) är rollen när den är döpt efter en. [[0029-klassen-ar-informationsobjektet-tillstandsmaskinen-ar-tillstandsvyn-anvandningsfallet-ar-tjansten-vardemangd-ar-ett-begrepp-och-uml-tas-in-for-lasarnas-skull-utan-tveksamma-rader|Beslut 29]].

Value Delivery Modeling Language (VDML) har en roll per samverkanstyp: Position i en organisationsenhet, Performer i en CapabilityMethod, Party i ett BusinessNetwork och Member i en Community, och RoleDefinition i rollbiblioteket. Alla är rollen. [[0028-varde-ar-en-elementtyp-i-strategiperspektivet-dit-vardeerbjudandet-flyttar-arbetssatt-ar-ett-begrepp-svaret-heter-hjalp-och-vdml-tas-in-med-rakneverket-omappat|Beslut 28]].

## Exempel

informationsarkitekt, enterprisearkitekt, huvudarkitekt (kallas också chefsarkitekt).
