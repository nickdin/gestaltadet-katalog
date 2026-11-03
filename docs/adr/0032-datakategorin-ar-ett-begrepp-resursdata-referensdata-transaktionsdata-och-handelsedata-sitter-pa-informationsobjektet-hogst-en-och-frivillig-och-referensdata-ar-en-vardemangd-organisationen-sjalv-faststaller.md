# Datakategorin är ett begrepp, resursdata, referensdata, transaktionsdata och händelsedata sitter på informationsobjektet, högst en och frivillig, och referensdata är en värdemängd organisationen själv fastställer

Beslutat av Nicklas i grillningen av ärende #32, 2026-11-02 till 11-03. Avgör om indelningen av information i slag, som informationsmodelleringen färgar sina rutor efter, är katalogens sak eller metodens, var den sitter, hur många slagen är, hur ett objekt bär sitt slag och var gränsen mot Värdemängd (`C-197`) går.

## Sammanhang

Informationsmodelleringens praxis delar informationen i resursdata (masterdata, kärndata: det verksamheten har), referensdata (fastställda standardförekomster, kodverk), transaktionsdata (det som sker) och händelsedata (det som inträffar). Informationsarkitektens bidrag skiljer sig per slag: central källa, standardförekomster, datafångst, sammanhang. Katalogen hade inget ord för slaget: Värdemängd (`C-197`) täcker referensdatans värden som text vid en uppgift, inte slaget som sådant. Frågan kom upp i grillningen av Informationsområde (ADR 0030), när färgerna i en ritad informationsmodell diskuterades, och ADR 0030 lämnade den som ett eget ärende.

Två beslut satte ramen. ADR 0018 avvisade två elementtyper för samma slags sak, så fyra typer under Informationsobjekt (`C-060`) var uteslutna; mönstret som finns är begreppet utan elementtyp, som Sammanställning (`C-162`) och Informationsområde (`C-198`). Men de två syns i lagret genom en relation, och slaget har ingen relation som visar det: det skulle bli det första begreppet under `C-060` som lagret inte kan läsa utan ett fält. Ett element bär i dag `id`, `type`, `level`, `sources`, `description` och `candidate`; förebilden för ett fält som pekar på begrepp är styrningselementets `aspects`, en lista länkar till begrepp av slaget `aspect`, som `check` kontrollerar.

Grillningen gick två rundor (5 + 6 frågor), och Nicklas tog rekommendationen i varje fråga. Exemplen som avgjorde gränsfallen: Hyresavtal, som har livscykel men ligger kvar och är det hyresfordringarna märks med; Betalning, som inträffar men förs genom lägen; Mätvärde, som ingen handlägger.

## Beslut

