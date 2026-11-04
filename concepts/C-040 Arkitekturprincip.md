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

Principen beslutas genom att ingå i en antagen referensarkitektur, som är principens bärare. Den gäller för ett eller flera arkitekturperspektiv, på den nivå som följer av den referensarkitektur som beslutar den. Arkitekturbeskrivningar prövas mot principen; en princip som ingen beskrivning går att pröva mot är inte en arkitekturprincip. En målarkitektur beslutar ingen princip, för där är valen redan gjorda: den utformas enligt principer som redan är beslutade och prövas mot dem. En nulägesarkitektur eller transitionsarkitektur beslutar heller aldrig en princip.

Verksamheten och verksamhetsdomänerna beslutar principer; lösningsnivån tillämpar dem, också när en lösning har andra lösningar i sig. En princip för en sorts lösning beslutas på den lägsta nivå som har alla berörda lösningar under sig.

ISO 42010:2022 räknar på samma sätt principerna till arkitekturen: "governing principles for the realization and evolution of this entity" ingår i definitionen av architecture.
