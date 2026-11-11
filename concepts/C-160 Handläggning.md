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

Handläggningen är ett verksamhetsbeteende ([[C-157 Verksamhetsbeteende]]) bredvid verksamhetsprocessen ([[C-130 Verksamhetsprocess]]) och verksamhetsfunktionen ([[C-158 Verksamhetsfunktion]]). Processen lägger fast sina steg i förväg. Handläggningen väljer dem efter hand, efter det enskilda ärendets omständigheter, och slutar i ett utfall, i förvaltningslagens mening oftast ett ärendebeslut ([[C-181 Ärendebeslut]]). Det enskilda ärendet är ett verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]) som handläggningen har åtkomst till; ordet ärende står för objektet, aldrig för beteendet. Det är det CMMN (Case Management Model and Notation) kallar ett case. Handläggningen realiserar en verksamhetsförmåga ([[C-069 Verksamhetsförmåga]]) som en process gör. Den namnges som processer och funktioner, med ett verb i infinitiv följt av objektet; typen bär skillnaden, inte namnet.

Stegen en handläggning väljer bland är verksamhetsaktiviteter ([[C-175 Verksamhetsaktivitet]]), CMMN:s Task, och processer och funktioner den rymmer eller utlöser. Handläggningen rymmer ([[C-100 aggregerar]]) alla sina aktiviteter. Den aktivitet som nås av en utlöser-relation ([[C-098 utlöser]]) från en händelse eller ett annat steg är planerad, och relationen med sitt villkor är CMMN:s ingångskriterium. Den som ingen relation pekar på är valbar, handläggarens val ur CMMN:s planeringstabell. När handläggningen eller en del av den är klar utlöser den en verksamhetshändelse ([[C-135 Verksamhetshändelse]]), CMMN:s milstolpe och utgångskriterium. Det tillstånd ([[C-182 Tillstånd]]) ärendet då är i läses ur händelsens namn.

CMMN:s etapp (Stage) är inget eget begrepp utan ett sätt att nästla. En etapp med fast stegföljd är en verksamhetsprocess handläggningen rymmer. En etapp vars steg väljs efter hand är en handläggning i handläggningen. En etapp utan den tyngden är en rubrik i beskrivningen. BPMN:s ad hoc-delprocess, steg utan fast ordning inuti en process, är på samma sätt en handläggning inuti processen. ArchiMate har inget case-element: en export skriver en handläggning som Business Process, med skillnaden förlorad på vägen ut. Beslut 17; stegen, etappen och milstolpen beslut 22.