- **Datakategori (`C-201`) är ett begrepp utan elementtyp**, "indelning av informationsobjekt efter hur verksamheten håller och fångar deras förekomster", associerat till Informationsobjekt (`C-060`) som det indelar. Datatyp är avrådd term, eftersom typ i katalogen betyder elementtyp; datakategori är kursmaterialets ord.
- **Fyra kategorier, som begrepp utan elementtyp under `C-060`**: Resursdata (`C-202`, med masterdata och kärndata som tillåtna termer), Referensdata (`C-203`), Transaktionsdata (`C-204`) och Händelsedata (`C-205`). Fyra och inte DAMA:s tre: händelsedata har ett eget bidrag, sammanhanget, och en egen natur, det inträffar och ändras inte, och bostadsbolagets Mätvärde är inte en transaktion.
- **Kategorin sitter på informationsobjektet, inte på verksamhetsobjektet (`C-159`).** Den säger hur informationen försörjs och hålls, inte vad beteendet hanterar; ett verksamhetsobjekt realiseras av flera informationsobjekt som kan vara av olika kategori, och ett verksamhetsobjekt kan sakna informationssida helt.
- **Ett objekt bär kategorin som ett fält på elementet, ett värde och aldrig en lista**, efter `aspects` mönster: de fem begreppen märks med ett eget slag, fältet länkar till ett av de fyra, `check` rapporterar en länk till något annat. Fältet är interlinguas ärende; tills det finns står kategorin som en mening i objektets beskrivning. Härledning ur lagret avvisades: att ett objekt realiserar ett verksamhetsobjekt med tillstånd skiljer inte Förening från Ansökan.
- **Kategorin är frivillig, och `check` kräver den aldrig.** Ett informationsområde (`C-198`) har ingen; kategorin sitter på objekten i det. En sammanställning (`C-162`) har ingen: de fyra beskriver det verksamheten håller och fångar, inte det den sätter samman.
- **Vad ägaren läser ut**: färg per kategori i informationsmodellen, och en listning av objekt per kategori, så att informationsägaren (`C-167`) ser sina resursdata att hålla källa för. Båda är interlinguas sak, i samma ärende som fältet; katalogen säger i `C-060` att kategorin finns för det.
- **Källan för resursdata är en egen fråga.** Kategorin säger att objektet ska ha en källa; vilken representation (`C-085`) på vilken lagringsyta (`C-165`) som äger förekomsten pekar lagret inte ut ännu. Anmärkningen till `C-202` säger att det är en fråga ägaren ska kunna svara på; ett eget ärende tar frågan.
- **Gränsen mot Värdemängd (`C-197`)**: en värdemängd organisationen själv fastställer, äger eller ger egna uppgifter, som Stödform med villkor och giltighetstid, är ett informationsobjekt av kategorin referensdata; en värdemängd som bara räknas upp vid uppgiften, som kommunkoderna, förblir text. Ingen ny regel: golvet i `C-060`, det som klassas, ägs eller regleras för sig är ett eget objekt, ger svaret.
- **Gränsfallen**: Hyresavtal är resursdata, det verksamheten har och märker sina transaktioner med, fast det har en livscykel. Betalning är transaktionsdata, den förs genom lägen, inkommen, avstämd, återbetald. Händelsedata är det ingen handlägger, bara registrerar och tolkar: Mätvärde, en inloggning.
- **Inga mappningsrader**: varken ArchiMate, UML eller SDMN har kategorin.

## Övervägda alternativ

- **Bara en anmärkning i `C-060` om indelningen som metod**, slaget i beskrivningstexten för gott. Katalogen ska svara när orden används, samma skäl som för Informationsområde i ADR 0030, och ingen vy kan färga efter text. Avvisat.
- **Inget alls.** Samma skäl. Avvisat.
- **Kategorin på verksamhetsobjektet**, med kursens ord att ett verksamhetsobjekt kan vara en händelse eller transaktion. Bidraget per kategori är informationsförsörjningens, och flera informationsobjekt av olika kategori kan realisera samma verksamhetsobjekt. Avvisat.
- **Tre kategorier som DAMA**, händelsedata under transaktionsdata. Tvingar Mätvärde in under transaktioner med en förklaring i varje modell. Avvisat.
- **Härledning ur lagret** i stället för ett fält. Förening har också tillstånd. Avvisat.
- **Datatyp som ord.** Typ betyder elementtyp i katalogen. Avrådd term.
- **Fältet som lista**, som `aspects`. Ett objekt har en kategori. Avvisat.

## Konsekvenser

- Nya begrepp `C-201` till `C-205`, utan typ: `C-201` associerat till `C-060`, de fyra med `C-060` som överordnat, `C-203` associerat till `C-197`; `C-202` med masterdata och kärndata som tillåtna termer, `C-201` med datatyp avrådd; anmärkning och exempel på var och en. Meningar tillagda i `C-060`, `C-162`, `C-197` och `C-198`.
- Interlingua, ett ärende: ett fält på elementet som länkar till en av de fyra kategorierna, ett värde, frivilligt, kontrollerat av `check` efter `aspects` mönster; renderingen färgar informationsmodellen per kategori; en listning av informationsobjekt per kategori.
- Katalogen, ett ärende: källan för resursdata, vilken representation på vilken lagringsyta som äger förekomsten, och om lagret ska peka ut den.
- Mallen körs inte om: ingen ny elementtyp. Inga mappningsrader.
