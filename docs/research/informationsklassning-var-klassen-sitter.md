# Informationsklassning: var klassen sitter

Skriven av AI, inte granskad. 2026-11-17.

Underlaget är skrivet inför en beslutsintervju om var klassen i informationssäkerheten ska sitta. Det ger fynd och möjliga vägar, inget beslut. Katalogen säger i dag att Informationsägaren (C-167) sätter klassen på Informationsobjektet (C-060) som typ, i fyra klasser, och att klassen är densamma i varje Verksamhetsbeteende (C-157) som använder objektet (beslut 31, 35, 40 och 57). Lagringsytan (C-165) får det högst klassade objektets krav. I underlaget betyder beteende ett verksamhetsbeteende, och processägaren är Processägare (C-206). Ett varv i Informationskartläggning, metoden i `docs/informationskartlaggning.md`, gäller ett beteende i taget. Underlaget prövar det mot lagar, föreskrifter, metoder och granskningar. Varje påstående har sin källa i parentes. Underlagets egna slutsatser är märkta *(slutsats i underlaget)*. Det som inte gick att läsa står under rubriken Det som inte gick att bekräfta.

## Fynden i tio rader

1. Svenska regler kräver att en myndighet klassar "sin information" i tre aspekter: konfidentialitet, riktighet och tillgänglighet. Spårbarhet står bara i ett allmänt råd. SKR:s KLASSA tar inte med den, och metodstödet nämner den bara i ett exempel, som en stödjande del. Katalogens fjärde klass har alltså svagare stöd än Informationstillgång (C-166) ger intryck av *(slutsats i underlaget)*.
2. De nya föreskrifterna för verksamheter under cybersäkerhetslagen, MCFFS 2026:11, ger informationsägaren ansvar för "informationsbehandling i system", inte för en informationstyp. Informationsägaren anger också acceptabla avbrottstider "för informationsbehandlingen".
3. Nästan alla metoder klassar information i ett sammanhang. Metodstödet klassar per klassningsobjekt, till exempel en process. BSI utgår från verksamhetsprocessen och dess information. NIST bedömer varje informationstyp för varje användning. Den nederländska BIO klassar per verksamhetsprocess, och processägaren väljer nivån.
4. Flera källor sätter klassen på typen: NIST FIPS 199, BSI och NIST IR 8496. Men bara två låter typens klass gälla oförändrad i varje användning: FIPS 199 och den brittiska klassningspolicyn, där bara den som skapat informationen får ändra klassen. Den brittiska gäller bara konfidentialitet.
5. Tillgängligheten sätts i kontinuitetsmetoderna på aktiviteten och härleds nedåt till resurserna. BSI visar samma kunddata med två olika krav på återställningspunkt i två processer, och det strängaste vinner. Katalogens skäl för samma klass i varje beteende, att skadan följer uppgifterna, gäller konfidentialiteten men bär inte för tillgängligheten *(slutsats i underlaget)*.
6. BSI skiljer tillgänglighet i normal drift från kontinuitet vid en kris. Katalogens enda tillgänglighetsklass kan blanda två mått *(slutsats i underlaget)*.
7. Alla källor behandlar en samling av information för sig. Säkerhetspolisen skiljer ackumulering, många likadana uppgifter, från aggregering, där samlingen ger en ny uppgift. Bara den nya uppgiften klassas om. Katalogens Sammanställning (C-162) skiljer inte mellan de två fallen *(slutsats i underlaget)*.
8. Flera källor skiljer ansvaret för reglerna om klassningen från klassningen av varje förekomst. BSI låter den som skapar informationen göra den första klassningen. Metodstödet låter en verksamhet höja, och ibland sänka, en gemensam klassning beroende på sammanhanget.
9. Granskningar visar att klassning ofta inte görs, görs olika av olika personer och kostar mycket. Alternativen är en baslinje för det mesta och egen klassning bara för undantagen, eller skydd som avgörs vid varje åtkomst.
10. Känslighet som uppstår först när två objekt kopplas ihop sitter i kopplingen, enligt alla källor som lästes. USA och Säkerhetspolisen klassar samlingen och låter delarna behålla sin nivå. Databasforskningen klassar relationen högt och objekten lågt. EU-domstolen låter det bero på vem som kan göra kopplingen. Ingen källa höjer båda objekten.

## Frågorna

### 1. Vad som krävs, och av vilken enhet

Svenska regler kräver klassning av information, men olika regler fäster kravet på olika enheter. Ingen regel säger att klassen ska sitta på en informationstyp.

**MSBFS 2020:6 kräver klassning av myndighetens information i tre aspekter.** Myndigheten ska "klassa sin information avseende konfidentialitet, riktighet och tillgänglighet i olika nivåer utifrån vilka konsekvenser ett bristande skydd kan få (informationsklassning)" (MSBFS 2020:6, 6 § punkt 1). Ansvaret "kan inte överlåtas" till en annan myndighet (7 §). Spårbarhet står bara i ett allmänt råd: "Myndighetens behov av spårbarhet samt autenticitet hos informationen liksom informationens behov av bevarande över tid bör beaktas vid informationsklassning" (allmänt råd till 6 §). Ett allmänt råd är inte bindande. Verifierat i föreskriftens text.

**Föreskrifterna gäller oförändrade, men utfärdaren har bytt.** MSB heter Myndigheten för civilt försvar (MCF) sedan 2026. Den 1 juli 2026 gick rätten att utfärda föreskrifterna över till FRA, där NCSC ingår. MCF skriver att "Föreskrifterna gäller oförändrat" (mcf.se, sidan om MSBFS 2020:6). MSBFS 2020:6 och 2020:7 har alltså kvar sina namn och nummer. Verifierat på mcf.se och ncsc.se.

**MSBFS 2020:7 gäller systemet.** Myndigheten ska "för varje informationssystem" utse en systemägare och göra en riskbedömning för enskilda informationssystem (MSBFS 2020:7, 3 och 4 §§). Föreskriften klassar ingenting själv. Verifierat.

**MCFFS 2026:11 knyter informationsägaren till behandlingen.** Föreskrifterna gäller väsentliga och viktiga verksamhetsutövare enligt cybersäkerhetslagen (2025:1506) och trädde i kraft den 1 oktober 2026. "All informationsbehandling i system ska ha en utsedd informationsägare och alla system ska ha en utsedd systemägare" (3 kap. 5 §). Informationsägaren ska "för den informationsbehandling som denne ansvarar för" bedöma vilken nivå av skydd informationen behöver i konfidentialitet, riktighet inklusive autenticitet, och tillgänglighet. Informationsägaren ska också meddela systemägaren "vad som är acceptabla tider för otillgänglighet och bristande funktionalitet för informationsbehandlingen" (3 kap. 7 §). Verksamhetsutövaren ska "värdera informationen" i samma tre aspekter (3 kap. 11 §). Spårbarhet är ingen aspekt i klassningen. Ordet spårbart står bara om hur ändringar förs in i produktionsmiljön. Verifierat. NCSC:s utkast till vägledning säger att informationsägaren har "ansvar för en viss typ eller mängd av information", ofta en avdelningschef eller en processägare. Det är ett utkast på remiss.

**Cybersäkerhetslagen och NIS2 kräver ingen klassning.** Lagen kräver åtgärder som skyddar "nätverks- och informationssystem" utifrån ett allriskperspektiv, bland annat "tillgångsförvaltning" (cybersäkerhetslagen 2 kap. 3 §). NIS2-direktivet säger detsamma i artikel 21.2. Ingen av dem säger vad som ska klassas. Klassningen kommer in genom MCFFS 2026:11. Lagen gäller en kommun och en region, och en statlig myndighet som beslutar om gränsöverskridande rörlighet (1 kap. 3 §). Den gäller också verksamheter i de sektorer som NIS2-direktivets bilagor räknar upp, om de är minst medelstora (1 kap. 4 §). Verifierat. Om exempelorganisationerna omfattas är inte prövat.

**Säkerhetsskyddet klassar den enskilda uppgiften.** "Säkerhetsskyddsklassificerade uppgifter ska delas in i säkerhetsskyddsklasser utifrån den skada som ett röjande av uppgiften kan medföra" (säkerhetsskyddslagen 2 kap. 5 §). En handling får den högsta klassen bland sina uppgifter: "Om handlingen innehåller uppgifter med olika säkerhetsskyddsklass, ska den högsta säkerhetsskyddsklassen avgöra vilken anteckning handlingen ska ha" (säkerhetsskyddsförordningen 3 kap. 7 §). Skalan gäller bara röjande. Verksamhetsutövaren klassar genom sin säkerhetsskyddsanalys, och lagen namnger ingen roll. Verifierat.

