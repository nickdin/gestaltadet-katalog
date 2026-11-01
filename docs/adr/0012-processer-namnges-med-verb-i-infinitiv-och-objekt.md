# Processer namnges med verb i infinitiv och objekt

*Sista ledet i Konsekvenser, att ett löpande ansvar är en verksamhetsförmåga, gäller inte längre: ADR 0015.*

Beslutat av Nicklas när en avdelnings processkarta ritades.

## Sammanhang

Processerna på kartan kom ur samtalen med namnen som cheferna använde: blandat substantiv (Bidragsgivning, Registerföring, Dataskyddsbedömning) och verbfraser (Ta fram årsredovisningen, Granska en redovisning). På kartan gick det inte att se vad som var en process med början och slut och vad som var ett löpande ansvar. Nicklas bad om en regel ur någon standard.

## Övervägda alternativ

- **Verb i infinitiv följt av objektet.** "Ta fram årsredovisningen", "Pröva en ansökan", "Göra dataskyddsbedömning". Så namnger ArchiMate sina processer, så gör BPMN-praxis för aktiviteter, och så ser de flesta klassificeringsstrukturer efter Riksarkivets föreskrift RA-FS 2008:4 ut. Namnet säger vad processen åstadkommer. Valt.
- **Från–till-namn**, Ljungberg och Larssons svenska processkola: "Från ansökan till beslut". Namnet säger var processen börjar och slutar, men blir långt och är ovanligt i myndigheters egna dokument. Avvisat.
- **Lämna namnen som de kom.** Inget att ändra, men kartan visar inte skillnaden mellan process och löpande ansvar. Avvisat.

## Konsekvenser

- Processerna på kartan döptes om efter regeln: Styra portföljen, Planera verksamheten, Följa upp verksamheten, Hantera risker och intern styrning och kontroll, Göra dataskyddsbedömning, Analysera omvärlden, Förmedla kunskap. De som redan hade verbnamn stod kvar.
- Regeln står i anmärkningen till `C-130 Verksamhetsprocess`.
- Det som inte går att namnge så är ingen process. Katalogen har ingen verksamhetsfunktion, med avsikt (anmärkningen till `C-077 Funktion`, mappningstabellens rad Business Function): ett löpande ansvar är en verksamhetsförmåga (`C-069`) under strategiperspektivet. Styra portföljen och Hantera risker och intern styrning och kontroll står kvar som processer tills någon säger att de inte har början och slut.
- I samma beslut: det som kommer ut ur en process ritas med en form, produkt, eftersom katalogens produkt (`C-014`) redan rymmer varor och tjänster. De tjänster kartan hade ritat som verksamhetstjänster typades om till produkter.
- Kartan ritar processer och produkter med draw.io:s ArchiMate-former, så bilden och lagrets ArchiMate-export säger samma sak.
