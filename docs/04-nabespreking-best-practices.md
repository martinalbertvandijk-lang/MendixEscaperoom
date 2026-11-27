# Nabespreking — van puzzel naar jullie eigen Mendix-app

De winst van dit spel zit in deze 10–15 minuten. Loop de zes fouten langs en stel bij elk de vraag: **"Zit dit in onze app?"** Laat het team zelf antwoorden — stilte is informatie.

## Kamer 1 → Threat modeling met STRIDE

**Wat het spel liet zien:** zes aanvallen, zes categorieën, één model. Een threat model is niets meer dan even serieus nadenken over *wat er mis kan gaan* vóórdat je bouwt.

**Vertaal naar de praktijk:**

- Neem STRIDE op in je refinement: bij elke story de vraag *"welke van de zes categorieën raakt deze feature?"* Vijf minuten per story is genoeg om de grote risico's te vangen.
- Teken de dataflow: gebruiker → browser (nanoflows) → runtime (microflows) → database → externe systemen. Bedreigingen ontstaan op de pijlen, niet in de hokjes.
- Mendix publiceert zelf een [security model en threat-model-aanpak voor de platformcomponenten](https://docs.mendix.com/releasenotes/security/) — gebruik dat als basis in plaats van het wiel opnieuw uit te vinden.
- Pak het aanvalsscenario van De Kraai als test: per feature de vraag *"als ik hier de client negeer, wat kan ik dan direct aanroepen?"*

## Kamer 2 → Entity access & XPath-constraints

**Wat het spel liet zien:** vier van de acht instellingen waren verkeerd, en drie van die vier lekten data. Access rights zijn niet "instellen als het werkt", maar het hart van je securitymodel.

**Vertaal naar de praktijk:**

- Zet het security level van elk project op **Production** vóór de eerste release, en werk daaronder. Prototype/demo-level schakelt je hele access model uit.
- Geef per module-role het minimum: create/read/write/delete per entity, begrensd met **XPath-constraints op `[%CurrentUser%]`** (bijv. `[aangevraagdDoor = '[%CurrentUser%]']`) of op teams/afdelingen via associations.
- Gebruik **attribute-level access rules** voor gevoelige velden (salaris, BSN, manager-opmerkingen): wie de entity mag lezen, ziet nog niet automatisch elk veld.
- **Delete-rechten** geven aan eindgebruikers is bijna nooit de juiste oplossing — gebruik statussen (Concept/Ingediend) in plaats van verwijderen.
- Vergeet **non-persistent entities niet**: ze eindigen net zo goed in de browser van de gebruiker en hebben dezelfde access rules nodig.
- Bekijk de [Mendix-documentatie over access rights](https://docs.mendix.com/refguide/security/) en loop bij elke release de access rules van gewijzigde entities na.

## Kamer 3 → Anonieme toegang & rolhygiëne

**Wat het spel liet zien:** één klikje te veel in het security-venster ("even oké geklikt") en het hele internet staat in je verlofadmin. Anoniem is de deur die het vaakst openstaat.

**Vertaal naar de praktijk:**

- Behandel de rol **Anoniem** als "de hele wereld": alles wat deze rol kan, kan De Kraai. Beperk het tot wat bewust publiek is (inloggen, publieke aanmelding).
- Accepteer nooit "de pagina werkt anders niet" als reden om rechten te verbreden: repareer dan de oorzaak (de juiste rol op de pagina of microflow), niet het symptoom.
- Controleer bij elke release de objecten die anoniem bereikbaar zijn, inclusief de **keten**: een microflow die een anonieme pagina aanroept erft mee.
- Geef nooit het bestaan of niet-bestaan van een account prijs ("dat e-mailadres bestaat niet" = een adresboek voor De Kraai). Antwoord generiek.
- Controleer of de anonymous user voldoende beperkte rechten heeft en of sessies van anonieme gebruikers tijdig verlopen.

## Kamer 4 → Vertrouw nooit de client (microflow vs. nanoflow)

**Wat het spel liet zien:** alleen versie B overleefde. Alles wat in de browser gebeurt — nanoflows, knop-visibility, client-side validatie — hoort bij de vijand.

**Vertaal naar de praktijk:**

- **Nanoflows zijn UX, geen security.** Rolchecks en autorisaties die ertoe doen, horen in een microflow (serverzijdig) of in de entity access rules — nooit alléén in een nanoflow.
- **Knop-visibility is geen beveiliging.** Verberg knoppen gerust voor de gebruikerservaring, maar de autorisatiecontrole staat serverzijdig.
- **Never trust the ID:** accepteer geen `VerlofaanvraagID` vanuit de client en haal die op zonder constraint. Retrieve altijd met een XPath-constraint die ownership of team afdwingt — dat voorkomt IDOR.
- Validatie die ertoe doet (bedragen, statussen, rekenkundige regels) hoort serverzijdig, bij voorkeur in de commit-flow of een validatie-microflow; client-side validatie is gebruiksgemak.

## Kamer 5 → De productie-checklist

**Wat het spel liet zien:** zeven bloedende wonden en één gewoonte die ze alle zeven had kunnen voorkomen.

**Vertaal naar de praktijk — gebruik dit als GA-checklist:**

| # | Check | Praktisch in Mendix |
|---|---|---|
| 1 | Security level op **Production** | Project → Security → Production; test met deze levelinstelling, niet met demo-level |
| 2 | Geen secrets in het model | API-keys/sleutels horen in de omgevingsconfiguratie of een secrets-manager, niet in een constante in git |
| 3 | Server-side validatie | Commit-flows valideren onafhankelijk van de UI |
| 4 | Geen "Ignore security" | Zoek vóór release alle microflows zonder securitycontrole op en verwijder de uitzonderingen |
| 5 | Audit trail | Log securityrelevante acties (goedkeuringen, salariswijzigingen, exports) in een log-entity: wie, wat, wanneer |
| 6 | Geen demo-accounts in productie | MxAdmin/demo en testgebruikers horen niet in de productieomgeving |
| 7 | Logging op externe koppelingen en scheduled events | Elke export/batch loggen: inhoudsomschrijving, bestemmeling, initiatiefnemer |
| 8 | Threat modeling als gewoonte | STRIDE-vraag in de refinement van elke feature |

## Slotvraag voor het team

> *"De Kraai zei: alles wat hij gebruikte, hadden wij zelf opengezet. Welke deur zetten wij volgende week dicht?"*

Zet de antwoorden direct in de backlog. Eén concrete fix per deelnemer is meer waard dan de hele bespreking.
