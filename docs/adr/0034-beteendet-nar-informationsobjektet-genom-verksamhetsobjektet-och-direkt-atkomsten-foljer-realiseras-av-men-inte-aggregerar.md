# Beteendet når informationsobjektet genom verksamhetsobjektet och direkt, och åtkomsten följer realiseras av men inte aggregerar

Beslutat av Nicklas i ärende #23, 2026-11-02, med tillägget från ärende #31 samma dag. Avgränsningen mot representationen gjordes 2026-11-03. Beslutet avgör hur ett verksamhetsbeteende når informationen: i två steg genom verksamhetsobjektet, i ett steg direkt till informationsobjektet, eller på båda sätten.

## Sammanhang

Ingen text sade om ett verksamhetsbeteende fick ha åtkomst direkt till ett informationsobjekt. Verksamhetsobjekt (`C-159`) och Verksamhetsbeteende (`C-157`) sade att beteendet har åtkomst till (`C-101`) verksamhetsobjektet, och att verksamhetsobjektet realiseras av (`C-094`) ett eller flera informationsobjekt (`C-060`). Vägen från process till information gick alltså i två steg (ADR 0016). Behandling (`C-168`) sade något annat: en behandling läses ur beteendet och de informationsobjekt beteendet har åtkomst till. Det är ett steg.

Frågan dök upp när ett upplägg för informationshantering prövades mot katalogen. Informationsägaren (`C-167`) vill se i vilka processer hens informationsobjekt behandlas. Det ritas som en matris med processer mot informationsobjekt, och matrisen måste byggas på det ena steget eller det andra. Med bara två steg går prövningen per behandling genom verksamhetsobjektet. Med bara ett steg har verksamhetsobjektet ingen roll i behandlingen.

Exemplet kommer från Myndigheten för föreningsstöd. Handläggningen Pröva ansökan har åtkomst till verksamhetsobjektet Ärende, som realiseras av informationsobjekten Ansökan och Förening. Är företrädaren ny läser handläggningen också Företrädare i registret. Företrädare aggregerar (`C-100`) Personnummer: en uppgift som klassas eller ägs för sig är ett eget informationsobjekt, och objektet som rymmer den aggregerar den (ADR 0018, ADR 0030). Behandlingen "samla in företrädarens personnummer" gäller Personnummer. Ärende #23 lät först Förening aggregera Personnummer och lät uppslaget gälla Förening. Exemplet här följer i stället exempelorganisationen: den lägger personuppgifterna i Företrädare, och Förening realiserar redan Ärende.

## Beslut

- **Båda relationerna finns.** Processvyn ritar beteendet med åtkomst till verksamhetsobjektet. Informationshanteringsvyn visar beteendet med åtkomst till informationsobjektet. Behandling (`C-168`) läses ur den relationen, ritad eller härledd, med läget läser, skriver eller båda som fältet `access` bär (ADR 0033).
- **Åtkomsten följer realiseras av, ett steg.** Har beteendet åtkomst till ett verksamhetsobjekt som realiseras av ett informationsobjekt, så har beteendet också åtkomst till informationsobjektet. Programmet härleder den åtkomsten; den ritas inte. Pröva ansökan har åtkomst till Ärende, alltså har handläggningen åtkomst till Ansökan och Förening.
- **Direkt ritas bara det som inte följer av regeln.** Det gäller uppslag i ett register (Pröva ansökan läser Företrädare när företrädaren är ny, och Företrädare realiserar inte Ärende), utlämnanden och sammanställningar som beteendet gör (`C-162`). En ritad åtkomst som regeln redan ger är överflödig, och programmet säger till.
- **Åtkomsten följer inte aggregerar (`C-100`).** Åtkomst till Företrädare ger ingen åtkomst till Personnummer, som Företrädare aggregerar. Når beteendet verkligen personnumret ritas den relationen direkt, och då är den inte överflödig. Programmet får peka ut en sådan möjlig åtkomst som en lucka att bekräfta, aldrig som ett fel.
- **Representationen avgörs för sig.** Ett verksamhetsbeteende har åtkomst till den representation (`C-085`) det tar emot, upprättar, kopierar, lämnar ut eller gallrar (ADR 0031). Det här beslutet säger inte om åtkomsten till ett objekt också når objektets representationer. Svaret beror på hur ett objekt kopplas till sina representationer i ett lager, och det har katalogen inte avgjort. Frågan är ärende #35.

