---
id: C-020
term: Regel
terms:
  - term: Regel
    language: sv
    source: catalogue
definition: styrmedel som binärt anger vad som ska gälla eller inte gälla
kind: governance-type
generic: "[[C-015 Styrmedel]]"
associative:
  - concept: '[[C-018 Princip]]'
    label: kan härledas ur
  - concept: '[[C-184 Påverkan]]'
    label: kan komma direkt ur
---
# C-020 Regel

**Definition:** styrmedel som binärt anger vad som ska gälla eller inte gälla

## Anmärkning

Handlingen eller läget prövas mot regeln. Regeln lämnar inget bedömningsutrymme i vad som ska gälla; att avgöra om den är följd kan ändå kräva omdöme. Regeln kräver ett läge och vidtar ingen åtgärd: "varje öppet ärende har en handläggare" är regeln, aktiviteten ([[C-126 Aktivitet]]) som tilldelar handläggaren står utanför den. Ett krav ([[C-021 Krav]]) är en regel vars läge är en egenskap hos styrobjektet.

Regeln är det SBVR (Semantics of Business Vocabulary and Business Rules) kallar behavioral business rule: en regel som förpliktar eller förbjuder ett sakläge, direkt prövbar och under verksamhetens jurisdiktion, det vill säga något organisationen själv kan ändra. Lagen är ingen regel i den meningen utan extern påverkan ([[C-029 Extern påverkan]]). Regeln är organisationens egen, härledd ur en princip via dess konsekvenser eller direkt ur påverkan ([[C-184 Påverkan]]), extern som intern. Hur hårt regeln upprätthålls, SBVR:s enforcement level, är text i regeln, ingen typ.

Regler som anger vad något är, SBVR:s definitional rule, är inga styrmedel. En nödvändighet som alltid gäller, "varje ärende har exakt en sökande", står i begreppets anmärkning och som multiplicitet på relationen mellan informationsobjekten ([[C-060 Informationsobjekt]]). En regel som avgör ett utfall för varje fall, när en ansökan är komplett, är en beslutslogik ([[C-178 Beslutslogik]]). En beslutslogik härleds ur regler: regeln är det som ska följas, logiken hur utfallet bestäms, det DMN kallar Knowledge Source (beslut 22). Beslut 23.

**Nödvändighet:** Varje regel har ett ursprung: en princip den härleds ur eller en påverkan den kommer direkt ur.

Motsvarar Constraint i Unified Modeling Language (UML) när villkoret säger vad som ska gälla i verksamheten, "sökanden är minst 18 år"; ett villkor som bara skyddar koden är applikationens insida. Beslut 29.

## Exempel

"Avvikelse från princip beslutas i arkitekturrådet."
