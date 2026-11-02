---
id: C-085
term: Representation
terms:
  - term: Representation
    language: sv
    source: catalogue
  - term: informationsbärare
    language: sv
    source: concept change
    status: admitted
  - term: handling
    language: sv
    source: concept change
    status: admitted
  - term: handlingstyp
    language: sv
    source: concept change
    status: admitted
definition: "konkret, ofta mänskligt läsbar form som ett informationsobjekt tar"
kind: element-type
associative:
  - concept: '[[C-060 Informationsobjekt]]'
    label: ger form åt
  - concept: '[[C-165 Lagringsyta]]'
    label: ligger på
---
# C-085 Representation

**Definition:** konkret, ofta mänskligt läsbar form som ett informationsobjekt tar

## Anmärkning

Motsvarar ArchiMates Representation. Informationsbärare i kartläggningens mening är representationen; stället den ligger på är lagringsytan ([[C-165 Lagringsyta]]), som aggregerar ([[C-100 aggregerar]]) den: samma representation kan ligga på flera ytor, och ytan finns kvar när representationen tas bort. En utskriven blankett eller en pappersakt är en representation, det fysiska som bär information. SDMN:s Document, ett dokument tryckt eller elektroniskt, är en representation, och dess Physical är det när saken bär information; utan informationssida är den ett verksamhetsobjekt ([[C-159 Verksamhetsobjekt]]). Beslutet: ADR 0024.

Handling och handlingstyp är tillåtna termer. Tryckfrihetsförordningens handling, "framställning i skrift eller bild samt upptagning", är en form, och katalogen ritar typer: elementet Ansökningsblankett är handlingstypen, den enskilda ansökan förekomsten. En handling som förvaras hos myndigheten och har kommit in eller upprättats är en allmän handling ([[C-199 Allmän handling]]). Ett verksamhetsbeteende ([[C-157 Verksamhetsbeteende]]) har åtkomst till ([[C-101 har åtkomst till]]) den representation det tar emot, upprättar, kopierar, lämnar ut eller gallrar; paret beteende och representation är handlingstypen per process, som arkivredovisningen ordnar bevarande och gallring ([[C-200 Gallring]]) efter, och vad som gäller för paret står i informationshanteringsplanen, inte i lagret. Att samma representation ligger på flera ytor betyder att den kopierats dit, och beteendet som gjorde kopian har gjort en behandling ([[C-168 Behandling]]); en kopia i annan form, utskriften, är en ny representation, och radering ska nå varje yta. Till representationen hör format och läsbarhet, märkningen av klassen, signering och låsning; äkthet, att handlingen är oförändrad över tid, är riktighet tillämpad på representationen under hela bevarandetiden. Representationen har inget tillstånd ([[C-182 Tillstånd]]): arkiverad och gallrad är aktiviteter i arkivvården, inte lägen hos handlingen, och att ärendet är arkiverat är verksamhetsobjektets tillstånd. Ett registerutdrag eller en fil för dataportabilitet är en representation myndigheten upprättar på begäran, av en sammanställning ([[C-162 Sammanställning]]), med formatkravet på representationen. Beslutet: ADR 0031.
