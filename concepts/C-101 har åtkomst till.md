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

Relationen går från det beteendeelement som har åtkomsten till det element det läser eller skriver. Motsvarar ArchiMates Access.

Från ett verksamhetsbeteende ([[C-157 Verksamhetsbeteende]]) får målet vara ett verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]), ett informationsobjekt ([[C-060 Informationsobjekt]]) eller en representation ([[C-085 Representation]], ADR 0031). Åtkomsten följer realiseras av ([[C-094 realiseras av]]) ett steg: den som har åtkomst till ett verksamhetsobjekt har också åtkomst till informationsobjekten som realiserar det. Den åtkomsten ritas inte; ritas den ändå är den överflödig. Åtkomst direkt till ett informationsobjekt ritas där den inte följer av verksamhetsobjektet: ett uppslag i ett register, ett utlämnande, en sammanställning. Åtkomsten följer däremot inte aggregerar ([[C-100 aggregerar]]). Åtkomst till Företrädare ger ingen åtkomst till Personnummer, som Företrädare aggregerar, så en ritad åtkomst till Personnummer är inte överflödig. Om åtkomsten till ett objekt också når dess representationer är inte avgjort. ADR 0034.

Relationen bär fältet `access` med värdet `read`, `write` eller `read-write`; markeringen `access: true` på begreppet säger det. Ur två åtkomster till samma objekt, ett beteende som skriver och ett som läser, härleder programmet flödet mellan beteendena. Det flödet lagras aldrig som flödar till ([[C-097 flödar till]]). ADR 0014, ADR 0033.

Motsvarar en handlings läsning eller skrivning av ett objekt i Unified Modeling Language (UML) (StructuralFeatureAction, LinkAction). ADR 0029.
