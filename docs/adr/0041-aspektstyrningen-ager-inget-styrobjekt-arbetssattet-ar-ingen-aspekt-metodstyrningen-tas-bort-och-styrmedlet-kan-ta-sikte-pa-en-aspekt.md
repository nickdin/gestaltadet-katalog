# Aspektstyrningen äger inget styrobjekt, arbetssättet är ingen aspekt, metodstyrningen tas bort, och styrmedlet kan ta sikte på en aspekt

*Beslut 50 preciserar två saker här. Den som har aspektens mandat fastställer regler men beslutar aldrig i ett enskilt fall. Och den som avgör ett undantag kan ge undantaget eller låta ändra regeln.*

Beslutat av Nicklas 12 november 2026, när två fynd om Metodstyrning (`C-051`) inte gick att avgöra utan att hela indelningen av styrningen prövades först.

## Sammanhang

Granskningen i #43 hade två fynd om Metodstyrning (`C-051`). Det första, F19: definitionen gjorde den till en aspektbaserad styrning med aspekten arbetssätt och metod, men den aspekten finns inte bland de fyra som Aspekt (`C-004`) räknar upp. Det andra, F20: beslut 26 avgränsade metodstyrningen till hur arkitekturen arbetas fram, medan beslut 28 och Arbetssätt (`C-196`) lät den gälla valet av arbetssätt i allmänhet.

Beslut 37 sköt fynden hit. Nicklas ville först pröva styrlogiken i ett stycke: Styrning (`C-002`), Styrobjekt (`C-003`), Aspekt (`C-004`), Objektbaserad styrning (`C-005`) och Aspektbaserad styrning (`C-006`). Han frågade också om metod är något annat än beteende och arbetssätt.

Katalogen sade inte heller varifrån en aspektbaserad styrning har sin befogenhet. Mandat (`C-189`) gäller ett styrobjekt, och ett styrobjekt har en ägare, aldrig två (beslut 35).

## Beslut

- **Indelningen i objektbaserad och aspektbaserad styrning håller.** Den objektbaserade styrningen äger sitt styrobjekt genom mandat. Den aspektbaserade äger inget styrobjekt. Myndighetens generaldirektör äger utvecklingsportföljen. Ekonomichefen styr kostnaden i portföljen, i handläggningen och i Ärendesystemet utan att äga något av dem.
- **Aspektstyrningens mandat är utdelat och begränsat till en aspekt.** Ägaren av det omslutande styrobjektet delar ut det, och ägandet stannar hos den ägaren. Generaldirektören ger ekonomichefen rätt att fastställa ekonomiregler för hela myndigheten. Mandat (`C-189`) behåller sin definition.
- **Aspektens styrmedel binder ägaren.** Ägaren beslutar inom dem. Ett undantag avgör den som gav båda sina mandat. Chefen för Bidragsenheten kan inte sätta regeln om personalbudgeten åt sidan, och ekonomichefen kan inte besluta om handläggningen. Generaldirektören avgör.
- **Aspekterna är fyra, och listan är sluten.** Arbetssätt är ingen aspekt. En aspekt gäller tvärs över alla perspektiv. Säkerheten gäller handläggningen, informationsobjektet Företrädare och Ärendesystemet. Handboken för handläggning av stöd gäller bara handläggningen.
- **Varje aspekt kan bära en styrning, och katalogen namnger dem den behöver.** Säkerhet (`C-112`) och Juridik (`C-113`) får ingen namngiven styrning nu.
- **Metod är Arbetssätt (`C-196`).** Metod står kvar som tillåten term. Ett arbetssätt kan beskrivas med de element lagret redan har, som ett återanvändbart mönster för beteendet. När en organisation antar arbetssättet står mönstret i en referensarkitektur (`C-041`).
- **Valet av arbetssätt är ett styrbeslut av den som har mandatet över styrobjektet.** En överordnad styrning kan binda valet med en regel. Chefen för Bidragsenheten väljer pm3 för förvaltningen av sin lösning. Generaldirektören fastställer regeln att initiativen i utvecklingsportföljen följer Scrum.
- **Metodstyrning (`C-051`) tas bort ur katalogen.** Den är inte aspektbaserad, eftersom arbetssätt inte är en aspekt. Den är inte objektbaserad, eftersom ingen äger arbetssättet som styrobjekt. Valet av arbetssätt kräver ingen egen styrningsform. F19 och F20 är därmed avgjorda.
- **Styrmedel (`C-015`) kan ta sikte på Aspekt (`C-004`).** Relationen sitter på familjen och är frivillig. Regeln att bara handläggare får läsa uppgifter om företrädare tar sikte på säkerheten. Bostadsbolagets regel att en felanmälan ska vara åtgärdad inom fem arbetsdagar tar inte sikte på någon aspekt.

## Övervägda alternativ

- **Arbetssätt som femte aspekt**, så att Metodstyrnings definition blir sann. Arbetssättet är en egenskap hos beteendet och inte hos allt som styrs. Avvisat.
- **En namngiven styrning per aspekt**, med två nya begrepp för säkerheten och juridiken. Två begrepp utan användning kostar mer än luckan. Avvisat.
- **Arbetssätt som en sort av referensarkitektur.** Scrum finns innan någon antagit det, och en referensarkitektur är antagen. Avvisat.
- **Metodstyrning kvar som begrepp eller som hänvisning i Arbetssätt (`C-196`).** Nicklas vill inte ha ordet med som begrepp. Avvisat.
- **En relation till Aspekt per sort av styrmedel.** Beslut 37 avvisade den för arkitekturprincipen. En relation på familjen säger samma sak en gång. Avvisat.

## Konsekvenser

- `C-051` Metodstyrning är borttaget, och dess id används inte igen. Meningen i beslut 26, "Metodstyrning (`C-051`) i lagret är något annat: styrningen av hur arkitekturen arbetas fram", gäller inte längre. Hur arkitekturen arbetas fram är ett arbetssätt i Arkitekturdisciplin (`C-116`), valt som alla andra. Meningen i beslut 28 om att valet av arbetssätt är det Metodstyrning handlar om gäller inte heller.
- Ny relation i frontmatter: `C-015` `kan ta sikte på` → `C-004`. Inga definitioner ändrade.
- Anmärkningar ändrade i `C-004`, `C-006` och `C-196`. `C-006` har inte längre metodstyrning bland exemplen.
- `docs/exempel/myndigheten-for-foreningsstod.md` har fått ekonomichefens regel, valen av arbetssätt och regeln som tar sikte på säkerheten.
- Ritningarna visar inte den nya relationen än. Rutan Aspekt togs bort ur två ritningar efter beslut 37 (#103) och ritas in igen i ett eget ärende.
- #71 stängs.
