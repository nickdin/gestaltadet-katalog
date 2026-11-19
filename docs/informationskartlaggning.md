# Informationskartläggning

Metoden börjar i en karta och slutar i beslut.

Informationskartläggning är ett [[C-196 Arbetssätt|arbetssätt]] för den som vill förbättra hur en verksamhet hanterar sin information. Verksamheten kartläggs en gång. Sedan går fyra perspektiv igenom samma karta: informationssäkerhet, dataskydd, offentlighet och arkiv, informationsförsörjning. Varje brist blir ett fynd, och varje fynd får ett beslut. Metoden står i beslut 55.

Ett varv gäller ett beteende och har sju steg. Steg 1 till 3 är en [[C-107 Kartläggning|kartläggning]]. Steg 4 till 7 går igenom kartan och slutar i beslut. Sidan följer ett exempel genom alla steg: analysfunktionen hos Myndigheten för föreningsstöd, en påhittad myndighet som fördelar statsbidrag till ideella föreningar.

## Steg 1: välj ett beteende

Ett varv gäller ett [[C-157 Verksamhetsbeteende|beteende]]: en [[C-130 Verksamhetsprocess|process]], en [[C-160 Handläggning|handläggning]] eller en [[C-158 Verksamhetsfunktion|funktion]]. Välj ett beteende i taget. Kartan byggs på för varje varv. Ett objekt som flera beteenden använder kommer upp i flera varv.

Exempel: Myndigheten för föreningsstöd väljer analysfunktionen. Handläggningen Pröva en ansökan är ett annat varv.

## Steg 2: intervjua dem som utför beteendet

En arkitekt leder varvet och håller kartan. Arkitekten intervjuar dem som utför beteendet, och de beskriver vad de gör. I samma intervju fångar arkitekten fyra saker:

- [[C-060 Informationsobjekt|informationsobjekten]], till exempel Ansökan och Företrädare
- [[C-085 Representation|representationerna]], till exempel en Excelfil
- [[C-165 Lagringsyta|lagringsytorna]], till exempel ett datalager
- [[C-071 Applikation|applikationerna]], till exempel Ärendesystemet.

Arkitekten fångar också vilka lagringsytor beteendet använder. På kartan har beteendet åtkomst till var och en av dem.

I intervjun sveper arkitekten också över lagringsytorna. Svepet hittar det som inget beteende når, till exempel en fil som ingen längre använder.

Kartan får börja grovt. Första dagen räcker ett [[C-198 Informationsområde|informationsområde]] med en ägare. Klassen står i klassningsförteckningen, på områdets rad. Kartan förfinas när ett perspektiv kräver det, till exempel när personnumret behöver bli ett eget objekt.

Exempel: Analysenheten läser Ansökan, Beslut och Utbetalning in i ett datalager i myndighetens analysplattform. Datalagret innehåller också kopior av Förening och Företrädare. Analysenheten sätter samman Utbetalningar per kommun och räknar fram Riskindikator per förening. På kartan finns också en Excelfil i enhetens grupprum.

## Steg 3: låt processägaren bekräfta kartan

[[C-206 Processägare|Processägaren]] bekräftar kartan innan perspektiven börjar. Kartan visar det som faktiskt görs. Processägaren stryker därför inget som görs men inte borde göras. Det blir ett fynd i nästa steg.

Exempel: Chefen för Analysenheten är processägare för analysfunktionen och bekräftar kartan. Excelfilen i grupprummet står kvar på kartan.

## Steg 4: gå igenom kartan ur fyra perspektiv

Fyra perspektiv går igenom samma karta. Varje perspektiv har en huvudfråga, och varje nej är ett fynd. Perspektiven är oberoende av varandra. När kartan har ägare går de igenom den i valfri ordning, eller samtidigt.

