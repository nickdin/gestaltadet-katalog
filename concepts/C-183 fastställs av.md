---
id: C-183
term: fastställs av
terms:
  - term: fastställs av
    language: sv
    status: preferred
    source: concept new
  - term: beslutas av
    language: sv
    source: concept change
definition: relationstyp som anger att ett styrmedel eller en bärare har beslutats eller antagits av ett annat arkitekturelement
kind: relation-type
key: decided_by
---
# C-183 fastställs av

**Definition:** relationstyp som anger att ett styrmedel eller en bärare har beslutats eller antagits av ett annat arkitekturelement

## Anmärkning

Relationen går från det fastställda till den som beslutat eller antagit det. Det fastställda är bäraren ([[C-016 Bärare]]) eller ett styrmedel ([[C-015 Styrmedel]]) utan bärare; den som beslutat är en aktör ([[C-073 Aktör]]) eller en roll ([[C-074 Roll]]). Ett forum ([[C-156 Forum]]) fastställer inget: det bereder, och en roll eller en aktör beslutar ([[0050-ett-beslut-fattas-av-den-som-har-bade-ram-och-mandat-ett-forum-beslutar-aldrig-aspekten-avgor-inga-enskilda-fall-och-domanens-agare-satter-losningens-ram|beslut 50]]). Relationen säger vem som beslutat, inte vem som får besluta: det är mandatet ([[C-189 Mandat]], [[0025-paverkan-och-bedomning-ar-elementtyper-strategin-ar-sammanhangande-styrbeslut-visionen-ar-ett-mal-utan-matt-och-bmm-tas-in-med-andamalet-som-katalogens-tillagg|beslut 25]]). Fastställa är förvaltningens ord för att anta ett styrdokument; beslutas av är tillåten term. [[0023-regeln-anger-vad-som-ska-galla-kravet-ar-en-sorts-regel-katalogen-ar-organisationens-ordlista-och-sbvr-tas-in-med-faststalls-av-som-relationstyp|Beslut 23]].

**Källa:** SBVR 1.5, authority has business jurisdiction over element of guidance.

## Motsvarigheter

ArchiMate och ARIS saknar motsvarighet. [[0023-regeln-anger-vad-som-ska-galla-kravet-ar-en-sorts-regel-katalogen-ar-organisationens-ordlista-och-sbvr-tas-in-med-faststalls-av-som-relationstyp|Beslut 23]].

Fastställa täcker SBVR:s båda fall, att skapa och att anta. [[0023-regeln-anger-vad-som-ska-galla-kravet-ar-en-sorts-regel-katalogen-ar-organisationens-ordlista-och-sbvr-tas-in-med-faststalls-av-som-relationstyp|Beslut 23]].
