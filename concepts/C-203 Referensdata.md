---
id: C-203
term: Referensdata
terms:
  - term: Referensdata
    language: sv
    status: preferred
    source: concept new
definition: informationsobjekt vars förekomster är fastställda standardvärden som andra objekts uppgifter hänvisar till
generic: '[[C-060 Informationsobjekt]]'
associative:
  - concept: '[[C-197 Värdemängd]]'
    label: är en fastställd
---
# C-203 Referensdata

**Definition:** informationsobjekt vars förekomster är fastställda standardvärden som andra objekts uppgifter hänvisar till

## Anmärkning

Referensdata är en värdemängd ([[C-197 Värdemängd]]) som organisationen själv fastställer, äger eller ger egna uppgifter. Golvet i informationsobjektet ger gränsen: det som klassas, ägs eller regleras för sig är ett eget objekt. En värdemängd som bara räknas upp vid en uppgift ([[C-161 Uppgift]]), som kommunkoderna, förblir text vid uppgiften och är inget objekt.

Ett begrepp, ingen elementtyp: en datakategori ([[C-201 Datakategori]]) för ett informationsobjekt ([[C-060 Informationsobjekt]]). Informationsarkitektens bidrag är fastställda standardförekomster och bred användning: ett kodverk med alla tillåtna värden, som andra objekts uppgifter hänvisar till. Beslutet: ADR 0032.

## Exempel

Stödform hos Myndigheten för föreningsstöd, med namn, villkor och giltighetstid; Lägenhetstyp hos Brinkstadsbostäder.
