# Handlingen är representationen, allmän handling och gallring är begrepp, förteckningarna bor utanför lagret, och lagringsytan får vara fysisk

Beslutat av Nicklas i grillningen av ärende #28, 2026-11-02. Avgör hur offentlighetens och arkivets begrepp, allmän handling, handlingstyp, registrering, bevarande och gallring, sekretess och informationshanteringsplan, uttrycks i katalogen, och var det de fyra regelverken vill veta om varje anker i lagret bor.

## Sammanhang

Ett upplägg för informationshantering ska svara åt fyra regelverk ur samma karta: informationssäkerhet, dataskydd, offentlighet och sekretess med diarieföring, och arkiv. Katalogen hade dataskyddets och informationssäkerhetens begrepp: Behandling (`C-168`), Behandlingsändamål (`C-163`), Rättslig grund (`C-164`), Informationstillgång (`C-166`) och Informationsägare (`C-167`). Men ingen begreppsfil nämnde allmän handling, gallring, bevarande, arkiv eller handlingstyp. Sekretess nämndes i förbigående i Uppgift (`C-161`) och Informationstillgång (`C-166`), och diariet bara i exempel.

Redan innan grillningen hade Nicklas avgjort i ärendet att handling och handlingstyp inte blir begrepp. Tryckfrihetsförordningens handling, "framställning i skrift eller bild samt upptagning", är en form, och Representation (`C-085`) är "konkret form som ett informationsobjekt tar". Katalogen ritar typer: elementet Ansökningsblankett är handlingstypen, och den enskilda ansökan är förekomsten. Den potentiella handlingen i tryckfrihetsförordningen 2 kap. 6 § är en sammanställning (`C-162`) utan representation ännu.

De fyra områdena och var kravet hänger, med representationen på plats:

| Område | Regelverk | Kravet hänger på |
|---|---|---|
| Informationssäkerhet | MSB:s föreskrifter, ISO 27000 | objektet (klass), lagringsytan (åtgärd) och representationen (märkning, signering, format) |
| Dataskydd | dataskyddsförordningen | behandlingen: beteende och objekt, med ändamål och rättslig grund; representationen för varje kopia och för utdragets format |
| Offentlighet och sekretess, med diarieföring | tryckfrihetsförordningen, offentlighets- och sekretesslagen | uppgiften (sekretess) och representationen (allmän handling, registrering, sekretessmarkering, utlämnande) |
| Arkiv | arkivlagen, Riksarkivets föreskrifter | representationen per process (bevarande och gallring, format, äkthet), och processen för klassificeringsstrukturen |

Återkommande i alla fyra är format och läsbarhet, märkning, äkthet, kopior, och händelserna inkommen, upprättad och gallrad. Gränsen går så: sekretessen sitter på uppgiften, ändamål och rättslig grund på behandlingen, behörighet och säkerhetskopia på lagringsytan, och klassen på objektet. Representationen får konsekvensen: märkningen av klassen, kopian som behandling, formatet som tillgänglighet.

Grillningen gick fem rundor (9 + 2 + 5 + 2 + 1 frågor). Två svar från Nicklas ändrade utfallet. Det första: bevarande och gallring ska inte blandas in i arkitekturbeskrivningen utan höra till en egen förteckning med samma styrobjekt. Det öppnade ADR 0018:s mening om att ändamål och rättslig grund står i beteendets beskrivning. Det andra: begreppen ska ändå finnas i katalogen, så att förteckningen och lagret talar samma språk. Det gav Gallring som begrepp.

## Beslut

