# Acceptanskön

Det som en körning på tavlan inte kunde pröva själv, i den ordning det ska prövas. Kön pekar; varje ärende bär sina rutor. En post står kvar tills den har gått igenom.

## Körningen 2026-11-18, ändringarna ae1b984..fb37c72 (våg 1)

Förberedelse: ingen. Posterna nedan läser den publicerade sajten, gestaltadet.se.

### [x] #129 — Rubriken bryts rätt på en telefon

Gick igenom 2026-11-19 på Nicklas telefon, stående. Rubrikerna på båda sidorna ryms på skärmen, och ingen av sidorna går att dra i sidled. Bindestrecket syntes inte, eftersom båda orden ryms på den telefonen. Ett ord bryts bara när det inte ryms. Ärendets ruta kräver att rubriken ryms, inte att ordet bryts.

Maskin: en riktig telefon. Nicklas prövar för hand.

1. Öppna https://gestaltadet.se/ på telefonen, stående.
2. Läs rubriken: det långa ordet bryts inne i sig självt med ett bindestreck ("verksamhets-arkitektur"), och sidan går inte att skrolla i sidled.
3. Gör samma sak på https://gestaltadet.se/katalog/file/C-139/index.html, sidan om Applikationsgränssnitt (C-139).

Provet går igenom när båda sidorna visar bindestrecket och ingen av dem skrollar i sidled. Servern har ingen svensk avstavningsordlista i Chromium, så där mättes bara bredden (`docs/acceptance-shots/issue-129-rubrik.txt`).

## Körningen 2026-11-18, ändringarna eb48f9d..98a6fbc (våg 3)

Förberedelse: draw.io på en dator med skärm, som program eller i webbläsaren på app.diagrams.net. Posten läser den publicerade sajten, gestaltadet.se, efter att vågen har pushat.

### [x] #148 — Formbiblioteket för draw.io öppnas med stegen på sidan

Gick igenom 2026-11-19 på laptopen, i draw.io i webbläsaren på svenska. Biblioteket visades till vänster under namnet library-drawio med 59 rutor. Rutan Applikation gick att dra in och behöll typen när den fick namnet Ärendesystemet. Stegen för Excalidraw gick också igenom, men filen lades in genom att dras till ritningen, eftersom provet inte kan fylla i datorns filväljare. Ingen har klickat sig igenom menyn i draw.io som program på datorn.

Maskin: en dator med skärm. Nicklas prövar för hand; ingen kan klicka i draw.io på servern.

1. Gå till https://gestaltadet.se/katalog/document/docs/formbibliotek.md/ och läs stegen under Öppna biblioteket i draw.io.
2. Gå till sidan Katalog och högerklicka på länken Formbibliotek för draw.io. Spara länken som en fil.
3. Öppna en ritning i draw.io.
4. Välj Fil, sedan Öppna bibliotek från och sedan Enhet. I draw.io som program på datorn: Fil och sedan Öppna bibliotek.
5. Välj filen `library-drawio.xml`.
6. Dra en ruta från biblioteket in i ritningen.

Provet går igenom när biblioteket visas bland formerna till vänster under filens namn, rutan går att dra in och varje menyord på sidan finns i draw.io. Stegen för Excalidraw på samma sida är inte heller prövade; pröva dem gärna samtidigt på excalidraw.com.
