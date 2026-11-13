# En princip klarar tre frågor, innehållet avgör om den är en arkitekturprincip, avvikelsen är ett eget begrepp, och policyn är en bärare

*Meningen att den som avgör en avvikelse kan lägga avgörandet hos någon annan genom en regel gäller inte längre i den formen. Avgörandet kan bara delegeras till en ägare med ram, och arkitekturrådet bereder men beslutar inte (beslut 50).*

Beslutat av Nicklas 12 november 2026, när katalogen sade var en princip står och vem som fastställer den men inte vad som gör en formulering till en princip.

## Sammanhang

Beslut 37 satte att en princip står i en bärare som den med mandat fastställer. Det sköt en fråga till #70: vad en bra princip är, vilka sorter som finns och var gränsen går mot mål, krav, regel och styrbeslut. Det sköt också ett exempel dit. Bostadsbolagets styrelse fastställde "en princip om att varje hyresgäst ska kunna göra sin felanmälan själv i appen", och ingen hade prövat om meningen var en princip.

Underlaget var Nicklas egna anteckningar om principer. Den bärande var ett prov i tre frågor, som katalogen bara hade som ritningen Beslutsschemat. En äldre anteckning sade emot katalogen på två punkter: den hade policy som egen nivå mellan princip och regel, och den sade att en arkitekturprincip för verksamheten är samma sak som en verksamhetsprincip.

Grillningen gick fem rundor och avgjorde varje fråga på ett fall ur de två exempelorganisationerna.

## Beslut

- **Tre frågor avgör om en formulering är en princip.** Vilka alternativ väljer den mellan? Vad härleds den ur? Vad följer av att välja så? Provet står i anmärkningen till Princip (`C-018`). Definitionen är orörd: den skiljer redan principen från grannarna.
- **Gränserna följer av provet.** "Handläggningstiden ska vara kort" pekar inte ut något alternativ och är ett mål (`C-017`). "Använd alltid Föreningsregistret" tillåter bara ett alternativ och är ett krav (`C-021`) eller en regel (`C-020`). "Ärendehanteringen byggs på Ärendesystemet" gäller en enda fråga och är ett styrbeslut (`C-019`). Gemensamt före eget ger riktningen och lämnar valet kvar, och är en princip.
- **Styrelsens mening om appen är ett krav.** Antingen går det att felanmäla i appen eller inte, och inget väljs bort. Detsamma gäller generaldirektörens mening om e-tjänsten. Principen bakom båda är Självbetjäning före personlig service, och meningarna är krav som följer av den. Exemplen är omskrivna så.
- **Varje princip har ett ursprung.** Princip (`C-018`) får nödvändigheten att varje princip härleds ur ett ändamål, en påverkan eller en bedömning. En princip utan ursprung går inte att väga och inte att ompröva. Att principen anger minst en konsekvens gäller sedan beslut 38.
- **En bra princip är en rätt skriven princip.** Den skrivs i fyra delar: namnet, riktningen med det som väljs bort, ursprunget och konsekvenserna. Formen följer de tre frågorna.
- **Innehållet avgör om principen är en arkitekturprincip.** Arkitekturprincipen (`C-040`) väljer mellan utformningar: vilka element som finns och hur de hänger ihop. Övriga principer väljer mellan handlingar i det löpande arbetet. Provet är om en arkitekturbeskrivning går att pröva mot principen. Självbetjäning före personlig service väljer mellan appen och kundcenter som kanal och är en arkitekturprincip. Akuta fel före planerat underhåll styr veckans arbetsordning och är det inte. Inget nytt begrepp behövs för verksamhetens princip.
- **En arkitekturprincip får stå i vilken fastställd bärare som helst.** Styrelsens princip är en arkitekturprincip redan i affärsplanen. Bärare (`C-016`) säger att ett styrmedel kan byta bärare utan att ändra innehåll, så en mening kan inte byta sort för att den flyttas. Beslutet ersätter beslut 37 på den punkten. Spärren `decided_by: [reference]` står kvar som beslut 38 läser den: bland arkitekturbeskrivningarna fastställer bara referensarkitekturen en princip.
- **Den som väljer väger, och vägningen går via principernas ursprung.** Texten om att principen kan behöva vägas mot andra principer står kvar. Ett val som har vägts har följt principerna, också den som vägde lättast. Krav och regler vägs inte.
- **Avvikelse (`C-213`) är ett nytt begrepp:** "skillnad mellan vad ett styrmedel anger och det som prövas mot det". Det gäller alla styrmedel. Utfallet avviker från målet, styrobjektet från kravet, handlingen från regeln och valet från principen. Måttstocken är styrmedlet, inte planen: planen är en bärare. Avvikelsen har ingen elementtyp.
- **Avvikelsen och beslutet om den är två saker.** Avvikelsen är skillnaden och finns också när ingen har beslutat något. Beslutet att godta den är ett styrbeslut (`C-019`) som anger sitt skäl. Ett val som har vägts mellan principer är ingen avvikelse. Valet avviker först när ingen annan princip bär det.
- **Ägaren väljer, och avvikelsen avgörs ovanför ägaren.** Den som äger styrobjektet fattar valen, prövar dem mot principerna och väger. Det är beslut 41 tillämpat på principen. En avvikelse från en arkitekturprincip avgör den som gav både ägaren och arkitekturstyrningen deras mandat. Chefen för Bidragsenheten kan inte sätta Gemensamt före eget åt sidan, och arkitekturstyrningen kan inte besluta om handläggningen. Generaldirektören avgör. En avvikelse från en princip som inte kommer ur en aspekt avgör den som fastställde principen. Den som avgör kan lägga avgörandet hos någon annan genom en regel. "Avvikelse från princip beslutas i arkitekturrådet" är en sådan regel.
- **Policyn är en bärare.** Ordet namnger dokumentet och säger inget om vad som står i det. Bostadsbolagets uthyrningspolicy rymmer en regel, en princip och ett mål, och varje mening prövas för sig. Policy står som exempel på Bärare (`C-016`).

