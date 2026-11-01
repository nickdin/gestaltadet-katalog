# Initiativ är en elementtyp i strategiperspektivet; projekt registreras som initiativ

Beslutat av Nicklas när den första beskrivningen av en avdelning skrevs i lagret.

## Sammanhang

Katalogen hade Initiativ (C-012) och Projekt (C-013) som begrepp utan `kind`: styrobjekt som portföljstyrningen och initiativstyrningen känner till, men inget som kan skrivas som element. När avdelningen beskrevs kunde de pågående insatserna, en ny e-tjänst, ett systembyte, en upphandling, bara stå som text i beskrivningen. Kartan visade då aldrig vad som pågår, och ingen relation kunde ritas mellan ett initiativ och det det ändrar. Samtidigt vill Nicklas kunna visa spårbarheten uppdrag, förmåga, initiativ och realisering i en och samma bild.

## Övervägda alternativ

- **Initiativ blir elementtyp i strategiperspektivet; projekt förblir begrepp.** Ett initiativ hör ihop med inriktningen: det är det som flyttar verksamheten mot vad den behöver kunna, och står därför bredvid verksamhetsförmågan (C-069) i det perspektivet. Ett projekt är ett initiativ i en viss form och registreras som initiativ, så som en intern produkt registreras som produkt. Valt.
- **Både initiativ och projekt blir elementtyper.** Ger en egen ruta för projekt till priset av att varje insats måste sorteras, och källmaterialet gör inte den skillnaden konsekvent. Avvisat.
- **Ingen elementtyp: initiativ är det som styrs, inte det som ritas.** Håller katalogen som den var; initiativen står under Åtgärder i beskrivningar och i portföljstyrningens egna listor. Kartan visar aldrig vad som pågår. Avvisat.
- **Ett sjunde perspektiv för förändring**, ArchiMates implementations- och migrationslager som eget perspektiv. Tungt, och mot ADR 0009:s sex perspektiv. Inte övervägt på allvar.

## Konsekvenser

- `C-012 Initiativ` får `kind: element-type` och täcks av `C-108 Strategiperspektiv`, vars `covers` nu är verksamhetsförmåga och initiativ. Interlinguas ADR 0008 håller: typen hör till exakt ett perspektiv.
- `C-013 Projekt` förblir ett begrepp; dess anmärkning säger att ett projekt registreras som initiativ.
- Initiativet motsvarar ArchiMates Work Package, som ligger utanför den 3.2-kärna mappningstabellerna täcker; C-012 står därför under `unmapped-concepts` i `mapping/archimate.yaml` och `mapping/aris.yaml`, på samma sätt som verksamhetsförmågan. En export tar inte med initiativen förrän tabellerna utökas.
- En beskrivnings pågående initiativ skrivs som element, inte som text, och visas i en vy ur strategiperspektivet. Hos Myndigheten för föreningsstöd är den nya e-tjänsten för redovisning och den automatiska beräkningen av verksamhetsbidraget två sådana element.
- Relationen från ett initiativ till det det ändrar är `påverkar` (C-102); vad ett initiativ ersätter uttrycks först i en målbild, med `ersätter` (C-104), inte i nuläget.
