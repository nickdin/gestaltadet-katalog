# Grundnivån i klassningen är ett beslut av informationsägaren, aldrig tystnad, och den når objektet genom egen rad eller områdets rad

*Exemplen med Bidragsinformation gäller i dag Utbetalningsinformation, där Utbetalning och Återkrav ligger. Regeln står oförändrad (beslut 71).*

Beslutat av Nicklas 18 november 2026, när beslut 58 hade lämnat frågan om en baslinje för klassningen till ett eget ärende.

## Sammanhang

Granskningar visar att klassning ofta inte görs fullt ut och att olika personer klassar olika. Flera metoder låter därför en gemensam nivå gälla för det mesta och analyserar bara det som avviker. Ärendet #180 frågade om katalogen ska beskriva en sådan ordning, där bara det som avviker klassas.

Beslut 58 flyttade klassen ut ur lagret. Klassen står i organisationens klassningsförteckning, och förteckningen pekar på informationsobjektet (`C-060`) på kartan. Om en organisation har en gemensam nivå hör därför till hennes egen metod. Kvar för katalogen är hur informationsägaren (`C-167`) läser kartan mot en förteckning som har en sådan nivå.

Underlaget `docs/research/informationsklassning-var-klassen-sitter.md` prövade frågan mot fyra källor: BSI-Standard 200-2, den brittiska klassningspolicyn, NIST och det svenska metodstödet. Ingen av dem låter ett objekt som ingen har bedömt få den gemensamma nivån. BSI avgör skyddsbehovet för varje objekt, också de som blir normala. NIST kategoriserar varje system innan skyddet väljs. Metodstödet säger "Att all information ska klassas" och har ett grundskydd bredvid. I källorna är nivån ett skydd för det som någon har bedömt som vanligt.

Grillningen gick två rundor och avgjorde varje fråga på ett fall hos Myndigheten för föreningsstöd. Anta att myndigheten har beslutat att den gemensamma nivån för konfidentialitet är intern.

## Beslut

- **Katalogen varken kräver eller avråder från en grundnivå.** Den säger hur informationsägaren läser kartan mot en klassningsförteckning som har en. Myndigheten för föreningsstöd väljer själv om den vill ha en grundnivå och vilket skydd som hör till den.
- **Ordet är grundnivå.** Grundnivån är den nivå i en klass som organisationen har beslutat ska gälla det mesta. Katalogen säger inte baslinje om klassningen, eftersom TOGAF:s *baseline architecture* är Nulägesarkitektur (`C-057`).
- **Grundnivån är ett beslut, aldrig tystnad.** Informationsägaren säger att grundnivån räcker för objektet. Beslutet kräver ingen analys, men det ska finnas. Analysenheten skapade Riskindikator per förening förra året, och ingen har klassat den. Den har inte grundnivån. Den saknar rad i förteckningen, och det är ett fynd.
- **Organisationen anger en grundnivå per klass.** Informationsägaren säger per klass om grundnivån räcker. Utbetalning är intern och har grundnivån i konfidentialitet. Ett fel i Utbetalning skickar pengar fel, så riktigheten avviker uppåt. Utbetalningar per kommun är öppen och avviker nedåt i konfidentialitet.
- **Grundnivån når objektet på samma väg som varje annan nivå.** Objektet har en egen rad, eller så gäller raden för dess informationsområde (`C-198`). Chefen för Bidragsenheten säger att grundnivån räcker för Bidragsinformation, och Utbetalning får konfidentialiteten därifrån. Organisationen ger ingenting nedåt till ett objekt som saknar rad. Informationsområdet är därför ingen grundnivå. Området är vägen som ett beslut om grundnivån når objekten på.
- **Området skymmer inte det som avviker.** I Bidragsinformation ligger också Återkrav, som visar vilka föreningar som har fått betala tillbaka. Det är känsligare än Utbetalning. Genomgången får därför en följdfråga: vilka objekt har grundnivån genom sitt område, och håller den för vart och ett? Återkrav blir ett fynd som informationsägaren beslutar om.
- **Huvudfrågan i informationssäkerheten får en ny lydelse.** Har informationsägaren tagit ställning till varje objekt på kartan, själv eller genom området, och klarar varje lagringsyta det förteckningen kräver? Det ersätter lydelsen i beslut 58.
- **Katalogen pekar inte ut vem som beslutar grundnivån.** Organisationen beslutar grundnivån, och informationsägaren beslutar om den räcker. Chefen för Register- och tillsynsenheten beslutar att den inte räcker för Företrädare.

## Övervägda alternativ

- **Tystnad betyder grundnivån.** Ett objekt utan rad har då grundnivån. Riskindikator per förening hade varit intern utan att någon hade tittat, och Excelfilen i Analysenhetens grupprum hade inte varit något fynd. Det går inte att skilja det bedömda från det glömda, och ingen läst källa gör så. Avvisat.
- **Varje objekt klassas med full analys**, som förut. Myndigheten hade klassat Ansökan, Beslut och Utbetalning lika noga som Företrädare. Granskningarna visar att en sådan ordning ofta inte blir gjord. Avvisat som enda väg: organisationen får välja en grundnivå.
- **Katalogen rekommenderar en grundnivå.** Valet hör till organisationens metod efter beslut 58. Avvisat.
- **Organisationens grundnivå ärvs nedåt som ett tredje led**, efter objektets egen rad och områdets rad. Det är tystnad med ett annat namn. Avvisat.
- **En enda grundnivå för båda klasserna.** Utbetalning visar att ett objekt kan vara vanligt i konfidentialitet och avvika i riktighet. Avvisat.
- **Ordet baslinje**, som i de engelska källorna. Katalogen hade då haft två betydelser av samma ord. Avvisat.
- **Katalogen pekar ut en roll som beslutar grundnivån.** Det är organisationens egen ordning. Avvisat.

## Konsekvenser

- Ingen definition ändras, och inga begrepp, relationer eller typer tillkommer. Grundnivå är ett ord i texten, inte ett begrepp med id.
- Sidan Informationskartläggning får den nya huvudfrågan och den nya följdfrågan. Anmärkningen i Informationsområde (`C-198`) får en mening om att området bär ett beslut om grundnivån till sina objekt. Texterna skrivs in genom #179, som för in beslut 58.
- Klassningsbeslutet säger varför objektet har nivån och vilken analys som ligger bakom. För ett objekt med grundnivån säger beslutet bara att grundnivån räcker.
- Beslut 58 har fått en not om huvudfrågans lydelse.
- Underlaget sade att klassen bara sitter på undantagen. Raden är rättad efter de fyra källorna.
- Ärendet #180 stängs.