**Offentlighets- och sekretesslagen fäster sekretessen på uppgiften.** Sekretess är "Ett förbud att röja en uppgift" (OSL 3 kap. 1 §). Prövningen görs när någon begär ut handlingen. Sekretessmarkeringen är frivillig: myndigheten "får" markera handlingen "Om det kan antas att en uppgift … inte får lämnas ut" (5 kap. 5 §). Katalogen följer redan detta i Uppgift (C-161). Verifierat.

**Dataskyddsförordningen bedömer risken per behandling.** Säkerheten ska stå i proportion till risken, med hänsyn till "the nature, scope, context and purposes of processing" (artikel 32.1). Konsekvensbedömningen gäller "the envisaged processing operations" (artikel 35.1). Ändamålet sätts vid insamlingen, och vidare behandling får inte vara oförenlig med det (artikel 5.1 b). Förordningen klassar inte information. Verifierat i förordningens text.

| Regel | Kräver klassning | Enheten | Vem |
|---|---|---|---|
| MSBFS 2020:6 | ja, tre aspekter | myndighetens information | myndigheten, med informationsägare enligt allmänt råd |
| MSBFS 2020:7 | nej | informationssystemet | systemägaren |
| MCFFS 2026:11 | ja, tre aspekter | information som behandlas i system, ansvar per behandling | informationsägaren |
| Cybersäkerhetslagen, NIS2 | nej | nätverks- och informationssystem | verksamhetsutövaren |
| Säkerhetsskyddslagen | ja, bara röjande | uppgiften, och handlingen efter sin högsta uppgift | verksamhetsutövaren |
| OSL | nej, sekretess prövas | uppgiften | myndigheten vid utlämnande |
| Dataskyddsförordningen | nej, risk bedöms | behandlingen och dess ändamål | den personuppgiftsansvarige |

### 2. Var metoderna sätter klassen

Metoderna klassar information. Men de flesta gör det inom ett sammanhang: en process, ett system eller en användning. Bara FIPS 199 och den brittiska policyn låter en klass gälla oförändrad i varje användning, och den brittiska gäller bara konfidentialitet.

**MSB:s och NCSC:s metodstöd klassar information inom ett klassningsobjekt.** "Det som ska klassas är information." Informationen samlas i ett klassningsobjekt, "en meningsfull del i organisationen där information hanteras, exempelvis en verksamhet, en enhet eller avdelning, en process, eller en tjänst". Klassningsobjektet kan också vara en informationstyp, "som exempelvis känsliga personuppgifter". Inom objektet finns informationsmängder, till exempel ett dokument eller en databas, och informationstyper (metodstödet, Klassning av information, daterad 4 februari 2025). Klassningsmodellen har konsekvensnivåer för konfidentialitet, riktighet och tillgänglighet, till exempel "Informationen kan tillåtas vara icke tillgänglig under…" (metodstödet, Klassningsmodell). Spårbarhet finns inte i klassningsmodellen. En sökning på hela webbplatsen gav en träff, ett exempel på arbetsmaterial för en workshop: "Spårbarhet är en stödjande del för egenskaperna ovan", och klassningen bedömer konfidentialitet, riktighet och tillgänglighet "(och i vissa fall spårbarhet)" (metodstödet, Arbetsmaterial workshop, exempel). Metodstödet ligger kvar på informationssakerhet.se med NCSC som avsändare och ska flyttas till ncsc.se i slutet av 2026. Verifierat.

**Ett it-system får minst den högsta klassen.** Systemet ska ha en skyddsnivå som motsvarar "de ingående informationsmängdernas högsta klassning". Det kan behöva en högre nivå när stora mängder lagras, när mängder sammanförs, eller när systemet utbyter information med system som har högre skyddsnivå (metodstödet, Klassning av information). Det är samma regel som katalogens Lagringsyta (C-165). Verifierat.

**SKR:s KLASSA klassar informationstillgångar i tre aspekter.** "Andra aspekter kan givetvis förekomma i en organisations klassningsarbete, såsom spårbarhet och oavvislighet, men dessa hanteras inte i KLASSA efter samråd med MSB" (KLASSA, Vägledning för informationsklassning). En grupperad tillgång "Bygger på de enskilda tillgångarnas klassificeringar", och för system gäller "Fokus är dock på informationen som hanteras i systemet" (KLASSA 5, vägledning och begreppslista). Verifierat.

**ISO/IEC 27001 och 27002:2022 kunde inte läsas.** Standarderna kostar pengar, och iso.org stängde ute automatisk hämtning. Den enda kontrolltext som lästes är 2013 års 8.2.1 i nederländsk översättning i BIO: "Informatie behoort te worden geclassificeerd met betrekking tot wettelijke eisen, waarde, belang en gevoeligheid voor onbevoegde bekendmaking of wijziging". Kontrollerna 5.9, 5.12 och 5.13 i 2022 års utgåva och ISO/IEC 27005 är inte lästa.

**NIST FIPS 199 klassar per informationstyp och tar maxvärdet för systemet.** En informationstyp får en säkerhetskategori: "SC information type = {(confidentiality, impact), (integrity, impact), (availability, impact)}". Information är "An instance of an information type". Systemets kategori "shall be the highest values (i.e., high water mark)" bland typerna i systemet (FIPS 199). Verifierat. Det är den källa som ligger närmast katalogen *(slutsats i underlaget)*.

**NIST SP 800-60 gör typens nivå preliminär och prövar den mot användningen.** Typerna hämtas ur verksamhetens processer, och systemägaren identifierar dem. Varje typ bedöms för "(i) each known variant of the information belonging to the type and (ii) each use of the information by the system under review". Nivån "can vary in different agencies or in dissimilar operational contexts" och kan ändras under livscykeln: ett kontrakt kan ha måttlig konfidentialitet under avtalstiden och låg efteråt (SP 800-60 vol. 1 rev. 1, avsnitt 4.2.2 och 4.3). Det finns bara ett tidigt arbetsutkast till en revision 2, från januari 2024. Verifierat.

**BSI börjar i verksamhetsprocessen och låter skyddsbehovet ärvas nedåt.** "Die Grundlage zur Bestimmung des Schutzbedarfs verschiedener Objekte ist der Schutzbedarf der Geschäftsprozesse und der zugehörigen Informationen. Der für diese Elemente ermittelte Schutzbedarf vererbt sich auf die für deren Verarbeitung genutzten Objekte" (BSI-Standard 200-2, avsnitt 8.2.2). Det gäller alla tre grundvärdena, och nivåerna är normal, hoch och sehr hoch. Varje verksamhetsprocess har en ansvarig, "Informationseigentümer" (avsnitt 3). Maximumprinzip ger ett system det högsta behovet bland det som körs där. Verifierat.

**Den nederländska BIO klassar per verksamhetsprocess, och processägaren väljer.** "De BBN-toets wordt voor ieder bedrijfsproces uitgevoerd" och "De keuze voor een BBN wordt gemaakt door de proceseigenaar" (BIO 1.04, 2020). Information som tas emot utan märkning behandlas "conform de classificatie-eisen van het ontvangende proces". Nya BIO2 (v1.3, januari 2026) klassar "een proces en een informatiesysteem", och vägledningen för baslinjetestet säger att systemet eller processen "erft automatisch het zwaarste risicoprofiel". Verifierat. Om BIO2 formellt har avskaffat de tre basnivåerna är inte bekräftat.

**Den brittiska klassningspolicyn låter skaparen klassa, bara för konfidentialitet.** Skaparen är "responsible for determining the classification, handling, dissemination and disposal of that information", och "Only the information creator from the originating organisation can reclassify". Den som använder informationen får ifrågasätta klassen med skäl (Government Security Classifications Policy, version 2.0, augusti 2024). Skalan har tre nivåer och gäller sekretess, inte riktighet eller tillgänglighet. Verifierat.

**DAMA-DMBOK kunde inte läsas.** Boken är inte fritt tillgänglig, och DAMA:s webbsida säger inget om klassning eller om ägare, förvaltare och förvarare. NIST:s ordlista har nästan samma definition för *information owner* och *information steward*. Där står också att en *data steward* "regularly assess classification criteria and test compliance to prevent security issues resulting from data aggregation" (NIST:s ordlista, CNSSI 4009). Ordlistan saknar *data custodian*.

**Märkning per förekomst är motsatsen.** NIST SP 800-162 gör klassningen till ett attribut på varje objekt, bredvid typ och ägare, och attributen ska sättas "as objects are created". CISA vill att organisationer ska "inventory, categorize, and label data", helst automatiskt (Zero Trust Maturity Model 2.0). Den brittiska policyn låter skaparen märka varje tillgång. Där sitter klassen på förekomsten, inte på typen. Verifierat.

