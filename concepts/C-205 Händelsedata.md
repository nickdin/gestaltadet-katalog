---
id: C-205
term: Händelsedata
terms:
  - term: Händelsedata
    language: sv
    status: preferred
    source: concept new
definition: informationsobjekt om något som inträffat vid en tidpunkt och som inte ändras efteråt
generic: '[[C-060 Informationsobjekt]]'
---
# C-205 Händelsedata

**Definition:** informationsobjekt om något som inträffat vid en tidpunkt och som inte ändras efteråt

## Anmärkning

Händelsedata registreras när något inträffar och ändras inte efteråt: ingen handlägger ett mätvärde, det tolkas. Skillnaden mot transaktionsdata ([[C-204 Transaktionsdata]]) är livscykeln: transaktionen förs genom tillstånd, händelsen har inträffat.

Ett begrepp, ingen elementtyp: en datakategori ([[C-201 Datakategori]]) för ett informationsobjekt ([[C-060 Informationsobjekt]]). Informationsarkitektens bidrag är detsamma som för transaktioner, standarddefinitioner och datafångst, och därtill ett sammanhang: vilken resurs händelsen gäller, när och i vilken enhet, så att den som ska analysera och besluta förstår den.

DAMA:s indelning har tre kategorier, master-, referens- och transaktionsdata. Händelsedata är en fjärde, eftersom katalogens exempel har ett objekt som inte är en transaktion. Beslut 32.

## Exempel

Mätvärde hos Brinkstadsbostäder, en avläsning av mätaren i en lägenhet; en inloggning i e-tjänsten hos Myndigheten för föreningsstöd.
