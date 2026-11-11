---
id: C-202
term: Resursdata
terms:
  - term: Resursdata
    language: sv
    status: preferred
    source: concept new
  - term: masterdata
    language: sv
    source: concept change
  - term: kärndata
    language: sv
    source: concept change
definition: informationsobjekt om det verksamheten har och som dess transaktioner hänvisar till
generic: '[[C-060 Informationsobjekt]]'
---
# C-202 Resursdata

**Definition:** informationsobjekt om det verksamheten har och som dess transaktioner hänvisar till

## Anmärkning

Resursdata är det verksamheten har: det som finns kvar mellan transaktionerna och som de märks med. En ansökan hänvisar till sin förening, en hyresfordran till sitt hyresavtal. Ett avtal är resursdata fast det har en livscykel: det ligger kvar i åratal och transaktionerna hänvisar till det. Masterdata och kärndata är tillåtna termer.

Ett begrepp, ingen elementtyp: en datakategori ([[C-201 Datakategori]]) för ett informationsobjekt ([[C-060 Informationsobjekt]]). Resursdata har vanligen en utsedd informationsägare ([[C-167 Informationsägare]]), skild från processägaren ([[C-206 Processägare]]) för objektets hem, eftersom många beteenden läser dem (beslut 35).

Informationsarkitektens bidrag är en central källa och bred användning. Varje resursdataobjekt ska ha en källa: den representation ([[C-085 Representation]]) på den lagringsyta ([[C-165 Lagringsyta]]) där förekomsten ägs, så att andra ytor hämtar därifrån. Var källan är pekar lagret inte ut ännu; det är en fråga informationsägaren ([[C-167 Informationsägare]]) ska kunna svara på. Beslut 32.

## Exempel

Förening, Företrädare och Kontonummer hos Myndigheten för föreningsstöd; Fastighet, Lägenhet, Hyresgäst och Hyresavtal hos Brinkstadsbostäder.
