---
id: C-011
term: Portfölj
terms:
  - term: Portfölj
    language: sv
    source: catalogue
definition: "sammanhållen mängd av initiativ och produkter som prioriteras och finansieras gemensamt"
kind: element-type
partitive: '[[C-008 Verksamhetsdomän]]'
---
# C-011 Portfölj

**Definition:** sammanhållen mängd av initiativ och produkter som prioriteras och finansieras gemensamt

## Anmärkning

Portföljen är ett styrobjekt ([[C-003 Styrobjekt]]), se portföljstyrning ([[C-044 Portföljstyrning]]). Både den centrala portföljen och varje delportfölj registreras som portfölj: portföljen aggregerar ([[C-100 aggregerar]]) sina delportföljer, och delportföljen aggregerar sina initiativ ([[C-012 Initiativ]]). Att portföljen också rymmer produkter ([[C-014 Produkt]]) uttrycks med samma relation; produkten står i ett annat perspektiv, så den relationen syns i lagret men i ingen vy. Elementtyp i strategiperspektivet ([[C-108 Strategiperspektiv]]), bredvid verksamhetsförmågan och initiativet. Beslut 19.

Förvaltningsobjektet, lösningen ([[C-055 Lösning]]), ingår inte i portföljen; dess leveransprodukter ([[C-174 Leveransprodukt]]) gör det, och ramen går till den lösning som realiserar dem. Beslut 20.

Portföljens ägare är den som äger det omslutande styrobjektet, eller den som ägaren har delegerat portföljen till ([[C-214 Delegation]]). Ägaren beslutar vad som startar, i vilken ordning och med vilken ram ([[C-210 Ram]]). Ägaren svarar för att urvalet flyttar verksamheten mot målen. Hur en lösning byggs om beslutar portföljens ägare inte om. Det gör lösningens ägare.

Portföljen ställer leveransprodukter mot initiativ. Produktens rad säger vad användarna får och vad det kostar att behålla det. Initiativets rad säger vad förändringen ger och kostar. Det som vägs är produkten, inte lösningen: en lösning med två leveransprodukter kan behålla den ena och dra ned på den andra. Ramen går sedan till lösningen eller till initiativet. Därför måste portföljens ägare vara den som får sätta lösningarnas ramar.

Två saker står inte i portföljen. Den ena är ett initiativ som en lösningsägare betalar ur lösningens egen ram. Den andra är verksamhetsprodukterna ([[C-173 Verksamhetsprodukt]]): dem väger ledningen mot annat när den sätter verksamhetens ramar, till exempel i verksamhetsplanen. Portföljen är inte hela organisationens budget. Beslut 46.

## Motsvarigheter

ArchiMate har inget portföljelement, så typen står under `unmapped-concepts` i mappningstabellerna, som initiativet.

## Exempel

Utvecklingsportföljen hos Myndigheten för föreningsstöd. I den står leveransprodukterna Föreningsregistret och Beräkningstjänsten bredvid initiativen ny e-tjänst för redovisning och automatisk beräkning av verksamhetsbidraget.
