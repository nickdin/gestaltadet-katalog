# Varje text på sajten säger vem som skrivit den och om Nicklas godkänt den

Beslutat av Nicklas 11 november 2026, när han ville att läsaren på gestaltadet.se alltid ska kunna se om en text är hans egen eller skriven av AI.

## Sammanhang

Nästan all text på sajten är skriven av AI. Nicklas bestämmer innehållet i grillningar, och Claude skriver orden. Sajten sade inget om det. Historiken visade till och med Nicklas namn ensamt på beskrivningar som Claude skrivit. En läsare kunde alltså inte skilja en text Nicklas står för ord för ord från en text han aldrig läst.

## Beslut

- **Varje text har ett av fyra lägen.**
  1. Skriven av Nicklas.
  2. Skriven av Nicklas, redigerad av AI, godkänd av Nicklas.
  3. Skriven av AI, granskad och godkänd av Nicklas.
  4. Skriven av AI, inte granskad.
- **Den som skrev orden är skribenten.** En definition som Nicklas bestämt i en grillning och Claude formulerat är skriven av AI. Kommenterar AI bara, och Nicklas skriver om själv, är texten fortfarande hans.
- **Godkännandet gäller ordalydelsen.** Nicklas har läst just den formuleringen och står för den som sin egen. Att han bestämt innehållet räcker inte.
- **Bara Nicklas godkänner.** Han pekar ut en namngiven text i taget, och Claude skriver in godkännandet med datum. Claude märker aldrig en text som godkänd på eget initiativ.
- **Varje ordändring av AI tar bort godkännandet**, även ett kommatecken. Texten går då till läge 4 tills Nicklas godkänt den igen. Ny text från AI börjar alltid i läge 4. Två ändringar tar inte bort godkännandet: att texten flyttas eller får en ändrad länk, och ett exakt byte av ett ord mot ett annat som Nicklas själv beställt.
- **Märkningen gäller det gestaltadet.se visar.** På en begreppssida märks definitionen, anmärkningen och exemplen var för sig. Ett beslut, en mappningstabell och en ritning är en text var. Startsidan märks per avsnitt. Termer, relationer och sidor som programmet bygger ur dem märks inte: de är uppgifter, inte formulerad text.
- **Läsaren ser en etikett vid varje text.** Etiketten säger läget och, för en godkänd text, datumet. Läge 4 har en egen dämpad färg, ingen varningsfärg. Etiketten länkar till sidan Så märks texterna, som förklarar lägena och visar hur många texter som är granskade.
- **Historiken visar att AI var med.** En ändring som Claude var medförfattare till står som "Nicklas med AI", och beskrivningarna märks som skrivna av AI och inte granskade.
- **Besluten ligger kvar på sajten som öppna arbetsanteckningar.** De skrivs inte om för läsaren. Läsaren möter dem under ordet beslut, inte ADR: "beslut 25", med länk. De får en egen sida, Besluten bakom katalogen, som säger vad de är. Varje besluts första rad säger för läsaren vem som beslutade, när och varför.
- **Allt som fanns när märkningen infördes börjar i läge 4.** Nicklas granskar startsidan, Så märks texterna och beslutssidans inledning innan märkningen syns. Resten granskar han efter hand, definitionerna först och besluten sist.

## Övervägda alternativ

- **Tre lägen, utan läget för text som Nicklas skrivit och AI redigerat.** Då hade en korrekturläst text från Nicklas sett ut som skriven av AI. Avvisat.
- **En gräns för hur liten en ändring får vara utan att räknas.** Någon måste då avgöra vad som är för litet, och det avgörandet syns inte för läsaren. Avvisat: varje ordändring räknas.
- **Märkning per sida eller per stycke.** Per sida kan Nicklas inte godkänna en definition utan att ha läst exemplen. Per stycke blir det för många märkningar att hålla reda på. Avvisat.
- **Vänta med märkningen tills texterna är granskade.** Sajten hade då fortsatt att se ut som Nicklas egen text under tiden. Avvisat: det ogranskade syns från första dagen.
- **Ta bort besluten från sajten och länka till GitHub.** Besluten hade varit lika publika som förut, men utan märkning. Avvisat.
- **Skriva om besluten för läsaren.** Det ger 30 långa texter som AI skrivit om och ingen människa läser, och en formulering som glider märker ingen. Avvisat nu; en omgång i klarspråk är ett eget ärende.

## Konsekvenser

- En mappningstabell är mest uppgifter men märks ändå som en text, eftersom varje rad är en bedömning som AI gjort.
- De stora svepen, bytet från ADR till beslut och de nya första raderna, görs innan Nicklas börjar granska. Annars faller godkännanden på vägen.
- Etiketterna, räkningen, beslutssidan och kontrollen av att en godkänd text inte ändrats är programmets arbete och ligger i interlinguas ärenden.
