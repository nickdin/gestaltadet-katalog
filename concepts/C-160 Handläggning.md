---
id: C-160
term: Handläggning
terms:
  - term: Handläggning
    language: sv
    status: preferred
    source: concept new
definition: verksamhetsbeteende kring ett enskilt ärende, med start och slut, vars steg väljs efter hand
kind: element-type
generic: '[[C-157 Verksamhetsbeteende]]'
---
# C-160 Handläggning

**Definition:** verksamhetsbeteende kring ett enskilt ärende, med start och slut, vars steg väljs efter hand

## Anmärkning

Det CMMN (Case Management Model and Notation) kallar ett case. Ett verksamhetsbeteende ([[C-157 Verksamhetsbeteende]]) bredvid verksamhetsprocessen ([[C-130 Verksamhetsprocess]]) och verksamhetsfunktionen ([[C-158 Verksamhetsfunktion]]): processen lägger fast sina steg i förväg, handläggningen väljer dem efter hand, efter det enskilda ärendets omständigheter, och slutar i ett utfall, i förvaltningslagens mening oftast ett ärendebeslut ([[C-181 Ärendebeslut]]). Det enskilda ärendet är ett verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]) som handläggningen har åtkomst till; ordet ärende står för objektet, aldrig för beteendet. Stegen en handläggning väljer bland är verksamhetsaktiviteter ([[C-175 Verksamhetsaktivitet]]), CMMN:s Task, och processer och funktioner den rymmer eller utlöser. Handläggningen rymmer ([[C-100 aggregerar]]) alla sina aktiviteter: den som nås av en utlöser-relation ([[C-098 utlöser]]) från en händelse eller ett annat steg är planerad, och relationen med sitt villkor är CMMN:s ingångskriterium; den som ingen relation pekar på är valbar, handläggarens val ur CMMN:s planeringstabell. När handläggningen eller en del av den är klar utlöser den en verksamhetshändelse ([[C-135 Verksamhetshändelse]]), CMMN:s milstolpe och utgångskriterium; det tillstånd ([[C-182 Tillstånd]]) ärendet då är i läses ur händelsens namn. CMMN:s etapp (Stage) är inget eget begrepp utan ett sätt att nästla: en etapp med fast stegföljd är en verksamhetsprocess handläggningen rymmer, en etapp vars steg väljs efter hand är en handläggning i handläggningen, och en etapp utan den tyngden är en rubrik i beskrivningen. BPMN:s ad hoc-delprocess, steg utan fast ordning inuti en process, är på samma sätt en handläggning inuti processen. Namnges som processer och funktioner, med ett verb i infinitiv följt av objektet; typen bär skillnaden, inte namnet. Realiserar en verksamhetsförmåga ([[C-069 Verksamhetsförmåga]]) som en process gör. ArchiMate har inget case-element: en export skriver en handläggning som Business Process, med skillnaden förlorad på vägen ut. Beslutet: ADR 0017; stegen, etappen och milstolpen ADR 0022.
