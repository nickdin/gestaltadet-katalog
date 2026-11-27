# Katalogen bär exemplens arkitektur, lagret är hemmet för namn och kopplingar, texten för skälen, och exemplen är små beskrivningar som delar element

Beslutat av Nicklas 27 november 2026, när de två exempelorganisationerna bara fanns som text och tre ritningar, och en läsare inte kunde öppna ett enda element ur dem.

## Sammanhang

Katalogen förklarar sina begrepp med två påhittade organisationer: Myndigheten för föreningsstöd och bostadsbolaget. Exemplen fanns som två texter och tre ritningar. Lagret höll bara begreppen och mappningstabellerna.

En läsare kunde därför läsa att Analysenheten tilldelas (`C-096`) en funktion, men inte öppna enheten och se kopplingen. Läsaren såg inte heller hur en arkitekturbeskrivning ser ut när begreppen används. Katalogen byggs med programmet interlingua, men visade bara en liten del av vad programmet kan.

Fem frågor behövde svar:

- Ska katalogen bära exemplens arkitektur, eller bara begreppen?
- Var bor elementen?
- Vem har rätt när texten och elementen säger olika?
- Hur stor är en exempelbeskrivning, och vem äger den?
- I vilken ordning registreras exemplen?

Frågorna avgjordes på fallet Analys hos Myndigheten för föreningsstöd.

## Beslut

### Vad katalogen bär

- **Katalogen bär exemplens arkitektur.** De två organisationerna registreras som element, relationer, ritningar och arkitekturbeskrivningar. En läsare kan öppna Analysenheten och se vad den är kopplad till.
- **Katalogen visar också vad interlingua kan.** Varje funktion i programmet visas en gång med ett fall ur exemplen: en inläst ritning, en vy, en tabell som korsar två slags element, en jämförelse mellan nuläge och målbild.
- **Elementen bor i det här lagret**, bredvid begreppen. Ett element pekar på sitt begrepp i samma lager, och definitionen behåller ett enda hem.

### Text och element

- **Lagret är hemmet för namn och kopplingar.** Vad en funktion heter och vem som tilldelas den står i lagret.
- **Texten i `docs/exempel/` är hemmet för berättelsen och skälen.** Den säger varför organisationen ser ut som den gör.
- **Texten påstår ingen koppling som lagret saknar.** Går de isär rättas texten. Ett namn byts i lagret först.

### Beskrivningarna

- **Exemplen är flera små beskrivningar, en per fråga.** "Informationen i Ta fram statistik, nuläge" är en beskrivning. "Vem som utför arbete i Analys, nuläge" är en annan.
- **Beskrivningarna delar element.** Analysenheten är samma element i alla beskrivningar som visar den.
- **En beskrivning hålls samman av sin organisation.** Element ur Myndigheten för föreningsstöd och ur bostadsbolaget blandas aldrig i en beskrivning.
- **Ägaren är en påhittad roll hos organisationen**, till exempel chefen för Analysenheten. Exemplet ska se ut som en beskrivning i bruk.

### Ordningen

- **Myndigheten för föreningsstöd registreras först**, ett fall i taget. Bostadsbolaget kommer när myndigheten har visat varje funktion i programmet en gång.
- **Den första beskrivningen läses in ur en ritning som redan finns**, kartan över funktionens information. Katalogen visar då hur en ritning blir arkitektur.

### Exemplet

- **Funktionen heter Ta fram statistik.** Kartan och texten kallade den Analysfunktionen. Det namnet ligger för nära förmågan Analys. Funktionen är ett enda element, och ritningarna och texterna byter namn.
- **Ta fram statistik är en verksamhetsfunktion (`C-158`).** Den är analytikernas löpande ansvar och har ingen bestämd början. Den rör inget enskilt ärende och är därför ingen handläggning (`C-160`).
- **Funktionen rymmer processer.** Bidragsenhetens månadsräkning börjar vid månadsskiftet, följer samma steg och lämnas till generaldirektören. Den är en verksamhetsprocess (`C-130`) inuti funktionen. Beskrivningen av vem som utför arbetet visar både funktionen och processen.
- **Riskindikator per förening blir tre element.** Produkten (`C-014`) är det Analys lämnar till Tillsyn. Produkten aggregerar (`C-100`) verksamhetsobjektet (`C-159`) med samma namn. Informationsobjektet (`C-060`) realiserar verksamhetsobjektet och är innehållet, som chefen för Analysenheten äger. Kedjan är den som [[0016-verksamhetsobjekt-ar-en-elementtyp|beslut 16]] bestämde.
- **"Producera statistik" står kvar som exempel i Verksamhetsprocess (`C-130`).** Det är ett allmänt exempel på hur en process namnges. Typen bär skillnaden mellan process och funktion, inte namnet.

## Övervägda alternativ

- **Ett eget lager per exempelorganisation.** Exemplen hade då legat för sig. Ett element pekar bara på begrepp i sitt eget lager, så varje lager hade behövt en kopia av begreppen. En ändrad definition hade fått göras på flera ställen. Avvisat.
- **En stor beskrivning per organisation.** Den hade visat allt på en gång. En läsare orkar öppna en liten beskrivning, och verkligt arbete görs en fråga i taget. Avvisat.
- **Berättelsen flyttar in i beskrivningarna, och `docs/exempel/` blir bara en ingång.** Då hade allt om ett fall stått på ett ställe. Begreppens anmärkningar lutar sig mot texten, och den är läsbar som den är. Avvisat nu.
- **Katalogens ägare står som ägare till beskrivningarna.** Det är sant om texten, men exemplet hade inte visat hur ägande ser ut i bruk. Vem som har skrivit en text visas på annat sätt ([[0039-varje-text-pa-sajten-sager-vem-som-skrivit-den-och-om-nicklas-godkant-den|beslut 39]]). Avvisat.
- **Två element, där Ta fram statistik är en del av Analysfunktionen.** Inget i texterna skiljer de två åt. Avvisat.
- **Elementen skrivs in för hand och ritningen ritas om.** Det hade gett samma element. Katalogen hade då inte visat hur en ritning läses in. Avvisat för den första beskrivningen.

## Konsekvenser

- Ingen definition ändras, och inga begrepp tillkommer.
- Lagret får element, relationer, beskrivningar, vyer och ritningar. Sajten visar dem bredvid begreppen.
- Namnet Analysfunktionen byts mot Ta fram statistik i ritningarna, i texten om myndigheten och i texten om informationskartläggning.
- Produkten Riskindikator per förening binds till sitt innehåll genom verksamhetsobjektet, som [[0016-verksamhetsobjekt-ar-en-elementtyp|beslut 16]] säger. Frågan ställdes i ärende #223 och fick det svaret samma dag.
- Startsidan behöver en väg in till exemplen. Det avsnittet skrivs i ett eget ärende.
- Arbetet samlas i ärende #222, med ett ärende per fall.
