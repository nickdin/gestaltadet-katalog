# Forum är en elementtyp som specialiserar verksamhetssamverkan

Beslutat av Nicklas när de öppna frågorna i den första beskrivningen av en avdelning behandlades.

## Sammanhang

Katalogen hade inget eget ord för ett forum, fast beslutskartan över hur avdelningen beslutar ritade ett dussin sådana. Avdelningens beslutsforum, föredragningarna, ledningsgrupperna, pulsmötena och råden, var typade som verksamhetssamverkan (C-141), ArchiMates Business Collaboration. Beskrivningen hade en öppen fråga om aktör (C-073) var det rätta i stället. Nicklas frågade om det alls behövs ett element för ett forum: ett forum är i alla fall ingen egen aktör.

## Övervägda alternativ

- **Nytt begrepp Forum, en specialisering av verksamhetssamverkan.** Ett forum är skilda aktörer som agerar tillsammans, alltså samverkan, men av en bestämd sort: det återkommer och är till för att bereda, diskutera eller besluta ärenden. Med ett eget ord säger katalogen vad ett forum är, och beslutskartan kan läsas utan ArchiMate-termer. Valt.
- **Behålla verksamhetssamverkan.** Rätt i ArchiMates mening, men ordet säger inget om att det är där besluten fattas, och frågan hade kommit tillbaka. Avvisat.
- **Aktör.** Ett team är en varaktig aktör; ett forum är chefer från skilda enheter som möts. Avvisat.
- **Inga forumelement: bara processen för att bereda, föredra och besluta ärenden, och styrdokumenten.** Beslutskartan förlorar sina rutor, och var ett beslut fattas är just det kartan ska visa. Avvisat.

## Konsekvenser

- `C-156 Forum` får `kind: element-type` och `generic: C-141 Verksamhetssamverkan`, och täcks av `C-109 Verksamhetsperspektiv`. Interlinguas ADR 0008 håller: typen hör till exakt ett perspektiv.
- Forumen i beskrivningen typas om till Forum. Verksamhetssamverkan finns kvar för samverkan som inte är ett forum.
- Forum står under `unmapped-concepts` i `mapping/archimate.yaml` och `mapping/aris.yaml`. En Business Collaboration importeras som verksamhetssamverkan, och ett forum typas för hand. En export skriver forumen som det deras generiska begrepp mappas till först när tabellerna säger det.
- `interlingua concept new` tar ingen `generic`; raden skrevs för hand, som i C-141.
