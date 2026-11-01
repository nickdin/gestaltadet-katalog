# Målet förblir styrmedel och ritas som styrmedelselement; portfölj är en elementtyp i strategiperspektivet

Beslutat av Nicklas i den första av grillningarna av de öppna frågorna inför draw.io-mallen.

## Sammanhang

Frågan väcktes i ett samtal om portföljstyrning: hur mål, initiativ, portfölj och delportföljer hänger ihop ska kunna ritas, och hur beslutsfattandet knyts dit. Initiativ är elementtyp sedan ADR 0010. Mål (`C-017`) är ett styrmedel, `kind: governance-type`, och frågan antog att det därför inte kan ritas i en vy.

Premissen stämde inte längre. Interlingua har styrmedelselement: ett element vars typ är ett styrmedel, utan detaljeringsgrad, beslutat av de antagna beskrivningar som listar det, och visat i varje vy vars perspektiv det namnger i `perspectives`. Lagret hade redan sådana, av typen bärare: organisationens verksamhetsplan, med sina huvudmål och förväntade resultat i sin text. Inget mål var skrivet.

Nicklas egen informationsmodell för effektuppföljning skiljer verksamhetsmål, effektmål och produktmål, i kedjan initiativ realiserar produktmål, produktmål bidrar till effektmål, effektmål bidrar till verksamhetsmål, med mått, mättillfälle, utfall, prognos och effektkategori runt effektmålet. Hans nylägesskiss byter produktmål mot leverabel och lägger till verksamhetsförmåga och verksamhetsförändring mellan leverabeln och målet. ArchiMates Goal är verksamhetsmålet, dess Outcome effektmålet.

Delportföljen fanns som informationsobjekt, i informationsperspektivet. En vy håller ett perspektivs element, så initiativen i sin delportfölj kunde inte bli en vy.

## Beslut

- Mål förblir styrmedel, `kind: governance-type`, och skrivs som styrmedelselement. Det namnger strategiperspektivet och de perspektiv vars vyer ska visa det: organisationens och avdelningens mål som initiativen prövas mot står i strategivyn, ett mål för en applikation också i applikationsvyn. Fältet säger var målet ritas, inte vad det påverkar.
- Relationen från ett initiativ till det mål det prövas mot är `påverkar` (`C-102`), ArchiMates Influence, samma pil som ADR 0010 gav initiativet mot det det ändrar. Initiativet påverkar också den verksamhetsförmåga det utvecklar. Ingen ny relationstyp.
- En måltyp. Verksamhetsmål (`C-169`) och effektmål (`C-170`) är begrepp som registreras som mål, som projekt registreras som initiativ; skillnaden är detaljeringsgrad och uttrycks med `förfinar` (`C-103`): effektmålet förfinar sitt verksamhetsmål, ett delmål sitt mål. Verksamhetsplanens förväntade resultat är effektmål.
- Produktmål tas inte in. Leverabel (`C-171`) är begreppet för det ett initiativ lämnar ifrån sig, och leverabeln registreras som det element den blir, applikation, process eller bärare, med initiativet som påverkar eller, i en målbild, ersätter det. Ingen ruta för ArchiMates Deliverable.
- Verksamhetsförändring (`C-172`) är ett begrepp, inget element: skillnaden mellan nulägets och målbildens beskrivningar, det `ersätter` och gapanalysen räknar fram. Den är en effekt (`C-024`), prövas mot effektmålet och ersätter det inte.
- Mått, mättillfälle, utfall, prognos, effektkategori och effekthemtagningsansvarig blir inte katalogbegrepp. Målvärde, måldatum, mått, kategori och ansvarig står i målets text; utfall och prognos är uppföljningens information och blir informationsobjekt den dag uppföljningen beskrivs.
- Bäraren ett mål står i aggregerar (`C-100`) sina mål: aggregering, inte består av, eftersom ett styrmedel kan byta bärare utan att ändra innehåll.
- Portfölj (`C-011`) blir elementtyp i strategiperspektivet, bredvid verksamhetsförmåga och initiativ. Både den centrala portföljen och varje delportfölj registreras som portfölj; portföljen aggregerar delportföljerna, delportföljen sina initiativ, och produkterna med samma relation, synlig i lagret men i ingen vy. Definitionen står kvar, liksom den öppna frågan om förvaltningsobjekt.
- ArchiMate: Goal och Outcome mappar båda till `C-017`, Outcome märkt tveksam. Portföljen står under `unmapped-concepts` i båda tabellerna, som initiativet. ARIS-tabellen är obekräftad i sin helhet; en rad för mål där är ett interlingua-ärende.
- Bilden blir en ny vy i strategiperspektivet, bredvid vyn över vad som pågår: organisationens verksamhetsplansmål som styrmedelselement, listade av avdelningens beskrivning för att visa att de gäller utan att beslutas där, avdelningens egna mål, dess initiativ med `påverkar` mot de mål de prövas mot, och delportföljen som aggregerar initiativen. Ett initiativ som inte prövas mot något mål står utan pil; det är vad bilden ska visa. Forumen och beslutsvägen stannar i vyn över hur portföljen styrs; inga styrbeslutselement per finansieringsbeslut nu. Den beskrivning som beslutar organisationens mål är organisationens egen; den behöver inte finnas för att målen ska kunna listas.

