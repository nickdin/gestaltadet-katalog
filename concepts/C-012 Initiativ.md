---
id: C-012
term: Initiativ
terms:
  - term: Initiativ
    language: sv
    source: catalogue
definition: "tidsbegränsad förändringsinsats med definierat slut"
kind: element-type
partitive: '[[C-011 Portfölj]]'
associative:
  - concept: '[[C-172 Verksamhetsförändring]]'
    label: åstadkommer
---
# C-012 Initiativ

**Definition:** tidsbegränsad förändringsinsats med definierat slut

## Anmärkning

Ett initiativ är det som flyttar verksamheten mot dess inriktning, och kartan ska kunna visa vad som pågår och vad det ändrar. Det är en elementtyp i strategiperspektivet ([[C-108 Strategiperspektiv]]), bredvid verksamhetsförmågan. Ett projekt registreras som ett initiativ ([[C-013 Projekt]]). Initiativet är också ett styrobjekt ([[C-003 Styrobjekt]]), se initiativstyrning ([[C-045 Initiativstyrning]]).

Initiativet påverkar den verksamhetsförmåga ([[C-069 Verksamhetsförmåga]]) det utvecklar och det mål ([[C-017 Mål]]) det prövas mot. Det initiativet lämnar ifrån sig, dess leverabel ([[C-171 Leverabel]]), registreras som det element det blir. Portföljen ([[C-011 Portfölj]]) aggregerar sina initiativ. Beslut 19.

Verksamhetsuppföljningen kallar ofta initiativen uppdrag: ett projekt, ett utvecklingsuppdrag, en förbättring registreras som initiativ. Det tidsbundna som inte förändrar något, ett regeringsuppdrag eller en analys på beställning, är inget initiativ utan ett ärende i en handläggning ([[C-160 Handläggning]]). Det handläggningen tillhandahåller är en verksamhetsprodukt ([[C-173 Verksamhetsprodukt]]). Beslut 20.

Den som ger initiativet dess ram ([[C-210 Ram]]) startar det och utser dess ägare. Det är en delegation ([[C-214 Delegation]]). Portföljens ägare gör det för initiativen i portföljen. En lösningsägare gör det för ett initiativ som ryms i lösningens egen ram, och det initiativet får ingen egen rad i portföljen: det ryms i lösningens rad (beslut 51). Ett initiativ får en egen rad när det behöver något lösningsägaren inte har: pengar utöver lösningens ram, eller en ändring i någon annans lösning.

Initiativets ägare beslutar om arbetet, alltså hur det läggs upp inom ramen och kraven, och svarar för att leverabeln blir klar. Ägaren till lösningen ([[C-055 Lösning]]) som ändras ställer kraven ([[C-021 Krav]]) på leverabeln och tar emot den. Lösningens ägare svarar också för effekten, för effekten uppstår i lösningen när initiativet är slut. Ryms kraven inte i ramen avgör den som satte ramen: antingen höjer hen ramen, eller så sänker lösningsägaren kravet. Initiativets ägare stryker inga krav. Är två lösningsägare oense avgör ägaren till det styrobjekt som omsluter båda.

Ett initiativ som bygger en ny lösning behöver någon som tar emot den. Den som startar initiativet utser därför samtidigt den blivande lösningsägaren, som ställer kraven från början. Ett initiativ utan mottagande ägare är ett fynd.

I ett projekt ([[C-013 Projekt]]) är beställaren initiativets ägare. Projektledaren leder arbetet åt ägaren och har inget eget mandat. Styrgruppen är ett forum ([[C-156 Forum]]): den ger råd och kan komma överens, men den beslutar inte. Beslutar styrgruppen i praktiken om omfattningen ersätter den ett mandat som saknas, på samma sätt som objektforumet i Objektstyrning ([[C-048 Objektstyrning]]).

Fyra vanliga ord sorteras efter vad som kommer ut. Vidmakthållande är att hålla en lösning och dess produkter i det skick de har: drift, support och rättningar. Det har inget slut och är därför inget initiativ. Ordet rymmer två saker. Drift och support är produktion och betalas ur produktionens ram. Rättningar av lösningen ändrar utformningen och betalas ur lösningens ram (beslut 47). Att rätta en enskild uppgift är registervård och produktion (beslut 50). Vidareutveckling är ett initiativ som ändrar en lösning som finns. Nyutveckling är ett initiativ som lämnar en lösning som inte fanns. Innovation är ett initiativ som prövar en idé och lämnar kunskap: en bedömning ([[C-185 Bedömning]]) som leder till ett styrbeslut om att gå vidare eller låta bli. Försöket förändrar inget i sig, men det är till för att avgöra en förändring och är därför ett initiativ och inget ärende.

Gränsen mellan förvaltning och portfölj går inte mellan vidareutveckling och nyutveckling. Den går där lösningens ram tar slut. Lösningen avgör sorten, inte tekniken. Byts en uttjänt applikation mot en ny på annan teknik är det vidareutveckling, för lösningen har samma ändamål och samma användare efteråt. Det är inte vidmakthållande, för bytet har ett slut. I portföljen vägs ett sådant initiativ på en risk ([[C-186 Risk]]) som undviks, inte på ett effektmål ([[C-170 Effektmål]]). Beslut 46.

## Motsvarigheter

Motsvarar ArchiMates Work Package, som ligger i implementations- och migrationslagret utanför den kärna mappningstabellerna täcker; initiativet står därför under `unmapped-concepts` där. Beslut 10.

Initiative i Business Architecture Core Metamodel (BACM) är ett initiativ, och dess Change den verksamhetsförändring ([[C-172 Verksamhetsförändring]]) initiativet åstadkommer. Beslut 27.

Initiativet är inte Business Motivation Models Course of Action, vägvalet, som är ett styrbeslut ([[C-019 Styrbeslut]]); initiativet är arbetet som genomför vägvalet (beslut 25).

## Exempel

Automatisk beräkning av verksamhetsbidraget hos Myndigheten för föreningsstöd: vidareutveckling som rör två lösningar och står i portföljen. Bidragsenhetens nya mallar för kompletteringsbegäran: vidareutveckling inom lösningens egen ram. Ett försök på åtta veckor som prövar om ansökningar kan förgranskas maskinellt: innovation.
