---
id: C-190
term: Värdeström
terms:
  - term: Värdeström
    language: sv
    status: preferred
    source: concept new
definition: uppsättning steg som vart och ett tillför en del av det värde ett värdeerbjudande utlovar
kind: element-type
associative:
  - concept: '[[C-069 Verksamhetsförmåga]]'
    label: använder
  - concept: '[[C-148 Värdeerbjudande]]'
    label: realiserar
---
# C-190 Värdeström

**Definition:** uppsättning steg som vart och ett tillför en del av det värde ett värdeerbjudande utlovar

## Anmärkning

Elementtyp i strategiperspektivet ([[C-108 Strategiperspektiv]]), bredvid verksamhetsförmågan och initiativet. Värdeströmmen säger vilket värde som byggs upp på vägen till ett värdeerbjudande ([[C-148 Värdeerbjudande]]), inte vem som gör vad: den är ingen process. Ett steg är också en värdeström, och helheten består av ([[C-062 består av]]) sina steg. Stegens ordning bär ingen betydelse som en process ordning gör; vårdens utredning, behandling och förebyggande kommer i den ordning fallet kräver.

Varje steg använder ([[C-095 använder]]) de verksamhetsförmågor ([[C-069 Verksamhetsförmåga]]) det förutsätter. Steget realiseras av ([[C-094 realiseras av]]) en verksamhetsprocess ([[C-130 Verksamhetsprocess]]) eller verksamhetsaktivitet, och värdeerbjudandet realiseras av värdeströmmen.

Motsvarar ValueStream och ValueStreamStage i Business Architecture Core Metamodel (BACM) och ArchiMates Value Stream. ADR 0027.

Value Delivery Modeling Language (VDML) har ingen egen klass för värdeströmmen: aktivitetsnätverket med sina ValueAdds är den. Varje steg realiserar ([[C-094 realiseras av]]) de värden ([[C-195 Värde]]) det tillför, så att värdeströmskartan visar värdet vid steget. ADR 0028.

## Exempel

ett bostadsbolags Att få en bostad: söka, få erbjudande, teckna avtal, flytta in; en myndighets Att få stöd: ansöka, få beslut, få utbetalning.
