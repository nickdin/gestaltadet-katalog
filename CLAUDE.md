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

## Frågor in, ändringar hans

Katalogen är hur Nicklas ser på saker. Frågor, invändningar och förslag från läsare är välkomna som ärenden och besvaras; en ändring i en definition gör Nicklas, eller Claude på hans ord. Arbete på programmet, en funktion, ett fel, ett kommando som beter sig fel, hör till interlinguas tracker, `nickdin/interlingua`, även när det upptäcks här.

## Kontroll

`~/Devbox/interlingua/.venv/bin/interlingua check .` kontrollerar lagret och ska sluta `no violations`.

## Synk

Git, remote `nickdin/gestaltadet-katalog`. Commit och push utan att fråga; `main` är enda grenen tills Nicklas säger annat.

## Agent skills

### Issue tracker

Ärendena bor i GitHub Issues i `nickdin/gestaltadet-katalog`, publikt, bara katalogens arbete; programmets går till `nickdin/interlingua`. Tavlan är https://github.com/users/nickdin/projects/22. Se `docs/agents/issue-tracker.md`.

### Triage labels

Två etiketter per öppet ärende: en typ (`bug`, `enhancement`, `question`) och en status (de fem standardrollerna plus `parked`), samt ämnesetiketten `needs-grilling`. Se `docs/agents/triage-labels.md`.

### Domain docs

Single-context: en `CONTEXT.md` i roten, ordlistan, och en `docs/adr/` i roten; begreppen definieras bara i `concepts/`. Se `docs/agents/domain.md`.