### 3. Samlingar av information

Alla källor behandlar en samling för sig. De skiljer sig i om samlingen får en egen klass eller om bara skyddet runt den höjs.

**Säkerhetspolisen skiljer ackumulering från aggregering.** Ackumulering är "en större samling av många liknande uppgifter, till exempel ett register över anställda", och den "leder i normalfallet inte till några konsekvenser för säkerhetsskyddsklassificeringen av uppgifterna eller uppgiftssamlingen". Aggregering betyder att man genom att kombinera uppgifterna "går att härleda ny information". "De nya uppgifter som går att härleda genom aggregering ska säkerhetsskyddsklassificeras, precis som alla andra uppgifter", och den nya uppgiften "blir då dimensionerande för de säkerhetsskyddsåtgärder som behöver vidtas". Nya uppgifter ska vara "konkreta och formulerbara", och det bör finnas spårbarhet i varför den uppstår (Säkerhetspolisen, Vägledning i säkerhetsskydd: Informationssäkerhet, oktober 2023, avsnitt 2.4). Verksamhetsutövaren klassar. Verifierat.

**De civila reglerna ser båda fallen som en risk att hantera.** "Myndigheten bör bedöma vilka risker det medför när information som myndigheten ansvarar för ackumuleras eller aggregeras" (MSBFS 2020:6, allmänt råd). MCFFS 2026:11 säger detsamma i ett allmänt råd. Metodstödet höjer i stället systemets skyddsnivå vid ackumulering och aggregering. Verifierat.

**BSI höjer behovet hos det som rymmer samlingen.** Kumulationseffekt betyder att många små skador tillsammans ger en större: "erhöht sich der Schutzbedarf des Objektes". Verteilungseffekt går åt andra hållet: behovet sänks när informationen är spridd och ett enskilt system inte bär det hela, och effekten "tritt hauptsächlich bezüglich des Grundwertes der Verfügbarkeit auf" (BSI 200-2, avsnitt 8.2.2). Effekterna gäller system, rum och förbindelser, inte informationen. Verifierat.

**Brittiska regeringen låter delarna behålla sin klass.** "Aggregating data will not usually affect the classification of the component information, but a new piece of data or set of data … may need to be classified at a higher level" (Guidance 1.5). Organisationen bedömer samlingen. Verifierat.

**NIST höjer systemet.** Om granskningen visar "increased sensitivity or criticality associated with information aggregates" kan systemets nivå behöva justeras (SP 800-60, avsnitt 4.4.2.1). NIST IR 8496 säger att aggregering skapar nya datatillgångar vars etiketter kan behöva uppdateras. IR 8496 finns bara som utkast från november 2023, och NIST drog tillbaka utkastet den 10 december 2025. Verifierat.

**Vem som klassar samlingen.** Säkerhetspolisen och den brittiska policyn låter verksamheten eller organisationen göra det. Katalogen ger det till processägaren för beteendet som upprättade sammanställningen (beslut 35). Ingen källa säger emot det, men ingen säger det heller *(slutsats i underlaget)*.

### 4. Typ och förekomst

Flera källor skiljer ansvaret för reglerna om klassningen från klassningen av varje förekomst.

**BSI har tre roller för klassning.** Den som skapar informationen, *Ersteller*, gör "Erst-Klassifikation" av varje post. Den fackansvarige, *Fachverantwortlicher* eller linjechefen, "konkretisiert Regelungen zur Klassifikation in seinem Bereich" och övervakar skaparnas klassning. Den klassningsansvarige skriver organisationens strategi och regler (BSI 200-2, tabell 1 i avsnitt 5). Samtidigt säger BSI att ordningen ska göra det möjligt "für jede Art der Information die korrekte Einstufung abzuleiten, ohne dass diese dafür explizit gekennzeichnet werden muss" (avsnitt 5.1). Verifierat. Typen bär alltså klassen, och förekomsten märks när det behövs *(slutsats i underlaget)*.

**NIST skiljer typen från förekomsten.** FIPS 199 klassar typen och kallar informationen en förekomst av typen. NIST IR 8496 beskriver klassningsschemat som "a taxonomy of all of an organization's known data asset types", och sedan märks varje tillgång. "The business owner is key for determining the data classifications" (IR 8496, tillbakadraget utkast). Verifierat.

**Den brittiska policyn klassar förekomsten.** Skaparen klassar varje tillgång. Det motsvarar USA:s *original classification*. Den amerikanska skillnaden mellan *original* och *derivative classification* är inte läst i källan.

**Metodstödet låter en verksamhet ändra en gemensam klassning.** En organisation kan klassa information som finns i många verksamheter gemensamt. "Verksamheter kan i vissa organisationer ha rätt att höja och ibland även sänka klassningen för dessa beroende på i vilket sammanhang informationen hanteras." En sänkning godkänns av ett informationssäkerhetsråd eller av de berörda informationsägarna, efter en riskbedömning (metodstödet, Klassning av information). Ansvaret följer verksamhetsansvaret: "Verksamhetsansvariga, exempelvis linjechefer, processägare, projektägare och informationsägare, ansvarar för att den egna informationen klassas". Verifierat.

**Den svenska uppdelningen mellan informationsägare, systemägare och linjechef** finns i MSBFS 2020:6 och 2020:7 och i MCFFS 2026:11. Informationsägaren svarar för informationen eller behandlingen, systemägaren för systemets säkerhetsåtgärder. Linjechefens ansvar för förekomsterna, som katalogen ger Linjechef (C-207), står inte i föreskrifterna. Metodstödet nämner linjechefen bland de verksamhetsansvariga som ser till att informationen klassas.

### 5. Kan informationsägaren känna den framtida användningen?

Den här frågan väger tyngst. Svaret skiljer sig mellan klasserna. Konfidentialiteten följer informationen i flera källor. Tillgängligheten sätts i kontinuitetsmetoderna på aktiviteten, och informationen får sitt krav från aktiviteterna som använder den.

**Kontinuitetsmetoderna sätter tidskravet på aktiviteten.** ISO/TS 22317 identifierar "the resources needed to perform prioritized activities following a disruption, including their dependencies, and requirements, specifying RTOs and applicable recovery point objectives (RPOs)" (ISO/TS 22317:2021, inledningen, läst i förhandsvisning). Längsta tålbara avbrott, MTPD, sätts på produkter, tjänster och aktiviteter. Återställningstiden, RTO, och återställningspunkten, RPO, sätts på resurserna. Resten av standarden och ISO 22301 avsnitt 8.2.2 är inte lästa.

**NIST SP 800-34 sätter tre mått på tre enheter.** Den längsta tålbara avbrottstiden, MTD, gäller "a mission/business process outage". RTO är den längsta tid "that a system resource can remain unavailable". RPO är den punkt "to which mission/business process data can be recovered", och den speglar "how much data loss the mission/business process can tolerate" (SP 800-34 rev. 1, avsnitt 3.2.1). Konsekvensanalysen börjar i systemets tillgänglighetskategori enligt FIPS 199 och förfinar den per process. Verifierat.

**BSI 200-4 härleder kravet från processen och tar det strängaste.** Längsta tålbara avbrott "wird anhand einer Bewertung des Schadenspotenzials je Geschäftsprozess ermittelt", och återställningstiden "wird aus der MTPD abgeleitet". När flera processer använder samma resurs "muss die kleinste RTO für diese Ressource gewählt werden" (BSI 200-4, kapitel 7 och avsnitt 7.2.3). För information sätts återställningspunkten som "eine fachliche Anforderung des Prozesseigentümers". BSI:s exempel ger samma kunddata två krav: "transaktionsgenau" i en process och "2 Tage" i en annan. Kraven slås ihop enligt en minimiprincip till det strängaste (tabell 26). Verifierat.

**BSI skiljer tillgänglighet i normal drift från kontinuitet.** "Die Verfügbarkeit im Normalbetrieb muss z. B. nicht zwangsläufig der Verfügbarkeit im Notbetrieb entsprechen." I BSI:s exempel får ett kundsystem hög tillgänglighet i skyddsbehovsanalysen, 99,9 procent per år, men inget kontinuitetskrav i konsekvensanalysen, eftersom verksamheten klarar sig utan det under en kris (BSI 200-4, avsnitt 2.4). Verifierat.

