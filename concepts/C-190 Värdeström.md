---
id: C-190
term: Värdeström
terms:
  - term: Värdeström
    language: sv
    status: preferred
    source: concept new
definition: uppsättning steg som vart och ett tillför en del av det värde ett värdeerbjudande utlovar
kind: element-type
associative:
  - concept: '[[C-069 Verksamhetsförmåga]]'
    label: använder
  - concept: '[[C-148 Värdeerbjudande]]'
    label: realiserar
---
# C-190 Värdeström

**Definition:** uppsättning steg som vart och ett tillför en del av det värde ett värdeerbjudande utlovar

## Anmärkning

Elementtyp i strategiperspektivet ([[C-108 Strategiperspektiv]]), bredvid verksamhetsförmågan och initiativet. Värdeströmmen säger vilket värde som byggs upp på vägen till ett värdeerbjudande ([[C-148 Värdeerbjudande]]), inte vem som gör vad: den är ingen process. Ett steg är också en värdeström, och helheten består av ([[C-062 består av]]) sina steg. Stegens ordning bär ingen betydelse som en process ordning gör; vårdens utredning, behandling och förebyggande kommer i den ordning fallet kräver.

Varje steg använder ([[C-095 använder]]) de verksamhetsförmågor ([[C-069 Verksamhetsförmåga]]) det förutsätter. Steget realiseras av ([[C-094 realiseras av]]) en verksamhetsprocess ([[C-130 Verksamhetsprocess]]) eller verksamhetsaktivitet, och värdeerbjudandet realiseras av värdeströmmen.

Värdeströmmen är inget styrobjekt ([[C-003 Styrobjekt]]), men någon ansvarar för den ([[C-209 Ansvar]]). Det är ägaren till lösningen ([[C-055 Lösning]]) som erbjuder produkten bakom värdeerbjudandet. Ägaren ansvarar för värdeerbjudandet, dess värden ([[C-195 Värde]]) och hela värdeströmmen. Den som äger en lösning med ett steg svarar inför den ägaren, mot krav ([[C-021 Krav]]) och överenskommelse ([[C-084 Överenskommelse]]). Chefen för Bidragsenheten ansvarar för Att få stöd. Anta att utbetalningen ligger i en egen lösning hos ekonomichefen. En förening som har väntat sex veckor på pengarna vänder sig ändå till chefen för Bidragsenheten, och ekonomichefen svarar inför hen. Kan de två inte enas avgör den närmaste som håller båda, här generaldirektören. Ansvaret följer av vilken lösning som erbjuder produkten, och ingen ritar det i lagret.

Värdeströmmen visar var det skaver, och förmågan vad som ska åtgärdas. Anta att Att få stöd tar fem månader mot utlovade fyra, och att steget få utbetalning står för sex veckor. Steget använder förmågan Utbetalning och återkrav. Den som ansvarar för förmågan ser då vilket mål som ska höjas. [[0066-formagan-och-vardestrommen-ar-inga-styrobjekt-men-nagon-ansvarar-for-dem-loftet-ar-ett-varde-och-vardestrommen-visar-vilken-formaga-som-ska-bli-battre|Beslut 66]].

## Motsvarigheter

Motsvarar ValueStream och ValueStreamStage i Business Architecture Core Metamodel (BACM) och ArchiMates Value Stream. [[0027-vardestrom-ar-en-elementtyp-i-strategiperspektivet-utfallet-ar-tillstandet-losningen-ar-formagans-implementation-och-bacm-tas-in-med-hinder-vinst-och-svar-som-begrepp-i-texten|Beslut 27]].

Value Delivery Modeling Language (VDML) har ingen egen klass för värdeströmmen: aktivitetsnätverket med sina ValueAdds är den. Varje steg realiserar ([[C-094 realiseras av]]) de värden ([[C-195 Värde]]) det tillför, så att värdeströmskartan visar värdet vid steget. [[0028-varde-ar-en-elementtyp-i-strategiperspektivet-dit-vardeerbjudandet-flyttar-arbetssatt-ar-ett-begrepp-svaret-heter-hjalp-och-vdml-tas-in-med-rakneverket-omappat|Beslut 28]].

## Exempel

ett bostadsbolags Att få en bostad: söka, få erbjudande, teckna avtal, flytta in; en myndighets Att få stöd: ansöka, få beslut, få utbetalning.