## Uppslaget i ArchiMate

Uppslaget gjordes i ärende #31, i ArchiMate 3.1 Specification. Open Groups sidor för version 3.2 kräver inloggning. Så vitt känt är reglerna nedan oförändrade i 3.2, men det är inte kontrollerat mot 3.2-texten.

- **Bilaga B.2.3, DR 4**, en säker härledning ("valid"): finns en strukturell relation p(a,b) och en beroenderelation q(c,b), så får relationen r(c,a) av beroendets typ härledas. Ansökan realiserar Ärende, en strukturell relation i ArchiMates riktning, och Pröva ansökan har åtkomst till Ärende. Alltså har Pröva ansökan åtkomst till Ansökan. Observera riktningen: katalogens realiseras av (`C-094`) går från det förverkligade elementet till förverkligaren, motsatt ArchiMates Realization. Regeln är densamma, men pilen är vänd.
- **Bilaga B.3.2, PDR 5**, en möjlig härledning ("potential"): finns p(a,b) strukturell och q(c,a) beroende, så *kan* r(c,b) härledas. Företrädare aggregerar Personnummer, och Pröva ansökan har åtkomst till Företrädare. Kanske har Pröva ansökan då åtkomst till Personnummer. Bilaga B.3 säger att sådana relationer "might be relevant but may also be wrong" och att modelleraren avgör.
- **Avsnitt 5.2.5**: en åtkomstrelation betyder att någon del av beteendet når någon del av det passiva elementet. Åtkomst till Företrädare säger därför inte vilken uppgift som rörs.
- **Avsnitt 5.2.2**: åtkomst går alltid från ett aktivt element eller ett beteende till ett passivt element. **Avsnitt 5.7**: en härledd relation är giltig och får ritas direkt, utan sina mellanled. **Bilaga B.2.3**, reglerna för åtkomst: åtkomst får bara härledas till ett passivt element. Ett verksamhetsbeteende med åtkomst till ett informationsobjekt, ArchiMates Data Object, är alltså en giltig härledd relation genom DR 4, och den får ritas.

Omvänd riktning är säker: har beteendet åtkomst till Personnummer, så har det åtkomst till Företrädare (DR 4 med aggregeringen som strukturell relation). Katalogen behöver ingen regel för det, eftersom helheten redan ritas.

## Övervägda alternativ

- **Bara genom verksamhetsobjektet**, som ADR 0016 läste. Då går ett uppslag i ett register inte att rita utan att registret först görs till en del av det verksamhetsobjekt som flödar. Informationsägarens matris får heller inget ankare för det beteendet faktiskt rör. Avvisat.
- **Bara direkt till informationsobjektet.** Då förlorar processvyn verksamhetsobjektet, det verksamheten själv talar om, och flödet mellan beteendena går inte längre att härleda ur det (ADR 0033). Avvisat.
- **Båda relationerna ritade för hand, utan härledning.** Varje åtkomst till ett verksamhetsobjekt skulle ritas en gång till, mot varje informationsobjekt som realiserar det. Det är samma sak sagd två gånger, och de två kopiorna kan glida isär. Avvisat.
- **Åtkomsten följer aggregerar**, så att åtkomst till Företrädare ger åtkomst till allt Företrädare aggregerar. ArchiMate kallar den härledningen möjlig, inte säker. Matrisen skulle då visa personnumret i varje beteende som läser företrädarens namn. Avvisat i #31.

## Konsekvenser

- Anmärkningen i Verksamhetsbeteende (`C-157`), Verksamhetsobjekt (`C-159`), Behandling (`C-168`) och har åtkomst till (`C-101`) säger samma sak och hänvisar hit.
- Programmet härleder åtkomsten ett steg genom den relationstyp katalogen markerar `realisation: true`, och `check` rapporterar en ritad åtkomst som härledningen redan ger (interlingua #923, stängt). Katalogens markering på `C-094` är ärende #30; tills den finns härleder programmet ingenting i ett lager som använder katalogen. Luckan för möjlig åtkomst genom aggregering är interlingua #957.
- Ärende #35 avgör om åtkomsten når representationen, och hur ett objekt kopplas till sina representationer.
- Ingen ny elementtyp och inga relationer i katalogen ändras. Mallen körs inte om.
