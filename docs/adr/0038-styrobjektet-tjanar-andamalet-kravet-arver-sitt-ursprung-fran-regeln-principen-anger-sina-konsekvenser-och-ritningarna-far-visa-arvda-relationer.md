# Styrobjektet tjänar ändamålet, kravet ärver sitt ursprung från regeln, principen anger sina konsekvenser, och ritningarna får visa ärvda relationer

Beslutat av Nicklas i grillningen av ärendena #90–#94, #98, #99, #101–#106, #108, #110–#113, 2026-11-09, två rundor (14 + 1 frågor). Ärendena kom ur aktualiseringen av ritningarna mot lagret (#73): pilar som ritningarna hade men lagret saknade, och ett schema som lagret sedan dess säger emot.

## Sammanhang

Regeln i #73 är att lagret vinner: en pil utan stöd i lagret står kvar tills Nicklas värderat den, och sedan får antingen lagret relationen eller ritningen mister pilen. Pilarna var av fyra slag. Relationer som anmärkningarna och besluten redan sade, på båda sidor, utan att någon frontmatter bar dem. Relationer som lagret har på ett överordnat begrepp, så att pilen går från det ärvande begreppet när det överordnade inte är med i ritningen. Förkortningar av en väg som lagret går i två steg. Och påståenden som besluten sedan pilen ritades har avvisat eller gjort smalare.

## Beslut

- **Frontmatter följer det texten och besluten redan säger.** Initiativ (`C-012`) åstadkommer Verksamhetsförändring (`C-172`); Verksamhetsförändring prövas mot Effektmål (`C-170`), direkt och inte via Bedömning (`C-185`), eftersom bedömningen är den som prövar medan relationen säger vad som prövas mot vad; Verksamhetsbeteende (`C-157`) har åtkomst till Verksamhetsobjekt (`C-159`); Verksamhetsobjekt realiseras av Informationsobjekt (`C-060`). Ingen ny definition, bara frontmatter som släpade efter.
- **Styrobjektet tjänar ändamålet.** Styrobjekt (`C-003`) får `tjänar` till Ändamål (`C-022`), 1..*: det är Ändamåls definition. Verksamhet (`C-007`), Verksamhetsdomän (`C-008`) och Lösning (`C-055`) ärver relationen via Arkitekturobjekt (`C-032`), som är en typ av Styrobjekt. Ett tillfälligt styrobjekt tjänar ett ändamål hos det det förändrar, så 1..* håller för alla.
- **En ritning får visa en ärvd relation** när det överordnade begreppet inte är med, och en ritning är ett urval som inte behöver visa alla relationer. Arkitekturprincip (`C-040`) härleds ur Ändamål genom Princip (`C-018`), och de tre pilarna *tjänar* i Arkitekturnivå står kvar. Ingen kopia läggs på det ärvande begreppet. Regeln står i README.
- **Principen anger sina konsekvenser, som association.** Princip (`C-018`) får `anger` till Konsekvens (`C-023`), 1..* vid Konsekvens: utan konsekvens är det en hållning. Konsekvens får `uttrycks som` till Krav (`C-021`), Regel (`C-020`) och Effekt (`C-024`), definitionens egna ord. Krav och regel är inte sorter av konsekvens: de kan komma direkt ur påverkan utan princip och är redan sorter av Styrmedel (`C-015`). Om Effekt är en typ av Konsekvens avgörs i #63.
- **Kravet ärver sitt ursprung från regeln.** Krav (`C-021`) mister sin egen `kan komma direkt ur` till Extern påverkan (`C-029`) och ärver Regels relation till Påverkan (`C-184`), som ADR 0037 gav regeln. Kravs egen relation var smalare än lagret: domänägarens krav på lösningarna under kommer ur intern påverkan.
- **Domänen använder ingen lösning.** Lösningar i andra domäner använder dess leveransprodukter (`C-174`), och deras behov blir intern påverkan på lösningens ändamål. Anmärkningen i Lösning (`C-055`) säger nu det; ingen relation.
- **Vägningen mellan principer är ingen relation.** Den sker i ett val, av den som väljer, mot de principer som berör valet. Ändamål (`C-022`) har samma mening och ingen relation till sig självt. Pilen *vägs mot* bort.
- **Bär och aggregerar är två nivåer.** *Bär* är begreppsrelationen från Bärare (`C-016`) till styrmedlet; aggregerar (`C-100`) är relationstypen lagret skriver den med mellan ett bärarelement och ett målelement, det ADR 0019 beskrev. Begreppsmodellen visar *bär*; anmärkningen i Bärare säger hur det skrivs i lagret.
- **Markeringen `decided_by: [reference]` är en spärr, ingen relation.** Bland arkitekturbeskrivningarna får bara en referensarkitektur fastställa en princip; en beskrivning av annat slag listar den utan att fastställa den. Verksamhetens princip fastställs genom sin bärare, utanför beskrivningarna. Princip (`C-018`) behåller markeringen, och ritningen behöver ingen pil Princip → Referensarkitektur.
- **Förkortningar ersätts av vägen lagret går.** Arkitektur (`C-031`) realiseras enligt Målarkitektur (`C-054`), inte enligt beskrivningen i allmänhet: Målarkitektur ritas in. Arkitekturbeskrivning (`C-035`) beskrivs ur perspektivet och följer metamodellen genom Arkitekturvy (`C-052`): vyn ritas in med lagrets tre relationer.
- **Det avvisade tas bort.** Arkitekturprincip gäller för Aspekt (`C-004`) avvisades i ADR 0037; pilen och rutan bort ur två ritningar. Schemat Styrobjektet som saknas tas bort ur `layout/`: lagret säger sedan ADR 0020 och ADR 0036 att det varaktiga styrobjektet finns, Lösning (`C-055`), och att felet sitter i delat mandat och i snittet.

