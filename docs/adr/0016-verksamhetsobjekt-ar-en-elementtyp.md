# Verksamhetsobjekt är en elementtyp, och informationsobjektet är dess informationssida

Beslutat av Nicklas i samma grillning som ADR 0014 och 0015.

## Sammanhang

En avdelnings processkarta ritade det som kommer ut ur en process som produkt, men många rutor var dokument och underlag: prognoser, rapporter, riktlinjer, beslut. Nicklas ville skilja produkten, erbjudandet mottagaren får, från verksamhetsobjektet, flödesobjektet en process hanterar vare sig det blir en produkt eller inte. Katalogen hade sömmen öppen: `C-060 Informationsobjekt` var mappat till både ArchiMates Business Object och Data Object, båda märkta tveksamma.

## Beslut

- Verksamhetsobjekt (`C-159`) är en elementtyp i verksamhetsperspektivet, ArchiMates Business Object: det ett verksamhetsbeteende hanterar och lämnar vidare. Exempel: en ansökan, ett initiativ, en utgiftsprognos, verksamhetsplanen, en tillsynsrapport.
- Informationsobjekt (`C-060`) är informationsperspektivets sida av samma sak, ArchiMates Data Object: ett verksamhetsobjekt realiseras av ett eller flera informationsobjekt.
- Produkt (`C-014`) är erbjudandet. Den aggregerar de verksamhetsobjekt mottagaren får och realiseras av beteendet som tar fram dem. Prognosrapporten aggregerar utgiftsprognosen; uppföljningsrapporten aggregerar samma objekt som uppföljningen av verksamhetsplanen.
- Ett beteende når ett verksamhetsobjekt med `C-101 har åtkomst till`.

## Övervägda alternativ

- **Låta `C-060` fortsätta täcka båda.** Skillnaden mellan produkt och flödesobjekt finns då bara i text, och mappningen förblir tveksam. Avvisat.
- **Produkt aggregerar informationsobjekt direkt.** Hoppar över det verksamheten själv talar om: ansökan, prognosen, planen. Avvisat.

## Konsekvenser

- `C-159 Verksamhetsobjekt` (elementtyp, täcks av `C-109`). Anmärkningarna i `C-060` och `C-014` omskrivna.
- `mapping/archimate.yaml`: Business Object till `C-159`, Data Object till `C-060`, ingen av dem tveksam längre. `mapping/aris.yaml`: `C-159` under `unmapped-concepts` tills en export visar ARIS typ.
- På kartan blir rapporterna, finansieringsbesluten, utvecklingsplanen, riktlinjerna och svaret till regeringen verksamhetsobjekt, inte produkter.
