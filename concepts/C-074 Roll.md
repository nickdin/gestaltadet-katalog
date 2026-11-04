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

En roll kräver kompetens ([[C-125 Kompetens]]), och kompetensen hämtas ofta ur en disciplin ([[C-124 Disciplin]]). Ett team eller en organisationsenhet kan verka i flera roller. En roll kan vara den som fastställer styrning ([[C-183 fastställs av]]), chefen för en organisationsenhet (ADR 0023). Rollen bär också mandat ([[C-189 Mandat]]): befogenheten att fastställa styrning som följer av positionen (ADR 0025).

Något ägs på tre sätt, och en regel säger när något får en ägarroll (ADR 0035). Ett styrmedel eller en bärare ägs av den som fastställt det ([[C-183 fastställs av]]). Ett styrobjekt, verksamheten, en domän, en portfölj, en lösning, ägs av den som har mandatet ([[C-189 Mandat]]) över det. Ett arkitekturelement får en ägarroll som egen typ bara när ett regelverk utanför katalogen frågar vem som svarar per element: informationsobjektet har informationsägaren ([[C-167 Informationsägare]]), verksamhetsbeteendet processägaren ([[C-206 Processägare]]), båda skrivna med ansvarar för ([[C-208 ansvarar för]]). Allt annat ägs genom det som rymmer det. Linjechefen ([[C-207 Linjechef]]) är begreppet för förekomsterna, som katalogen inte ritar.

Motsvarar ArchiMates Business Role.

Value Delivery Modeling Language (VDML) har en roll per samverkanstyp: Position i en organisationsenhet, Performer i en CapabilityMethod, Party i ett BusinessNetwork och Member i en Community, och RoleDefinition i rollbiblioteket. Alla är rollen. ADR 0028.

Motsvarar Actor i Unified Modeling Language (UML), som UML självt definierar som en roll en användare eller ett annat system spelar mot subjektet. Ett annat system är en applikation ([[C-071 Applikation]]), och aktören ([[C-073 Aktör]]) som spelar rollen ritas inte där. Simbanan (ActivityPartition) är rollen när den är döpt efter en. ADR 0029.

## Exempel

informationsarkitekt, enterprisearkitekt.