## Övervägda alternativ

- **Bäraren avgör sorten**, så att styrelsens princip blir arkitekturprincip först när en referensarkitektur tar in den. Samma mening skulle byta sort vid flytten, och Bärare (`C-016`) säger att innehållet inte ändras. Avvisat.
- **Ett eget begrepp för verksamhetens princip.** En princip som inte är en arkitekturprincip är en Princip (`C-018`), och nivån är en uppgift på principen. Avvisat.
- **En lista över egenskaper hos en bra princip**, som TOGAF:s *understandable*, *robust*, *complete*, *consistent* och *stable*. Formen i fyra delar prövar samma sak och går att följa när man skriver. Avvisat.
- **Kraven på en princip i definitionen.** Definitionen bär redan valet, som är det som skiljer principen från grannarna. Resten är vägledning. Avvisat.
- **Policy som eget begrepp**, en nivå mellan princip och regel, eller som term för Princip. Beslut 25 gjorde Business Motivation Models *business policy* till Princip, men på svenska är policyn dokumentet. En term där skulle lura läsaren. Avvisat.
- **Avvikelsen som ett styrbeslut**, utan eget begrepp. Organisationer använder ordet för skillnaden, också den som upptäcks i efterhand och som ingen beslutat om. Avvisat.
- **Avvikelsen mätt mot planen.** Planen är en bärare, och det som avviker gör det från ett mål eller ett styrbeslut i den. En måttstock räcker. Avvisat.
- **Avvikelsen avgörs av den som har mandat över principen.** För en arkitekturprincip är det arkitekturstyrningen, som inte äger styrobjektet och inte kan besluta om det (beslut 41). Avvisat.

## Konsekvenser

- Nytt begrepp: Avvikelse (`C-213`), utan elementtyp. Nya relationer i frontmatter: `C-213` `mäts mot` → `C-015`, och `C-019` `kan godta` → `C-213`. Inga definitioner ändrade.
- Anmärkningar ändrade i Princip (`C-018`), Arkitekturprincip (`C-040`), Styrbeslut (`C-019`) och Bärare (`C-016`). Princip har också ny text under Motsvarigheter och Exempel.
- Meningen i beslut 37, att arkitekturprincipen beslutas genom att ingå i en antagen referensarkitektur, gäller inte längre som enda väg. Arkitekturprincipen tar nivån hos det styrobjekt den fastställs för.
- `docs/exempel/brinkstadsbostader.md` har fått styrelsens två principer, kravet om appen, uthyrningspolicyn och en avvikelse. `docs/exempel/myndigheten-for-foreningsstod.md` har fått generaldirektörens princip, kravet om e-tjänsten, Gemensamt före eget och avvikelsen med det egna registret.
- `CONTEXT.md`: posten Princip säger att principen väljer när flera alternativ är möjliga och att arkitekturprincipen väljer mellan utformningsalternativ.
- Ritningen Beslutsschemat har fått utfallens ord rättade efter beslut 37 och det här beslutet.
- Ritningarna visar inte Avvikelse (`C-213`) än.
- Delegation och delegationsordning är inte avgjorda här. De har en egen grillning i #150.
- #70 stängs.
