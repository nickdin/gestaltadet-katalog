---
id: C-135
term: Verksamhetshändelse
terms:
  - term: Verksamhetshändelse
    language: sv
    source: catalogue
definition: "händelse som inträffar i verksamheten eller dess omvärld"
kind: element-type
generic: "[[C-078 Händelse]]"
---
# C-135 Verksamhetshändelse

**Definition:** händelse som inträffar i verksamheten eller dess omvärld

## Anmärkning

Att en handling kommer in till myndigheten eller upprättas där är en verksamhetshändelse. Den gör representationen ([[C-085 Representation]]) till en allmän handling ([[C-199 Allmän handling]]) och utlöser ([[C-098 utlöser]]) registreringen: en verksamhetsaktivitet ([[C-175 Verksamhetsaktivitet]]) med åtkomst till representationen, som skriver diarieposten i diariet, en lagringsyta ([[C-165 Lagringsyta]]). Hos Myndigheten för föreningsstöd kommer en ansökan om bidrag in som e-post och registreras i diariet samma dag (beslut 31).

Motsvarar ArchiMates Business Event. BPMN:s start-, mellan- och sluthändelser och CMMN:s EventListener är verksamhetshändelser, med sorten (meddelande, tid, fel, signal) i beskrivningen. CMMN:s milstolpe (Milestone), ett nåbart mål utan eget arbete, är den verksamhetshändelse som en handläggning ([[C-160 Handläggning]]) eller en del av den utlöser när den är klar. Händelsen utlöser ([[C-098 utlöser]]) det tillstånd ([[C-182 Tillstånd]]) ärendet då nått, och i en tillståndsvy ritas den så. Beslut 22; tillståndet som elementtyp beslut 24.

Motsvarar händelsen (SignalEvent, TimeEvent, ChangeEvent, CallEvent) i Unified Modeling Language (UML) när den utlöser en övergång i ett verksamhetsobjekts tillståndsmaskin, och det som startar, avbryter eller avslutar en aktivitet. Slaget av händelse är text i beskrivningen, som BPMN:s händelsedefinitioner. Beslut 29.
