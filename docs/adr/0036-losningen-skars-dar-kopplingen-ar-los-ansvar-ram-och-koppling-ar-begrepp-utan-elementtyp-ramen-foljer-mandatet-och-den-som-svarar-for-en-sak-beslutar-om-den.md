# Lösningen skärs där kopplingen är lös; Ansvar, Ram och Koppling är begrepp utan elementtyp; ramen följer mandatet, och den som svarar för en sak beslutar om den

Beslutat av Nicklas 4 november 2026, efter ett samtal om vad effektiv styrning är och om pm3:s objektstyrning är ett effektivt sätt att styra. Beslutet avgör vad ett effektivt snitt av lösningar är, om ansvar och mandat är två begrepp, och vad som måste finnas för att ett mandat ska vara reellt.

Beslut 49 ändrar en punkt här: Koppling (`C-211`) har fått en vidare definition och råder också mellan styrobjekt och mellan det två ägare håller.

## Sammanhang

Samtalet började i frågan vad effektiv styrning är och om objektstyrning (`C-048`), pm3:s förvaltningsobjekt, är ett effektivt sätt att styra. Nicklas erfarenhet: objektet sammanfaller sällan med en lösning som har en ägare, och därför fungerar det sällan. Med katalogens ord brister objektstyrningen på tre sätt. Målet landar på objektet i stället för på förmågan, fast beslut 20 sätter målet på förmågan och ramen på lösningen. Mandatet är delat mellan en objektägare från verksamheten och en från IT, fast styrning (`C-002`) förutsätter mandat. Och återkopplingen är ett år lång.

Det delade mandatet visade sig vara kärnan. pm3 delar ägandet längs komponentaxeln: verksamheten äger beteende och information, IT äger tekniken, och objektet ritas som ett överlapp mellan dem. Då äger var och en sina komponenter, och det enda som gör dem till en lösning, att de hänger ihop, äger ingen. Katalogen sade redan att det som bara kan beskrivas ur ett perspektiv är en vy och ingen lösning (`C-055`). Ansvar som skärs på komponent utan lösningsansvar är ägarskap över vyer.

Men felet är oftast snittet, inte forumet. Traditionella organisationer skär ansvaret på komponent därför att lösningarna aldrig skurits. Lagret hade reglerna för var en lösning går, ändamål och användare, en förmåga per lösning, det flera använder bryts ut, men inget prov som säger om ett snitt är bra. Och lagret skilde mandat (`C-189`), befogenheten att besluta, från att ansvara för (`C-208`), att äga och ytterst svara för, utan att säga det. Ramen nämndes i åtta begrepp och beslut 20 utan att vara ett begrepp.

Nicklas drev fyra saker som formade utfallet: att en förmåga kan realiseras av två lösningar som inte behöver ändras tillsammans, så att tvingad samförändring är ett fynd som kan gå åt båda hållen; att kopplingens täthet är måttet, med Normal Accidents och cybernetiken som bakgrund; att ansvar är ett så vanligt och svårorienterat ord att det behöver ett begrepp, så att en begreppsmodell kan ritas; och att ett fynd kan vara ett snitt som går att ändra eller ett som inte går.

## Beslut

- **Provet för ett snitt står i Lösning (`C-055`), fyra delar.** Samförändring: två lösningar ska kunna ändras var för sig; måste de alltid ändras tillsammans är snittet fel, och förmågekartan visar om de är en lösning eller hör till två förmågor. Gränssnittet: gränsen går där kopplingen är lös, och det som korsar den är en leveransprodukt (`C-174`) med krav (`C-021`) och överenskommelse (`C-084`); provet gäller komponenterna, resurser korsar fritt. Mandatet: ägaren kan besluta över varje komponent innanför och har ramen att genomföra. Delning: det flera använder bryts ut. Parnas (1972) nämns som regelns källa. Katalogen definierar provet; en organisation som antar det gör det som arkitekturprincip (`C-040`) i sin referensarkitektur. Katalogen får ingen egen referensarkitektur.
- **IT:s ägande är tre saker och aldrig en fjärde**, i `C-055`: arkitekturansvar (`C-117`) för vyerna, systemägare per applikation under lösningsägaren, och egna plattformslösningar som levererar leveransprodukter mot krav. Aldrig lösningsägare till verksamhetens lösning.
- **Koppling (`C-211`) är ett begrepp utan elementtyp**: graden i vilken en ändring i en lösning eller komponent tvingar fram en ändring i en annan vid samma tidpunkt. Tät och lös är ändarna, i texten. Perrow (1984) är källan. Kopplingen råder mellan lösningar, och lösningen avgränsas av den. Två sorters fynd: en tät koppling som går att lösa blir ett initiativ (`C-012`); en som inte går att lösa skrivs som en bedömning (`C-185`) på lösningen, som ägaren bär.
- **Ansvar (`C-209`) är ett begrepp utan elementtyp**: skyldighet för en roll att svara för ett styrobjekts utfall eller för ett arkitekturelement, och att stå till svars för det. Mandat är rätten att besluta, ansvar är att svara för utfallet, och de hör till samma roll: **för varje sak som ägs beslutar den som svarar för den.** Regeln gäller per sak, inte per roll, så tredelningen i beslut 35 står: linjechefen beslutar om och svarar för förekomsterna, processägaren om och för typen. Arkitekturansvar (`C-117`) får Ansvar som generiskt begrepp. Ansvaret för ett styrobjekt följer mandatet; ansvaret för ett arkitekturelement skrivs med ansvarar för (`C-208`).
- **Vad ett ansvar förutsätter står i Ansvar**: befogenheten, en regel; ramen över styrobjektet; ett styrobjekt skuret så att besluten når det utfallet beror på; och att utfallet prövas mot målet genom en bedömning som leder till styrbeslut. Befogenheten kan hållas utan medel, ansvaret kan inte bäras utan. Saknas något har rollen befogenheten men kan inte bära ansvaret, och det är katalogens namn på det pm3 gör.
- **Ram (`C-210`) är ett begrepp utan elementtyp under Styrmedel (`C-015`)**: resurser som en överordnad styrning tilldelar ett styrobjekt för en planeringsperiod. Registreras som regel (`C-020`) när den ritas. **Ramen följer mandatet**: den som har mandatet över ett styrobjekt håller dess ram, och ramen sätts av den som äger det omslutande styrobjektet. Ingen relationstyp för pengar i lagret; beslut 20 står.
- **Begreppsmodellen**, fjorton relationer mellan begreppen, ritad som "Mandat och ansvar begreppsmodell" i `layout/`: Roll bär Mandat och Ansvar; Mandat avser Styrobjekt, ges som Regel, utövas genom Styrbeslut; Ansvar avser Styrobjekt, förutsätter Mandat, prövas genom Bedömning; Bedömning prövar mot Mål och leder till Styrbeslut; Ram tilldelas Styrobjekt och följer Mandat; Koppling råder mellan Lösning, Lösning avgränsas av Koppling. Avvikelse är inget begrepp: den är innehållet i en bedömning.
- **Objektforumet**, i `C-048`: ett kravforum när var sida äger en hel lösning, en kommitté som ersätter ett saknat mandat när två halvägare möts. Snittet avgör vilket.

