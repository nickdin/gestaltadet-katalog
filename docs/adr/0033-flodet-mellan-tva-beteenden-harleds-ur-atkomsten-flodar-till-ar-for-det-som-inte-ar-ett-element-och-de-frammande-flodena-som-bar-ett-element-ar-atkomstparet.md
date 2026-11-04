# Flödet mellan två beteenden härleds ur åtkomsten, flödar till är för det som inte är ett element, och de främmande flödena som bär ett element är åtkomstparet

Beslutat av Nicklas i grillningen av ärende #29, 2026-11-03. Avgör vad katalogen gör åt att det som flödar mellan två beteenden bara stod som text på pilen, så att inget kunde kontrollera att avsändaren skriver det och mottagaren läser det, eller att det alls finns som element.

## Sammanhang

Ett verksamhetsobjekt (`C-159`) är det ett beteende hanterar och lämnar vidare. Hanterar är har åtkomst till (`C-101`). Lämnar vidare var flödar till (`C-097`) mellan två beteenden, med objektet som text på pilen. ArchiMate gör likadant. VDML-mappningen lämnade "DeliverableFlow carries BusinessItem" omappad, med motiveringen att det som bärs är flödets etikett. När Ärende flödar från Pröva ansökan till Fatta beslut visste lagret därför inte att texten är verksamhetsobjektet Ärende. Processbilden och åtkomstrelationerna kunde glida isär utan att `check` sade något.

ADR 0014 hade redan valt vägen: lagret lagrar åtkomsten, inte flödet, och pilen från process till process i översikten är en slutsats ur åtkomsterna. Då var beslutet en ritregel, och pilen ritades för hand tills programmet härledde den. Natten före grillningen stängdes interlingua #843. Åtkomstrelationen bär sedan dess fältet `access` (`read`, `write`, `read-write`), och markeringen `access: true` på relationstypen säger vilken typ som är åtkomsten. `interlingua flow` räknar ut flödena i en vy: en pil från A till B märkt X, där A skriver X, B läser X och X inte visas i vyn. Katalogens del, markeringen på `C-101`, låg parkerad som #14 i väntan på det.

Grillningen ställde upp tre vägar: låta texten vara; ett fält på flödar till som pekar på objektet, så att `check` kan kräva åtkomsterna; eller härleda flödet och låta flödar till vara för annat. Den gick två rundor (3 + 4 frågor) och en efterfråga om exporten. Nicklas tog rekommendationen i varje fråga.

## Beslut

