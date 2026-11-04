---
id: C-209
term: Ansvar
terms:
  - term: Ansvar
    language: sv
    status: preferred
    source: concept new
definition: skyldighet för en roll att svara för ett styrobjekts utfall eller för ett arkitekturelement, och att stå till svars för det
associative:
  - concept: '[[C-074 Roll]]'
    label: bärs av
  - concept: '[[C-003 Styrobjekt]]'
    label: avser
  - concept: '[[C-189 Mandat]]'
    label: förutsätter
  - concept: '[[C-185 Bedömning]]'
    label: prövas genom
---
# C-209 Ansvar

**Definition:** skyldighet för en roll att svara för ett styrobjekts utfall eller för ett arkitekturelement, och att stå till svars för det

## Anmärkning

Ansvar och mandat ([[C-189 Mandat]]) är två ord för samma plats. Mandatet är rätten att besluta om något. Ansvaret är att svara för hur det går. För varje sak som ägs beslutar den som svarar för den. Det är regeln som gör ägande prövbart: hitta något som någon svarar för utan att få besluta om, så är det ett fynd.

Ett begrepp, ingen egen typ. Ansvaret för ett styrobjekt följer mandatet över det och skrivs inte med någon relation. Ansvaret för ett arkitekturelement skrivs med ansvarar för ([[C-208 ansvarar för]]): informationsägarens för informationsobjektet, processägarens för verksamhetsbeteendet. Arkitekturansvaret ([[C-117 Arkitekturansvar]]) är ett ansvar för vyerna.

Ansvaret kan inte bäras utan medel, för ingen kan svara för ett utfall den inte kan flytta. Befogenheten kan däremot hållas utan medel: den är en regel i arbetsordningen. Fyra saker måste finnas:

- befogenheten, en regel ([[C-020 Regel]]);
- ramen ([[C-210 Ram]]) över styrobjektet;
- ett styrobjekt skuret så att besluten når det utfallet beror på, provet för ett snitt i Lösning ([[C-055 Lösning]]);
- att utfallet prövas mot målet ([[C-017 Mål]]) genom en bedömning ([[C-185 Bedömning]]) som leder till styrbeslut ([[C-019 Styrbeslut]]).

Saknas något av dem har rollen befogenheten men kan inte bära ansvaret. Det är vad som händer i pm3:s objektstyrning ([[C-048 Objektstyrning]]): objektägaren från verksamheten svarar för lösningen, IT håller ramen och forumet beslutar. ADR 0036.

## Exempel

Lösningsägaren för Felanmälan svarar för att en felanmälan är åtgärdad inom fem arbetsdagar och beslutar om processen, informationen och fastighetssystemets modul tillsammans. Generaldirektören svarar för myndighetens uppdrag inför regeringen.
