# Facilitatorhandleiding — Operation VEILIG

Lees dit één keer door en je kunt het spel leiden. Voorbereiding: ± 10 minuten.

## 1. Benodigdheden

- [ ] 1 set geprinte puzzels per team (uit `02-puzzels-deelnemers.md`)
- [ ] 1 antwoordformulier per team (uit `05-antwoordformulier.md`)
- [ ] 6 enveloppes per team met daarin de letterfragmentkaarten (V, E, I, L, I, G — zie `03-antwoorden-en-oplossingen.md`). **Nummer de enveloppes 1 t/m 6** — dat is meteen de positie van de letter.
- [ ] Timer zichtbaar voor de groep (75 minuten)
- [ ] Optioneel: een laptop/tablet met een "Emergency Console" (bijv. een Forms-tool of gewoon een tekstdocument op het scherm) waar het eindwachtwoord in getypt moet worden
- [ ] Optioneel sfeer: donkerder licht, alarmgeluid bij tijdsgebeurtenissen, "De Kraai"-podcaststem of chatberichten die je live verstuurt

## 2. Spelvorm

- **Klassiek (aanbevolen):** 3–6 spelers, 75 minuten, facilitator controleert antwoorden en geeft bij elk goed antwoord de enveloppe van die kamer.
- **Race-modus:** meerdere teams tegelijk, eerste team dat VEILIG intypt wint.
- **Remote:** deel de puzzels als document per kamer (kopieer per kamer een nieuw doc en deel het pas als de vorige kamer is opgelost), gebruik breakout rooms en het chatkanaal als "noodlijn van de beveiligingsdienst".
- **Zelfsturend (zonder facilitator):** print de antwoorden achterop de enveloppes of verstopt in een QR-code per kamer; teams controleren zichzelf.

## 3. Draaiboek

| Tijd | Wat | Wie |
|---|---|---|
| 0:00–0:10 | Sfeer neerzetten, introverhaal voorlezen (uit `01-verhaal-en-spelregels.md`), spelregels + antwoordformulier uitdelen | Facilitator |
| 0:10–0:20 | **Kamer 1 — De Manifestkaart** (threat modeling / STRIDE) | Team |
| 0:20–0:30 | **Kamer 2 — De Domeinmodel-kluis** (entity access) | Team |
| 0:30–0:40 | **Kamer 3 — De Anonieme Deur** (anonieme toegang) | Team |
| 0:40–0:50 | **Kamer 4 — De Nanoflow-val** (client vs. server) | Team |
| 0:50–1:00 | **Kamer 5 — De Serverkamer** (GA-checklist) | Team |
| 1:00–1:05 | **Finale:** wachtwoord VEILIG samenstellen en "intypen" in de Emergency Console | Team |
| 1:05–1:15 | **Nabespreking** per kamer met de vertaalslag naar jullie eigen app (uit `04-nabespreking-best-practices.md`) | Facilitator + team |

Je mag de kamers in willekeurige volgorde uitgeven, maar de bovenstaande volgorde bouwt het beste op: eerst denken (threat model), dan model, dan runtime, dan gedrag, dan proces.

## 4. Spanning opvoeren (optioneel)

Gebruik deze "De Kraai"-berichten op de gezette momenten (voorlezen of chatten):

- **0:20** — *"Leuk hoor, jullie poging. Ik heb ondertussen alvast het salarisrapport van alle 4.000 medewerkers gedownload. Tikt lekker snel."*
- **0:40** — *"Die anonieme deur van jullie? Die liet ik expres open. Kadootje."*
- **1:00** — *"Nog 5 minuten en dan is er van FlowPortaal niets meer over. Kusjes, De Kraai."*

Als een team na 12 minuten in een kamer vastloopt: geef één gratis **hint** (zie de hintsectie per kamer in de antwoorden). Tweede hint kost 2 minuten speeltijd. Dit houdt de druk erin zonder frustratie.

## 5. Rollen van de facilitator

1. **Gamedmaster:** controleert antwoorden (heet in het spel: "de back-up van de beveiligingsdienst"), geeft enveloppes uit.
2. **Stem van De Kraai:** leest de dreigberichten voor — dit maakt of breekt de sfeer. Overdrijf gerust.
3. **Coach in de debrief:** de winst zit in de nabespreking, niet in de puzzel. Reserveer de volle 10 minuten daarvoor.

## 6. Na het spel

- Vraag elk teamlid: *"Welke van de zes fouten zit in ónze app?"* — eerlijk antwoord levert meestal minstens één concrete backlog-item op.
- Zet de uitkomsten direct in de retro/backlog: threat modeling als sprint-ritueel, een access-rights-review per story, en de GA-checklist uit kamer 5 als definitie-of-done-item.
