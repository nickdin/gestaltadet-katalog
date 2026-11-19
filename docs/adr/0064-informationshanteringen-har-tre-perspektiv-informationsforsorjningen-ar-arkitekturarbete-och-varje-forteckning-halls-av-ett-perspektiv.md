# Informationshanteringen har tre perspektiv, informationsförsörjningen är arkitekturarbete, och varje förteckning hålls av ett perspektiv

Beslutat av Nicklas 19 november 2026, när ett underlag hade visat vilken dokumentation reglerna kräver av varje perspektiv och vad den pekar på i kartan.

## Sammanhang

Beslut 55 gav informationskartläggningen fyra perspektiv: informationssäkerhet, dataskydd, offentlighet och arkiv, och informationsförsörjning. Beslut 58 sade att perspektiven fattar sina beslut i sina egna förteckningar. Beslut 61 sade att kontinuitetskravets tid står i en förteckning utanför lagret, men inte i vilken.

Ärendet #201 visade att sidan Informationskartläggning hade lagt kontinuitetskravet och återställningstiden i förteckningen över kraven på behandlingarna. Ingen av de två raderna gäller en behandling (`C-168`). Ärendet #202 frågade sedan vad varje perspektiv dokumenterar. De som arbetar i perspektiven är oftast olika personer. Kartan kan alla använda, men dokumentationen behöver hållas isär.

Underlaget `docs/research/perspektivens-dokumentation.md` läste lag, föreskrifter och myndigheternas vägledningar för varje perspektiv. Tre fynd bar besluten:

- Underlaget fann nästan ingen krävd dokumentation för informationsförsörjningen.
- Cybersäkerhetslagen har samma slags roller som informationssäkerheten och pekar på samma saker i kartan.
- Kontinuitetens dokument har den prioriterade aktiviteten som rad. Aktiviteten beror på resurser som kartan inte bär: personal, lokaler, el och leverantörer.

## Beslut

### Tre perspektiv

- **Informationshanteringen har tre perspektiv: informationssäkerhet, dataskydd, och offentlighet och arkiv.** De tre håller dokumentation som ligger utanför arkitekturen och tar stöd i kartan. Det ändrar beslut 55, som sade fyra.
- **Informationsförsörjningen är arkitekturarbete, inget perspektiv.** Arkitekten läser samma karta som en del av arkitekturarbetet. Datalagret hos Myndigheten för föreningsstöd hämtar Förening ur Ärendesystemet och inte ur Föreningsregistret, som är källan. Arkitekten ser det i kartan. Fyndet blir en bedömning (`C-185`) som går till målarkitekturen.
- **Varvet slutar när de tre perspektivens fynd har beslut.** Arkitektens bedömning följer arkitekturarbetets egen takt och håller inte varvet öppet. Det ändrar punkten om varvets slut i beslut 55.
- **Cybersäkerhetslagens krav hör till informationssäkerheten.** Lagen ger inget eget perspektiv. Den ställer fler krav på informationssäkerhetens dokumentation.
- **Kontinuiteten förblir en granne, som i beslut 61.** Den som arbetar med kontinuiteten läser kartan för applikationerna och informationen och kompletterar den med det kartan inte bär. Genomföra ansökningsomgången får stå still högst en dag. Kravet gäller också handläggarna och lokalen.

### Förteckningarna

- **Kontinuitetskravet står i en egen förteckning över kontinuitetskraven.** Raden pekar på beteendet: Genomföra ansökningsomgången, en dag.
- **Återställningstiden står på en egen rad i samma förteckning.** Raden pekar på applikationen eller lagringsytan: Föreningsregistret, en dag. Den som går igenom kartan frågar då om resursen klarar tiden, utan att härleda tiden själv.
- **Förteckningen över kraven på behandlingarna bär bara tillgänglighet och spårbarhet.** Varje rad pekar på paret beteende och objekt.
- **Processägaren ställer kraven, och informationssäkerheten håller förteckningen.** Chefen för Bidragsenheten säger hur länge Genomföra ansökningsomgången klarar sig utan Företrädare. Kravet står sedan bland informationssäkerhetens dokument. Varje förteckning har på så sätt ett perspektiv som håller den.
- **Processägaren är ofta också informationsägare för objekten i sin process.** Chefen för Bidragsenheten äger både Genomföra ansökningsomgången och Ansökan. Ett objekt som många processer använder har en annan ägare: chefen för Register- och tillsynsenheten äger Förening.
- **Klassningsförteckningen står kvar som i beslut 58.** Sidan säger att förteckningen är en rekommendation i myndigheternas metodstöd och inget krav i föreskrifterna.

### Vad metoden säger om dokumentationen

- **Metoden beskriver bara kopplingen till kartan.** För varje perspektiv säger sidan vilka dokument perspektivet håller, vad varje dokument pekar på i kartan och var läsaren hittar resten. Hur dokumentationen ska se ut i sin helhet beskriver andra bättre.
- **Det allmänna ordet är dokumentation.** Sidan talar om varje perspektivs dokumentation. Ett dokument heter förteckning, lista eller register bara där lagen, föreskriften eller vägledningen själv säger så. Föreskrifterna för statliga myndigheter kräver till exempel "dokumentation över" it-miljön, inte en förteckning. Namnen i det här beslutet på dokumentationen av kontinuitetskraven och av kraven på behandlingarna är arbetsnamn, och ärendena #201 och #202 väljer orden efter den här regeln.
- **Kopplingen prövas mot källorna.** Det sidan säger om ett dokument ska gå att belägga i lag, föreskrift eller den ansvariga myndighetens vägledning.

## Övervägda alternativ

- **Kontinuitetskravet och återställningstiden står kvar i förteckningen över kraven på behandlingarna, som får ett vidare namn.** Varje annan förteckning pekar på en sorts sak. Avvisat.
- **Återställningstiden får ingen rad.** Den som går igenom kartan får då härleda den varje gång. Avvisat.
- **Kontinuiteten blir ett perspektiv.** Kartan bär inte personalen och lokalerna, så perspektivet kan inte besvara sina frågor ur kartan. Avvisat, som i beslut 61. Metoden kan breddas senare.
- **Cybersäkerheten blir ett eget perspektiv.** Samma person skulle läsa samma applikation två gånger med samma fråga. Avvisat.
- **Förteckningen över kraven på behandlingarna är processägarens egen och hör inte till något perspektiv.** Källorna lägger kravet på tillgänglighet hos informationssäkerheten. Avvisat.
- **Informationsförsörjningen står kvar som perspektiv, och sidan säger att kraven på dokumentation är få.** Ett perspektiv utan dokumentation utanför arkitekturen är arkitekturarbete. Avvisat.
- **Fyndet om källan lämnar metoden helt.** Fyndet syns i kartan, och någon måste se det. Avvisat.

## Konsekvenser

- Ingen definition ändras, och inga begrepp, relationer eller typer tillkommer.
- Besluten 55, 58 och 61 har fått var sin not om vad det här beslutet ändrar.
- Sidan Informationskartläggning och anmärkningarna som nämner förteckningarna skrivs om i ärendena #201 och #202. Ritningen Informationskartläggning följer med i #202.
- Underlaget fann tre fel som har egna ärenden: #203 om rättslig grund i registerförteckningen, #204 om handlingstyp och handlingsslag, och #205 om vem som beslutar om gallring i exemplet.
