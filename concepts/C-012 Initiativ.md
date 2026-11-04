---
id: C-012
term: Initiativ
terms:
  - term: Initiativ
    language: sv
    source: catalogue
definition: "tidsbegränsad förändringsinsats med definierat slut"
kind: element-type
partitive: '[[C-011 Portfölj]]'
---
# C-012 Initiativ

**Definition:** tidsbegränsad förändringsinsats med definierat slut

## Anmärkning

Ett initiativ är det som flyttar verksamheten mot dess inriktning, och kartan ska kunna visa vad som pågår och vad det ändrar. Det är en elementtyp i strategiperspektivet ([[C-108 Strategiperspektiv]]), bredvid verksamhetsförmågan. Ett projekt registreras som ett initiativ ([[C-013 Projekt]]). Initiativet är också ett styrobjekt ([[C-003 Styrobjekt]]), se initiativstyrning ([[C-045 Initiativstyrning]]). Motsvarar ArchiMates Work Package, som ligger i implementations- och migrationslagret utanför den kärna mappningstabellerna täcker; initiativet står därför under `unmapped-concepts` där. ADR 0010.

Initiativet påverkar den verksamhetsförmåga ([[C-069 Verksamhetsförmåga]]) det utvecklar och det mål ([[C-017 Mål]]) det prövas mot. Det initiativet lämnar ifrån sig, dess leverabel ([[C-171 Leverabel]]), registreras som det element det blir. Portföljen ([[C-011 Portfölj]]) aggregerar sina initiativ. ADR 0019.

Verksamhetsuppföljningen kallar ofta initiativen uppdrag: ett projekt, ett utvecklingsuppdrag, en förbättring registreras som initiativ. Det tidsbundna som inte förändrar något, ett regeringsuppdrag eller en analys på beställning, är inget initiativ utan ett ärende i en handläggning ([[C-160 Handläggning]]). Det handläggningen tillhandahåller är en verksamhetsprodukt ([[C-173 Verksamhetsprodukt]]). ADR 0020.

Initiativet är inte Business Motivation Models Course of Action, vägvalet, som är ett styrbeslut ([[C-019 Styrbeslut]]); initiativet är arbetet som genomför vägvalet (ADR 0025).

Initiative i Business Architecture Core Metamodel (BACM) är ett initiativ, och dess Change den verksamhetsförändring ([[C-172 Verksamhetsförändring]]) initiativet åstadkommer. ADR 0027.
