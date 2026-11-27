---
id: C-097
term: flödar till
terms:
  - term: flödar till
    language: sv
    source: catalogue
definition: relationstyp som anger att något som inte är ett eget element i lagret går från ett arkitekturelement till ett annat
kind: relation-type
key: flows_to
flow: true
---
# C-097 flödar till

**Definition:** relationstyp som anger att något som inte är ett eget element i lagret går från ett arkitekturelement till ett annat

## Anmärkning

Relationen går från det avsändande elementet till mottagaren, och det som går står i relationens beskrivning: ett meddelande, en signal, en överlämning utan eget objekt. Det som är ett element i lagret flödar aldrig som text. Ett verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]) eller ett informationsobjekt ([[C-060 Informationsobjekt]]) når beteendet med har åtkomst till ([[C-101 har åtkomst till]]): avsändaren skriver det och mottagaren läser det. Pilen mellan de två beteendena är programmets slutsats ur de två åtkomsterna, aldrig en lagrad relation. Den som vill kontrollera vad som går gör det till ett element; då härleds pilen. Två steg som båda skriver samma objekt får pilar åt båda hållen; ordningen i kedjan är utlösers ([[C-098 utlöser]]) sak.

## Motsvarigheter

Motsvarar ArchiMates Flow och BPMN:s Message Flow när etiketten är fri text. [[0014-processerna-ar-organisationens-och-kartan-delas-per-process|Beslut 14]], bekräftat och avgränsat i [[0033-flodet-mellan-tva-beteenden-harleds-ur-atkomsten-flodar-till-ar-for-det-som-inte-ar-ett-element-och-de-frammande-flodena-som-bar-ett-element-ar-atkomstparet|beslut 33]].

I Unified Modeling Language (UML) bär ObjectFlow och InformationFlow alltid ett element, liksom DeliverableFlow i Value Delivery Modeling Language (VDML); de är åtkomstparet, inte denna relation. [[0029-klassen-ar-informationsobjektet-tillstandsmaskinen-ar-tillstandsvyn-anvandningsfallet-ar-tjansten-vardemangd-ar-ett-begrepp-och-uml-tas-in-for-lasarnas-skull-utan-tveksamma-rader|Beslut 29]], ändrat i [[0033-flodet-mellan-tva-beteenden-harleds-ur-atkomsten-flodar-till-ar-for-det-som-inte-ar-ett-element-och-de-frammande-flodena-som-bar-ett-element-ar-atkomstparet|beslut 33]].