**MSB:s lathund sätter avbrottstiden på aktiviteten.** Verksamheten bedömer "acceptabel avbrottstid för respektive aktivitet". För informations- och it-system kan även en återställningspunkt anges: "den punkt till vilken det är nödvändigt att återställa den information som används av en prioriterad aktivitet" (MSB, lathund för kontinuitetshantering, MSB2372, september 2024). Metodstödet säger samma sak: "Hur lång tid en störning är acceptabel kan dock variera mellan olika verksamheter i organisationen" (metodstödet, Kontinuitetshantering för informationstillgångar). Verifierat.

**MCFFS 2026:11 lägger avbrottstiden på behandlingen.** Informationsägaren meddelar acceptabla avbrottstider "för informationsbehandlingen" (3 kap. 7 §). Verksamhetsutövaren fastställer en prioritetsordning för att återställa verksamheten (14 §) och acceptabla avbrottstider för produktionsmiljön (15 §). NCSC:s utkast härleder tiderna ur kontinuitetsarbetet. Verifierat.

**NIST SP 800-60 nämner just den framtida användaren.** Information med låg känslighet "may be used by other systems to enable extremely sensitive or critical functions (e.g., air traffic control use of weather information)" (SP 800-60, s. 27). Systemägaren kan höja systemets tillgänglighet när konsekvensanalysen visar att systemet måste vara i drift inom fyra till åtta timmar, "irrespective of the aggregated information type availability security impact level" (avsnitt 4.4.2.3). Verifierat.

**Konfidentialiteten följer informationen i flera källor.** Den brittiska policyn låter bara skaparen ändra klassen. Säkerhetsskyddet och OSL klassar uppgiften. NIST IR 8496 säger att skyddskraven "are highly likely to change over time, while the data classifications themselves tend to be static" (IR 8496, tillbakadraget utkast). Det stöder katalogens skäl i beslut 57 för konfidentialiteten *(slutsats i underlaget)*.

**Dataskyddet låter användningen styra.** Ändamålet sätts per behandling. Vidare behandling prövas mot bland annat "the context in which the personal data have been collected" (dataskyddsförordningen artikel 6.4 b). Konsekvensbedömningen gäller behandlingar "performed in a specific context and for a specific purpose" (Artikel 29-gruppen, WP248 rev. 01, 2017). Att EDPB har ställt sig bakom WP248 är inte bekräftat i den lästa filen.

**Omklassning.** Metodstödet vill att klassningen ses över årligen och vid större förändringar. NIST IR 8496 säger att varje datatillgång "should be monitored … for changes". Säkerhetspolisen påpekar att ny funktion i ett system kan ge nya sammanställningar och därmed nya uppgifter. Mottagarens roll skiljer sig. Den brittiska policyn låter mottagaren bara ifrågasätta klassen. Metodstödet låter en verksamhet höja, och med godkännande sänka, en gemensam klassning. BIO låter mottagarens process klassa information som kommer in utan märkning.

**Spårbarhet saknas som egen klass i alla internationella källor.** BSI behandlar "Authentizität und Nicht-abstreitbarkeit als Spezialfälle der Integrität" (BSI 200-2). FIPS 199 räknar "non-repudiation and authenticity" till riktigheten. Ingen källa sätter spårbarhet varken på aktiviteten eller på informationen.

### 6. Kritik och alternativ

Granskningar och forskning visar att klassning ofta inte används och att den görs olika. Alternativen flyttar arbetet till en baslinje eller till själva åtkomsten.

**Klassning görs sällan i praktiken.** Riksrevisionen fann att "Det är få forskare som klassar sina forskningsdata i enlighet med lärosätenas modeller för informationsklassning". 21 av 24 lärosäten har en modell, oftast för it-system och informationsmängder, nästan lika ofta för informationstyper. Bara 1 av 24 lyfte klassningen som något som fungerar bra. Vid ett granskat lärosäte "implementerades aldrig" modellen (Riksrevisionen, RiR 2023:20, Informationssäkerhet vid universitet och högskolor, avsnitt 3.2.2). Verifierat.

**Ansvar och tidpunkt är oklara.** Riksrevisionen återger MSB:s enkät från 2014: 67 procent av myndigheterna hade en klassningsmodell, 41 procent hade inte uttalat vem som ansvarar och 59 procent hade inte bestämt när klassningen ska göras (RiR 2014:23, Informationssäkerheten i den civila statsförvaltningen, avsnitt 4.1.3). Siffrorna är andrahandsuppgifter. Riksrevisionen återger också en intervju om att myndigheter "hanterar samma information, men med olika nivå på skydd och klassning". Verifierat.

**Olika personer klassar olika.** Klassning bygger på "subjektiva bedömningar vilket kan leda till inkonsekventa klassningar". Två klassningar med olika personer kan ge olika resultat. Färre än 20 procent av 139 svarande myndigheter tyckte att verktygen uppfyllde deras behov (MSB, VISKA: Verktygsstöd för anpassningsbar informationsklassning, 2024). Verifierat.

**Grov klassning höjer allt.** En doktorsavhandling beskriver det vanligaste arbetssättet, att klassa en process eller ett system: "some information might be overclassified as all information in the process/application/system will inherit the highest classification", och riskerna i enskilda tillgångar missas (Bergström, Supporting Information Security Management, 2020, avsnitt 2.3). Verifierat. Samma sak kan gälla katalogens regel för lagringsytan *(slutsats i underlaget)*.

**Överklassning kostar och hindrar delning.** Brittiska regeringen ersatte 2014 ett system med sex nivåer. Skälet var "a tendency to over mark documents rather than to manage risk properly" (Cabinet Office, pressmeddelande 17 oktober 2013). I USA säger en lag från 2010 att överklassning "interferes with accurate, actionable, and timely information sharing, increases the cost of information security" (Public Law 111-258, 2 §). En amerikansk granskning från 2006 fann 56 olika beteckningar för känslig men oklassad information, med olika regler för liknande information (GAO-06-385). Verifierat.

**Forskningen är tunn.** Problemen i klassning är "human–organizational challenges … evident in the activities but have received little attention in research" (Andersson, Problems in information classification: insights from practice, Information & Computer Security 31(4), 2023; bara sammanfattningen läst). En avhandling från 2026 försvarar klassningen och säger att det subjektiva är "a necessary and unavoidable component of meaningful classification decisions" (Andersson, Beyond Levels, Luleå tekniska universitet 2026; bara sammanfattningen läst).

**Alternativ 1: en baslinje, och analys bara för undantagen.** BSI: "Nur bei einem signifikant höheren Schutzbedarf muss zusätzlich eine Risikoanalyse … durchgeführt werden" (BSI 200-2). Brittiska regeringens lägsta nivå täcker omkring 90 procent av verksamheten med grundskydd (pressmeddelande 2013). BIO2 ersätter de tre basnivåerna med en riskbaserad ansats (nederländska regeringens nyhet om BIO2). NIST:s baslinjer är "a starting point" som organisationen anpassar (SP 800-53B). Här sitter klassen bara på undantagen.

**Alternativ 2: attributbaserad åtkomst.** Åtkomst ges "based on assigned attributes of the subject, assigned attributes of the object, environment conditions, and a set of policies". Klassningen är ett attribut på objektet bredvid typ och ägare, och attributen ska sättas "as objects are created" (NIST SP 800-162). Här sitter klassen på förekomsten och vägs vid varje åtkomst mot vem som frågar och i vilket sammanhang.

**Alternativ 3: nollförtroende och dataorienterat skydd.** "Access to resources is determined by dynamic policy … policies can vary based on the sensitivity of the resource/data" (NIST SP 800-207). CISA vill att organisationer ska "inventory, categorize, and label data", helst automatiskt (Zero Trust Maturity Model 2.0, 2023). Här sitter känsligheten på resursen och prövas per session.

### 7. Känslighet som uppstår i kopplingen mellan två objekt

Frågan kommer från ärende #177. En värdemängd för hälsotillstånd är inte känslig för sig. Den blir känslig först när den kopplas till en person. En adress är öppen, men att en person med skyddad identitet bor där är känsligt. Inget av objekten bär känsligheten ensamt, och den gäller inte varje förekomst. Källorna är överens om att känsligheten sitter i kopplingen. De skiljer sig i var klassen skrivs: på samlingen, på relationen eller hos den som kan göra kopplingen.

**Dataskyddsförordningen avgör känsligheten genom kopplingen till en person.** Personuppgifter är "any information relating to an identified or identifiable natural person", och identifieringen kan vara indirekt (artikel 4.1). Uppgifter om hälsa är personuppgifter "which reveal information about his or her health status" (artikel 4.15 och skäl 35). Om någon är identifierbar avgörs av "all the means reasonably likely to be used, such as singling out, either by the controller or by another person" (skäl 26). Pseudonymiserade uppgifter förblir personuppgifter så länge nyckeln finns, och nyckeln ska hållas "separately" (artikel 4.5). Verifierat.