- **Informationssäkerhet.** Har informationsägaren tagit ställning till varje objekt på kartan, själv eller genom området, och klarar varje lagringsyta det förteckningen kräver? Frågan räknar in återställningstiden: hur fort en lagringsyta eller en applikation måste vara i bruk igen. [[C-167 Informationsägare|Informationsägaren]] går igenom.
- **Dataskydd.** Har varje [[C-168 Behandling|behandling]] av personuppgifter ett [[C-163 Behandlingsändamål|ändamål]] och en [[C-164 Rättslig grund|rättslig grund]] i registerförteckningen? Processägaren går igenom.
- **Offentlighet och arkiv.** Har varje handlingstyp per process ett beslut om bevarande eller [[C-200 Gallring|gallring]] i informationshanteringsplanen? Processägaren går igenom.
- **Informationsförsörjning.** Har varje [[C-202 Resursdata|resursdataobjekt]] en enda källa, och hämtar kopiorna därifrån? Arkitekten går igenom.

Kontinuiteten är inget femte perspektiv. Kontinuitetskravet är den längsta tid beteendet får stå still, och processägaren ställer det. Kontinuiteten gäller beteendet och alla dess resurser: personal, lokaler, applikationer och information. Informationssäkerheten läser den del som rör information och applikationer. Det gör den genom återställningstiden, som härleds ur kontinuitetskravet. Beslut 61.

Exempel: Varje perspektiv ger ett fynd i analysfunktionen. Fynden står under steg 5.

## Steg 5: skriv varje fynd som en avvikelse eller en bedömning

Ett fynd är en [[C-213 Avvikelse|avvikelse]] när organisationen har fastställt ett [[C-015 Styrmedel|styrmedel]] att pröva mot, till exempel en [[C-020 Regel|regel]]. Annars är fyndet en [[C-185 Bedömning|bedömning]], oftast en [[C-186 Risk|risk]]. En lag är en [[C-184 Påverkan|påverkan]] utifrån. Lagen blir ett styrmedel först när organisationen har härlett en egen regel ur den.

Exempel: Analysfunktionen har fyra fynd, ett per perspektiv.

- **Informationssäkerhet: en avvikelse.** En analytiker har exporterat Riskindikator per förening till en Excelfil i enhetens grupprum. Grupprummet är en lagringsyta som hela myndigheten kan öppna, och Riskindikator per förening är känslig. Myndigheten har fastställt regeln att behörigheten på en lagringsyta följer den högsta klassen där. Filen går emot regeln, och därför är fyndet en avvikelse.
- **Dataskydd: en bedömning.** Datalagret innehåller Företrädare, som är personuppgifter. Analysfunktionens ändamål i registerförteckningen nämner bara Ansökan, Beslut och Utbetalning. Myndigheten har ingen egen regel om vad registerförteckningen ska innehålla. Chefen för Analysenheten bedömer fyndet som en risk: en företrädare kan fråga varför uppgifterna finns i datalagret, och myndigheten har inget svar.
- **Offentlighet och arkiv: en bedömning.** Informationshanteringsplanen har ingen rad för kopiorna i datalagret, och ingen gallrar dem. Myndigheten har ingen regel om kopior. Chefen för Analysenheten bedömer fyndet som en risk: kopiorna kan ligga kvar när originalen är gallrade.
- **Informationsförsörjning: en bedömning.** Datalagret hämtar Förening ur Ärendesystemet och inte ur Föreningsregistret, som är källan. Antalet medlemmar skiljer sig därför ibland mellan datalagret och registret. Myndigheten har ingen regel om att en kopia hämtas ur källan. Den som har [[C-117 Arkitekturansvar|arkitekturansvaret]] bedömer fyndet som en svaghet, eftersom skillnaden redan finns.

En skillnad är inget fynd. Analysenheten har satt samman Utbetalningar per kommun ur Utbetalning och Förening. Utbetalningar per kommun är öppen, fast Utbetalning är intern. En summering får klassas lägre än sina delar.

## Steg 6: låt den som har mandatet besluta om varje fynd

Den som har [[C-189 Mandat|mandatet]] beslutar att åtgärda fyndet eller att leva med det. Att leva med ett fynd är ett [[C-019 Styrbeslut|styrbeslut]]. Varvet slutar när varje fynd har ett beslut. En lista över fynd som ingen beslutar om ändrar inget.

Exempel: Myndigheten åtgärdar tre fynd och lever med ett.

