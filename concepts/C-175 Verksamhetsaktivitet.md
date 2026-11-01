---
id: C-175
term: Verksamhetsaktivitet
terms:
  - term: Verksamhetsaktivitet
    language: sv
    status: preferred
    source: concept new
definition: avgränsat stycke arbete som en aktör i verksamheten utför som ett steg i ett verksamhetsbeteende
kind: element-type
generic: '[[C-126 Aktivitet]]'
partitive: '[[C-157 Verksamhetsbeteende]]'
---
# C-175 Verksamhetsaktivitet

**Definition:** avgränsat stycke arbete som en aktör i verksamheten utför som ett steg i ett verksamhetsbeteende

## Anmärkning

Ett steg i ett verksamhetsbeteende ([[C-157 Verksamhetsbeteende]]): i en verksamhetsprocess ([[C-130 Verksamhetsprocess]]), en handläggning ([[C-160 Handläggning]]) eller en verksamhetsfunktion ([[C-158 Verksamhetsfunktion]]), som rymmer den ([[C-100 aggregerar]]). Det BPMN kallar Task i en process och CMMN kallar Task i ett ärende; en aktivitet som en roll ([[C-074 Roll]]) tilldelas är BPMN:s User Task och CMMN:s HumanTask, en som en applikationstjänst ([[C-128 Applikationstjänst]]) realiserar är BPMN:s Service Task. Namnges som beteendena, med ett verb i infinitiv följt av objektet. Ett steg utlöser ([[C-098 utlöser]]) nästa. ArchiMate har ingen aktivitetstyp: en export skriver en verksamhetsaktivitet som Business Process, med skillnaden förlorad på vägen ut, och en import läser varje Business Process som verksamhetsprocess. I ARIS är den EPC:ns funktion (OT_FUNC). Insidan av en process ritas i BPMN och insidan av en handläggning i CMMN; en arkitekturbeskrivning visar aktiviteterna när flödet är det den ska visa, inte annars (ADR 0014). Beslutet: ADR 0022.

Motsvarar Activity i Value Delivery Modeling Language (VDML), arbete som en deltagare i en roll bidrar med; en aktivitet vars arbete görs av en hel CapabilityMethod ritas som det beteendet, som det yttre beteendet rymmer, så som BPMN-tabellen gör med Sub-Process. ADR 0028.
