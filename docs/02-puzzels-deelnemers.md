# Puzzels voor deelnemers — Operation VEILIG

*Deze puzzels worden per kamer uitgedeeld. Teams mogen alles annotated, verscheurd en beschrift worden.*

**Context voor alle kamers:** FlowPortaal is een Mendix-app met deze user roles: **Werknemer**, **Manager**, **HR**, **Salarisbeheer** en **Anoniem**. De app heeft ca. 4.000 gebruikers. De plek waar alles samenkomt is het domeinmodel hieronder — hou dit bij de hand.

## Het domeinmodel van FlowPortaal (alle kamers)

```
Module: Verlof
  Werknemer (persistent)
    - Naam, E-mailadres, InDienstSinds, Team (enum: Finance, IT, Sales, HR)
  Verlofaanvraag (persistent)
    - DatumVan, DatumTot, Reden, Status (enum: Concept, Ingediend, Goedgekeurd, Afgekeurd)
    - OpmerkingManager
    - Association: Verlofaanvraag ──aangevraagdDoor──> Werknemer
    - Association: Verlofaanvraag ──beoordeeldDoor──> Werknemer (de manager)

Module: Beloning
  Salarisgegevens (persistent)
    - BSN, SalarisMaandelijks, IBAN, Banknaam
    - Association: Salarisgegevens ──1──> Werknemer
  SalarisRapport (non-persistent)
    - RapportHTML, AantalMedewerkers, TotaalLoonkost

Module: MijnAccount
  Profiel (persistent, generalisatie van Account)
    - Standaard Mendix Account-attributen + Telefoonnummer
```

---

# KAMER 1 — De Manifestkaart

*Thema: threat modeling. Tijd: 10 minuten.*

De Kraai heeft een manifest in de codebase achtergelaten. Hij beschrijft zes aanvallen — de aanvallen die hij **heeft uitgevoerd of geprobeerd**. Het incidentteam van Noorderlicht heeft nooit een threat model gemaakt voor FlowPortaal. Als ze dat wél hadden gedaan, hadden ze deze zes aanvallen zelf opgeschreven.

De beveiligingsdienst werkt met het standaard **STRIDE**-model:

| Letter | Categorie | Betekenis |
|---|---|---|
| **S** | Spoofing | Iemand doet zich voor als iemand anders |
| **T** | Tampering | Iemand knutselt met gegevens onderweg of in opslag |
| **R** | Repudiation | Iemand kan ontkennen dat hij iets heeft gedaan, want het is nergens gelogd |
| **I** | Information disclosure | Gegevens lekken naar iemand die ze niet mag zien |
| **D** | Denial of service | De app wordt onbruikbaar gemaakt |
| **E** | Elevation of privilege | Iemand krijgt rechten die hij niet zou moeten hebben |

### De zes aanvallen uit het manifest

| # | Uitspraak van De Kraai |
|---|---|
| 1 | *"Ik logde in als de CFO. Ik hoefde zijn wachtwoord niet eens te raden — zijn sessie lag gewoon op internet, onversleuteld, omdat iemand 'HTTPS verplicht' had uitgezet voor 'even testen'."* |
| 2 | *"De salarisbatch die naar de externe salarisprovider ging? Ik heb onderweg het IBAN in mijn eigen rekening veranderd. Niemand merkte het, er was geen controle som op de batch."* |
| 3 | *"Manager De Vries zegt dat hij verlofaanvraag #1042 nooit heeft goedgekeurd. Bewijs het maar eens. Er staat nergens wie wat wanneer deed."* |
| 4 | *"Wist je dat ik als gewone werknemer één URL kon aanpassen en het volledige salarisrapport van alle 4.000 medewerkers binnenkreeg? Heel aardig van de makers."* |
| 5 | *"Vijftigduizend inlogpogingen per minuut, tien minuten lang. Daarna kon niemand meer inloggen. Zelfs jullie HR-directeur niet. Ik heb niet één account gepakt — ik heb gewoon alles platgelegd."* |
| 6 | *"Ik paste in het goedkeuringsscherm één veldje aan en ineens was ik manager van mezelf. Goedgekeurd, door mijzelf, over mijn eigen aanvraag. Mooi systeem, dat jij ook je eigen verlof mag goedkeuren."* |