- **Allmän handling (`C-199`) är ett begrepp utan elementtyp**, "representation som förvaras hos myndigheten och som har kommit in dit eller upprättats där", underordnat Representation (`C-085`). Den registreras som en representation. Elementets beskrivning säger att den är allmän, när den blir det och vilka undantagen är. Handling och handlingstyp är tillåtna termer på `C-085`, inga egna begrepp.
- **Registrering är inget begrepp.** Att en handling kommer in eller upprättas är en verksamhetshändelse (`C-135`). Den utlöser registreringen, en verksamhetsaktivitet (`C-175`) med åtkomst till representationen. Diariet är en lagringsyta (`C-165`) och diarieposten ett informationsobjekt (`C-060`), med diarienumret som ärendets identifierande uppgift. Ett begrepp för ett enskilt steg hade öppnat för ett begrepp per steg.
- **Gallring (`C-200`) är ett begrepp utan elementtyp**, "förstöring av allmänna handlingar, beslutad per handlingstyp och verksamhetsprocess med en frist", arkivets motsvarighet till Behandlingsändamål (`C-163`). Bevarande är utgångsläget och inget eget begrepp. Att gallra är en aktivitet, och gallrad betyder borttagen från varje lagringsyta. Representationen har inget tillstånd (`C-182`): att ärendet är arkiverat är verksamhetsobjektets läge.
- **Förteckningarna bor utanför lagret, lagret ger ankaret.** Varje regelverk fäster sina uppgifter på ett par i lagret: behandlingen på beteende och informationsobjekt, handlingstypen på beteende och representation. Vad som gäller för paret, ändamål, rättslig grund, bevarande och gallring med frist, står i regelverkets förteckning: registerförteckningen enligt dataskyddsförordningens artikel 30, arkivredovisningen, informationshanteringsplanen. Det ändras av juridiska skäl utan att arkitekturen gör det. Lagret bär ingen kopia och ingen pekare. ADR 0018:s mening om att ändamål och rättslig grund står i beteendets beskrivning ersätts.
- **Klassen stannar i lagret.** Den är informationsägarens beslut om informationen själv, och lagret räknar med den: ytan får det högst klassade objektets krav, området ger klassen nedåt (ADR 0030), och sammanställningen klassas för sig. De andra är beslut om vad som får göras med informationen.
- **Begreppen stannar i katalogen fast värdena lämnar lagret.** Behandlingsändamål (`C-163`), Rättslig grund (`C-164`) och Gallring (`C-200`) är begrepp, så att förteckningen och lagret talar samma språk. Det som lämnar lagret är värdet per anker.
- **Sekretessen sitter på uppgiften (`C-161`)**, det tydligaste fallet av reglering för sig. En uppgift som omfattas av sekretess är ett eget informationsobjekt med paragrafen i sin beskrivning. Sammanhanget "i ärende om" läses ur beteendet som har åtkomst, och sekretessmarkeringen på handlingen är representationens märkning (#26).
- **Informationshanteringsplanen är en bärare (`C-016`)**, inget begrepp. Den bär reglerna om registrering, bevarande och gallring per process och handlingstyp, och myndigheten fastställer den. Riksarkivets föreskrifter är den påverkan reglerna kommer ur. Detsamma gäller arkivredovisningen; registerförteckningen bär inga regler. Klassificeringsstrukturen är processkartan (`C-130`) läst ur lagret.
- **Representationen är ett tredje mål för har åtkomst till (`C-101`)**: beteendet har åtkomst till den representation det tar emot, upprättar, kopierar, lämnar ut eller gallrar. Ärende #23 frågar om beteendet når informationsobjektet direkt eller via verksamhetsobjektet; det får representationen som tredje mål att avgöra på samma gång.
- **Kopior:** samma representation på flera ytor är kopierad dit, och beteendet som gjorde kopian har gjort en behandling. En kopia i annan form är en ny representation. Radering ska nå varje yta. **Äkthet** är riktighet tillämpad på representationen över bevarandetiden, ingen femte klass. **Utlämnande**, registerutdrag och dataportabilitet är behandlingen lämna ut, med en representation i begärd form som utfall. Utdraget och portabilitetsfilen är sammanställningar upprättade på begäran.
- **Lagringsyta (`C-165`) får vara fysisk.** Definitionen blir "plats där representationer av information förvaras". En applikation tillhandahåller en digital yta; ett pappersarkiv eller ett skåp är en yta utan applikation. Typen stannar i applikationsperspektivet. Ärendeakten som plats är en lagringsyta per ärende. CMMN:s CaseFile förblir verksamhetsobjektet (`C-159`), och pappersakten är en representation.
- **Ägaren till en sammanställning avgörs inte här.** Arkivredovisningen ordnar handlingen under den process som upprättade den. Informationsägaren till sammanställningen står oavgjord tills rollen som äger ett verksamhetsbeteende finns (#24).
- **Tabellen ovan står bara här.** Begreppen bär var sin del; en läsartext i `docs/` hade varit en andra kopia.

## Övervägda alternativ

- **Allmän handling som text i `C-085` utan begrepp.** Ordet används dagligen på varje myndighet, och katalogen ska svara när ordet används (ADR 0030). Avvisat.
- **Allmän handling och handlingstyp som egna begrepp bredvid representationen.** Ärendets första bild. Nicklas avgjorde i ärendet att handlingen är formen och handlingstypen typen. Ett begrepp till hade varit samma sak sedd från lagen. Avvisat.
- **Bevarande och gallring som text i representationens eller beteendets beskrivning**, efter mönstret i ADR 0018 för ändamål och rättslig grund. Det var rekommendationen i första rundan. Nicklas: juridiken hör till en egen förteckning med samma styrobjekt. Ersatt av beslutet om förteckningarna.
- **Pekare i lagret till förteckningen**, "gallras enligt informationshanteringsplanen". En kopia som ruttnar. Avvisat.
- **Gallringsfrist som regel (`C-020`) med representationen som styrobjekt.** Styrobjekt (`C-003`) är verksamheten, en domän, en portfölj, inte en blankett. Fristen är det planen fastställer. Avvisat.
- **Registrering som begrepp.** Ordet är vanligt, men registreringen har inget värde per anker som förteckningen håller. Den är ett steg som alltid görs. Avvisat.
- **Ett begrepp Sekretess.** Katalogens princip att konfidentialiteten följer innehållet täcker det. Sekretessen är ett fall av reglering för sig. Avvisat.
- **Pappersarkivet som anläggning (`C-091`)**, ArchiMates Facility, med definitionen av lagringsyta orörd. Det ger två typer för "var ligger handlingen", och den som frågar måste veta vilken. Avvisat; definitionen vidgas.
- **Representationen med tillstånd**, arkiverad och gallrad som lägen. Tillståndet är verksamhetsobjektets och ingen annans (ADR 0024). Avvisat.
- **Att avgöra ägaren till sammanställningen nu**, som ägaren av det beteende som upprättade den. Rollen finns inte förrän #24 är avgjort, så det hade varit ett svar utan någon att peka på. Uppskjutet.

## Konsekvenser

- Nya begrepp `C-199` Allmän handling, underordnat `C-085`, och `C-200` Gallring, med associativa relationer till `C-085` och `C-016`, båda med anmärkning och exempel. `C-085` får handling och handlingstyp som tillåtna termer. `C-165` får ny definition.
- Meningar tillagda i `C-016`, `C-085`, `C-130`, `C-135`, `C-161`, `C-162`, `C-165`, `C-166`, `C-168` och `C-182`. Meningen om beskrivningen i `C-168` omskriven. ADR 0018 får en rad om att den meningen ersatts.
- Interlingua: ett ärende om att lämna ut ankarna som tabell, så att förteckningarna kan upprättas och förnyas ur kartan. Fyra listor: behandlingar (beteende och informationsobjekt, med ägare), handlingstyper (beteende och representation), klassificeringsstrukturen (processkartan som träd) och per lagringsyta (representationerna och det högst klassade objektet).
- Ärende #23 får en kommentar om representationen som tredje mål för `C-101`.
- Mallen körs inte om: ingen ny elementtyp.
