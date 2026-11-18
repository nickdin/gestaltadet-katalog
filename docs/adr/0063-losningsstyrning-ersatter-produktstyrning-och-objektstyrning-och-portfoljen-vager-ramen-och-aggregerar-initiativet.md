# Lösningsstyrning ersätter Produktstyrning och Objektstyrning, och portföljen väger ramen och aggregerar initiativet

Beslutat av Nicklas 18 november 2026, när ärendet #156 frågade om två ritningar stämde med beslut 46 och katalogen hade två begrepp för samma styrning.

Beslutet ändrar beslut 46 på en punkt: produktstyrning och objektstyrning är inte längre två begrepp.

## Sammanhang

Beslut 46 sade att Produktstyrning (`C-047`) och Objektstyrning (`C-048`) är samma styrning med samma ägare. Katalogen hade ändå två begrepp för den. Produktstyrning hade definitionen "objektbaserad styrning där styrobjektet är en lösning, sedd från de produkter lösningen erbjuder". Objektstyrning hade definitionen "objektbaserad styrning där styrobjektet är ett förvaltningsobjekt". Båda avgränsades av Lösning (`C-055`).

Ärendet #156 frågade om två ritningar visade det beslut 46 hade ändrat. Ritningen Styrning flöde hade en ruta för Produktstyrning med texten "styrobjekt: produkten". Efter beslut 46 är Produkt (`C-014`) inget styrobjekt. Ritningen Mandat och ansvar begreppsmodell visade varken Portfölj (`C-011`) eller Initiativ (`C-012`), fast båda har var sin ägare efter beslut 46.

Portfölj (`C-011`) hade ingen relation till Ram (`C-210`). Att portföljen väger ramarna stod bara i anmärkningen.

Frågan avgjordes i två rundor i #156.

## Beslut

- **Ritningarna ska säga det katalogen säger nu.**
- **Objektstyrning (`C-048`) utgår som eget begrepp.** Produktstyrning och objektstyrning är samma styrning med samma ägare, och de blir ett begrepp.
- **Begreppet heter Lösningsstyrning.** Katalogen döper styrningen efter styrobjektet, och styrobjektet är lösningen. Orden produktstyrning och objektstyrning blir avrådda ord på begreppet. Definitionen är "objektbaserad styrning där styrobjektet är en lösning".
- **Portfölj (`C-011`) får två relationer.** Portfölj väger Ram (`C-210`), och Portfölj aggregerar Initiativ (`C-012`). Ritningen Mandat och ansvar begreppsmodell visar båda.
- **Initiativets egen ram får ingen egen relation.** Den visas av att Ram tilldelas Styrobjekt (`C-003`), eftersom initiativet är ett styrobjekt.

## Konsekvenser

- Lösningsstyrning har id `C-047`. Id `C-048` har utgått och står i `retired-ids.yaml`.
- Anmärkningen i Lösningsstyrning (`C-047`) bär det som de två begreppen sade: att produkten inte är ett styrobjekt, skillnaden mot Produktionsstyrning (`C-215`), pm3:s två objektägare och de två sorterna av objektforum.
- Initiativ (`C-012`), Ansvar (`C-209`), Lösning (`C-055`), Produkt (`C-014`), Produktionsstyrning (`C-215`) och Objektbaserad styrning (`C-005`) hänvisar till Lösningsstyrning.
- Portfölj (`C-011`) har relationen väger till Ram (`C-210`). Att portföljen aggregerar initiativet står i lagret som att Initiativ (`C-012`) är en del av Portfölj (`C-011`). Den relationen fanns redan, och lagret tar inte emot en andra relation mellan samma två begrepp.
- Ritningen Styrning flöde har en ruta för Lösningsstyrning och en pil dit från Initiativstyrning, märkt LEVERABEL efter Leverabel (`C-171`).
- Ritningen Mandat och ansvar begreppsmodell har rutorna Portfölj (`C-011`) och Initiativ (`C-012`) och de två pilarna.
- De äldre besluten som nämner Produktstyrning och Objektstyrning står kvar som de skrevs.