- **Informationssäkerhet.** Chefen för Analysenheten beslutar att Excelfilen flyttas till en lagringsyta som bara enheten kan öppna. Avvikelsen är då rättad, och regeln står kvar.
- **Dataskydd.** Chefen för Register- och tillsynsenheten är informationsägare för Företrädare. Hen beslutar att kopian av Företrädare tas bort ur datalagret.
- **Offentlighet och arkiv.** Chefen för Analysenheten beslutar att informationshanteringsplanen får en rad för kopiorna i datalagret. En kopia gallras när originalet gallras.
- **Informationsförsörjning.** Chefen för Register- och tillsynsenheten är informationsägare för Förening. Hen beslutar att skillnaden får stå kvar i år, eftersom det kostar mer att byta källa än skillnaden gör. Hen skriver beslutet med skälet, och det prövas igen i nästa varv. Att leva med fyndet är ett styrbeslut.

Ett beslut som kräver en ändring blir ett [[C-021 Krav|krav]] i [[C-054 Målarkitektur|målarkitekturen]]. Kartan visar nuläget tills ändringen är gjord. Beslutet att ta bort kopian av Företrädare skrivs som ett krav på datalagret i målarkitekturen. Kartan visar kopian tills den är borta.

## Steg 7: gör om varvet

Gör om varvet när något ändras, och annars en gång om året. En ändring är att beteendet, applikationen eller lagringsytan ändras.

Exempel: Om myndigheten byter analysplattform ändras applikationen. Då gör myndigheten om varvet för analysfunktionen.

## Vem som gör vad

Verksamheten gör arbetet själv. Specialisterna ger råd och granskar.

- **De som utför beteendet** beskriver vad de gör.
- **Arkitekten** leder varvet och håller kartan. Arkitekten går också igenom informationsförsörjningen. Frågan om en enda källa går över flera beteenden, och bara kartan visar alla kopior.
- **Processägaren** bekräftar kartan och ställer kraven på tillgänglighet och spårbarhet för behandlingarna i sitt beteende. Processägaren ställer också kontinuitetskravet på beteendet. Processägaren går också igenom dataskydd och offentlighet och arkiv för sitt beteende. Både behandlingen och handlingstypen läses ur beteendet.
- **Informationsägaren** klassar sina objekt i konfidentialitet och riktighet och går igenom informationssäkerheten. Informationsägaren för ett resursdataobjekt beslutar om fynden i informationsförsörjningen.
- **Specialisterna**, till exempel dataskyddsombudet, ger råd och granskar. De gör inte genomgången, för det är inte deras uppdrag.
- **Den som har mandatet** beslutar om varje fynd.

## Vad kartan bär och inte bär

Kartan bär beteendet, informationsobjekten med ägare, representationerna, lagringsytorna och applikationerna. Kartan visar också vilka beteenden som har åtkomst till varje lagringsyta. Kartan beskriver hur det är.

Kartan bär inga beslut ur de fyra perspektiven. Den visar vem som beslutar, aldrig vad hen har beslutat. Klassningen står därför inte på kartan. Den som går igenom kartan läser ihop den med förteckningarna.

Besluten står på andra ställen:

- Klassningsförteckningen säger nivån i konfidentialitet och riktighet för varje objekt. Den pekar på objektet på kartan. Ett objekt har en egen rad, eller så gäller raden för dess informationsområde.
- Klassningsbeslutet säger varför objektet har nivån, vilken analys som ligger bakom och vilka skydd som är valda. För ett objekt med grundnivån säger beslutet bara att grundnivån räcker, utan analys.
- Förteckningen över kraven på behandlingarna säger processägarens krav på tillgänglighet och spårbarhet. Den pekar på paret beteende och objekt. Förteckningen har också en rad för processägarens kontinuitetskrav: hur länge ett beteende får stå still. Den raden pekar på beteendet. Återställningstiden härleds ur kontinuitetskravet och står på en egen rad i samma förteckning. Den raden pekar på applikationen eller lagringsytan.
- Registerförteckningen säger ändamål och rättslig grund.
- Informationshanteringsplanen säger vad som bevaras och vad som gallras.

Exempel: Anta att Genomföra ansökningsomgången får stå still högst en dag när pengarna ska betalas ut. Förteckningen över kraven på behandlingarna har då en rad som pekar på Genomföra ansökningsomgången och säger en dag. Anta också att återställningstiden för Föreningsregistret blir en dag. Den står på en rad i samma förteckning, och raden pekar på Föreningsregistret.

