---
id: C-071
term: Applikation
terms:
  - term: Applikation
    language: sv
    source: catalogue
definition: "avgränsad programvara som tillhandahåller funktionalitet åt verksamheten genom ett eget gränssnitt"
kind: element-type
generic: "[[C-122 Resurs]]"
---
# C-071 Applikation

**Definition:** avgränsad programvara som tillhandahåller funktionalitet åt verksamheten genom ett eget gränssnitt

## Anmärkning

Systemägare är vardagens ord för den som har mandat ([[C-189 Mandat]]) över en applikation. Systemägaren är skild från informationsägaren ([[C-167 Informationsägare]]) till det applikationen lagrar och från lösningsägaren ([[C-055 Lösning]]). Systemägare är inget begrepp (ADR 0035).

Motsvarar ArchiMates Application Component.

Motsvarar Component i Unified Modeling Language (UML), och Actor när aktören är ett annat system. Komponenterna inuti en applikation är dess insida och ritas inte i lagret (ADR 0026). Applikationen består av sina gränssnitt (Interface, Port), realiseras av sin artefakt (Manifestation) och använder det gränssnitt kopplingen (Connector) går till. ADR 0029.
