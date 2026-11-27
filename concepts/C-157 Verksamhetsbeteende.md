---
id: C-157
term: Verksamhetsbeteende
terms:
  - term: Verksamhetsbeteende
    language: sv
    status: preferred
    source: concept new
definition: det aktörer i verksamheten gör, ordnat som process, handläggning eller funktion
associative:
  - concept: '[[C-159 Verksamhetsobjekt]]'
    label: har åtkomst till
---
# C-157 Verksamhetsbeteende

**Definition:** det aktörer i verksamheten gör, ordnat som process, handläggning eller funktion

## Anmärkning

Verksamhetsbeteende är familjebegreppet för verksamhetsperspektivets beteenden: verksamhetsprocess ([[C-130 Verksamhetsprocess]]), verksamhetsfunktion ([[C-158 Verksamhetsfunktion]]) och handläggning ([[C-160 Handläggning]], [[0017-handlaggning-ar-en-elementtyp-under-verksamhetsbeteende|beslut 17]]). De tre är syskon av samma rang, skilda åt av hur arbetet är ordnat. Processen har start, slut och fast stegföljd. Handläggningen har start och slut, men stegen väljs efter hand. Funktionen har varken start eller slut. Alla tre kan realisera en verksamhetsförmåga ([[C-069 Verksamhetsförmåga]]), har åtkomst till verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]), kan utlösa varandra och rymma varandra. Stegen i alla tre är verksamhetsaktiviteter ([[C-175 Verksamhetsaktivitet]]), som beteendet rymmer. [[0015-process-arende-och-funktion-ar-tre-verksamhetsbeteenden-av-samma-rang|Beslut 15]]; aktiviteterna [[0022-aktivitet-och-beslutslogik-ar-elementtyper-bpmn-cmmn-och-dmn-tas-in-som-bestandsdelar-i-beteendet-med-egna-mappningstabeller|beslut 22]]. En processägare ([[C-206 Processägare]]) äger beteendet, skrivet med ansvarar för ([[C-208 ansvarar för]]); ett beteende utan egen har det omslutande beteendets ([[0035-processagaren-ar-en-roll-linjechefen-ett-begrepp-agandet-skrivs-med-ansvarar-for-typerna-ags-och-forekomsterna-svarar-linjen-for-och-styrobjekten-ags-genom-mandat|beslut 35]]).

Beteendet når informationen på två sätt. Processvyn ritar åtkomsten till verksamhetsobjektet, och genom det har beteendet åtkomst till de informationsobjekt ([[C-060 Informationsobjekt]]) som realiserar det ([[C-094 realiseras av]]). Den åtkomsten härleds och ritas inte. Direkt till ett informationsobjekt ritas bara det som inte följer av verksamhetsobjektet: ett uppslag i ett register, ett utlämnande, en sammanställning beteendet gör. Åtkomsten följer inte aggregerar ([[C-100 aggregerar]]). Behandlingen ([[C-168 Behandling]]) läses ur beteendets åtkomst till informationsobjektet, ritad eller härledd. [[0034-beteendet-nar-informationsobjektet-genom-verksamhetsobjektet-och-direkt-atkomsten-foljer-realiseras-av-men-inte-aggregerar|Beslut 34]].

Processägaren ställer ett kontinuitetskrav på beteendet: den längsta tid beteendet får stå still. Kravet är ett krav ([[C-021 Krav]]) på hela beteendet, och det gäller vilken resurs som än faller bort: personal, lokaler, applikationer eller information. Tiden står i dokumentationen av kontinuiteten, utanför lagret. Tål delar av beteendet olika långa stopp gäller värsta fallet. Anta att en vattenläcka hos bostadsbolaget får vänta högst fyra timmar och en droppande kran fem arbetsdagar. Båda är Åtgärda en felanmälan, och processen får fyra timmar. Nuläget delar beteendet först när verksamheten utför delen för sig. Har bolaget en jour som egen process med egen ordning, står jouren som ett eget beteende med sin egen tid. [[0061-kontinuitet-ar-ett-krav-pa-hela-beteendet-tillgangligheten-far-tva-matt-och-aterstallningstiden-harleds-till-resursen|Beslut 61]] och [[0064-informationshanteringen-har-tre-perspektiv-informationsforsorjningen-ar-arkitekturarbete-och-varje-forteckning-halls-av-ett-perspektiv|64]].

Arkivredovisningens klassificeringsstruktur är beteendena lästa ur lagret, ingen egen sak. Det Riksarkivets föreskrifter om arkivredovisning kallar process är allt arbete som avsätter handlingar. I lagret är det ett verksamhetsbeteende, ordnat som process, handläggning eller funktion. Handlingarna som beteendet avsätter är dess handlingsslag ([[C-200 Gallring]]). Genomföra ansökningsomgången hos Myndigheten för föreningsstöd avsätter ansökningsärenden. HR:s löpande arbete med att försörja myndigheten med personal är en funktion, och den avsätter anställningsbeslut. När ett beteende rymmer ett annat väljer myndigheten i sin klassificeringsstruktur vilket av dem som bär handlingsslaget. En handling redovisas under ett beteende, inte under två. [[0031-handlingen-ar-representationen-allman-handling-och-gallring-ar-begrepp-forteckningarna-bor-utanfor-lagret-och-lagringsytan-far-vara-fysisk|Beslut 31]] och [[0067-arkivet-har-tva-enheter-handlingsslaget-lases-ur-verksamhetsbeteendet-och-handlingstypen-ar-representationen-redovisad-under-aktiviteten-dar-handlingen-kommer-in-eller-upprattas|67]].

## Motsvarigheter

Motsvarar CapabilityBehavior i Business Architecture Core Metamodel (BACM), beteendebeskrivningen som levererar en förmåga, en av flera varianter som ger samma utfall. De regler och policyer BACM låter samma klass bära är i lagret styrmedel ([[C-015 Styrmedel]]). [[0027-vardestrom-ar-en-elementtyp-i-strategiperspektivet-utfallet-ar-tillstandet-losningen-ar-formagans-implementation-och-bacm-tas-in-med-hinder-vinst-och-svar-som-begrepp-i-texten|Beslut 27]].

Motsvarar CapabilityMethod i Value Delivery Modeling Language (VDML), ett återanvändbart aktivitetsnätverk som levererar en förmåga, likt en processdefinition men lika gärna en ärendetyp. Ett beteende följer ett arbetssätt ([[C-196 Arbetssätt]]), som står i dess text. [[0028-varde-ar-en-elementtyp-i-strategiperspektivet-dit-vardeerbjudandet-flyttar-arbetssatt-ar-ett-begrepp-svaret-heter-hjalp-och-vdml-tas-in-med-rakneverket-omappat|Beslut 28]].
