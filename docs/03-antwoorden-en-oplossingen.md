# Antwoorden en oplossingen — ALLEEN FACILITATOR

**Niet aan deelnemers tonen vóór het spel.** De letterfragmentkaarten staan onderaan.

---

## Kamer 1 — De Manifestkaart (controlewoord)

| # | Aanval | STRIDE | Waarom |
|---|---|---|---|
| 1 | Inloggen als CFO via gestolen, onversleutelde sessie | **S — Spoofing** | Hij doet zich voor als iemand anders |
| 2 | IBAN aanpassen in de salarisbatch onderweg | **T — Tampering** | Gegevens onderweg gewijzigd |
| 3 | Goedkeuring ontkennen, want nergens gelogd | **R — Repudiation** | Geen audit trail |
| 4 | Salarisrapport van 4.000 medewerkers inzien als gewone werknemer | **I — Information disclosure** | Data lekt binnen de eigen rol |
| 5 | 50.000 inlogpogingen per minuut | **D — Denial of service** | App onbruikbaar gemaakt |
| 6 | Zichzelf manager-rechten geven in het goedkeuringsscherm | **E — Elevation of privilege** | Rechten verhoogd |

**Controlewoord in volgorde 1 t/m 6: S-T-R-I-D-E → STRIDE.** De letters vallen samen met de volgorde van het model zelf — dat mag je in de debrief als knipoog gebruiken: *"hij schreef jullie letterlijk het model voor."*

**Extra vraag:** bij aanval 4 (Information disclosure) had een threat model de meeste impact gehad: één access-rule in het model hàd het lek al gedicht, terwijl de code "goed" was. Ook 3 en 6 zijn pure model-features (logging, rechtencontrole), geen code-kwaliteit.

### Hints (als het team vastloopt)
- Hint 1: "Lees per zin wát er misgaat, niet hóe. Wie doet zich voor? Wat wordt veranderd? Wat kan niemand bewijzen?"
- Hint 2: "Aanval 2 gebeurt *onderweg*. Aanval 5 gebeurt niet op data — maar op beschikbaarheid."

---

## Kamer 2 — De Domeinmodel-kluis

| # | Oordeel | Uitleg |
|---|---|---|
| A | **J** | Juist: create + read/write op eigen aanvragen, begrensd op status Concept. Least privilege, precies zo bedoeld. |
| B | **F** | Salarisgegevens zijn het meest gevoelige bezit van de app. Alleen Salarisbeheer leest die; een Werknemer hooguit zijn eigen. |
| C | **J** | Juist: XPath-constraint op eigen team + beperkte schrijfrechten (alleen Status). |
| D | **F** | Anoniem + salarisrapport = het hele internet leest je rapport. Anoniem krijgt hooguit publieke, bewust gedeelde data. |
| E | **F** | Delete-rechten voor alle eindgebruikers is bijna nooit nodig. Verwijderen hoort bij een beheer-/onderhoudsrol of een expliciete bevestigde actie. |
| F | **J** | Juist: attribute-level access rules. Zelfs als je een entity mag lezen, zie je alleen de velden die je mag zien. |
| G | **J** | Juist: schrijven op salarisgegevens alleen via een gecontroleerde flow met dubbele verificatie. |
| H | **F** | Non-persistent entities hebben óók access rules nodig: ze worden naar de browser gestuurd en zijn net zo leesbaar. Geen rechten instellen = standaard te ruim voor wie ze mag gebruiken. |

**Aantal fout ingesteld: 4** (B, D, E, H). Kluiscombinatie: "er zijn er 4".

**Extra vraag (bewering A):** de XPath-constraint is bijvoorbeeld:

```
[aangevraagdDoor = '[%CurrentUser%]']
```

 eventueel uitgebreid met de statusbegrenzing in de access rule zelf (`and Status = 'Concept'`) — of met een aparte regel per status. Kernpunt voor de debrief: **constraints zitten in de access rule, niet in de pagina.** Een pagina kan je niet vertrouwen op het verbergen van data.

