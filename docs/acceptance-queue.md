# Acceptanskön

Det som en körning på tavlan inte kunde pröva själv, i den ordning det ska prövas. Kön pekar; varje ärende bär sina rutor. En post står kvar tills den har gått igenom.

## Körningen 2026-11-18, ändringarna ae1b984..fb37c72 (våg 1)

Förberedelse: ingen. Posterna nedan läser den publicerade sajten, gestaltadet.se.

### [ ] #129 — Rubriken bryts rätt på en telefon

Maskin: en riktig telefon. Nicklas prövar för hand.

1. Öppna https://gestaltadet.se/ på telefonen, stående.
2. Läs rubriken: det långa ordet bryts inne i sig självt med ett bindestreck ("verksamhets-arkitektur"), och sidan går inte att skrolla i sidled.
3. Gör samma sak på https://gestaltadet.se/katalog/file/C-139/index.html, sidan om Applikationsgränssnitt (C-139).

Provet går igenom när båda sidorna visar bindestrecket och ingen av dem skrollar i sidled. Servern har ingen svensk avstavningsordlista i Chromium, så där mättes bara bredden (`docs/acceptance-shots/issue-129-rubrik.txt`).
