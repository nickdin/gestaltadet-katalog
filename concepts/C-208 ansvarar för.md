---
id: C-208
term: ansvarar för
terms:
  - term: ansvarar för
    language: sv
    status: preferred
    source: concept new
definition: relationstyp som anger att en roll äger ett annat arkitekturelement och svarar för det
kind: relation-type
key: responsible_for
---
# C-208 ansvarar för

**Definition:** relationstyp som anger att en roll äger ett annat arkitekturelement och svarar för det

## Anmärkning

Relationen går från rollen till det den äger: informationsägaren ([[C-167 Informationsägare]]) till informationsobjektet ([[C-060 Informationsobjekt]]), processägaren ([[C-206 Processägare]]) till verksamhetsbeteendet ([[C-157 Verksamhetsbeteende]]). Den svarar på frågan vem som äger, och skiljer ägandet från utförandet: tilldelas ([[C-096 tilldelas]]) säger vem som utför. Härledningen nedåt ([[0030-informationsomradet-ar-ett-begrepp-utan-elementtyp-ett-informationsobjekt-som-bestar-av-sina-objekt-varje-objekt-har-ett-hem-och-nivan-far-vara-grov|beslut 30]]) och förteckningarna med ägare per behandling ([[0031-handlingen-ar-representationen-allman-handling-och-gallring-ar-begrepp-forteckningarna-bor-utanfor-lagret-och-lagringsytan-far-vara-fysisk|beslut 31]]) behöver det svaret.

Relationen säger vem som äger och svarar, inte vem ägaren svarar inför. Processägaren svarar inför ägaren till lösningen ([[C-055 Lösning]]) där beteendet ligger, och informationsägaren inför ägaren till lösningen där objektet skapas. [[0057-en-agarroll-svarar-infor-en-losnings-agare-ordet-ytterst-stryks-ur-tre-definitioner-och-klassen-ar-densamma-i-varje-beteende|Beslut 57]].

Relationen är bara för ägarrollerna. Ett styrmedel eller en bärare ägs av den som fastställt det ([[C-183 fastställs av]]), och ett styrobjekt av den som har mandatet ([[C-189 Mandat]]) över det.

## Motsvarigheter

ArchiMates Assignment får inte gå från en roll till ett passivt objekt, så ArchiMate saknar motsvarighet och exporten får Association. [[0035-processagaren-ar-en-roll-linjechefen-ett-begrepp-agandet-skrivs-med-ansvarar-for-typerna-ags-och-forekomsterna-svarar-linjen-for-och-styrobjekten-ags-genom-mandat|Beslut 35]].