**Information om ett föremål kan bli personuppgift genom ändamålet.** Artikel 29-gruppen tar ett hus värde som exempel: "The value of a particular house is information about an object". Värdet är ingen personuppgift när det visar prisnivån i ett område, men det är det när det används för att bestämma ägarens skatt. Uppgifter "relating to" en person kräver ett innehåll, ett ändamål eller ett resultat som gäller personen (WP136, yttrande 4/2007, exempel 5). Samma yttrande säger att uppgifter "combined with other pieces of information (whether the latter is retained by the data controller or not)" kan peka ut en person. Ett senare yttrande namnger tre risker: att peka ut en person, att koppla ihop poster, och att sluta sig till ett värde, "the possibility to deduce, with significant probability, the value of an attribute from the values of a set of other attributes" (WP216, yttrande 05/2014, avsnitt 3). Verifierat.

**Uppgifter som indirekt avslöjar något känsligt är känsliga uppgifter.** EU-domstolen fann att uppgifter "liable to disclose indirectly the sexual orientation of a natural person" är känsliga personuppgifter enligt artikel 9.1. Domstolen avvisade en tolkning som skiljer mellan olika slag av känsliga uppgifter och pekade på ordet "reveal" i definitionen av uppgifter om hälsa (mål C-184/20, punkt 124 och domslutet). Verifierat.

**Samma uppgift kan vara personuppgift för en part och inte för en annan.** Ett fordons identifikationsnummer är personuppgift för den som rimligen kan koppla det till en person, "even if the VIN is not, in itself, personal data for them" (mål C-319/22, punkt 49). Pseudonymiserade uppgifter ska inte anses vara personuppgifter "in all cases and for every person" (mål C-413/23 P, punkt 86). Verifierat. Skyddad identitet står inte i artikel 9. Känsligheten i adressfallet kommer ur sekretessreglerna, men vilken paragraf i OSL som gäller är inte kontrollerad.

**USA klassar samlingen bara när den visar ett nytt samband.** "Compilations of items of information that are individually unclassified may be classified if the compiled information reveals an additional association or relationship that … is not otherwise revealed in the individual items of information" (Executive Order 13526, 1.7 e). De enskilda delarna behåller sin lägre klass och märks "U". Dokumentet märks med samlingens klass och ska förklara "the circumstances involved with association" (DoD Manual 5200.01 vol. 2, 2012). Samlingen klassas bara där delarna realistiskt kan föras samman (vol. 1, bilaga 4). Verifierat i 2012 års text. Den gällande versionen från 2025 gick inte att hämta.

**Säkerhetspolisen säger samma sak med svenska ord.** När en samling gör det möjligt att härleda något nytt är det en ny uppgift som klassas för sig (Vägledning i säkerhetsskydd: Informationssäkerhet, avsnitt 2.4, se fråga 3). Verifierat.

**NIST sätter nivån på den samling personuppgifter som finns, inte på fälttypen.** NIST skiljer *linked* information, som är kopplad till annan information om personen, från *linkable* information, som kan kopplas. Om den andra källan finns i samma system utan skydd som håller isär källorna räknas uppgifterna som kopplade. Organisationen ska bedöma "the sensitivity of each individual PII data field, as well as the sensitivity of the PII data fields together". Vissa kombinationer, som namn och kortnummer, är känsligare än fälten var för sig. Tre listor med samma fält kan få nivåerna låg, måttlig och hög beroende på sammanhanget (SP 800-122, avsnitt 2.1, 3.1 och 3.2.3). Verifierat.

**Databasforskningen klassar relationen.** I databaser med flera säkerhetsnivåer är "sensitive associations among entities of different types … best treated by representing the sensitive association separately and classifying the individual entities low and the relationship high". En känslig koppling mellan egenskaper hos samma entitet hanteras genom att de egenskaper som bidrar mest lagras för sig med högre klass (Lunt, Aggregation and inference: facts and fallacies, IEEE Symposium on Security and Privacy 1989; bara sammanfattningen läst). Senare forskning uttrycker samma sak som villkor på mängder av attribut, till exempel att namn och lön inte får lagras tillsammans i klartext (Aggarwal med flera, Two Can Keep a Secret, CIDR 2005, läst i sin helhet). Ciriani med flera bryter känsliga kopplingar genom att dela upp data (ACM TISSEC 2010; bara sammanfattningen läst).

**ISO/IEC 29100 och 27701 kunde inte läsas.** Inget i underlaget bygger på dem. BSI:s Kumulationseffekt gäller skador som läggs ihop på ett system, inte nytt innehåll ur en koppling (BSI 200-2, avsnitt 8.2.2).

Sammanfattat ger källorna tre platser för klassen. Den första är samlingen eller kopplingen som ett eget objekt, med delarna kvar på sin nivå: USA, Säkerhetspolisen och Lunt. Den andra är den samling som faktiskt finns hos en verksamhet, bedömd i sitt sammanhang: NIST SP 800-122. Den tredje är parten som kan göra kopplingen: EU-domstolen. Ingen källa som lästes sätter klassen på båda objekten för att kopplingen finns.

## Möter metoden

Varje fynd nedan säger vad Informationskartläggning redan gör, vad källorna gör annorlunda och vilka vägar som öppnas. Varje väg har ett fall ur exempelorganisationerna. Ett fall som börjar med "Anta att" bygger på något som inte står i exemplen i dag. Meningar märkta *(slutsats i underlaget)* är underlagets egna slutsatser, inte en källas.

### Spårbarhet som fjärde klass

**Metoden i dag.** Informationsägaren klassar objektet i fyra klasser, och kartan bär nivån i varje klass. Informationstillgång (C-166) säger att spårbarheten kommer från MSB:s metodstöd och SKR:s KLASSA.

**Källorna.** MSBFS 2020:6 och MCFFS 2026:11 binder bara tre aspekter. Spårbarhet står i ett allmänt råd, "bör beaktas". KLASSA tar uttryckligen inte med den. Metodstödet nämner den bara i ett exempel på arbetsmaterial, som "en stödjande del" och "i vissa fall". BSI och NIST räknar äkthet och oavvislighet till riktigheten. Hänvisningen i Informationstillgång (C-166) stämmer alltså för metodstödets exempel men inte för KLASSA *(slutsats i underlaget)*.

**Vägar.**

- **Behåll fyra klasser och rätta hänvisningen.** Informationstillgång (C-166) säger då att spårbarheten är katalogens val med stöd i ett allmänt råd och i metodstödets exempel. Anta att Myndigheten för föreningsstöd klassar Beslut högt i spårbarhet, eftersom myndigheten måste kunna visa vem som ändrade ett beslut.
- **Lägg spårbarheten under riktigheten.** Loggning står kvar som åtgärd men tjänar riktigheten. Kartan bär tre nivåer i stället för fyra. Anta att Beslut får hög riktighet, och att loggningen i Ärendesystemet är en åtgärd för den.
- **Gör spårbarheten till ett krav på behandlingen.** Spårbarhet gäller vem som gjort vad. Kravet läses då ur beteendet, på samma sätt som ändamålet. Anta att analysfunktionen måste kunna visa hur Riskindikator per förening räknades fram, medan Utbetalningar per kommun inte kräver det.

### Informationsägaren per behandling

**Metoden i dag.** Informationsägaren äger objektet som typ och klassar det. Klassen är densamma i varje beteende (beslut 57). Paret beteende och informationsobjekt är redan ankaret för behandlingen och för registerförteckningen (beslut 31).

**Källorna.** MCFFS 2026:11 kräver en informationsägare för "All informationsbehandling i system". Informationsägaren bedömer skyddsnivån "för den informationsbehandling som denne ansvarar för" och anger avbrottstider för behandlingen. NCSC:s utkast till vägledning talar i stället om "en viss typ eller mängd av information". Föreskrifterna gäller den som omfattas av cybersäkerhetslagen. Om exempelorganisationerna gör det är inte prövat.

**Vägar.**

- **Behåll informationsägaren per objekt och läs behandlingen ur kartan.** Kartan visar vilka beteenden som har åtkomst till objektet. Varje sådant par är en informationsbehandling, och informationsägaren för objektet svarar för den. Chefen för Register- och tillsynsenheten svarar då för Företrädare både i registret och i analysfunktionens datalager.
- **Låt processägaren vara informationsägare för behandlingen i sitt beteende.** Informationsägaren för objektet sätter golvet. Processägaren svarar för skyddet i sin behandling. Chefen för Analysenheten svarar då för Företrädare i datalagret, inom den nivå chefen för Register- och tillsynsenheten har satt. Katalogen har redan regeln att den som upprättar en sammanställning äger den (beslut 35).
- **Gör paret till ett element med en egen nivå.** Det ger flest beslut, men det följer föreskriftens ordval närmast *(slutsats i underlaget)*. Analysfunktionens behandling av Utbetalning får egen nivå i tillgänglighet, skild från Genomföra ansökningsomgångens behandling av samma objekt.

