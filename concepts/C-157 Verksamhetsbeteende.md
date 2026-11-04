---
id: C-157
term: Verksamhetsbeteende
terms:
  - term: Verksamhetsbeteende
    language: sv
    status: preferred
    source: concept new
definition: det aktörer i verksamheten gör, ordnat som process, handläggning eller funktion
---
# C-157 Verksamhetsbeteende

**Definition:** det aktörer i verksamheten gör, ordnat som process, handläggning eller funktion

## Anmärkning

Verksamhetsbeteende är familjebegreppet för verksamhetsperspektivets beteenden: verksamhetsprocess ([[C-130 Verksamhetsprocess]]), verksamhetsfunktion ([[C-158 Verksamhetsfunktion]]) och handläggning ([[C-160 Handläggning]], ADR 0017). De tre är syskon av samma rang, skilda åt av hur arbetet är ordnat. Processen har start, slut och fast stegföljd. Handläggningen har start och slut, men stegen väljs efter hand. Funktionen har varken start eller slut. Alla tre kan realisera en verksamhetsförmåga ([[C-069 Verksamhetsförmåga]]), har åtkomst till verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]), kan utlösa varandra och rymma varandra. Stegen i alla tre är verksamhetsaktiviteter ([[C-175 Verksamhetsaktivitet]]), som beteendet rymmer. Beslutet: ADR 0015; aktiviteterna ADR 0022. En processägare ([[C-206 Processägare]]) äger beteendet, skrivet med ansvarar för ([[C-208 ansvarar för]]); ett beteende utan egen har det omslutande beteendets (ADR 0035).

Beteendet når informationen på två sätt. Processvyn ritar åtkomsten till verksamhetsobjektet, och genom det har beteendet åtkomst till de informationsobjekt ([[C-060 Informationsobjekt]]) som realiserar det ([[C-094 realiseras av]]). Den åtkomsten härleds och ritas inte. Direkt till ett informationsobjekt ritas bara det som inte följer av verksamhetsobjektet: ett uppslag i ett register, ett utlämnande, en sammanställning beteendet gör. Åtkomsten följer inte aggregerar ([[C-100 aggregerar]]). Behandlingen ([[C-168 Behandling]]) läses ur beteendets åtkomst till informationsobjektet, ritad eller härledd. ADR 0034.

Motsvarar CapabilityBehavior i Business Architecture Core Metamodel (BACM), beteendebeskrivningen som levererar en förmåga, en av flera varianter som ger samma utfall. De regler och policyer BACM låter samma klass bära är i lagret styrmedel ([[C-015 Styrmedel]]). ADR 0027.

Motsvarar CapabilityMethod i Value Delivery Modeling Language (VDML), ett återanvändbart aktivitetsnätverk som levererar en förmåga, likt en processdefinition men lika gärna en ärendetyp. Ett beteende följer ett arbetssätt ([[C-196 Arbetssätt]]), som står i dess text. ADR 0028.
