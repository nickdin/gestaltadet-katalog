---
id: C-011
term: Portfölj
terms:
  - term: Portfölj
    language: sv
    source: catalogue
definition: "sammanhållen mängd av initiativ och produkter som prioriteras och finansieras gemensamt"
kind: element-type
partitive: '[[C-009 Utvecklingsdomän]]'
---
# C-011 Portfölj

**Definition:** sammanhållen mängd av initiativ och produkter som prioriteras och finansieras gemensamt

## Anmärkning

Portföljen är ett styrobjekt ([[C-003 Styrobjekt]]), se portföljstyrning ([[C-044 Portföljstyrning]]). Både den centrala portföljen och varje delportfölj registreras som portfölj: portföljen aggregerar ([[C-100 aggregerar]]) sina delportföljer, och delportföljen aggregerar sina initiativ ([[C-012 Initiativ]]). Att portföljen också rymmer produkter ([[C-014 Produkt]]) uttrycks med samma relation; produkten står i ett annat perspektiv, så den relationen syns i lagret men i ingen vy. Elementtyp i strategiperspektivet ([[C-108 Strategiperspektiv]]), bredvid verksamhetsförmågan och initiativet. ADR 0019.

Förvaltningsobjektet, lösningen ([[C-055 Lösning]]), ingår inte i portföljen; dess leveransprodukter ([[C-174 Leveransprodukt]]) gör det, och ramen går till den lösning som realiserar dem. ADR 0020.

ArchiMate har inget portföljelement, så typen står under `unmapped-concepts` i mappningstabellerna, som initiativet.
