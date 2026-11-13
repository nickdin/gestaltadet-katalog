# Målet förblir styrmedel och ritas som styrmedelselement; portfölj är en elementtyp i strategiperspektivet

*Två led gäller inte längre. Produkter står inte i portföljen. Och delportföljen är ingen egen sort: varje verksamhetsdomän har en portfölj, och de ligger i varandra (beslut 51).*

Beslutat av Nicklas 29 oktober 2026, när han ville kunna rita hur mål, initiativ och portföljer hänger ihop.

## Sammanhang

Frågan väcktes i ett samtal om portföljstyrning: hur ska det gå att rita hur mål, initiativ, portfölj och delportföljer hänger ihop, och hur knyts beslutsfattandet dit? Initiativ är elementtyp sedan beslut 10. Mål (`C-017`) är ett styrmedel, `kind: governance-type`, och frågan antog att det därför inte kan ritas i en vy.

Premissen stämde inte längre. Interlingua har styrmedelselement: ett element vars typ är ett styrmedel. Det har ingen detaljeringsgrad, beslutas av de antagna beskrivningar som listar det, och visas i varje vy vars perspektiv det namnger i `perspectives`. Lagret hade redan sådana, av typen bärare: organisationens verksamhetsplan, med sina huvudmål och förväntade resultat i sin text. Inget mål var skrivet.

Nicklas egen informationsmodell för effektuppföljning skiljer verksamhetsmål, effektmål och produktmål. Kedjan är: initiativ realiserar produktmål, produktmål bidrar till effektmål, effektmål bidrar till verksamhetsmål. Runt effektmålet står mått, mättillfälle, utfall, prognos och effektkategori. Hans nylägesskiss byter produktmål mot leverabel och lägger till verksamhetsförmåga och verksamhetsförändring mellan leverabeln och målet. ArchiMates Goal är verksamhetsmålet, dess Outcome effektmålet.

Delportföljen fanns som informationsobjekt, i informationsperspektivet. En vy håller ett perspektivs element, så initiativen i sin delportfölj kunde inte bli en vy.

## Beslut

- Mål förblir styrmedel, `kind: governance-type`, och skrivs som styrmedelselement. Målet namnger strategiperspektivet och de perspektiv vars vyer ska visa det. Organisationens och avdelningens mål, som initiativen prövas mot, står i strategivyn; ett mål för en applikation står också i applikationsvyn. Fältet säger var målet ritas, inte vad det påverkar.
- Relationen från ett initiativ till det mål det prövas mot är `påverkar` (`C-102`), ArchiMates Influence. Det är samma pil som beslut 10 gav initiativet mot det det ändrar. Initiativet påverkar också den verksamhetsförmåga det utvecklar. Ingen ny relationstyp.
- En måltyp. Verksamhetsmål (`C-169`) och effektmål (`C-170`) är begrepp som registreras som mål, som projekt registreras som initiativ. Skillnaden mellan dem är detaljeringsgrad och uttrycks med `förfinar` (`C-103`): effektmålet förfinar sitt verksamhetsmål, ett delmål sitt mål. Verksamhetsplanens förväntade resultat är effektmål.
- Produktmål tas inte in. Leverabel (`C-171`) är begreppet för det ett initiativ lämnar ifrån sig. Leverabeln registreras som det element den blir, applikation, process eller bärare; initiativet påverkar elementet eller, i en målbild, ersätter det. Ingen ruta för ArchiMates Deliverable.
- Verksamhetsförändring (`C-172`) är ett begrepp, inget element. Den är skillnaden mellan nulägets och målbildens beskrivningar, det som `ersätter` och gapanalysen räknar fram. Den är en effekt (`C-024`): den prövas mot effektmålet och ersätter det inte.
- Mått, mättillfälle, utfall, prognos, effektkategori och effekthemtagningsansvarig blir inte katalogbegrepp. Målvärde, måldatum, mått, kategori och ansvarig står i målets text. Utfall och prognos är uppföljningens information och blir informationsobjekt den dag uppföljningen beskrivs.
- Bäraren som ett mål står i aggregerar (`C-100`) sina mål. Det är aggregering, inte består av, eftersom ett styrmedel kan byta bärare utan att ändra innehåll.
- Portfölj (`C-011`) blir elementtyp i strategiperspektivet, bredvid verksamhetsförmåga och initiativ. Både den centrala portföljen och varje delportfölj registreras som portfölj. Portföljen aggregerar delportföljerna och delportföljen sina initiativ; produkterna aggregeras med samma relation, synlig i lagret men i ingen vy. Definitionen står kvar, liksom den öppna frågan om förvaltningsobjekt.
- ArchiMate: Goal och Outcome mappar båda till `C-017`, Outcome märkt tveksam. Portföljen står under `unmapped-concepts` i båda tabellerna, som initiativet. ARIS-tabellen är obekräftad i sin helhet, och en rad för mål där är ett interlingua-ärende.
- Bilden blir en ny vy i strategiperspektivet, bredvid vyn över vad som pågår. Den visar organisationens verksamhetsplansmål som styrmedelselement, listade av avdelningens beskrivning för att visa att de gäller utan att beslutas där; avdelningens egna mål; dess initiativ med `påverkar` mot de mål de prövas mot; och delportföljen som aggregerar initiativen. Ett initiativ som inte prövas mot något mål står utan pil, och det är vad bilden ska visa. Forumen och beslutsvägen stannar i vyn över hur portföljen styrs; inga styrbeslutselement per finansieringsbeslut nu. Den beskrivning som beslutar organisationens mål är organisationens egen, och den behöver inte finnas för att målen ska kunna listas.

