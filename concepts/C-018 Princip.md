---
id: C-018
term: Princip
terms:
  - term: Princip
    language: sv
    source: catalogue
definition: "styrmedel som anger vilken riktning som ska väljas när flera alternativ är möjliga"
kind: governance-type
decided_by: [reference]
generic: "[[C-015 Styrmedel]]"
associative:
  - concept: "[[C-022 Ändamål]]"
    label: härleds ur
  - concept: '[[C-184 Påverkan]]'
    label: härleds ur
  - concept: '[[C-185 Bedömning]]'
    label: härleds ur
  - concept: '[[C-023 Konsekvens]]'
    label: anger
---
# C-018 Princip

**Definition:** styrmedel som anger vilken riktning som ska väljas när flera alternativ är möjliga

## Anmärkning

Principen är ett ställningstagande med generalitet: den gäller alla val av en viss typ, till skillnad från beslutet, som gäller ett enskilt fall. Valet prövas mot principen; riktningen är given men valet lämnas kvar. Principen härleds ur ett ändamål, en påverkan ([[C-184 Påverkan]]) eller en bedömning ([[C-185 Bedömning]]), anger sina konsekvenser, är prövbar men inte binär och kan behöva vägas mot andra principer.

Tre frågor avgör om en formulering är en princip (beslut 43):

1. Vilka alternativ väljer den mellan? En princip finns för att ett val finns. Kan ingen säga vad som väljs bort styr formuleringen inget val. "Handläggningstiden ska vara kort" pekar inte ut något alternativ och är ett mål ([[C-017 Mål]]).
2. Vad härleds den ur? Utan ursprung går principen inte att väga mot andra principer, och ingen vet när den ska omprövas.
3. Vad följer av att välja så? Konsekvenserna gör principen prövbar: styrobjektet prövas mot ett krav, handlingen mot en regel och utfallet mot en effekt. Utan konsekvenser är formuleringen en hållning ([[C-025 Hållning]]).

Två gränser till följer av svaren. En formulering som bara tillåter ett alternativ är ett krav ([[C-021 Krav]]) eller en regel ([[C-020 Regel]]): "Använd alltid Föreningsregistret" lämnar inget val. En formulering som gäller en enda fråga är ett styrbeslut ([[C-019 Styrbeslut]]): "Ärendehanteringen byggs på Ärendesystemet." Gemensamt före eget ger riktningen, lämnar valet kvar och gäller alla val av det slaget. Den är en princip.

En princip skrivs i fyra delar: namnet, riktningen med det som väljs bort, ursprunget och konsekvenserna. "Gemensamt före eget. En lösning använder det som redan finns gemensamt, som Föreningsregistret, hellre än att bygga eget. Principen härleds ur ändamålet lägre samlad förvaltningskostnad. Krav: varje lösning redovisar vad den bygger eget." Formen följer de tre frågorna, så en princip som är skriven i den har klarat provet.

**Nödvändighet:** Varje princip har ett ursprung: ett ändamål, en påverkan eller en bedömning. Varje princip anger minst en konsekvens.

Den som fattar valet väger principerna, i det enskilda valet. Vägningen går via principernas ursprung. När Gemensamt före eget står mot en princip om oberoende lösningar frågar den som väljer vilket ändamål som väger tyngst just här: lägre förvaltningskostnad eller färre beroenden. Ett val som har vägts har följt principerna, också den som vägde lättast. Krav och regler vägs inte. Två som strider mot varandra kan inte båda följas, så en av dem ändras eller en avvikelse godtas.

Ett val som går emot principens riktning utan att någon annan princip bär det är en avvikelse ([[C-213 Avvikelse]]). Den som äger styrobjektet fattar valen och väger principerna men kan inte sätta en princip åt sidan. Avvikelsen godtas genom ett styrbeslut ovanför ägaren, och principen gäller oförändrad för nästa val.

Principen står i en bärare ([[C-016 Bärare]]) som den med mandat ([[C-189 Mandat]]) fastställer: affärsplanen, verksamhetsplanen, en riktlinje, en policy, en referensarkitektur. Bäraren avgör inte sorten. En arkitekturprincip ([[C-040 Arkitekturprincip]]) är en princip som väljer mellan utformningar, och den är det i vilken bärare den än står (beslut 43). Bland arkitekturbeskrivningarna är det bara referensarkitekturen som fastställer principer. Arkitekturprincipen tar nivån hos det styrobjekt den fastställs för, har ingen detaljeringsgrad och anger de perspektiv den gäller. Beslut 37. Markeringen `decided_by: [reference]` på Princip och Arkitekturprincip är en spärr, ingen relation: bland arkitekturbeskrivningarna får bara en referensarkitektur fastställa en princip, och en målarkitektur, nulägesarkitektur eller transitionsarkitektur som listar den visar att den gäller utan att fastställa den. Verksamhetens princip fastställs genom sin bärare, utanför beskrivningarna.

Den som har mandat ([[C-189 Mandat]]) formulerar principen som svar på en bedömning ([[C-185 Bedömning]]) (beslut 23, beslut 25).

## Motsvarigheter

Principen är SBVR:s och Business Motivation Models business policy: styrning som inte är direkt prövbar, finns för att vägleda och som regler härleds ur. På svenska är en policy oftast dokumentet: en bärare ([[C-016 Bärare]]) som kan rymma principer, regler och mål. Policy är därför ingen term för principen (beslut 43).

## Exempel

"Utveckla för återanvändning." "Gemensamt före eget." "Akuta fel före planerat underhåll."