### Tillgänglighet sätts på aktiviteten

**Metoden i dag.** Informationsägaren sätter tillgängligheten på objektet, och den är densamma i varje beteende (beslut 57). Huvudfrågan i steg 4 är om varje lagringsyta klarar det högst klassade objektet där.

**Källorna.** Kontinuitetsmetoderna sätter avbrottstiden på aktiviteten och härleder återställningstiden till resurserna. Återställningspunkten sätts på informationen, men per process och av processägaren. Flera processer på samma resurs ger det strängaste kravet. MCFFS 2026:11 lägger avbrottstiden på behandlingen. Skälet i beslut 57 gäller skadan av ett röjande. Skadan av ett avbrott beror på vad beteendet ska göra just då, så skälet bär inte för tillgängligheten *(slutsats i underlaget)*.

**Vägar.**

- **Behåll tillgängligheten på objektet som ett golv, och låt varje beteende lägga till sitt krav.** Processägaren anger avbrottstid och återställningspunkt för sitt beteende. Lagringsytan och applikationen får det strängaste kravet av alla beteenden som använder dem, samma minimiprincip som hos BSI. Anta att uthyrningen hos Brinkstadsbostäder klarar två dagar utan Hyresgäst, medan Åtgärda en felanmälan behöver hyresgästens telefonnummer inom en timme vid en vattenläcka. Uthyrningschefen sätter golvet, teknisk chef anger timmen som processägare, och fastighetssystemet måste klara timmen.
- **Flytta tillgängligheten till beteendet.** Informationsägaren sätter konfidentialitet och riktighet. Processägaren sätter tillgängligheten genom en konsekvensanalys av beteendet. Kartan visar då nivåer på två ställen: på objektet och på beteendet. Anta att Utbetalning hos Myndigheten för föreningsstöd tål en veckas avbrott i analysfunktionen men inte en dag i Genomföra ansökningsomgången när pengarna ska betalas ut. Chefen för Bidragsenheten sätter kravet för ansökningsomgången, chefen för Analysenheten för analysfunktionen.
- **Dela tillgängligheten i två mått.** Tillgänglighet i normal drift sitter på objektet eller applikationen. Kontinuitet vid en kris sitter på beteendet, som i BSI 200-4. Anta att Hyresavtal har hög tillgänglighet i normal drift, men att bolaget klarar sig en vecka utan att se avtalen under en kris. Anta också att Åtgärda en felanmälan har ett kontinuitetskrav, eftersom akuta fel måste åtgärdas även när systemet ligger nere.

### Klassen i ett sammanhang

**Metoden i dag.** Klassen sitter på objektet och är densamma i varje beteende. Det som beteendet skapar är ett eget objekt med egen klass (beslut 57). Ett objekt kan delas upp när nivån beror på en uppgift (beslut 40).

**Källorna.** För konfidentialiteten stöder säkerhetsskyddet, OSL och den brittiska policyn katalogen. SP 800-60 prövar däremot varje typ mot varje användning. Metodstödet låter en verksamhet höja och ibland sänka en gemensam klassning efter sammanhanget. BIO låter mottagarens process klassa information som kommer in utan märkning. OSL fäster dessutom sekretessen i ett sammanhang, "i ärende om", som katalogen redan läser ur beteendet (Uppgift (C-161)).

**Vägar.**

- **Behåll klassen på objektet.** Kartan räknar då med en nivå per objekt, och det stöds för konfidentialiteten. Företrädare har samma klass i Registrera en ny företrädare som i analysfunktionens datalager.
- **Låt informationsägaren sätta ett golv som ett beteende får höja men inte sänka.** En sänkning kräver informationsägarens ja, som i metodstödet. Teknisk chef hos Brinkstadsbostäder får höja kravet på Hyresgäst i Åtgärda en felanmälan, men inte sänka det under uthyrningschefens golv.
- **Sätt klassen på paret beteende och objekt.** Paret är redan ankaret för behandlingen (beslut 31). Kartan får då en nivå per åtkomst, inte per objekt. Det stämmer med SP 800-60. Kostnaden är fler klassningsbeslut. Riksrevisionen fann att klassningsmodeller redan i dag ofta inte används. Anta att Hyresgäst får hög konfidentialitet i uthyrningen, där inkomstuppgifterna finns, och låg i Åtgärda en felanmälan, där bovärden bara ser namn och telefonnummer.

### Ackumulering och aggregering

**Metoden i dag.** En sammanställning klassas för sig, högre genom sammanställningseffekten och lägre när uppgiften försvinner (Sammanställning (C-162)). Exemplet är förteckningen över alla föreningars företrädare, som är känsligare än varje företrädare för sig. Processägaren för beteendet som upprättade sammanställningen äger den (beslut 35).

**Källorna.** Säkerhetspolisen skiljer ackumulering, som normalt inte ändrar klassen, från aggregering, som ger en ny uppgift med egen klass. Metodstödet och BSI höjer i stället systemets eller lagringens skydd vid ackumulering. Den brittiska policyn låter delarna behålla sin klass. Katalogens förteckning över alla företrädare är ackumulering i Säkerhetspolisens mening *(slutsats i underlaget)*.

**Vägar.**

- **Behåll ett fall.** Varje sammanställning klassas för sig, som i dag. Förteckningen över alla föreningars företrädare är en sammanställning med egen klass, liksom Riskindikator per förening.
- **Skilj fallen åt.** Ackumulering höjer lagringsytans krav men ger inget nytt objekt. Aggregering ger ett nytt informationsobjekt, en sammanställning med egen klass och ägare. Hos Myndigheten för föreningsstöd är alla Företrädare i datalagret en ackumulering. Den höjer datalagrets krav. Riskindikator per förening är en aggregering. Den är ett nytt objekt, och chefen för Analysenheten klassar det.
- **Kräv att den nya uppgiften går att formulera.** Säkerhetspolisen kräver att den nya uppgiften är konkret och att skälet går att spåra. Följdfrågan i steg 4 blir: vilken ny uppgift går att utläsa ur samlingen? Förteckningen över utsatta roller hos Brinkstadsbostäder ger uppgiften vilka anställda som är utsatta för hot. Ingen enskild Yrkesroll visar det.

### Typen och förekomsten

**Metoden i dag.** Informationsägaren äger typen. Linjechefen svarar för förekomsterna. Värsta fallet gäller, och när nivån blir för hög delas objektet upp (beslut 40). Märkningen sitter på representationen (Representation (C-085)).

**Källorna.** BSI låter den som skapar informationen klassa varje post inom den fackansvariges regler. Den brittiska policyn låter skaparen klassa. NIST SP 800-162 sätter klassningen som ett attribut på varje objekt när objektet skapas. FIPS 199 och NIST IR 8496 klassar typen och märker förekomsten.

**Vägar.**

- **Behåll värsta fallet och uppdelningen.** Yrkesroll får nivån för de utsatta rollerna, eller så blir Utsatt roll ett eget objekt.
- **Låt informationsägaren ge regeln och den som skapar förekomsten sätta nivån.** Informationsägaren säger när en förekomst ska ha högre nivå. Linjechefens medarbetare märker förekomsten när den skapas. Kartan bär regeln, inte varje förekomst. Anta att informationsägaren för Yrkesroll hos Brinkstadsbostäder beslutar regeln att en roll som handlägger avhysningar är utsatt. Den som lägger upp en ny roll märker den enligt regeln.

### Baslinje i stället för klassning av varje objekt

**Metoden i dag.** Huvudfrågan i informationssäkerheten är om varje informationsobjekt har en ägare och en klass.

**Källorna.** Granskningarna visar att klassning ofta inte görs fullt ut och görs olika. BSI, brittiska regeringen och BIO2 använder en baslinje för det mesta och analyserar bara undantagen.

**Vägar.**

- **Behåll frågan som den är.** Varje objekt får sin klass. Myndigheten för föreningsstöd klassar Ansökan, Beslut och Utbetalning lika noga som Företrädare.
- **Inför en baslinje.** Organisationen beslutar en nivå som gäller alla objekt utan egen klass. Informationsägaren klassar bara det som avviker. Huvudfrågan blir: avviker objektet från baslinjen, och har det i så fall en klass? Anta att baslinjen hos Myndigheten för föreningsstöd är intern. Företrädare, Kontonummer och Riskindikator per förening avviker och får egen klass, medan Utbetalning har baslinjen. Informationsområde (C-198) gör redan något liknande, eftersom området ger klassen nedåt.

