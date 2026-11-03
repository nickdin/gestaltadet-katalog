---
id: C-201
term: Datakategori
terms:
  - term: Datakategori
    language: sv
    status: preferred
    source: concept new
  - term: datatyp
    language: sv
    source: concept change
    status: deprecated
definition: indelning av informationsobjekt efter hur verksamheten håller och fångar deras förekomster
associative:
  - concept: '[[C-060 Informationsobjekt]]'
    label: indelar
---
# C-201 Datakategori

**Definition:** indelning av informationsobjekt efter hur verksamheten håller och fångar deras förekomster

## Anmärkning

Ett begrepp, ingen elementtyp. Informationsmodelleringens praxis delar informationen i fyra kategorier: resursdata ([[C-202 Resursdata]]), referensdata ([[C-203 Referensdata]]), transaktionsdata ([[C-204 Transaktionsdata]]) och händelsedata ([[C-205 Händelsedata]]), och informationsarkitektens bidrag skiljer sig per kategori: en central källa för resursdata, fastställda standardförekomster för referensdata, standarddefinitioner och datafångst för transaktioner, och för händelser dessutom ett sammanhang som gör dem begripliga för den som ska analysera. Kategorin sätts på informationsobjektet ([[C-060 Informationsobjekt]]), inte på verksamhetsobjektet ([[C-159 Verksamhetsobjekt]]): den säger hur informationen försörjs och hålls, inte vad beteendet hanterar, och ett verksamhetsobjekt realiseras av flera informationsobjekt som kan vara av olika kategori. Ett informationsobjekt har högst en kategori, och kategorin är frivillig: ett informationsområde ([[C-198 Informationsområde]]) har ingen utan läses av sina objekt, och en sammanställning ([[C-162 Sammanställning]]) har ingen, eftersom de fyra beskriver det verksamheten håller och fångar, inte det den sätter samman. Kategorin finns för att en informationsmodell ska kunna färgas efter den och informationsägaren ([[C-167 Informationsägare]]) lista sina resursdata; tills interlingua bär den som ett fält på elementet står den som en mening i objektets beskrivning. Datatyp avråds som term, eftersom typ i katalogen betyder elementtyp. Varken ArchiMate, UML eller SDMN har kategorin, så den har inga mappningsrader. Beslutet: ADR 0032.

## Exempel

Förening är resursdata, Stödform referensdata och Ansökan transaktionsdata hos Myndigheten för föreningsstöd; Mätvärde är händelsedata hos Brinkstadsbostäder.