## Övervägda alternativ

- **Proven som katalogens egna arkitekturprinciper i en referensarkitektur.** C-040 säger att en princip beslutas genom en antagen referensarkitektur, och katalogen är ingen sådan. Avvisat; exempelorganisationerna antar provet i stället, så att läsaren ser hur man gör. Kan omprövas om fler principer samlas.
- **Samförändring som fynd bara om lösningen.** Nicklas: en förmåga kan ha två lösningar som ändras var för sig; tvingad samförändring kan betyda att förmågekartan är för fin lika väl som att lösningarna är en. Ersatt av ett fynd åt båda hållen.
- **Slå ihop två lösningar som en plattform tvingar att ändras tillsammans.** De har olika ändamål och användare. Avvisat; fyndet riktas mot plattformens gränssnitt och skrivs som krav eller bedömning.
- **Koppling som text i C-055.** Rekommendationen i andra rundan. Nicklas: begrepp utan elementtyp, så att det kan stå i begreppsmodellen. Ersatt.
- **Ansvar som mening i Mandat.** Rekommendationen i första rundan, med regeln mot kaninhålet som skäl. Nicklas: ordet är för vanligt och för svårorienterat, och utan begrepp kan sambanden inte ritas. Ersatt av begreppet.
- **Avvikelse som begrepp.** Innehållet i en bedömning, inget eget. Avvisat.
- **Ram som styrbeslut.** Styrbeslutet är ett vägval i en enskild fråga; ramen gäller för en period och anger binärt vad som får förbrukas. Regel valdes.
- **Ramen som relation i lagret.** Pengaflödet är ekonomistyrning och ritas inte (beslut 20). Relationen finns i begreppsmodellen, inte som relationstyp.
- **Forummeningen i Forum (C-156).** Skulle peka ut pm3 i ett allmänt begrepp. Lagd i C-048.

## Konsekvenser

- Nya begrepp `C-209` Ansvar, `C-210` Ram (generisk `C-015`) och `C-211` Koppling, alla utan elementtyp, med anmärkning och exempel. `C-117` får generiskt begrepp `C-209`. Associativa relationer med etikett på `C-209`, `C-189`, `C-185`, `C-210`, `C-211` och `C-055` enligt begreppsmodellen.
- Meningar tillagda i `C-003`, `C-048`, `C-055`, `C-117`, `C-185` och `C-189`. Mappningstabellerna ändras inte: inga nya typer.
- Exempelorganisationerna: Brinkstadsbostäders Felanmälan som lösning med teknisk chef som lösningsägare, och fastighetssystemets delade release som tät koppling buren som bedömning; myndighetens handläggning med Föreningsregistret som leveransprodukt i lös koppling, och snittprovet som arkitekturprincip i myndighetens referensarkitektur.
- Ritningen "Mandat och ansvar begreppsmodell" i `layout/`, gjord med `diagram-editable`.
- #38: delen om delat ägarskap är avgjord av regeln per sak; resten står kvar. #40: Beers krav att en enhet har resurser för sin autonomi är detsamma som medel för ansvaret.
- #42, klarspråk i katalogens texter, öppnades ur grillningens runda 3: texterna här är skrivna i den andan, de äldre väntar.