### Känslighet i kopplingen

**Metoden i dag.** Klassen sitter på informationsobjekten, inte på relationerna. Värdemängd (C-197) är text vid en uppgift, utan egen klass. När nivån beror på värdet i en uppgift gäller värsta fallet, eller så blir delmängden ett eget objekt (beslut 40). En Sammanställning (C-162) klassas för sig. Relationen associeras med (C-099) har ingen klass. Följdfrågorna i steg 4 frågar efter det högst klassade objektet på varje lagringsyta, inte efter vilka objekt som går att koppla ihop där.

**Källorna.** Känsligheten sitter i kopplingen, och de enskilda delarna behåller sin lägre nivå. Kopplingen kan gå indirekt, genom ett föremål som en lägenhet eller ett hus. Om en uppgift alls är personuppgift beror på om den som har den kan göra kopplingen.

Fallet som vägarna nedan använder: Anta att Brinkstadsbostäder anpassar lägenheter av hälsoskäl, till exempel med ramp eller ett nytt badrum. Teknisk chef äger ett nytt informationsobjekt Lägenhetsanpassning, med uppgifterna åtgärd och skäl. Skälet tar sina värden ur en värdemängd Hälsotillstånd. Lägenhetsanpassning hör till Lägenhet, inte till Hyresgäst. Anta också att en hyresgäst har skyddad identitet. Hyresavtal kopplar Hyresgäst till Lägenhet, och lägenhetens adress är öppen.

**Vägar.**

- **Värsta fallet på det objekt som håller kopplingen.** Det är katalogens regel i dag. Hyresavtal håller kopplingen mellan hyresgästen och adressen, så Hyresavtal får den nivå som hyresgästen med skyddad identitet kräver. Lägenhetsanpassning får nivån för uppgifter om hälsa, eftersom bovärden kan se vem som bor i lägenheten. Kostnaden är att alla hyresavtal och alla anpassningar får den högsta nivån, fast de flesta inte behöver den.
- **Gör kopplingen till ett eget informationsobjekt med egen klass.** Delarna behåller sin nivå, som hos Lunt och i USA. Hyresavtal, Hyresgäst och Lägenhet har sin vanliga nivå. Kopplingen mellan en hyresgäst med skyddad identitet och en lägenhet blir ett eget objekt, Skyddat boende, klassat högt och hanterat för sig. Det följer beslut 40: det som regleras för sig blir ett eget objekt. Uthyrningschefen äger det, eftersom kopplingen uppstår i uthyrningen.
- **Sätt klassen på relationen.** Relationen mellan Lägenhetsanpassning och Hyresgäst, eller kedjan genom Hyresavtal, bär nivån. Det kräver något katalogen inte har: en klass på en relation, och en regel för hur en lagringsyta ärver den. Kartan visar då var kopplingen finns, men varje relation måste bedömas.
- **Låt kartan fråga efter kopplingen.** Ingen klass flyttas. Steg 4 får en följdfråga: vilka objekt på lagringsytan går att koppla till en person, direkt eller genom andra objekt på kartan? Svaret ger lagringsytans krav, som när NIST räknar uppgifter som kopplade om källorna finns i samma system utan åtskillnad. Fastighetssystemet rymmer både Lägenhetsanpassning och Hyresavtal. Därför måste det klara nivån för uppgifter om hälsa, fast inget av objekten är klassat så. En utskrift av Lägenhetsanpassning utan hyresavtal har bara sin egen nivå.
- **Värdemängden får aldrig klassen.** Ingen lästa källa sätter klassen på listan över möjliga värden. Listan över hälsotillstånd är öppen referensdata. Det känsliga är att ett värde ur listan står vid en lägenhet där en känd person bor.

## Det som inte gick att bekräfta

- **ISO/IEC 27001:2022, 27002:2022 (kontrollerna 5.9, 5.12 och 5.13) och 27005:2022.** Standarderna kostar pengar. iso.org visade bara en robotkontroll, och en ny hämtning med en annan klientidentitet stoppades av behörighetssystemet. Inget om dem i underlaget bygger på kontrolltexten.
- **ISO 22301:2019 avsnitt 8.2.2 och ISO/TS 22317:2021 avsnitt 5.5 och 5.6.** Bara SIS förhandsvisningar lästes, och de slutar före avsnitten om resurser. Om ISO räknar information som en egen resurs är inte bekräftat.
- **Australiens skyddsramverk, PSPF.** Webbplatsen stängde förbindelsen, och en arkiverad kopia stoppades av behörighetssystemet. Inget om PSPF ingår.
- **DAMA-DMBOK.** Boken är inte fritt tillgänglig och är inte läst.
- **USA:s original och derivative classification.** Inte läst i källan.
- **Avtal om delning av data, dataskyddsförordningens artiklar 26 och 28 och EU:s dataförordning.** Inte lästa. Om mottagaren av delad information gör en egen riskbedömning enligt dem är inte prövat.
- **Om BIO2 har avskaffat de tre basnivåerna.** Ordet saknas i BIO2 v1.3, men inget beslut om det har lästs.
- **NCSC:s slutliga vägledning till MCFFS 2026:11.** Bara utkastet finns.
- **EDPB:s ställningstagande till WP248.** Inte bekräftat.
- **NIST SP 800-34, om en ny revision är på gång.** Inte bekräftat.
- **SKR:s rapport om informationssäkerhet i fastighetsområdet och för sakernas internet**, med ett avsnitt om aggregerade mängder. Hämtningen misslyckades.
- **Nyare siffror från MSB eller MCF om hur många myndigheter som klassar.** Inga hittades efter 2014 års enkät.
- **Brittiska riksrevisionen (NAO) om övergången 2014.** Ingen rapport hittades.
- **Tre forskningsartiklar** (Bergström och Åhlfeldt 2014, Kaarst-Brown och Thompson 2015, Fibikova och Müller 2010). Förlagen stängde ute hämtningen. De nämns bara som de återges i VISKA och i avhandlingen från 2020.
- **ISO/IEC 29100 och 27701.** ISO:s sida med fria standarder är stängd, och iso.org visade bara en robotkontroll.
- **DoD Manual 5200.01 i gällande lydelse från 2025.** Webbplatserna nekade hämtning. Citaten är ur 2012 års text i ett webbarkiv. Uttrycket *classification by association* som en egen lära finns inte i de lästa texterna, bara "additional association or relationship" och "compilation or association".
- **Lunt 1989, Dawson med flera 1999 och Ciriani med flera 2010.** Bara sammanfattningarna lästes. Databasen anger 2003 som år för Lunts artikel, men DOI:n pekar på konferensen 1989.
- **EDPB:s riktlinjer 01/2025 om pseudonymisering i slutlig form.** Bara remissversionen från januari 2025 är bekräftad.
- **Vilken paragraf i OSL som skyddar adressen till en person med skyddad identitet.** Inte kontrollerad.

## Källor

### Svenska regler och stöd

