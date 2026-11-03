---
id: C-206
term: Processägare
terms:
  - term: Processägare
    language: sv
    status: preferred
    source: concept new
definition: 'roll som ytterst ansvarar för ett verksamhetsbeteende: hur det är ordnat och att det följer de regler och beslut som gäller för det'
kind: element-type
generic: '[[C-074 Roll]]'
associative:
  - concept: '[[C-157 Verksamhetsbeteende]]'
    label: ansvarar för
---
# C-206 Processägare

**Definition:** roll som ytterst ansvarar för ett verksamhetsbeteende: hur det är ordnat och att det följer de regler och beslut som gäller för det

## Anmärkning

Typ i verksamhetsperspektivet, en typ av roll ([[C-074 Roll]]), och det andra ledet i ett upplägg för informationshantering: informationsägaren ([[C-167 Informationsägare]]) äger informationsobjektet som typ, dess struktur, klass och vad som får göras med det; processägaren äger verksamhetsbeteendet ([[C-157 Verksamhetsbeteende]]) som typ, hur det är ordnat, dess regler och kontroller, och att det klarar klassens krav; förekomsterna, de faktiska ärendena och uppgifterna, svarar linjechefen ([[C-207 Linjechef]]) för, chefen för den organisationsenhet som tilldelas beteendet. Riktigheten är därmed tre saker: kravet är informationsägarens, kontrollen i beteendet processägarens och att förekomsten stämmer linjens. Ordet säger process, men rollen äger alla tre slagen av beteende, handläggning ([[C-160 Handläggning]]) och verksamhetsfunktion ([[C-158 Verksamhetsfunktion]]) lika väl: katalogen svarar när ordet används. Ägarskapet skrivs med ansvarar för ([[C-208 ansvarar för]]) från rollen till beteendet; att en roll eller en enhet tilldelas ([[C-096 tilldelas]]) beteendet säger vem som utför, inte vem som äger. Ett beteende utan egen processägare har det omslutande beteendets, längs består av ([[C-062 består av]]), en härledning som läses ur lagret och aldrig kopieras; en verksamhetsaktivitet ([[C-175 Verksamhetsaktivitet]]) har aldrig egen ägare.

Behandlingarna ([[C-168 Behandling]]) i beteendet ska hålla sig inom informationsägarens beslut; att de gör det prövar processägaren, och rutinen som säger hur är en bärare ([[C-016 Bärare]]) som fastställs av ([[C-183 fastställs av]]) processägaren med det mandat ([[C-189 Mandat]]) som följer av positionen. Processägaren är utgångsläget för vem som äger informationen: ett informationsobjekts ägare är, om inget annat beslutats, processägaren för objektets hem, det beteende där förekomsterna skapas (ADR 0030), och den som upprättar en sammanställning ([[C-162 Sammanställning]]) äger den. Processägaren äger beteendet, inte lösningen ([[C-055 Lösning]]): den som äger allt som behövs för att leverera, aktörer, processer, information och teknik, är lösningsägaren, den som har mandatet över lösningen som styrobjekt. En intern produkt beteendet behöver, en leveransprodukt ([[C-174 Leveransprodukt]]) ur en annan lösning, har sin egen processägare; den yttre ställer krav ([[C-021 Krav]]) på det den tar emot, och ansvaret byter hand vid leveransen. Ofta är linjechefen också processägare och informationsägare, och delningen syns först när rollerna skiljs åt. Skrivs ut som ArchiMates Business Role, som informationsägaren. Beslutet: ADR 0035.

## Exempel

teknisk chef för processen Felanmälan hos bostadsbolaget; chefen för Bidragsenheten för handläggningen av ansökan hos Myndigheten för föreningsstöd; chefen för analysenheten för analysfunktionen.
