# Flödet mellan två beteenden härleds ur åtkomsten, flödar till är för det som inte är ett element, och de främmande flödena som bär ett element är åtkomstparet

Beslutat av Nicklas i grillningen av ärende #29, 2026-11-03. Avgör vad katalogen gör åt att det som flödar mellan två beteenden bara stod som text på pilen, så att inget kunde kontrollera att avsändaren skriver det och mottagaren läser det, eller att det alls finns som element.

## Sammanhang

Verksamhetsobjekt (`C-159`) är det ett beteende hanterar och lämnar vidare. Hanterar är har åtkomst till (`C-101`); lämnar vidare var flödar till (`C-097`) mellan två beteenden, med objektet som text på pilen. ArchiMate gör likadant, och VDML-mappningen lämnade "DeliverableFlow carries BusinessItem" omappad med motiveringen att det som bärs är flödets etikett. När Ärende flödar från Pröva ansökan till Fatta beslut visste lagret inte att texten är verksamhetsobjektet Ärende, och processbilden och åtkomstrelationerna kunde glida isär utan att `check` sade något.

ADR 0014 hade redan valt vägen: lagret lagrar åtkomsten, inte flödet, och pilen process till process i översikten är en slutsats ur åtkomsterna. Beslutet var då en ritregel; pilen ritades för hand tills programmet härledde den. Natten före grillningen stängdes interlingua #843: åtkomstrelationen bär fältet `access` (`read`, `write`, `read-write`), markeringen `access: true` på relationstypen säger vilken typ som är åtkomsten, och `interlingua flow` räknar ut flödena i en vy, en pil A till B märkt X där A skriver X och B läser X och X inte visas i vyn. Katalogens del, markeringen på `C-101`, låg parkerad som #14 i väntan på det.

Tre vägar ställdes upp: låta texten vara; ett fält på flödar till som pekar på objektet, så att `check` kan kräva åtkomsterna; eller härleda flödet och låta flödar till vara för annat. Grillningen gick två rundor (3 + 4 frågor), och Nicklas tog rekommendationen i varje fråga.

## Beslut

- **Ett elements väg mellan två beteenden lagras aldrig som flödar till (`C-097`).** Den är programmets slutsats ur två åtkomster: avsändaren skriver objektet, mottagaren läser det. ADR 0014 står kvar; väg 2, ett fält på flödet, vore samma sak sagd två gånger.
- **Flödar till (`C-097`) är för det som inte är ett eget element i lagret.** Ny definition: "relationstyp som anger att något som inte är ett eget element i lagret går från ett arkitekturelement till ett annat". Det som går står i beskrivningen: ett meddelande, en signal, en överlämning utan eget objekt. Den gamla definitionens information, materiel och värde träffas alla av regeln: information och materiel är verksamhetsobjekt (en fysisk sak utan informationssida är det sedan ADR 0024), och värde är sedan ADR 0028 elementtypen Värde (`C-195`), som en värdeströms steg realiserar. Luckan försvinner med regeln: det som är ett element flödar aldrig som text, och den som vill kontrollera innehållet gör det till ett element, varpå pilen härleds.
- **Pilar åt båda hållen godtas.** Två steg som båda läser och skriver samma objekt, Pröva ansökan och Fatta beslut mot Ärende hos Myndigheten för föreningsstöd, får en pil åt varje håll i översikten. Pilen säger att objektet går mellan dem, inte vilket steg som kommer först; ordningen i kedjan är utlösers (`C-098`) sak.
- **Mappningsraderna följer vad flödet bär.** Där den främmande notationens flöde alltid bär ett element flyttar raden till har åtkomst till (`C-101`): UML:s ObjectFlow och InformationFlow, VDML:s DeliverableFlow mellan aktiviteter och mellan parter, och "DeliverableFlow carries BusinessItem", som var omappad. Där etiketten får vara fri text står raden kvar på `C-097` med en kommentar om att ett flöde vars etikett är ett element skrivs som åtkomstparet: ArchiMates Flow och BPMN:s Message Flow. BPMN:s Message behåller `C-159` med omskriven kommentar.
- **Har åtkomst till (`C-101`) markeras `access: true`** (#14), så att ett lager som använder katalogen kan sätta läget på sina åtkomstrelationer och programmet kan härleda flödena. Att sätta läget på ett lagers relationer är varje lagers eget arbete.
- **Programmet säger till när en lagrad pil troligen är överflödig.** Där A skriver X, B läser X och lagret dessutom håller en flödar till från A till B skriver `check` en informationsrad, som för en dubblerad relation i dag, inte en överträdelse: pilen kan bära ett meddelande vid sidan av objektet, och programmet kan inte läsa texten.
- **ArchiMate-exporten skriver de härledda flödena som Flow-relationer** märkta med objektets namn, så att översikten ser likadan ut hos en ArchiMate-läsare som i katalogen. Efter interlingua #909, som skriver åtkomstläget i exporten.

## Övervägda alternativ

- **Låta texten vara**, som ArchiMate och den gamla VDML-raden. Enkelt, men flödets innehåll kontrolleras aldrig och bilden kan glida ifrån åtkomsterna. Avvisat.
- **Ett fält på flödar till som pekar på objektet**, så att `check` kräver att avsändaren skriver och mottagaren läser det. Flödet och de två åtkomsterna säger då samma sak, och ADR 0014 avvisade redan det. Avvisat.
- **Behålla definitionens information, materiel och värde** och bara lägga till regeln. Alla tre är element i lagret; en definition som räknar upp dem säger emot regeln. Avvisat.
- **Flytta alla främmande flödesrader till åtkomsten.** ArchiMates Flow och BPMN:s Message Flow får bära fri text, och då är de denna relation. Avvisat.
- **Överträdelse i `check` för den överflödiga pilen.** Programmet vet inte vad texten betyder, och pilen kan vara ett meddelande. Avvisat; informationsrad.

## Konsekvenser

- `C-097`: ny definition och anmärkning. `C-159`: en mening om att lämnar vidare är den härledda pilen. `C-101`: markeringen `access: true` och en anmärkning om fältet och härledningen; #14 stängs med det.
- Mappningsrader flyttade i `mapping/uml.yaml` (ObjectFlow, InformationFlow, kommentaren på InformationFlow realization) och `mapping/vdml.yaml` (DeliverableFlow, tre rader, och elementradens motivering); kommentarer i `mapping/archimate.yaml` (Flow) och `mapping/bpmn.yaml` (Message, Message Flow).
- Interlingua, två ärenden: informationsraden i `check` för en lagrad flödar till som åtkomsten redan ger, och ArchiMate-exporten av härledda flöden som Flow-relationer, efter #909.
- Ett lager som använder katalogen sätter läget på varje åtkomstrelation; en relation utan läge är en lucka som `check --gaps` listar och härledningen hoppar över.
- Ingen ny elementtyp; mallen körs inte om.