- MSBFS 2020:6, Myndigheten för samhällsskydd och beredskaps föreskrifter om informationssäkerhet för statliga myndigheter. https://www.mcf.se/sv/regler/gallande-regler/msbfs-20206/
- NCSC, Regler och föreskrifter. https://www.ncsc.se/sv/regler-och-foreskrifter/
- MSBFS 2020:7, föreskrifter om säkerhetsåtgärder i informationssystem för statliga myndigheter. https://www.mcf.se/sv/regler/gallande-regler/msbfs-20207/
- MCFFS 2026:11, Myndigheten för civilt försvars föreskrifter och allmänna råd om säkerhetsåtgärder och ledningens utbildning för väsentliga och viktiga verksamhetsutövare. https://www.mcf.se/sv/regler/gallande-regler/mcffs-202611/
- NCSC, utkast till föreskriftsvägledning för MCFFS 2026:11. https://www.ncsc.se/siteassets/radgivning-och-stod/foreskrifter/utkast-foreskriftsvagledning-till-foreskrifterna-om-sakerhetsatgarder-och-ledningens-utbildning.pdf
- Cybersäkerhetslag (2025:1506) och cybersäkerhetsförordning (2025:1507). https://data.riksdagen.se/dokument/sfs-2025-1506.text
- Säkerhetsskyddslag (2018:585) och säkerhetsskyddsförordning (2021:955). https://data.riksdagen.se/dokument/sfs-2018-585.text, https://data.riksdagen.se/dokument/sfs-2021-955.text
- Säkerhetspolisen, Vägledning i säkerhetsskydd: Informationssäkerhet, oktober 2023. https://sakerhetspolisen.se/download/18.3752daf918b497112712b/1698133722307/Informationssa%CC%88kerhet_anpassad.pdf
- Offentlighets- och sekretesslag (2009:400). https://data.riksdagen.se/dokument/sfs-2009-400.text
- Metodstöd för systematiskt informationssäkerhetsarbete: Klassning av information, https://www.informationssakerhet.se/sv/anvanda/klassning-av-information/; Klassningsmodell, https://www.informationssakerhet.se/sv/utforma/klassningsmodell/; Kontinuitetshantering för informationstillgångar, https://www.informationssakerhet.se/sv/utforma/kontinuitetshantering-for-informationstillgangar/; Arbetsmaterial workshop, exempel, https://metodstod-informationssakerhet.msb.se/contentassets/0066c136b0ac4416ac1008d7eb29c1af/arbetsmaterial-workshop--exempel.pdf
- MSB, Lathund för kontinuitetshantering, MSB2372, 2024. https://rib.msb.se/filer/pdf/30703.pdf
- SKR, KLASSA: Vägledning för informationsklassning, https://klassa.skr.se/sidor/stodmaterial/Informationsklassning/vagledning-for-informationsklassning; KLASSA 5 vägledning, https://klassa.skr.se/sidor/stodmaterial/sida/getfile/a-klassa-5-vagledning/32; Begrepp, https://klassa.skr.se/sidor/stodmaterial/Begrepp

### EU

- Dataskyddsförordningen, (EU) 2016/679. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679
- NIS2-direktivet, (EU) 2022/2555. https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- Artikel 29-gruppen, WP248 rev. 01, riktlinjer om konsekvensbedömning, 2017. https://ec.europa.eu/newsroom/document.cfm?doc_id=47711
- Artikel 29-gruppen, WP136, yttrande 4/2007 om begreppet personuppgifter. https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2007/wp136_en.pdf
- Artikel 29-gruppen, WP216, yttrande 05/2014 om anonymiseringstekniker. https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2014/wp216_en.pdf
- EDPB, riktlinjer 01/2025 om pseudonymisering, remissversion. https://www.edpb.europa.eu/system/files/2025-01/edpb_guidelines_202501_pseudonymisation_en.pdf
- EU-domstolen, mål C-582/14, C-319/22, C-413/23 P och C-184/20. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62014CJ0582, https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62022CJ0319, https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62023CJ0413, https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62020CJ0184

### Klassning genom koppling

- Executive Order 13526, Classified National Security Information, 2009, avsnitt 1.7 e. https://www.archives.gov/isoo/policy-documents/cnsi-eo.html
- 32 CFR del 2001, Classified National Security Information. https://www.ecfr.gov/current/title-32/subtitle-B/chapter-XX/part-2001
- DoD Manual 5200.01 vol. 1 och 2, 2012, i webbarkivet vid University of North Texas. https://webarchive.library.unt.edu/web/20130218000000id_/http://www.dtic.mil/whs/directives/corres/pdf/520001_vol1.pdf
- NIST SP 800-122, Guide to Protecting the Confidentiality of Personally Identifiable Information, 2010. https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-122.pdf
- NIST IR 8053, De-Identification of Personal Information, 2015. https://nvlpubs.nist.gov/nistpubs/ir/2015/NIST.IR.8053.pdf
- NIST SP 800-188, De-Identifying Government Datasets, 2023. https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-188.pdf
- Teresa F. Lunt, Aggregation and inference: facts and fallacies, IEEE Symposium on Security and Privacy 1989, doi 10.1109/SECPRI.1989.36284. Bara sammanfattningen läst.
- Aggarwal med flera, Two Can Keep a Secret: A Distributed Architecture for Secure Database Services, CIDR 2005. https://www.cidrdb.org/cidr2005/papers/P16.pdf
- Ciriani med flera, Combining fragmentation and encryption to protect privacy in data storage, ACM TISSEC 2010. Bara sammanfattningen läst.

### Internationella metoder

- NIST FIPS 199, Standards for Security Categorization of Federal Information and Information Systems, 2004. https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.199.pdf
- NIST SP 800-60 vol. 1 rev. 1, 2008. https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-60v1r1.pdf
- NIST SP 800-60 rev. 2, initial working draft, 2024. https://csrc.nist.gov/pubs/sp/800/60/r2/iwd
- NIST IR 8496, Data Classification Concepts and Considerations, initial public draft, 2023, tillbakadraget 2025. https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8496.ipd.pdf
- NIST SP 800-34 rev. 1, Contingency Planning Guide, 2010. https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf
- NIST:s ordlista, information owner, information steward, data steward. https://csrc.nist.gov/glossary
- BSI-Standard 200-2, IT-Grundschutz-Methodik, 2017. https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_2.pdf
- BSI-Standard 200-4, Business Continuity Management, 2023. https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_4.pdf
- UK Cabinet Office, Government Security Classifications Policy, version 2.0, 2024. https://www.gov.uk/government/publications/government-security-classifications/government-security-classifications-policy-html
- UK Cabinet Office, Guidance 1.5: Considerations for security advisors. https://www.gov.uk/government/publications/government-security-classifications/guidance-15-considerations-for-security-advisors-html
- Baseline Informatiebeveiliging Overheid, BIO 1.04, 2020. https://www.bio-overheid.nl/media/hj2fau4b/20200617-bio-v1-0-4zv-def.pdf
- BIO2 v1.3, 2026. https://www.bio-overheid.nl/media/dr4inbhc/20260109-baseline-informatiebeveiliging-overheid-2-bio2-v13-def.pdf
- Handreiking en onderbouwing Generieke Baselinetoets BIO2 v3.2, 2026. https://www.bio-overheid.nl/media/x2ofw5hk/20261014-handreiking-en-onderbouwing-generieke-baselinetoets-bio2-v32-v10-def-dt.pdf
- Nederländska regeringen, Baseline Information Security for Government revised. https://www.nldigitalgovernment.nl/news/baseline-information-security-for-government-revised/
- ISO/TS 22317:2021 och ISO 22301:2019, förhandsvisning hos SIS. https://www.sis.se/api/document/preview/80032409/, https://www.sis.se/api/document/preview/80017864/

### Granskningar, forskning och alternativ

- Riksrevisionen, RiR 2023:20, Informationssäkerhet vid universitet och högskolor: hanteringen av skyddsvärda forskningsdata. https://data.riksdagen.se/fil/30DBCD72-59B8-465C-9660-0586329987D1
- Riksrevisionen, RiR 2014:23, Informationssäkerheten i den civila statsförvaltningen. https://data.riksdagen.se/dokument/H2B523.html
- MSB, VISKA: Verktygsstöd för anpassningsbar informationsklassning, 2024. https://rib.msb.se/filer/pdf/30947.pdf
- Erik Bergström, Supporting Information Security Management: Developing a Method for Information Classification, doktorsavhandling, 2020. https://his.diva-portal.org/smash/get/diva2:1458263/FULLTEXT01.pdf
- Andersson, Problems in information classification: insights from practice, Information & Computer Security 31(4), 2023, doi 10.1108/ICS-10-2022-0163. Bara sammanfattningen läst.
- Andersson, Beyond Levels: Supporting Information Classification, doktorsavhandling, Luleå tekniska universitet, 2026. Bara sammanfattningen läst, ur DiVA, post diva2:2047026.
- UK Cabinet Office, Radical overhaul for Whitehall security, pressmeddelande 2013. https://www.gov.uk/government/news/radical-overhaul-for-whitehall-security
- Public Interest Declassification Board, Transforming the Security Classification System, 2012. https://www.archives.gov/files/declassification/pidb/recommendations/transforming-classification.pdf
- Reducing Over-Classification Act, Public Law 111-258, 2010. https://www.govinfo.gov/content/pkg/PLAW-111publ258/html/PLAW-111publ258.htm
- US GAO, GAO-06-385, 2006. https://www.govinfo.gov/content/pkg/GAOREPORTS-GAO-06-385/html/GAOREPORTS-GAO-06-385.htm
- NIST SP 800-53B, Control Baselines, 2020. https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53B.pdf
- NIST SP 800-162, Guide to Attribute Based Access Control, 2014. https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-162.pdf
- NIST SP 800-207, Zero Trust Architecture, 2020. https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf
- CISA, Zero Trust Maturity Model 2.0, 2023. https://www.cisa.gov/sites/default/files/2023-04/zero_trust_maturity_model_v2_508.pdf
