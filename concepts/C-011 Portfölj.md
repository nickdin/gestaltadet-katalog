---
id: C-011
term: Portfölj
terms:
  - term: Portfölj
    language: sv
    source: catalogue
definition: sammanhållen mängd av ramar för ändring och initiativ som ägaren till en verksamhet eller verksamhetsdomän väger mot varandra
kind: element-type
partitive: '[[C-008 Verksamhetsdomän]]'
---
# C-011 Portfölj

**Definition:** sammanhållen mängd av ramar för ändring och initiativ som ägaren till en verksamhet eller verksamhetsdomän väger mot varandra

## Anmärkning

Portföljen är ett styrobjekt ([[C-003 Styrobjekt]]), se portföljstyrning ([[C-044 Portföljstyrning]]). Både den centrala portföljen och varje delportfölj registreras som portfölj: portföljen aggregerar ([[C-100 aggregerar]]) sina delportföljer, och delportföljen aggregerar sina initiativ ([[C-012 Initiativ]]). Att portföljen också rymmer produkter ([[C-014 Produkt]]) uttrycks med samma relation; produkten står i ett annat perspektiv, så den relationen syns i lagret men i ingen vy. Elementtyp i strategiperspektivet ([[C-108 Strategiperspektiv]]), bredvid verksamhetsförmågan och initiativet. Beslut 19.

Förvaltningsobjektet, lösningen ([[C-055 Lösning]]), ingår inte i portföljen. Det som står där, bredvid initiativen, är ramarna för ändring. Beslut 47, som ändrar beslut 20 på den punkten, och beslut 50.

Portföljen hör till verksamheten eller till den verksamhetsdomän ([[C-008 Verksamhetsdomän]]) som har fått en delportfölj. En domän har högst en portfölj. Beslut 47.

Portföljens ägare är den som äger det omslutande styrobjektet, eller den som ägaren har delegerat portföljen till ([[C-214 Delegation]]). Ägaren beslutar vad som startar, i vilken ordning och med vilken ram ([[C-210 Ram]]). Ägaren svarar för att urvalet flyttar verksamheten mot målen. Hur en lösning byggs om beslutar portföljens ägare inte om. Det gör lösningens ägare.

Portföljen väger det som ändrar utformningen: ramarna för ändring och initiativen. I verksamhetens portfölj står domänernas ramar för ändring. Domänens rad säger vad rättningar av lösningarna och små ändringar kostar per år. Initiativets rad säger vad förändringen ger och kostar. Ramen går sedan till domänen eller till initiativet. Domänens ägare sätter varje lösnings ram ur domänens ram. Har domänen en delportfölj står lösningarnas ramar där. Portföljens ägare pekar alltså aldrig ut pengarna till en lösning i en domän som någon annan äger. Beslut 47 och 50. Definitionen säger fortfarande initiativ och produkter. Ny lydelse prövas i ärende 159.

Två saker står inte i portföljen. Den ena är ett initiativ som en lösningsägare betalar ur lösningens egen ram. Den andra är produktionen. Vad verksamhetsprodukterna ([[C-173 Verksamhetsprodukt]]) får kosta, och vad drift och support av leveransprodukterna ([[C-174 Leveransprodukt]]) får kosta, väger ledningen mot annat när den sätter verksamhetens ramar, till exempel i verksamhetsplanen. Portföljen är inte hela organisationens budget. Beslut 46 och 47.

Den som sätter både produktionens ram och ramen för ändring håller balansen mellan i dag och i morgon. Portföljen fördelar den ena ramen. Verksamhetsplanen är en bärare ([[C-016 Bärare]]) och rymmer båda. Balansen hör till det livskraften ([[C-216 Livskraft]]) kräver. Beslut 49.

## Motsvarigheter

ArchiMate har inget portföljelement, så typen står under `unmapped-concepts` i mappningstabellerna, som initiativet.

## Exempel

Utvecklingsportföljen hos Myndigheten för föreningsstöd. I den står ramen för ändring i domänen Registerföring och tillsyn, 0,5 miljoner kronor per år, bredvid initiativen ny e-tjänst för redovisning och automatisk beräkning av verksamhetsbidraget. Chefen för Register- och tillsynsenheten lägger de 0,5 miljonerna på rättningar av registerlösningen.
