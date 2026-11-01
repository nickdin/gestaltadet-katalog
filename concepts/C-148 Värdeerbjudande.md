---
id: C-148
term: Värdeerbjudande
terms:
  - term: Värdeerbjudande
    language: sv
    source: catalogue
definition: "det som en eller flera produkter utlovas göra för en målgrupp eller en namngiven aktör"
kind: element-type
value_proposition:
  aimed_at: "[[C-152 riktas till]]"
  meets: "[[C-153 möter]]"
associative:
  - concept: "[[C-145 Målgrupp]]"
    label: riktas till
  - concept: "[[C-073 Aktör]]"
    label: riktas till
  - concept: "[[C-146 Behov]]"
    label: möter
  - concept: "[[C-014 Produkt]]"
    label: bygger på
---
# C-148 Värdeerbjudande

**Definition:** det som en eller flera produkter utlovas göra för en målgrupp eller en namngiven aktör

## Exempel

ett bidrag som går att söka på en kväll, riktat till föreningarnas företrädare: rätt belopp betalas ut i tid utan att föreningen själv behöver räkna ut det.

## Anmärkning

Värdeerbjudandet riktas till exakt en målgrupp eller en namngiven aktör, bygger på en eller flera produkter och möter ett eller flera behov. Det står mellan produkt och behov: en produkt möter ett behov bara genom ett värdeerbjudande, aldrig direkt. Produkten är det som levereras ([[C-014 Produkt]]); värdeerbjudandet är vad den utlovas göra, och samma produkt kan bära olika värdeerbjudanden till olika målgrupper. Hör till verksamhetsperspektivet eftersom verksamheten utformar det. Elementets text säger hur det svarar på vart och ett av behoven.

Texten per behov är ett svar ([[C-194 Svar]]), ett begrepp utan typ: hur erbjudandet röjer behovets hinder och ger dess vinst, och ett behov utan svar är passningen synliggjord. ValueProposition i Business Architecture Core Metamodel (BACM) mappas hit och dess ValueItem till svaret; passningens mått, ValueCharacteristic, väntar på ett måttbegrepp. Värdeerbjudandet realiseras av ([[C-094 realiseras av]]) en värdeström ([[C-190 Värdeström]]), stegen där värdet byggs upp. ADR 0027.
