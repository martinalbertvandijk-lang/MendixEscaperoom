# Mendix Escaperoom: **OPERATION VEILIG**

Een escaperoom-achtig bedrijfsspel waarmee Mendix-developers **beleven** waarom security geen bijzaak is. Geen slides, geen quiz — maar een gehackte app, een hacker die achtervolgt, en zes puzzels die je alleen oplost als je écht begrijpt hoe security in Mendix werkt.

> **Het wachtwoord dat alles opent, is pas compleet als je begrijpt wat je fout had gedaan.**

---

## Het verhaal in één alinea

Om 02:13 's nachts krijgt je team een alarm: productie-app **FlowPortaal** van employer Noorderlicht Software is gegijzeld door de hacker **De Kraai**. Hij heeft de data gekopieerd, de app op slot gezet en vijf sporen van zijn aanval achtergelaten. Elk spoor wijst op een echte securityfout in de Mendix-app. Los de sporen op, herstel de fout, verzamel de zes letterfragmenten — en typ het ontsleutelingswachtwoord in de Emergency Console voordat De Kraai de database wist. Tijd: **75 minuten**.

## Voor wie?

- Mendix-developers (junior t/m senior), scrumteams, architects
- 1 team van 3–6 spelers per sessie (meerdere teams parallel kan, met race-element)
- Geen Mendix-omgeving nodig — volledig speelbaar met de geprinte kaarten

## De vijf kamers → zes best practices

| Kamer | Puzzel | Mendix-onderwerp |
|---|---|---|
| 1. De Manifestkaart | Dreigingen categoriseren | **Threat modeling met STRIDE** |
| 2. De Domeinmodel-kluis | Toegangsrechten-matrix goed/fout | **Entity access & XPath-constraints** |
| 3. De Anonieme Deur | Vind de objecten die anoniem openstaan | **Anonieme toegang & rolhygiëne** |
| 4. De Nanoflow-val | Welke implementatie is veilig? | **Nooit de client vertrouwen** (microflow vs. nanoflow) |
| 5. De Serverkamer | Productie-checklist sorteren | **GA-checklist: validatie, secrets, logging, security level** |

## Wat zit er in deze repo?

| Bestand | Voor wie | Inhoud |
|---|---|---|
| [docs/00-facilitator-handleiding.md](docs/00-facilitator-handleiding.md) | Facilitator | Benodigdheden, draaiboek, timing, varianten |
| [docs/01-verhaal-en-spelregels.md](docs/01-verhaal-en-spelregels.md) | Spelers | Introverhaal + regels (voorlezen of delen) |
| [docs/02-puzzels-deelnemers.md](docs/02-puzzels-deelnemers.md) | Spelers | Alle 5 kamers met puzzelmateriaal om te printen |
| [docs/03-antwoorden-en-oplossingen.md](docs/03-antwoorden-en-oplossingen.md) | **Alleen facilitator!** | Alle antwoorden, codes en valkuilen |
| [docs/04-nabespreking-best-practices.md](docs/04-nabespreking-best-practices.md) | Facilitator + team | Debrief per kamer, vertaald naar jullie eigen Mendix-app |
| [docs/05-antwoordformulier.md](docs/05-antwoordformulier.md) | Spelers | Printbaar invulformulier |

## Snelstart voor de facilitator

1. Print de puzzels uit [docs/02-puzzels-deelnemers.md](docs/02-puzzels-deelnemers.md) (1 set per team) en het antwoordformulier uit [docs/05-antwoordformulier.md](docs/05-antwoordformulier.md).
2. Knip de zes **letterfragmentkaarten** (staan bij de antwoorden) en stop ze in enveloppes: één per opgeloste kamer.
3. Lees [docs/00-facilitator-handleiding.md](docs/00-facilitator-handleiding.md) door — 10 minuten voorbereiding is genoeg.
4. Start de klok, lees het verhaal voor, en laat de doodsbang-maar-gemotiveerde squad los op De Kraai. 🐦‍⬛