### Opdracht

1. Wijs elke aanval de juiste STRIDE-categorie toe (elke categorie komt **precies één keer** voor).
2. Schrijf op het antwoordformulier bij elke aanval de letter (S/T/R/I/D/E).
3. Als je klaar bent, vormen de zes letters in de volgorde 1 t/m 6 een woordje. Dit is je **controlewoord** — laat het aan de back-up van de beveiligingsdienst zien.

*Extra vraag voor het antwoordformulier: bij welke van deze zes aanvallen had een threat model het team wél kunnen redden, zelfs als de code al geschreven was?*

---

# KAMER 2 — De Domeinmodel-kluis

*Thema: entity access rights. Tijd: 10 minuten.*

In de kluis van de afdeling zit een uitdraai van de toegangsrechten zoals de vorige developer ze had ingesteld ("het werkte, dus klaar"). De Kraai heeft er acht uitspraken bijgeschreven over wat er volgens hem **mogelijk is in FlowPortaal**. Achter elk van zijn beweringen schuilt óf een fout ingestelde access rule, óf een juiste beslissing die het team goed heeft gedaan.

De beveiligingsdienst herinnert je aan het uitgangspunt: **least privilege** — iedereen krijgt het minimum aan rechten dat nodig is, en `Delete`-rechten krijgen eindgebruikers vrijwel nooit.

### De acht beweringen

| # | Bewering over FlowPortaal |
|---|---|
| A | *"Een gewone Werknemer kan een nieuwe Verlofaanvraag aanmaken, z'n eigen aanvragen lezen en bewerken — maar alleen zolang de status 'Concept' is. Via een XPath-constraint op zijn eigen aanvragen."* |
| B | *"Diezelfde gewone Werknemer kan de Salarisgegevens van álle collega's lezen. Handig voor op de vrijdagmiddag."* |
| C | *"Een Manager kan Verlofaanvragen van zijn eigen team lezen en op status 'Ingediend' goedkeuren of afkeuren. Van teams waar hij niets mee te maken heeft, ziet hij niets."* |
| D | *"De rol Anoniem heeft leesrechten op SalarisRapport, zodat mensen zonder account 'even het aantal medewerkers' kunnen opvragen."* |
| E | *"Alle rollen hebben delete-recht op Verlofaanvraag, zodat niemand ooit tegen een aanvraag aanloopt die hij niet kan weggooien."* |
| F | *"De opmerkingen van de manager in een afgekeurde aanvraag (OpmerkingManager) kunnen alleen door de manager en HR worden gelezen — de gewone Werknemer ziet zijn eigen aanvraag, maar niet dat veld. Atribute-level access rules, mooi geregeld."* |
| G | *"Aan Salarisgegevens mag alleen de rol Salarisbeheer schrijven. Werknemers kunnen hun eigen IBAN niet zomaar wijzigen — dat gaat via een bevestigde microflow met dubbele controle."* |
| H | *"Het SalarisRapport is een non-persistent entity, dus die heeft helemaal geen access rules nodig. Rechten instellen op iets dat niet wordt opgeslagen is zonde van de tijd."* |

### Opdracht

1. Beoordeel elke bewering: **juist ingesteld** of **fout ingesteld** (dit is een securitygevaar).
2. Zet op het antwoordformulier bij elke letter J of F.
3. **Tel hoeveel beweringen fout ingesteld zijn.** Dat aantal is de kluiscombinatie van deze kamer: *"Er zijn er ___"* — laat het aan de back-up zien.

*Extra vraag voor het antwoordformulier: bewering A klopt bijna — welke XPath-constraint hoort er exact bij om te zorgen dat een Werknemer alleen z'n eigen aanvragen ziet?*

---

