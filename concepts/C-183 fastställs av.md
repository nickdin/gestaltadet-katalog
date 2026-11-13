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

Relationen går från det fastställda till den som beslutat eller antagit det. Det fastställda är bäraren ([[C-016 Bärare]]) eller ett styrmedel ([[C-015 Styrmedel]]) utan bärare; den som beslutat är en aktör ([[C-073 Aktör]]) eller en roll ([[C-074 Roll]]). Ett forum ([[C-156 Forum]]) fastställer inget: det bereder, och en roll eller en aktör beslutar (beslut 50). Relationen säger vem som beslutat, inte vem som får besluta: det är mandatet ([[C-189 Mandat]], beslut 25). Fastställa är förvaltningens ord för att anta ett styrdokument; beslutas av är tillåten term. Beslut 23.

**Källa:** SBVR 1.5, authority has business jurisdiction over element of guidance.

## Motsvarigheter

ArchiMate och ARIS saknar motsvarighet. Beslut 23.

Fastställa täcker SBVR:s båda fall, att skapa och att anta. Beslut 23.