[[C-035 Arkitekturbeskrivning|Arkitekturbeskrivningen]] ska inte bära all information som perspektiven behöver.

Grundnivån är den nivå i en klass som organisationen har beslutat ska gälla det mesta. En organisation väljer själv om den vill ha en grundnivå. Grundnivån är ett beslut, aldrig tystnad: informationsägaren säger att den räcker för objektet. Ett objekt som helt saknar rad i klassningsförteckningen har ingen klass, och det är ett fynd.

Kartan delar ett objekt först när verksamheten hanterar delen för sig. Bostadsbolaget Brinkstadsbostäder hanterar i dag alla hyresavtal lika. Vill informationsägaren att avtalen för hyresgäster med skyddade personuppgifter hanteras för sig, står Skyddat hyresavtal i målarkitekturen. Det flyttar till kartan den dag uthyrningen gör så.

## Så når ett perspektivs fynd de andra

Det som ändrar kartan skrivs in i kartan. Ett perspektiv kan hitta ett nytt objekt, en ny lagringsyta, en kopia eller en åtkomst. Perspektivet lämnar det till arkitekten, som skriver in det i kartan. Så får de andra perspektiven veta det. Allt annat stannar i perspektivets egen förteckning.

## Följdfrågor under varje huvudfråga

Varje huvudfråga har följdfrågor som hjälper den som går igenom kartan.

### Informationssäkerhet

- Har varje informationsobjekt på kartan en informationsägare?
- Har varje objekt en rad i klassningsförteckningen, en egen eller områdets?
- Vilka objekt har grundnivån genom sitt område, och håller den för vart och ett?
- Vilket är det högst klassade objektet på varje lagringsyta?
- Vilka beteenden har åtkomst till lagringsytan, och vilket är det strängaste kravet på tillgänglighet och spårbarhet bland dem?
- Vilka objekt på lagringsytan går att koppla ihop till en ny uppgift?
- Vilka kan öppna lagringsytan?
- Vilken återställningstid ger kontinuitetskravet varje lagringsyta och applikation, och klarar de tiden?

Exempel: Anta att myndigheten har beslutat att grundnivån för konfidentialitet är intern. Chefen för Bidragsenheten har sagt att grundnivån räcker för informationsområdet Bidragsinformation. I området ligger Återkrav, som visar vilka föreningar som har fått betala tillbaka. Återkrav är känsligare än Utbetalning. Grundnivån håller alltså inte för Återkrav, och det blir ett fynd som informationsägaren beslutar om.

Exempel: Analysfunktionen har åtkomst till datalagret och klarar en vecka utan Förening. Pröva en ansökan har åtkomst till Föreningsregistret och behöver Förening samma dag. Datalagret ska klara veckan, och Föreningsregistret dagen.

Exempel: Anta att Genomföra ansökningsomgången får stå still högst en dag när pengarna ska betalas ut, och att processen saknar reservrutin, alltså en rutin som säger hur den utförs när en resurs är borta. Föreningsregistret måste då vara i bruk igen inom dagen. Det är återställningstiden, och den som går igenom kartan frågar om Föreningsregistret klarar den.

### Dataskydd

- Vilka informationsobjekt på kartan är personuppgifter?
- Vilka beteenden läser eller skriver dem?
- Står varje sådan behandling i registerförteckningen?
- Nämner ändamålet varje objekt som behandlingen når?

### Offentlighet och arkiv

- Vilka handlingstyper upprättar beteendet, och vilka tar det emot?
- Har varje handlingstyp en rad i informationshanteringsplanen?
- Har kopiorna en rad?
- Vem gallrar, och när?

### Informationsförsörjning

- Vilka informationsobjekt på kartan är resursdata?
- Vilken lagringsyta är källan för varje sådant objekt?
- Var finns kopiorna?
- Hämtas varje kopia ur källan?

## Tre ritningar visar exemplet

Ritningarna finns på sidan Ritningar, under rubriken Exempel.

- **Analysfunktionen karta** visar kartan med ägarna utsatta.
- **Analysfunktionen karta med fynd** visar samma karta med fynden numrerade.
- **Informationskartläggning steg** visar de sju stegen. Steg 7 är pilen tillbaka till steg 1.