- **Ett elements väg mellan två beteenden lagras aldrig som flödar till (`C-097`).** Den är programmets slutsats ur två åtkomster: avsändaren skriver objektet, mottagaren läser det. ADR 0014 står kvar. Väg 2, ett fält på flödet, vore samma sak sagd två gånger.
- **Flödar till (`C-097`) är för det som inte är ett eget element i lagret.** Ny definition: "relationstyp som anger att något som inte är ett eget element i lagret går från ett arkitekturelement till ett annat". Vad som går står i beskrivningen: ett meddelande, en signal, en överlämning utan eget objekt. Regeln träffar allt den gamla definitionen räknade upp, information, materiel och värde. Information och materiel är verksamhetsobjekt; en fysisk sak utan informationssida är det sedan ADR 0024. Värde är sedan ADR 0028 elementtypen Värde (`C-195`), som en värdeströms steg realiserar. Med regeln försvinner luckan: det som är ett element flödar aldrig som text. Den som vill kontrollera innehållet gör det till ett element, och då härleds pilen.
- **Pilar åt båda hållen godtas.** Två steg som båda läser och skriver samma objekt får en pil åt varje håll i översikten, som Pröva ansökan och Fatta beslut mot Ärende hos Myndigheten för föreningsstöd. Pilen säger att objektet går mellan dem, inte vilket steg som kommer först. Ordningen i kedjan är utlösers (`C-098`) sak.
- **Mappningsraderna följer vad flödet bär.** Bär den främmande notationens flöde alltid ett element flyttar raden till har åtkomst till (`C-101`). Det gäller UML:s ObjectFlow och InformationFlow, VDML:s DeliverableFlow mellan aktiviteter och mellan parter, och "DeliverableFlow carries BusinessItem", som var omappad. Får etiketten vara fri text står raden kvar på `C-097`, med en kommentar om att ett flöde vars etikett är ett element skrivs som åtkomstparet. Det gäller ArchiMates Flow och BPMN:s Message Flow. BPMN:s Message behåller `C-159` med omskriven kommentar.
- **Har åtkomst till (`C-101`) markeras `access: true`** (#14). Då kan ett lager som använder katalogen sätta läget på sina åtkomstrelationer, och programmet kan härleda flödena. Att sätta läget på ett lagers relationer är varje lagers eget arbete.
- **Programmet säger till när en lagrad pil troligen är överflödig.** Skriver A X, läser B X och håller lagret dessutom en flödar till från A till B, så skriver `check` en informationsrad, som för en dubblerad relation i dag. Det är ingen överträdelse: pilen kan bära ett meddelande vid sidan av objektet, och programmet kan inte läsa texten.
- **ArchiMate-exporten skriver inga härledda pilar.** Den säger vad lagret håller: åtkomsterna med sitt läge (interlingua #909). Grillningen sade först ja till härledda Flow-relationer i exporten. Men interlinguas ADR 0021, från grillningen av #843 den 1 november, hade redan avvisat dem: en läsare av exporten kan inte skilja dem från lagrade. Nicklas lät det beslutet stå. En ArchiMate-läsare får översiktens pilar ur programmets flödeslistning.

## Övervägda alternativ

- **Låta texten vara**, som ArchiMate och den gamla VDML-raden. Enkelt, men flödets innehåll kontrolleras aldrig, och bilden kan glida ifrån åtkomsterna. Avvisat.
- **Ett fält på flödar till som pekar på objektet**, så att `check` kräver att avsändaren skriver och mottagaren läser det. Flödet och de två åtkomsterna säger då samma sak, och ADR 0014 avvisade redan det. Avvisat.
- **Behålla definitionens information, materiel och värde** och bara lägga till regeln. Alla tre är element i lagret, och en definition som räknar upp dem säger emot regeln. Avvisat.
- **Flytta alla främmande flödesrader till åtkomsten.** ArchiMates Flow och BPMN:s Message Flow får bära fri text, och då är de denna relation. Avvisat.
- **Överträdelse i `check` för den överflödiga pilen.** Programmet vet inte vad texten betyder, och pilen kan vara ett meddelande. Avvisat; en informationsrad i stället.
- **Härledda Flow-relationer i ArchiMate-exporten**, märkta med objektets namn. Redan avvisat i interlinguas ADR 0021: läsaren ser inte skillnad på en härledd och en lagrad pil. Avvisat igen.

## Konsekvenser

- `C-097` får ny definition och anmärkning. `C-159` får en mening om att lämnar vidare är den härledda pilen. `C-101` får markeringen `access: true` och en anmärkning om fältet och härledningen; #14 stängs med det.
- Mappningsrader flyttade i `mapping/uml.yaml` (ObjectFlow, InformationFlow, kommentaren på InformationFlow realization) och `mapping/vdml.yaml` (DeliverableFlow, tre rader, och elementradens motivering). Kommentarer i `mapping/archimate.yaml` (Flow) och `mapping/bpmn.yaml` (Message, Message Flow).
- Interlingua får ett ärende, #989: informationsraden i `check` för en lagrad flödar till som åtkomsten redan ger. Exporten lämnas som ADR 0021 säger.
- Ett lager som använder katalogen sätter läget på varje åtkomstrelation. En relation utan läge är en lucka: `check --gaps` listar den, och härledningen hoppar över den.
- Ingen ny elementtyp; mallen körs inte om.