# KAMER 3 — De Anonieme Deur

*Thema: anonieme toegang. Tijd: 10 minuten.*

Nina's laatste bericht bevatte een netwerkkaart van FlowPortaal zoals de applicatie die nu **echt** bedient — inclusief wat er via de rol **Anoniem** bereikbaar is. De Kraai gebruikt anonieme toegang altijd als eerste: het is de deur die developers vergeten.

De regel van de beveiligingsdienst: **alles wat anoniem bereikbaar is, is bereikbaar voor de hele wereld, inclusief De Kraai.** Anoniem mag alleen wat echt voor iedereen bedoeld is (inlogpagina, aanmeldformulier voor een evenement, publieke info).

### De kaart: wat is er bereikbaar?

| # | Object | Type | Bereikbaar via rol Anoniem? | Toelichting |
|---|---|---|---|---|
| 1 | Pagina `Login` | Pagina | ✅ Ja | Bevat de inlog- en wachtwoordvergeten-flow |
| 2 | Pagina `Event_Aanmelden` | Pagina | ✅ Ja | Publieke aanmelding voor het bedrijfsfeest, schrijft naar `Aanmelding` |
| 3 | Entity `Aanmelding` | Entity access | ✅ Ja, create én read op álle Aanmeldingen | Create moest kunnen, "read erbij kon geen kwaad" — inclusief naam en telefoonnummer van elke aangemelde collega |
| 4 | Microflow `DS_MijnVerlofOverzicht` | Microflow | ✅ Ja | Kwam "per ongeluk" in de rol Anoniem terecht via het security-venster ("even oké geklikt") |
| 5 | Entity `Verlofaanvraag` | Entity access | ✅ Ja, read via de anonieme rol | Stond aan omdat "de pagina anders niet werkte" |
| 6 | Microflow `MF_ZoekMedewerker` | Microflow | ✅ Ja | Anonieme personeelszoeker: zoekt op naam en geeft volledige personeelsgegevens terug, inclusief BSN en salaris — "handig voor de receptie" |

### Opdracht

1. Onderzoek de zes objecten. Welke zijn **terecht** anoniem en welke zijn **onterecht** anoniem bereikbaar (en dus de deuren die De Kraai gebruikte)?
2. Zet op het antwoordformulier per nummer: **OK** of **DEUR**.
3. Noteer de nummers van alle DEUR-objecten op volgorde. Dat is de deurcode van deze kamer.

*Extra vragen voor het antwoordformulier: bij #6 — wat kan De Kraai met deze zoekflow? En wat moet er met object 5 gebeuren zodra de anonieme rol wordt ingetrokken?*

---

# KAMER 4 — De Nanoflow-val

*Thema: de client vertrouwen. Tijd: 10 minuten.*

In de code vindt het team vier versies van de verlofgoedkeuring. Slechts één ervan kan tegen De Kraai. De beveiligingsdienst heeft één wet: **alles wat in de browser gebeurt, kan De Kraai zien en veranderen. Nanoflows draaien in de browser. Vertrouw nooit alleen de client.**

### De vier implementaties

| Versie | Implementatie |
|---|---|
| A | Een **nanoflow** controleert of de ingelogde gebruiker de rol Manager heeft, en zo ja: zet de Verlofaanvraag op status Goedgekeurd en commit hem. Netjes met een toast-melding als je geen manager bent. |
| B | Een **microflow** haalt de Verlofaanvraag op via XPath mét de constraint dat de aanvraag bij een collega uit het eigen team hoort, controleert serverzijdig of de gebruiker de rol Manager heeft, zet de status op Goedgekeurd en commit. Geen van de checks kan worden overgeslagen door de client. |
| C | Een **microflow** krijgt als parameter een `VerlofaanvraagID` (een string) vanuit de client, haalt de aanvraag op **zonder** XPath-constraint op de oorsprong, controleert de rol Manager en commit de goedkeuring. |
| D | Een pagina met een knop "Goedkeuren" die alleen zichtbaar is voor de rol Manager (visibility op de knop gebaseerd op de rollen van de gebruiker). De knop start een nanoflow die de goedkeuring commit. Verder geen enkele controle. |