### Hints
- Hint 1: "Er zitten meer fouten in dan je denkt. Vraag per bewering: wie móét dit kunnen — en wie níet?"
- Hint 2: "Non-persistent betekent niet 'onzichtbaar voor de client'."

---

## Kamer 3 — De Anonieme Deur

| # | Oordeel | Uitleg |
|---|---|---|
| 1 | **OK** | Inlogpagina anoniem: noodzakelijk. |
| 2 | **OK** | Publieke aanmelding voor een evenement: precies waar anoniem voor bestaat. |
| 3 | **DEUR** | Create mag misschien, maar read op álle aanmeldingen betekent dat de hele wereld de naam en het telefoonnummer van elke aangemelde collega kan ophalen. Leesrechten voor anoniem zijn vrijwel altijd fout. |
| 4 | **DEUR** | "Even oké geklikt" in het security-venster: een microflow mét persoonlijke verlofdata is anoniem bereikbaar. Klassiek voorbeeld van een security-instelling die per ongeluk wordt aangepast. |
| 5 | **DEUR** | Read op Verlofaanvraag voor anoniem, "omdat de pagina anders niet werkte": het symptoom werd weggepakt in plaats van de oorzaak (de juiste rol op de pagina/microflow zetten). |
| 6 | **DEUR** | Een anonieme zoekflow die BSN en salaris teruggeeft. Dit is letterlijk wat De Kraai in Kamer 1 (aanval 4) oogstte. |

**Deurcode: 3-4-5-6.**

**Extra vragen:**
- Object 6 is een open adresboek: zonder inloggen haalt De Kraai BSN en salaris van elke medewerker op. Een anonieme flow die personeelsgegevens teruggeeft hoort niet te bestaan — de zoekfunctie hoort achter login, met een rol die er iets mee mag.
- Object 5 intrekken betekent: de access rule voor Anoniem op Verlofaanvraag verwijderen én controleren wie de aanroepende pagina/microflow echt nodig heeft — daarna de pagina her-inrichten voor de juiste rollen. Les: het security-venster werkt niet "omdat het moet"; het is de kluisdeur zelf.
- Bonuspunt voor teams die dit zelf noemen: generieke "bestaat niet"-meldingen (bij wachtwoord-reset of zoeken) voorkomen dat De Kraai het platform gebruikt als adresboek (account-enumeration).

### Hints
- Hint 1: "Elke ✅ heeft een eigenaar met een reden. Wie is de reden bij 3, 4, 5 en 6?"
- Hint 2: "Wat zou De Kraai typen in het zoekveld van object 6?"

---

## Kamer 4 — De Nanoflow-val

| Versie | Oordeel | Waarom |
|---|---|---|
| A | **KRAAI-VOER** | Nanoflows draaien in de browser. De rolcheck gebeurt in de client en de commit ook. De Kraai opent de app met zijn eigen tooling, slaat de check over en roept de commit rechtstreeks aan — of hij past de nanoflow-runtime aan. De toast-melding voor "geen manager" is decoratie. |
| B | **VEILIG** | Serverzijdige rolcheck + XPath-constraint die de aanvraag aan het eigen team koppelt. De client kan niets omzeilen: elke stap gebeurt in de runtime. |
| C | **KRAAI-VOER** | De aanvraag wordt opgehaald op ID **zonder** ownership/team-constraint. De Kraai gokt of doorloopt IDs (aanval 4 uit Kamer 1) en keurt andermans — of zijn eigen — aanvraag goed. Dit is IDOR: Insecure Direct Object Reference. |
| D | **KRAAI-VOER** | Knop-visibility is UI, geen security. Zichtbaarheid voor de rol Manager staat los van wat de nanoflow accepteert: de commit is zonder enige servercontrole aanroepbaar. |

**Aantal sluitgaten: 3** (A, C, D). Alleen versie B overleeft De Kraai.

**Extra vragen:**
- Bij A en D zit de controle in de browser; de browser behoort aan De Kraai. Een rolcheck in een nanoflow is een UX-melding, geen beveiliging.
- Versie C = aanval 4 uit Kamer 1 = **IDOR**. De remedie is in Mendix: retrieve met een XPath-constraint op `[aangevraagdDoor/beoordeeldDoor...]` ten opzichte van de `[%CurrentUser%]` (of de rolcontrole serverzijdig vóór de mutatie), nooit vertrouwen op het ID dat de client meestuurt.

