---
id: C-040
term: Arkitekturprincip
terms:
  - term: Arkitekturprincip
    language: sv
    source: catalogue
definition: "princip som ingår i en arkitektur och anger vilken riktning som ska väljas mellan designalternativ"
kind: governance-type
decided_by: [reference]
generic: "[[C-018 Princip]]"
partitive: "[[C-031 Arkitektur]]"
associative:
  - concept: "[[C-033 Arkitekturnivå]]"
    label: gäller på
  - concept: "[[C-036 Arkitekturperspektiv]]"
    label: gäller för
  - concept: "[[C-034 Arkitekturelement]]"
    label: tillämpas på
---
# C-040 Arkitekturprincip

**Definition:** princip som ingår i en arkitektur och anger vilken riktning som ska väljas mellan designalternativ

## Anmärkning

Principen är en del av arkitekturen: det mest allmänna av dess val. Den styr de mer detaljerade valen i samma arkitektur, och arkitekturen som helhet styr arkitekturobjektet. Principen hör till arkitekturen på den nivå där den beslutas och når nivåerna under, eftersom domänens arkitektur är en del av verksamhetens. Den är inget arkitekturelement: elementen uttrycker de bestämda valen, principen är ett allmänt val som tillämpas på dem.

Vad principen väljer mellan avgör om den är en arkitekturprincip. Arkitekturprincipen väljer mellan utformningar: vilka element som finns och hur de hänger ihop. Övriga principer väljer mellan handlingar i det löpande arbetet. Provet är om en arkitekturbeskrivning går att pröva mot principen. Bostadsbolagets Självbetjäning före personlig service väljer mellan appen och kundcenter som kanal, och en målarkitektur för felanmälan går att pröva mot den. Den är en arkitekturprincip. Akuta fel före planerat underhåll styr veckans arbetsordning, och ingen beskrivning går att pröva mot den. Den är en princip men ingen arkitekturprincip. Beslut 43.

Arkitekturprincipen står i en bärare som den med mandat fastställer. Styrelsen kan fastställa den i affärsplanen, och den är en arkitekturprincip redan där. Bland arkitekturbeskrivningarna är det bara referensarkitekturen som fastställer en arkitekturprincip. En referensarkitektur som listar en princip ur affärsplanen visar att den gäller. Principen gäller för ett eller flera arkitekturperspektiv, på nivån hos det styrobjekt den fastställs för. Arkitekturbeskrivningar prövas mot principen. En målarkitektur beslutar ingen princip, för där är valen redan gjorda: den utformas enligt principer som redan är beslutade och prövas mot dem. En nulägesarkitektur eller transitionsarkitektur beslutar heller aldrig en princip.

Verksamheten och verksamhetsdomänerna beslutar principer; lösningsnivån tillämpar dem, också när en lösning har andra lösningar i sig. En princip för en sorts lösning beslutas på den lägsta nivå som har alla berörda lösningar under sig.

Arkitekturstyrningen ([[C-049 Arkitekturstyrning]]) är aspektbaserad. Dess principer binder den som äger ett styrobjekt, men valen är ägarens: ägaren väljer, prövar valet mot principerna och väger dem. En avvikelse ([[C-213 Avvikelse]]) kan varken ägaren eller den som har arkitekturstyrningens mandat godta ensam. Den avgör den som gav båda sina mandat, eller den som en regel lägger avgörandet hos: "Avvikelse från princip beslutas i arkitekturrådet." Beslut 41, beslut 43.

ISO 42010:2022 räknar på samma sätt principerna till arkitekturen: "governing principles for the realization and evolution of this entity" ingår i definitionen av architecture.