## Övervägda alternativ

- **Mål som elementtyp i strategiperspektivet.** Målet är en måttstock som alla andra styrmedel, hör inte till ett perspektiv, och interlinguas ADR 0008 hade låst det till strategin. Avvisat.
- **`realiseras av` från mål till initiativ.** Säger att initiativet ensamt gör målet nått; ArchiMate reserverar Realization mot ett Goal för Outcome. Avvisat. **En ny relationstyp "bidrar till"**: ett ord till för Influence. Avvisat.
- **Tre styrmedelstyper**, verksamhetsmål, effektmål, produktmål: tre rutor i mallens Styrmedel-grupp och varje mål måste sorteras, för en skillnad som är detaljeringsgrad. Avvisat. **Två typer**, Mål och Effektmål. Avvisat av samma skäl.
- **Utfall som eget begrepp för ArchiMates Outcome.** Att målet nåddes är prövningen, inte ett element. Avvisat; i stället en Outcome-rad till `C-017`.
- **Leverabel som elementtyp.** Varje leverans får två element, leverabeln och det den är, med en pil emellan. Avvisat. **Lämna ordet helt.** Avvisat: ordet ska vara sökbart och säga var saken står.
- **Verksamhetsförändring som element.** Ritar det programmet redan räknar ut. Avvisat; begrepp med anmärkning.
- **En egen relationstyp "utvecklar"** mellan initiativ och förmåga. `påverkar` räcker. Avvisat.
- **Portfölj förblir begrepp och informationsobjekt.** Bilden kan då bara bli en lös ritning i `layout/`, utan vy. Avvisat. **Portfölj som arkitekturobjekt.** Får då ingen ruta i någon vy. Avvisat.
- **Ingen relation mellan mål och bärare**, bara `sources`. Kopplingen syns då bara i filen. Avvisat. **En ny relationstyp "bär".** Avvisat.
- **Bygga ut vyn över vad som pågår med målen** i stället för en ny vy. Den svarar på vad som pågår, den nya på vad det prövas mot. Avvisat.
- **Alla mål namnger bara strategiperspektivet.** Enklare regel, men ett applikationsmål kan aldrig stå bredvid sin applikation. Avvisat.

## Konsekvenser

- `C-011 Portfölj` får `kind: element-type`; `C-108 Strategiperspektiv` täcker verksamhetsförmåga, initiativ och portfölj. Delportföljen är en portfölj och flyttar ur informationsvyn.
- `C-169 Verksamhetsmål`, `C-170 Effektmål` (båda under `C-017`, effektmålet förfinar verksamhetsmålet), `C-171 Leverabel`, `C-172 Verksamhetsförändring`: begrepp utan `kind`, med anmärkningar som säger hur de används. `C-017`, `C-012` och `C-024` får anmärkningarna ovan.
- `mapping/archimate.yaml`: raden Outcome till `C-017`, tveksam; `C-011` under `unmapped-concepts`. `mapping/aris.yaml`: `C-011` under `unmapped-concepts`.
- draw.io-mallen byggs om från täckningslistorna: strategigruppen får rutan Portfölj; Styrmedel-gruppen ändras inte.
- Nästa steg: de första målen som styrmedelselement, verksamhetsplanens huvudmål med sina förväntade resultat som effektmål, verksamhetsplanen som aggregerar dem, initiativen med `påverkar`, och den nya vyn med sin ritning i `layout/`. Hos Myndigheten för föreningsstöd vore målen regleringsbrevets: att nio av tio ansökningar är beslutade inom fyra månader, att andelen bidrag som återkrävs minskar.
- Frågan om förmågetjänst, parkerad tills detta var klart, kan tas (ADR 0021).
- Begreppsmodellen `layout/Verksamhetsinformation begreppsmodell.drawio.svg` rörs inte: inget av dagens begrepp finns i den. Målkedjan har en egen syskonbild, `layout/Målstyrning begreppsmodell.drawio.svg`: styrmedel, ändamål, bärare, portfölj, verksamhetsmål, mål, initiativ, verksamhetsförmåga, effektmål, verksamhetsförändring, leverabel och effekt med relationerna ovan.