### Hints
- Hint 1: "Welke van deze vier blijft veilig als de gebruiker geen browser gebruikt, maar Postman?"
- Hint 2: "Versie C haalt iets op dat niet van hem is. Hoe heet dat?" (verwijzing naar Kamer 1, aanval 4)

---

## Kamer 5 — De Serverkamer

**Alle acht post-its zijn echte bevindingen.** De sortering die de beveiligingsdienst hanteert:

| Bak | Post-its | Reden |
|---|---|---|
| **BLIKSEM** (app-fix vóór GA) | 1, 2, 3, 4, 5, 6, 7 | Dit zijn configureerbare of codeerbare gaten in de app zelf: security level (1), secrets (2), server-side validatie (3), "Ignore security" (4), audit trail (5), demo-accounts (6), logging op de export (7). Elk item is een deur die De Kraai vannacht opnieuw kan gebruiken. |
| **FOUW-DIEFSTAL** (structureel) | 8 | Threat modeling is geen code-fix maar een werkwijze. Het is óók de enige post-it die álle andere post-its had kunnen voorkomen. |

**Aantal bloedende wonden (BLIKSEM): 7.**

**Extra vraag (mini-threat model voor de salarisexport):** voorbeeld van een goed antwoord — het team hoeft er maar twee te benoemen:

- **T — Tampering:** iemand knutselt met de export onderweg → versleutel het transport, controleer de integriteit (checksum/ondertekening), en log de batch-inhoud.
- **I — Information disclosure:** het exportbestand belandt bij de verkeerde partij → versleutel opslag, beperk de bestemmeling (constante in de omgeving, niet in git), en log wie wat wanneer ophaalt.
- **R — Repudiation:** niemand kan bewijzen dat de export liep → schrijf elke run met inhoudsomschrijving en initiatiefnemer weg in een log-entity.
- **E — Elevation of privilege:** alleen een beheerrol mag de export triggeren; de scheduled event draait onder een aparte, minimale technische gebruiker.

### Hints
- Hint 1: "Niet één post-it is onschuldig. De vraag is alléén: code-fix of werkwijze?"
- Hint 2: "Welke post-it had de andere zeven kunnen voorkomen?"

---

## De finale

De zes fragmenten op positie geven: **V-E-I-L-I-G**. Wachtwoord van de Emergency Console: **VEILIG**.

Het spreekwoord dat bij de onthulling past (laat de facilitator voorlezen): *"Veiligheid in Mendix is geen feature die je ooit toevoegt. Het is de manier waarop je elke feature bouwt. De Kraai heeft niet Mendix gebroken — hij heeft de plekken gepakt waar niemand even had nagedacht."*

---

## De letterfragmentkaarten (print, knip, per enveloppe)

> Enveloppe 1 → **V** — *positie 1* — "De eerste letter, van de eerste fout: jullie dachten nooit na over wat er mis kán gaan."
> Enveloppe 2 → **E** — *positie 2* — "Van het domeinmodel: de kluis zat open omdat niemand de deur had dichtgezet."
> Enveloppe 3 → **I** — *positie 3* — "Van de anonieme deur: wat iedereen mag, mag De Kraai."
> Enveloppe 4 → **L** — *positie 4* — "Van de browser: wat daar gebeurt, gehoorzaamt mij, niet jou."
> Enveloppe 5 → **I** — *positie 5* — "Van de serverkamer: zeven bloedende wonden, en ze waren allemaal voorkombaar."
> Enveloppe 6 → **G** — *positie 6* — "De laatste letter staat voor wat jullie nu wél zijn: gewaarschuwd. Gefeliciteerd, incidentteam."

**Let op:** enveloppe 5 en 6 komen samen uit Kamer 5 (één per correct gesorteerde bak) — of deel enveloppe 6 pas uit na de extra mini-threat model-opdracht.
