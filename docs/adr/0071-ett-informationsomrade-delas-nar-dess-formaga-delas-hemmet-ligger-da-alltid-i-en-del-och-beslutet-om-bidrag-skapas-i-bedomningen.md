# Ett informationsområde delas när dess förmåga delas, hemmet ligger då alltid i en del, och beslutet om bidrag skapas i bedömningen

Beslutat av Nicklas 23 november 2026, när [[0069-en-formaga-kan-besta-av-formagor-delarna-tacker-helheten-utan-overlapp-och-formagan-finns-for-att-verksamheten-ska-kunna-planera-sin-utveckling|beslut 69]] hade sagt att ett informationsområde får ha sitt hem i en del av en förmåga, men ingen hade modellerat informationen i Bidragsprövning mot dess två delar.

## Sammanhang

[[0069-en-formaga-kan-besta-av-formagor-delarna-tacker-helheten-utan-overlapp-och-formagan-finns-for-att-verksamheten-ska-kunna-planera-sin-utveckling|Beslut 69]] lät Verksamhetsförmåga (`C-069`) bestå av förmågor. Det sade också att verksamheten modellerar om informationen när en förmåga delas, och att modelleringen prövar både förmågans snitt och informationens. Katalogen hade inget exempel på det. Om de två delarna av Bidragsprövning täcker hela förmågan var därför inte prövat mot informationen (#216).

Modelleringen visade tre saker som texterna inte hade sett:

- Informationsområde (`C-198`) sade att ett område aldrig förfinas genom att det delas. [[0069-en-formaga-kan-besta-av-formagor-delarna-tacker-helheten-utan-overlapp-och-formagan-finns-for-att-verksamheten-ska-kunna-planera-sin-utveckling|Beslut 69]] sade att området kan delas.
- Bidragsinformation rymde Utbetalning och Återkrav. De skapas i förmågan Utbetalning och återkrav, inte i Bidragsprövning.
- Objektet Beslut rymde både beslut om bidrag och beslut om återkrav. Två förmågor skapade alltså förekomster av samma objekt.

Frågorna avgjordes på fallet Myndigheten för föreningsstöd.

## Beslut

### Reglerna

- **Ett informationsområde delas när dess förmåga delas, och bara då.** Annars förfinas området som förut, genom att nya objekt läggs under det. Meningen i [[0030-informationsomradet-ar-ett-begrepp-utan-elementtyp-ett-informationsobjekt-som-bestar-av-sina-objekt-varje-objekt-har-ett-hem-och-nivan-far-vara-grov|beslut 30]] om att ett område aldrig delas gäller inte längre i den formen.
- **Har en förmåga delar ligger varje hem i en del, aldrig i helheten.** Regeln i [[0030-informationsomradet-ar-ett-begrepp-utan-elementtyp-ett-informationsobjekt-som-bestar-av-sina-objekt-varje-objekt-har-ett-hem-och-nivan-far-vara-grov|beslut 30]] står: hemmet är förmågan där förekomsterna skapas. Delarna täcker allt helheten kan ([[0069-en-formaga-kan-besta-av-formagor-delarna-tacker-helheten-utan-overlapp-och-formagan-finns-for-att-verksamheten-ska-kunna-planera-sin-utveckling|beslut 69]]), så varje förekomst skapas i någon del.
- **Området för helheten får stå kvar.** Det består då av delarnas områden. Det bär informationsägaren och raden i klassningsförteckningen, så att ägaren inte behöver säga samma sak två gånger.

### Modellen av Bidragsprövning

- **Bidragsinformation består av två områden.** Bedömningsinformation hör hemma i Bedömning av rätt till bidrag. Beräkningsinformation hör hemma i Beräkning av bidrag.
- **Bedömningen skapar Villkorsbedömning.** Handläggaren prövar tre villkor för Föreningen Norrsken: demokratiskt uppbyggd, två år gammal och minst tusen medlemmar. Objektet bär varje villkor med utfallet.
- **Beräkningen skapar Bidragsberäkning.** Beräkningstjänsten räknar ut 240 000 kronor ur 1 200 medlemmar och 8 lokalavdelningar. Underlaget och beloppet är uppgifter i samma objekt, för de kan inte leva utan varandra.
- **Beslut om bidrag skapas i bedömningen.** Föreningen Ekbacken får avslag, och där räknar ingen ut något belopp. Ett beslut finns alltså utan beräkning, men aldrig utan bedömning. Beslutet hämtar beloppet ur Bidragsberäkning som ett beroende. Att beslutet skrivs efter uträkningen är ordning, och ordningen hör till processen ([[0069-en-formaga-kan-besta-av-formagor-delarna-tacker-helheten-utan-overlapp-och-formagan-finns-for-att-verksamheten-ska-kunna-planera-sin-utveckling|beslut 69]]).
- **Ansökan skapas också i bedömningen.** Att ta emot ansökan är första steget i bedömningen. Det är en aktivitet och ingen egen förmåga, för ingen vill sätta ett eget mål för mottagandet.
- **Bidragsprövning saknar ingen del.** Varje objekt fick ett hem i en av de två delarna.

### Snittet

- **Snittet håller för frågan vad som hör ihop mer än något annat.** Beslutet går inte att förstå utan villkorsbedömningen: de skrivs i samma ärende och lever lika länge. Över gränsen går bara en relation, den från beslutet till beräkningen.
- **Det syns när något ändras.** Byter myndigheten till automatisk beräkning ändras Bidragsberäkning. Ansökan, Villkorsbedömning och Beslut om bidrag rörs inte.

### Det som låg fel

- **Utbetalning och Återkrav får ett eget område, Utbetalningsinformation.** Det hör hemma i förmågan Utbetalning och återkrav.
- **Beslut delas i Beslut om bidrag och Beslut om återkrav.** Ett återkrav beslutas i handläggningen Pröva ett återkrav, och Beslut om återkrav ligger därför i Utbetalningsinformation.
- **Redovisning hör hemma i Utbetalningsinformation.** Norrsken redovisar året efter att 40 000 kronor inte har använts, och Pröva ett återkrav startar. Redovisningen skapas inte i prövningen av bidraget. Tillsynen startar på en anmälan eller ett stickprov, inte på redovisningen.
- **Ägandet ändras inte.** Chefen för Bidragsenheten är informationsägare för alla objekten.

### Lösningen

- **Ansökningshandläggningen aggregerar Bidragsinformation,** alltså båda delarnas områden. Utbetalning ingår inte i lösningen utan är ett beroende.
- **En utskuren Beräkningstjänst håller Beräkningsinformation.** Den mindre lösningen och delens område följer då varandra.

## Övervägda alternativ

- **Bidragsprövning får en tredje del, Beslutsfattande.** Delen klarar inte provet i [[0065-ingen-ager-formagan-portfoljens-agare-satter-dess-mal-malet-sager-vad-utformningen-ska-klara-och-formagan-provas-pa-om-den-kan-fa-ett-eget-mal|beslut 65]]. Målet att högst ett av hundra beslut ändras efter överklagande är ett mål för bedömningen. Avvisat.
- **Beslut hör hemma i helheten Bidragsprövning.** Då hade en förmåga med delar ändå haft något eget, mot regeln att delarna täcker helheten utan rest. Avvisat.
- **Underlaget och beloppet är två objekt.** De skapas i samma uträkning och kan inte leva utan varandra. Avvisat.
- **Bidragsinformation ersätts av två skilda områden.** Informationsägaren hade fått två rader i klassningsförteckningen som säger samma sak. Avvisat.
- **Redovisning hör hemma i Tillsyn.** Tillsynen granskar hur bidrag använts, men den skapar inte redovisningen. Avvisat.

## Konsekvenser

- Ingen definition ändras, och inga begrepp eller relationer tillkommer.
- Informationsområde (`C-198`), Verksamhetsförmåga (`C-069`), Informationsägare (`C-167`), exemplet Myndigheten för föreningsstöd och sidan Informationskartläggning har fått text om detta.
- [[0030-informationsomradet-ar-ett-begrepp-utan-elementtyp-ett-informationsobjekt-som-bestar-av-sina-objekt-varje-objekt-har-ett-hem-och-nivan-far-vara-grov|Beslut 30]], [[0060-grundnivan-i-klassningen-ar-ett-beslut-av-informationsagaren-aldrig-tystnad-och-den-nar-objektet-genom-egen-rad-eller-omradets-rad|60]] och [[0069-en-formaga-kan-besta-av-formagor-delarna-tacker-helheten-utan-overlapp-och-formagan-finns-for-att-verksamheten-ska-kunna-planera-sin-utveckling|69]] har fått var sin not. Exemplen om grundnivån i [[0060-grundnivan-i-klassningen-ar-ett-beslut-av-informationsagaren-aldrig-tystnad-och-den-nar-objektet-genom-egen-rad-eller-omradets-rad|beslut 60]] gäller i dag Utbetalningsinformation.
- Vilken lösning som håller Utbetalningsinformation är inte avgjort. Frågan prövas i #152.
- Ritningen i #215 visar två delar. Ingen tredje del tillkom.
