---
id: C-126
term: Aktivitet
terms:
  - term: Aktivitet
    language: sv
    source: catalogue
definition: avgränsat stycke arbete som utförs som ett steg i ett beteende
---
# C-126 Aktivitet

**Definition:** avgränsat stycke arbete som utförs som ett steg i ett beteende

## Anmärkning

Familjebegrepp; typerna är verksamhetsaktivitet ([[C-175 Verksamhetsaktivitet]]), applikationsaktivitet ([[C-176 Applikationsaktivitet]]) och teknikaktivitet ([[C-177 Teknikaktivitet]]), var och en del av sitt perspektivs beteende. Det är samma byggsten vare sig stegen är ordnade i följd i en process ([[C-070 Process]]), väljs efter hand i en handläggning ([[C-160 Handläggning]]) eller samlas i en funktion ([[C-077 Funktion]]).

Ett steg utlöser ([[C-098 utlöser]]) nästa. Ett meddelande mellan två parter flödar till ([[C-097 flödar till]]). Ett vägskäl är ingen egen sak utan en aktivitet som använder ([[C-095 använder]]) en beslutslogik ([[C-178 Beslutslogik]]) och utlöser flera steg, med villkoret i relationens beskrivning. En parallell förgrening är flera utlöser från samma steg.

Sorten av steg är ingen typ utan läses ur aktivitetens relationer: tilldelas ([[C-096 tilldelas]]) en roll, realiseras av ([[C-094 realiseras av]]) en applikationstjänst, använder en beslutslogik, utlöser en process eller en handläggning. Beslut 22.

## Motsvarigheter

Aktiviteten är steget, det BPMN och CMMN båda kallar Task. Att ett steg utlöser ([[C-098 utlöser]]) nästa är BPMN:s sekvensflöde. Ett vägskäl är BPMN:s gateway. Sorterna är BPMN:s User, Manual, Service, Script, Business Rule, Send och Receive Task, eller CMMN:s HumanTask, ProcessTask, CaseTask och DecisionTask. Beslut 22.
