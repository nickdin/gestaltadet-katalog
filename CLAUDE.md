# CLAUDE.md: gestaltadet-katalog

GestaltaDets begreppskatalog: begreppen, mappningstabellerna, besluten bakom dem och de två exempelorganisationerna. Publik, CC BY 4.0. Programmet som läser lagret är interlingua (`~/Devbox/interlingua`, `nickdin/interlingua`); dess README säger hur det används. Filen är på svenska som allt annat här, eftersom läsaren är svensk och data aldrig översätts.

## Svenska

Data och samtal här är svenska. Översätt aldrig data för att kod eller text ska läsas lättare. Engelska ord som är termer i sig (EDGY:s *journey*, TOGAF:s *architecture domain*) står kvar som främmande ord.

## Katalogens enda hem

En definition ändras här och ingen annanstans. Element, relationer, beskrivningar och vyer skrivs med `interlingua`-kommandona, inte för hand; text under rubrikerna i en fil får läggas till.

## Ingen verklig organisation

Katalogen är allmän och nämner ingen verklig arbetsgivare, enhet, system eller internt dokument, varken i filerna, i commit-meddelandena eller i ärendena. Varje exempel hämtas ur de två påhittade organisationerna i `docs/exempel/`: Myndigheten för föreningsstöd och bostadsbolaget. Lag och allmänna ramverk nämns fritt: förvaltningslagen, myndighetsförordningen, pm3, ArchiMate, BPMN, DMN, SBVR. Ett behov som en verklig organisations dokument gav upphov till skrivs som ett allmänt behov. Arbete som kräver att en verklig organisation nämns hör till ett privat repo, inte hit.

## Skriv ut termen

Ett id säger Nicklas ingenting ensamt: skriv alltid termen vid det, "Uppdrag (C-149)", i samtal, frågor, ärenden och commit-meddelanden.

## Klarspråk

All text som skrivs här, anmärkningar, beslut, exempel och ordlistan, skrivs i klarspråk med `klarsprak`-skillen: det viktigaste först, ett ämne per stycke, en tanke per mening, aktören utsatt, samma ord för samma sak. Nivån är Lösning (C-055) efter #42. En text som skrivs under en grillning skrivs om innan den checkas in; definitionerna rörs inte utan egen grillning.

## Vem som skrivit texten

Varje text på gestaltadet.se har ett av fyra lägen (ADR 0039): skriven av Nicklas; skriven av Nicklas, redigerad av AI och godkänd; skriven av AI, granskad och godkänd av Nicklas; skriven av AI, inte granskad.

- Bara Nicklas godkänner, en namngiven text i taget. Skriv in godkännandet med datum när han pekat ut texten. Märk aldrig något som godkänt på eget initiativ.
- Ny text från Claude är alltid "skriven av AI, inte granskad".
- Varje ordändring av Claude i en godkänd text tar bort godkännandet, även ett kommatecken. Säg det innan du ändrar i en godkänd text. Två ändringar tar inte bort det: att texten flyttas eller får en ändrad länk, och ett exakt byte av ett ord mot ett annat som Nicklas beställt.
- Läsaren möter ordet beslut, inte ADR: "beslut 25". Ett nytt besluts första rad säger för läsaren vem som beslutade, när och varför.

## Grillningar

Varje fråga i en grillning bär ett konkret exempel i själva dialogen, hämtat ur de två exempelorganisationerna. Nicklas avgör frågan på fallet, inte på principen. Exemplen skrivs in i filerna först när svaret är givet.

## Ritningar

En pil i en ritning i `layout/` som saknar relation i lagret tas inte bort. Lämna pilen och lägg ett `question`-ärende; Nicklas värderar om lagret eller ritningen har rätt.

En ritning läggs i sitt ämnes mapp under `layout/`. Ritningssidan skriver `publish` själv ur de mappar som `drawings:` i `settings.yaml` räknar upp, och en ny ämnesmapp läggs till där.

## Frågor in, ändringar hans

Katalogen är hur Nicklas ser på saker. Frågor, invändningar och förslag från läsare är välkomna som ärenden och besvaras; en ändring i en definition gör Nicklas, eller Claude på hans ord. Arbete på programmet, en funktion, ett fel, ett kommando som beter sig fel, hör till interlinguas tracker, `nickdin/interlingua`, även när det upptäcks här.

## Valvanteckningen

En session här får bocka av och skriva i valvanteckningen `2. Områden/GestaltaDet/GestaltaDet.md` (Nicklas, 2026-11-01 och 2026-11-11). Resten av valvet läser den bara.

## Kontroll

`~/Devbox/interlingua/.venv/bin/interlingua check .` kontrollerar lagret och ska sluta `no violations`.

`check` går igenom även före en ändring. Den bevisar därför aldrig ensam att en ruta om något som ändrats är uppfylld. En sådan ruta får ett prov som ger ett annat svar på basen än på grenen, sparat under `docs/acceptance-shots/`.

Interlinguas skrivande kommandon vägrar köra när arbetskopian har ändringar som inte är committade. Committa därför varje steg innan nästa kommando (sett i tre sessioner, 2026-11-02 till 2026-11-05).

## Synk och publicering

Git, remote `nickdin/gestaltadet-katalog`. Commit och push utan att fråga; `main` är enda grenen tills Nicklas säger annat.

Varje push till `main` publicerar. Arbetsflödet `Publicera katalogen` (`.github/workflows/publicera.yml`) bygger då om gestaltadet.se, och bygget tar flera minuter. Kontrollera det efter push med `gh run list --workflow publicera.yml -L 1`, och säg i svaret om sajten är uppdaterad.

## Agent skills

### Issue tracker

Ärendena bor i GitHub Issues i `nickdin/gestaltadet-katalog`, publikt. De tar katalogens arbete och sajtens: ritningarna, startsidan och den grafiska profilen. Programmets arbete går till `nickdin/interlingua`. Tavlan är https://github.com/users/nickdin/projects/22. Se `docs/agents/issue-tracker.md`.

### Triage labels

Två etiketter per öppet ärende: en typ (`bug`, `enhancement`, `question`) och en status (de fem standardrollerna plus `parked`), samt ämnesetiketten `needs-grilling`. Se `docs/agents/triage-labels.md`.

### Domain docs

Single-context: en `CONTEXT.md` i roten, ordlistan, och en `docs/adr/` i roten; begreppen definieras bara i `concepts/`. Se `docs/agents/domain.md`.
