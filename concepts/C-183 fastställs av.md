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

Relationen går från det fastställda till den som beslutat eller antagit det. Det fastställda är bäraren ([[C-016 Bärare]]) eller ett styrmedel ([[C-015 Styrmedel]]) utan bärare; den som beslutat är en aktör ([[C-073 Aktör]]), en roll ([[C-074 Roll]]) eller ett forum ([[C-156 Forum]]). Relationen säger vem som beslutat, inte vem som får besluta: det är mandatet ([[C-189 Mandat]], ADR 0025). Fastställa är förvaltningens ord för att anta ett styrdokument och täcker SBVR:s båda fall, att skapa och att anta; beslutas av är tillåten term. ArchiMate och ARIS saknar motsvarighet. Beslutet: ADR 0023.

**Källa:** SBVR 1.5, authority has business jurisdiction over element of guidance.
