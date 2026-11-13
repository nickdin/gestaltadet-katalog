---
id: C-211
term: Koppling
terms:
  - term: Koppling
    language: sv
    status: preferred
    source: concept new
definition: grad i vilken en ändring i ett arkitekturelement, en lösning eller ett styrobjekt tvingar fram en ändring i ett annat vid samma tidpunkt
associative:
  - concept: '[[C-055 Lösning]]'
    label: råder mellan
  - concept: '[[C-003 Styrobjekt]]'
    label: råder mellan
---
# C-211 Koppling

**Definition:** grad i vilken en ändring i ett arkitekturelement, en lösning eller ett styrobjekt tvingar fram en ändring i ett annat vid samma tidpunkt

## Anmärkning

Ett begrepp, ingen egen typ. Tät och lös är skalans två ändar och står i texten, inte som egna begrepp. Tät koppling betyder att det ena måste ändras samtidigt som det andra: ingen slack i tid, inget utbyte av delar. Lös koppling betyder att det ena kan ändras utan att det andra måste ändras samtidigt.

Kopplingen är måttet på ett snitt. Gränsen mellan två lösningar ([[C-055 Lösning]]) går där kopplingen är lös, och en leveransprodukt ([[C-174 Leveransprodukt]]) med krav ([[C-021 Krav]]) är formen för en lös koppling. Kopplingen är ett omdöme man gör när man skär, inte något som registreras mellan varje par av lösningar. Fynden är av två sorter. En tät koppling som går att lösa blir ett initiativ ([[C-012 Initiativ]]) i portföljen. En som inte går att lösa skrivs som en bedömning ([[C-185 Bedömning]]) på lösningen, som dess ägare bär med öppna ögon. Beslut 36.

Ordet är Charles Perrows, ur Normal Accidents (1984), där tät koppling tillsammans med sammansatta samspel är det som gör olyckor oundvikliga.

## Exempel

Fastighetssystemets moduler delar grunddata och release: tät koppling mellan Felanmälan och Hyra. Ansökningshandläggningen använder Föreningsregistret som leveransprodukt: lös koppling.
