# Arkitekturobjektet är ett styrobjekt som har en utformning, och arkitekturen säger vilka arkitekturobjekt objektet delas in i

Beslutat av Nicklas 18 november 2026, när han såg att definitionerna av arkitektur och arkitekturobjekt förklarade varandra och att arkitekturen inte sade vilka arkitekturobjekt som ska finnas.

## Sammanhang

Arkitektur (`C-031`) definierades som utformningen av ett arkitekturobjekt. Arkitekturobjekt (`C-032`) definierades som "styrobjekt som en arkitektur avser". Läsaren som slog upp det ena ordet skickades till det andra, och ingen av definitionerna sade vad som gör ett styrobjekt till ett arkitekturobjekt.

Definitionen av Arkitektur (`C-031`) talade dessutom bara om ett objekts form och funktion. Hos Myndigheten för föreningsstöd finns fem verksamhetsdomäner under generaldirektören, och registerlösningen är en egen lösning eftersom två lösningar delar Föreningsregistret. Det är val om vilka arkitekturobjekt som ska finnas, och katalogen sade inte vems arkitektur de hör till. Ärendet är #182.

## Beslut

- **Arkitekturobjektet definieras utan ordet arkitektur.** Arkitekturobjekt (`C-032`) definieras "styrobjekt som har en utformning: verksamheten, en verksamhetsdomän eller en lösning". Arkitektur (`C-031`) fortsätter att säga arkitekturobjekt.
- **Ett styrobjekt utan utformning har ingen arkitektur.** Generaldirektörens portfölj och initiativet Automatisk beräkning är styrobjekt men inga arkitekturobjekt. Initiativet ändrar utformningen av två lösningar och har ingen egen.
- **Det omgivande objektets arkitektur säger vilka arkitekturobjekt objektet delas in i.** Verksamhetens arkitektur säger vilka verksamhetsdomäner som finns, och domänens arkitektur säger vilka lösningar som finns i domänen. Arkitektur (`C-031`) definieras "grundläggande utformning av ett arkitekturobjekt, beskriven eller inte: dess form och funktion, vilka arkitekturobjekt det delas in i och de principer som styr hur det realiseras och förändras".
- **Att verksamheten själv finns säger ingen arkitektur.** Regeringen har inrättat Myndigheten för föreningsstöd.

## Övervägda alternativ

- **Bryta cirkeln i Arkitektur (`C-031`)**, som då hade sagt "utformning av ett styrobjekt". Då hade också portföljen och initiativet kunnat ha en arkitektur. Avvisat.
- **Låta de två definitionerna stå som ett par**, så som ISO 42010 gör med arkitektur och system. Läsaren hade fortfarande behövt läsa båda för att förstå den ena. Avvisat.
- **Säga indelningen bara i anmärkningen**, eftersom den redan ryms i ordet form. Avvisat: definitionen ska säga det själv.
- **Låta bara verksamhetens arkitektur säga vilka arkitekturobjekt som finns.** Då hade chefen för Bidragsenheten inte själv kunnat bryta ut en ny lösning i domänen Bidragsgivning. Avvisat.

## Konsekvenser

- Nya definitioner i `C-031` och `C-032`. Relationerna är oförändrade: Arkitektur (`C-031`) avser fortfarande Arkitekturobjekt (`C-032`) och kan ingå i sig själv.
- Anmärkningen i `C-031` är omskriven i klarspråk och säger indelningen. Stycket om ISO 42010 står under Motsvarigheter, och begreppet har fått ett exempel. `C-032` har fått ett stycke om styrobjekt utan utformning.
- `CONTEXT.md`: posten Arkitekturobjekt säger att arkitekturobjektet har en utformning.
- Beslut 37 gäller i övrigt: arkitekturen finns alltid, beskriven eller inte. Definitionen i beslut 37 är ersatt av den här.
- Tre ritningar i `layout/Arkitektur/` och en i `layout/Principer/` bär de gamla definitionerna i sin text. De rättas i #183.