## Övervägda alternativ

- **Mål som elementtyp i strategiperspektivet.** Målet är en måttstock som alla andra styrmedel och hör inte till ett perspektiv; interlinguas beslut 8 hade låst det till strategin. Avvisat.
- **`realiseras av` från mål till initiativ.** Det säger att initiativet ensamt gör målet nått, och ArchiMate reserverar Realization mot ett Goal för Outcome. Avvisat. **En ny relationstyp "bidrar till"**: ett ord till för Influence. Avvisat.
- **Tre styrmedelstyper**, verksamhetsmål, effektmål, produktmål. Det ger tre rutor i mallens Styrmedel-grupp, och varje mål måste sorteras, för en skillnad som är detaljeringsgrad. Avvisat. **Två typer**, Mål och Effektmål. Avvisat av samma skäl.
- **Utfall som eget begrepp för ArchiMates Outcome.** Att målet nåddes är prövningen, inte ett element. Avvisat; i stället får `C-017` en Outcome-rad.
- **Leverabel som elementtyp.** Varje leverans får två element, leverabeln och det den är, med en pil emellan. Avvisat. **Lämna ordet helt.** Avvisat: ordet ska vara sökbart och säga var saken står.
- **Verksamhetsförändring som element.** Det ritar det programmet redan räknar ut. Avvisat; den blir ett begrepp med anmärkning.
- **En egen relationstyp "utvecklar"** mellan initiativ och förmåga. `påverkar` räcker. Avvisat.
- **Portfölj förblir begrepp och informationsobjekt.** Bilden kan då bara bli en lös ritning i `layout/`, utan vy. Avvisat. **Portfölj som arkitekturobjekt.** Den får då ingen ruta i någon vy. Avvisat.
- **Ingen relation mellan mål och bärare**, bara `sources`. Kopplingen syns då bara i filen. Avvisat. **En ny relationstyp "bär".** Avvisat.
- **Bygga ut vyn över vad som pågår med målen** i stället för en ny vy. Den vyn svarar på vad som pågår, den nya på vad det prövas mot. Avvisat.
- **Alla mål namnger bara strategiperspektivet.** Regeln är enklare, men ett applikationsmål kan då aldrig stå bredvid sin applikation. Avvisat.

## Konsekvenser

- `C-011 Portfölj` får `kind: element-type`, och `C-108 Strategiperspektiv` täcker verksamhetsförmåga, initiativ och portfölj. Delportföljen är en portfölj och flyttar ur informationsvyn.
- `C-169 Verksamhetsmål`, `C-170 Effektmål`, `C-171 Leverabel` och `C-172 Verksamhetsförändring` blir begrepp utan `kind`, med anmärkningar som säger hur de används. Verksamhetsmål och effektmål står båda under `C-017`, och effektmålet förfinar verksamhetsmålet. `C-017`, `C-012` och `C-024` får anmärkningarna ovan.
- I `mapping/archimate.yaml` får Outcome en rad till `C-017`, märkt tveksam, och `C-011` står under `unmapped-concepts`. I `mapping/aris.yaml` står `C-011` under `unmapped-concepts`.
- draw.io-mallen byggs om från täckningslistorna: strategigruppen får rutan Portfölj; Styrmedel-gruppen ändras inte.
- Nästa steg är de första målen som styrmedelselement: verksamhetsplanens huvudmål, med sina förväntade resultat som effektmål; verksamhetsplanen som aggregerar dem; initiativen med `påverkar`; och den nya vyn med sin ritning i `layout/`. Hos Myndigheten för föreningsstöd vore målen regleringsbrevets: att nio av tio ansökningar är beslutade inom fyra månader, att andelen bidrag som återkrävs minskar.
- Frågan om förmågetjänst, parkerad tills detta var klart, kan tas (beslut 21).
- Begreppsmodellen `layout/Verksamhetsinformation begreppsmodell.drawio.svg` rörs inte, eftersom inget av dagens begrepp finns i den. Målkedjan har en egen syskonbild, `layout/Målstyrning begreppsmodell.drawio.svg`, med styrmedel, ändamål, bärare, portfölj, verksamhetsmål, mål, initiativ, verksamhetsförmåga, effektmål, verksamhetsförändring, leverabel och effekt, och relationerna ovan.
