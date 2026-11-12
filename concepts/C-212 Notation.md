---
id: C-212
term: Notation
terms:
  - term: Notation
    language: sv
    status: preferred
    source: concept new
definition: uppsättning symboler, med regler för hur de används, som arkitekturelement och relationer ritas med i ett diagram
associative:
  - concept: '[[C-039 Metamodell]]'
    label: står för typerna i
---
# C-212 Notation

**Definition:** uppsättning symboler, med regler för hur de används, som arkitekturelement och relationer ritas med i ett diagram

## Exempel

katalogens egen, rutorna i draw.io-mallen; ArchiMates, BPMN:s, UML:s.

## Anmärkning

Notationen säger hur något ritas. Metamodellen ([[C-039 Metamodell]]) säger vad det är. I BPMN är den rundade rutan symbolen, och regeln är att den står för en aktivitet. Vad en aktivitet är säger metamodellen.

Notationen hör till diagrammet ([[C-106 Diagram]]), inte till vyn. Exempel: Myndigheten för föreningsstöd ritar handläggningen av en bidragsansökan två gånger, en gång med BPMN:s symboler och en gång med ArchiMates. Vyn är densamma, och elementen är av samma typer i katalogen. Ett diagram får blanda notationer.

En notation har en hemmetamodell, och symbolerna står för dess typer. Notationen läggs på en annan metamodell genom en mappningstabell. Katalogens verksamhetsaktivitet ([[C-175 Verksamhetsaktivitet]]) är BPMN:s Task och ritas därför som en rundad ruta. Katalogens egen notation är rutorna i draw.io-mallen. Den behöver ingen tabell, eftersom symbolerna redan står för katalogens typer.

ISO 42010:s model kind rymmer både metamodellen och notationen, och katalogen håller isär dem. Beslut 42.
