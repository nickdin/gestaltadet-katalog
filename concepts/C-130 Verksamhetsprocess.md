---
id: C-130
term: Verksamhetsprocess
terms:
  - term: Verksamhetsprocess
    language: sv
    source: catalogue
definition: "process som aktörer i verksamheten utför"
kind: element-type
generic: "[[C-070 Process]]"
---
# C-130 Verksamhetsprocess

**Definition:** process som aktörer i verksamheten utför

## Anmärkning

Motsvarar ArchiMates Business Process. Namnges med ett verb i infinitiv följt av objektet: Ta fram årsredovisningen, Producera statistik, Göra dataskyddsbedömning. Namnet säger vad processen åstadkommer, och en process har en början och ett slut. Det som inte går att namnge så är ingen process. Ett löpande ansvar är en verksamhetsfunktion ([[C-158 Verksamhetsfunktion]]), som namnges på samma sätt; typen bär skillnaden. Beslutet: ADR 0012, ändrat i ADR 0015. En process är ett verksamhetsbeteende ([[C-157 Verksamhetsbeteende]]): den har en egen start, en händelse som sätter igång den, och ett eget resultat som någon utanför kedjan tar emot. Det som saknar endera är en verksamhetsaktivitet ([[C-175 Verksamhetsaktivitet]]) i någon annan process (ADR 0014). Motsvarar BPMN:s Process; stegen i den är verksamhetsaktiviteter och ritas i BPMN, en delprocess är en process processen rymmer (ADR 0022).

Motsvarar Activity i Unified Modeling Language (UML) när aktörer i verksamheten utför den, med stegen som Action; tabellen speglar BPMN-tabellen rad för rad. ADR 0029.