## Övervägda alternativ

- **Tre kopior av tjänar**, en på var och en av Verksamhet, Verksamhetsdomän och Lösning. Säger samma sak tre gånger och ändras på tre ställen. Avvisat.
- **Egen härleds ur på Arkitekturprincip**, så att pilen får stöd utan regel om arv. En dubblett av Princips relation. Avvisat.
- **Komposition mellan princip och konsekvens.** Konsekvensen är ingen exklusiv del som följer principen i lagret, och *anger* är ordet texten redan använder. Avvisat.
- **Krav, regel och effekt som sorter av konsekvens.** Krav och regel kan komma direkt ur påverkan och har redan Styrmedel som överordnat begrepp. Avvisat för dem; Effekt prövas i #63.
- **Verksamhetsförändring prövas mot effektmålet via bedömningen.** Lagret har redan formen det prövade → det det prövas mot. Avvisat.
- **Relationen använder från Verksamhetsdomän till Lösning**, 0..* åt båda håll. Mekanismen är leveransprodukten. Avvisat.
- **Pilen Princip → Referensarkitektur i ritningen**, om markeringen stod kvar. Markeringen är en spärr, och verksamhetens princip fastställs av sin bärare. Avvisat.
- **Schemat Styrobjektet som saknas ritas om som exempelorganisationens nuläge.** Exempelorganisationerna har portfölj och lösningsägare med ram och mål; ett nuläge att rita finns inte. Avvisat; vill Nicklas ha berättelsen blir det ett nytt schema ur Objektstyrning (`C-048`) och ADR 0036.

## Konsekvenser

- Nya relationer i frontmatter: `C-003` `tjänar` → `C-022`; `C-012` `åstadkommer` → `C-172`; `C-018` `anger` → `C-023`; `C-023` `uttrycks som` → `C-021`, `C-020`, `C-024`; `C-157` `har åtkomst till` → `C-159`; `C-159` `realiseras av` → `C-060`; `C-172` `prövas mot` → `C-170`. Borttagen: `C-021` `kan komma direkt ur` → `C-029`. Anmärkningar ändrade i `C-016`, `C-018`, `C-021` och `C-055`. Inga definitioner ändrade.
- `CONTEXT.md`: posten Styrmedelselement säger att `decided_by` är en spärr. `README.md`: regeln om ärvda relationer i ritningar.
- Ritningarna: Från princip till krav får rutan Påverkan (`C-184`), Begreppsmodell arkitekturprinciper får Målarkitektur (`C-054`) och Arkitekturvy (`C-052`); pilarna *använder*, *vägs mot*, *aggregerar*, *gäller för* (Aspekt), *beskrivs ur*, *följer* (från beskrivningen) och Kravs *kan komma direkt ur* bort; *anger* ritas som association. `layout/Styrobjektet som saknas.drawio.svg` borttagen, och med den dess post på ritningssidan (`.github/pages/ritningar/index.html`).
- Begreppsmodell arkitekturprinciper saknar rutan Påverkan (`C-184`) och visar därför inte Regels och Principens relationer till den; ett urval, antecknat i #73. #63 får hänvisning hit för F15 och F17, #70 för vägningen, #71 för aspekten.
