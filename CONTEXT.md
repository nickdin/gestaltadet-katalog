# Ordlista

Posterna nedan definierar de ord katalogen själv är byggd av. De kom från interlinguas `CONTEXT.md` vid commit `4f9b954` (interlinguas #355 berättelse 54 och #356), tillsammans med beslutet som nu heter `docs/adr/0009-utsidan-ar-ett-sjatte-perspektiv.md`. Först flyttade de oförändrade på engelska till det privata lager som föregick katalogen, så att inget resonemang gick förlorat på vägen. Interlinguas ordlista behåller det programmet själv känner till.

Nio poster där sade både något om programmet och något om den här katalogen: *Perspective*, *Governance element*, *Principle*, *Value proposition*, *Canvas*, *Aspect*, *Architecture object*, *Replacement* och *Canvas note*. Det som gäller katalogen står nedan (interlinguas #355 berättelse 55, #357). Det som gäller vilken katalog som helst står kvar i interlinguas ordlista. Sist står vilka av katalogens begrepp interlinguas ordlista hänvisade till med id.

Posterna är översatta till svenska (#4) med samma innehåll som de engelska: samma påståenden, samma gränsdragningar. Engelska ord som är termer i sig står kvar som främmande ord i kursiv. Posternas namn är katalogens termer med begreppets id. En post utan id är ett ord ordlistan behöver men som inte är ett begrepp i katalogen. Begreppen definieras i `concepts/`: säger ordlistan och katalogen olika är katalogen den enda definitionen.

## Språket

### Beskrivningar och vad de är gjorda av

**Canvas**:
Det finns tre: affärsmodellen (*business model*), uppdragsmodellen (*mission model*) och behov mot erbjudande. Varje arkitekturobjekt kan ha affärsmodellens eller uppdragsmodellens canvas, eller båda.

**Arkitekturperspektiv (C-036)**:
Den ståndpunkt som styr en vy och avgör vilka elementtyper den täcker. Det finns sex: strategi (affär), verksamhet, information (som rymmer data), applikation, teknik och upplevelse. Upplevelse är utsidan: vem organisationen finns för, vad de behöver och vad de går igenom (EDGY:s *Experience*). Upplevelse rymmer det som finns där utan organisationen (målgrupp, behov, resa). Det organisationen gör för dem hör till verksamhet. Varje elementtyp och arkitekturobjektstyp hör till exakt ett perspektiv, så att den har en ägare. Finns samma slags sak i flera perspektiv har var och en en egen typ (verksamhetstjänst, applikationstjänst, tekniktjänst). Var och en är då ett slags tjänst, ett familjebegrepp som inte självt är en typ. Vem som äger ett perspektivs vyer och principer är ett teams sak, aldrig perspektivets egen.
_Undvik_: *viewpoint*, lager, *architecture domain* (TOGAF:s ord för det)

**Aspekt (C-004)**:
En egenskap hos det som styrs som går tvärs igenom varje perspektiv: Säkerhet (C-112), Juridik (C-113), Ekonomi (C-114) och Struktur och sammanhang (C-115). Listan är sluten och katalogens egen, och varje aspekt är ett eget begrepp.

**Disciplin (C-124)**:
Ett område av kunskap och praxis, vidare än någon enskild organisation: "vad disciplinen säger om X". Ett begrepp för gemensam förståelse, aldrig något en organisation registrerar. En disciplin behöver inte följa ett perspektiv. Tjänstedesign utformar och prövar både upplevelsen och lösningen, över perspektiven.
_Undvik_: team, roll, arkitekturdisciplin (det slags disciplin som gäller arkitektur)

**Arkitekturdisciplin (C-116)**:
En disciplin vars område är arkitekturens kunskap och praxis: informationsarkitektur, enterprisearkitektur. Varje perspektiv hör till en arkitekturdisciplin, och en disciplin kan hålla flera: verksamhetsarkitektur håller verksamhet och upplevelse. Enterprisearkitektur är den som inget eget perspektiv har. Den har i stället sammanhanget tvärs över perspektiven och arkitekturstyrningen, Arkitekturstyrning (C-049).
_Undvik_: disciplin (det vida ordet), perspektiv, team, roll

**Roll (C-074)**:
Det en aktör uppträder som inom organisationen, med det ansvar som hör till: informationsarkitekt, enterprisearkitekt. Aktören är en person, ett team eller en organisationsenhet. En roll kräver kompetens, och kompetensen hämtas ofta ur en disciplin.
_Undvik_: disciplin (området, inte organisationens eget)

**Team (C-123)**:
En grupp människor som arbetar med en gemensam uppgift, inom en organisationsenhet eller över flera. Det är en virtuell organisation vid sidan av den formella linjen, av det slag ett projekt ofta bemannas med. Ett team är ett eget begrepp och ett slags aktör, liksom en organisationsenhet är det. Ingen av dem är ett slags den andra, och registrerade är båda element av typen aktör. Ett team uppträder i en eller flera roller och kan bära arkitekturansvar. Ett team är aldrig ett perspektiv: det kan bära flera perspektiv hos flera arkitekturobjekt, eller ett perspektiv för hela verksamheten.
_Undvik_: organisationsenhet (den formella linjen, med egen ledning), disciplin, perspektiv

**Arkitekturansvar (C-117)**:
Ett teams ansvar för ett eller flera perspektiv hos ett eller flera arkitekturobjekt: "Team Information bär information för domänen Bidragsgivning". Den som bär det äger de vyerna och de principer som gäller för dem.
_Undvik_: arkitekturdomän (en domän har ett eget uppdrag; arkitekturarbete är en funktion i någon annans tjänst), *architecture domain* (TOGAF:s ord för ett perspektiv), ägarskap

**Enterprisearkitektur**:
En arkitekturdisciplin. Inom en organisation är det den roll som bär ansvaret för verksamhetsnivån, hela verksamheten, över alla perspektiv. Dess vyer använder alla perspektiven utan att vara ett.
_Undvik_: ett eget perspektiv

**Canvasanteckning**:
Något en beskrivning säger som hör hemma i en ruta på en canvas och inte namnger något slags sak. Till exempel vem som betalar för vilken produkt, vilka resurser som kostar mest, hur organisationen förhåller sig till en målgrupp, vems stöd ett uppdrag behöver.

### Vad beskrivningar beskriver

**Arkitekturobjekt (C-032)**:
Den verksamhet, verksamhetsdomän eller lösning en beskrivning handlar om. Varje arkitekturobjekt är ett styrobjekt, Styrobjekt (C-003), det en styrning gäller. Ett arkitekturobjekt är alltså ett styrobjekt som en arkitektur handlar om, eftersom arkitektur finns för att styrningen av det ska fungera bättre.

**Styrmedelselement**:
Ett element av någon av styrmedelstyperna (ändamål, mål, princip, arkitekturprincip, styrbeslut, regel, krav) eller av bärare, det dokument de är skrivna i. Styrmedel (C-015) namnger familjen i katalogen och är aldrig självt en typ: ingen skriver ett styrmedel, man skriver en princip eller en regel. Typen kan ange vilka slags beskrivningar som fastställer den (`decided_by` på styrmedelstypens begrepp, en lista av beskrivningsslag). Katalogen markerar princip och arkitekturprincip så.

**Princip (C-018)**:
Ett styrmedelselement av typen princip eller arkitekturprincip: en hållning som säger vilken riktning som ska väljas mellan utformningsalternativ. Den fastställs genom att listas i en antagen referensarkitektur, som är dess bärare. En nuläges- eller transitionsbeskrivning kan visa en princip som gäller men fastställer den aldrig. En beskrivning prövas aldrig mot en princip den själv fastställer.

### Utsidan

**Målgrupp (C-145)**:
Människor som delar ett behov eller en situation och som organisationen finns för. Ett slags människor, aldrig en part: den kan inte agera, skriva under eller kontaktas. Den finns där oavsett om någon produkt erbjuds den. En elementtyp i upplevelseperspektivet, och den enda typen för det canvasarna kallar *customer segment* och *beneficiary*. Om en målgrupp betalar eller inte avgör inte vad den är.
_Undvik_: *customer segment*, *beneficiary*, aktör (en part som kan agera), mottagare (positionen hos den målgrupp eller aktör ett värdeerbjudande riktas till, eller hos den aktör en produkt levereras till: ena änden av en relation, aldrig en typ)

**Behov (C-146)**:
Det människor vill åstadkomma och få gjort (EDGY:s *task*). Det är personens eget och finns där oavsett om organisationen möter det. Dess egen text säger tre saker: vad som står i vägen för det, hindret (Hinder (C-192)); vad som vinns med det, vinsten (Vinst (C-193)); och vad människor i dag använder för att få det gjort. Inget av de tre är en typ. En elementtyp i upplevelseperspektivet.
_Undvik_: *task* (på svenska läses det som ett uppdrag), ärende, krav (ett styrmedelselement)

**Resa (C-147)**:
De händelser och aktiviteter människor går igenom i sina liv (EDGY:s *journey*). Den är personens, inte organisationens: den kan gå genom flera organisationer och finns där utan någon av dem. En elementtyp i upplevelseperspektivet.
_Undvik_: process (det organisationen gör)

**Värdeerbjudande (C-148)**:
Det en produkt utlovas göra för någon. Det riktas till en målgrupp eller en namngiven aktör, bygger på en eller flera produkter och möter ett eller flera behov. För varje behov har det en hjälp (Hjälp (C-194)) som säger hur det röjer behovets hinder och ger dess vinst. En produkt är det som levereras, och samma produkt kan bära olika värdeerbjudanden till olika målgrupper. Värdeerbjudandet står mellan produkt och behov: en produkt möter ett behov bara genom ett värdeerbjudande, aldrig direkt. En elementtyp i strategiperspektivet sedan ADR 0028, för affärsmodellen är strategi och värdeerbjudandet dess kärna.
_Undvik_: produkt, erbjudande

**Kanal**:
En andra term för verksamhetsgränssnitt, Verksamhetsgränssnitt (C-138). Där en aktör gör sina verksamhetstjänster tillgängliga är det medel människor använder för att nå aktören: samma sak sedd från sina två sidor.
_Undvik_: en egen typ

**Uppdrag (C-149)**:
Det organisationen, eller en del av den, har att göra. För en myndighet ger regeringen uppdraget. En verksamhetsdomän skärs ut efter sitt uppdrag: att pröva ansökningar om statsbidrag är ett, att föra register över föreningarna ett annat. Ett rent begrepp, aldrig en typ. Varje uppdrag har sin egen logik: att fullgöra ett *mission* eller att få betalt för det som erbjuds. Lagret skriver inte ner logiken någonstans. Den canvas som ritas säger den.
_Undvik_: *mission* (uppdragsmodellens ord, *mission model canvas*), ändamål (det ett uppdrag ger)

### Tiden

**Ersättning**:
Hur en målarkitektur säger att en sak blir en annan sak: ett nytt element som *ersätter* det gamla, genom en relation av typen ersätter (C-104), det gamla borttaget.

### Katalogens begrepp bakom interlinguas ord

Katalogens egna termer (svenska, `C-nnn`) är auktoriteten. De engelska orden nedan är de namn interlinguas kod och dokumentation använder för dem.

Interlinguas ordlista hänvisade till katalogens begrepp med id på de här ställena. Hänvisningarna flyttades hit när ordlistan skrevs om (interlinguas #357):

- **Concept**: `C-nnn`
- **Description**: Arkitekturbeskrivning (C-035)
- **View**: Arkitekturvy (C-052)
- **Perspective**: Arkitekturperspektiv (C-036)
- **Aspect**: Aspekt (C-004)
- **Detail level**: Detaljeringsgrad (C-038)
- **Architecture object**: Arkitekturobjekt (C-032), Styrobjekt (C-003)
- **Architecture level**: Arkitekturnivå (C-033)
- **Element**: Arkitekturelement (C-034)
- **Time perspective**: Tidsperspektiv (C-037)