### Opdracht

1. Beoordeel elke versie: **VEILIG** of **KRAAI-VOER** (onveilig).
2. Zet op het antwoordformulier per versie V of K.
3. **Tel hoeveel versies KRAAI-VOER zijn.** Dat aantal is het "aantal sluitgaten" van deze kamer — laat het aan de back-up zien.

*Extra vragen voor het antwoordformulier: (1) waarom kan De Kraai bij versie A en D de rolcheck en de zichtbaarheid omzeilen? (2) welke aanval uit Kamer 1 lijkt sterk op versie C — en hoe heet deze aanvalsfamilie (afkorting met vier letters)?*

---

# KAMER 5 — De Serverkamer

*Thema: de productie-checklist. Tijd: 10 minuten.*

In de serverkamer hangt een bord met acht post-its — de aantekeningen van Nina na haar snelle audit van 02:07. Elke post-it is een bevinding. De vraag die het team moet beantwoorden is niet "welke zijn fout" — **ze zijn allemaal fout** — maar wél: bij welke hoort een **blokkerende fix vóór GA**, en bij welke een **beveiligingsmaatregel die het team structureel moet inregelen**?

### De acht post-its van Nina

| # | Bevinding |
|---|---|
| 1 | "Security level van het project staat op Prototype/DEMOMODE, 'even zo laten tot na de demo' — dat was 8 maanden geleden." |
| 2 | "De API-key van de salarisprovider staat als constante in het model, in git, met een commentaarregel 'niet committen hoor!'. De sleutel staat er dus in." |
| 3 | "Validatie van het IBAN staat alleen in de UI (client-side). De microflow die opslaat controleert niets." |
| 4 | "Op 2 microflows staat 'Ignore security' aangevinkt. Beide komen via één pagina in de productieflow." |
| 5 | "Er is nergens een audit trail: wie welke aanvraag heeft goedgekeurd, is nergens vastgelegd." |
| 6 | "De demo-gebruikers MxAdmin/demo en hruser/demo bestaan nog in productie." |
| 7 | "Een scheduled event exporteert elke nacht salarisgegevens naar een externe locatie; er is geen logging van wat er verstuurd wordt en er loopt geen enkele rol- of omgevingscontrole op wie de export mag triggeren." |
| 8 | "Er is nooit een threat model gemaakt. Nooit. Voor geen enkele feature." |

### Opdracht

1. Sorteer de post-its in twee bakken:
   - **BLIKSEM** = moet vóór GA gefixed worden, anders kan De Kraai vannacht opnieuw binnenkomen;
   - **FOUW-DIEFSTAL** = structurele verbetering (proces/gewoonte) die geen applicatie-fix is maar het team sterker maakt.
2. Zet op het antwoordformulier per post-it BLIKSEM of FOUW-DIEFSTAL.
3. Noteer hoeveel post-its in de bak BLIKSEM zitten — dat is het aantal "bloedende wonden" van deze kamer.

*Extra vraag voor het antwoordformulier: voor post-it 8 — maak in 3 minuten een mini-threat model voor de salarisexport van post-it 7. Kies 2 STRIDE-categorieën en schrijf bij elke categorie één concrete maatregel in Mendix.*

---

# DE FINALE — De Emergency Console

Alle zes letterfragmenten zijn binnen. Leg ze op volgorde zoals de kaarten aangeven en typ het wachtwoord in de Emergency Console.

> *"Het wachtwoord is wat jullie de hele avond deden zonder het te weten: precies wat De Kraai wilde dat jullie níet zouden doen."*

Tik het woord in. Als de console groen wordt, heeft de back-up van de beveiligingsdienst het systeem hersteld — en krijgt De Kraai te horen dat hij verliest, niet aan een firewall, maar aan een team dat gewoon, saai en grondig zijn werk doet.

*Na de finale: nabespreking met de facilitator.*
