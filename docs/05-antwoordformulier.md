# Antwoordformulier — Operation VEILIG

*Teamnaam: ______________________ Starttijd: ________*

## Kamer 1 — De Manifestkaart

| # | Aanval | STRIDE-letter |
|---|---|---|
| 1 | CFO / sessie | |
| 2 | IBAN onderweg | |
| 3 | Goedkeuring ontkend | |
| 4 | Salarisrapport van iedereen | |
| 5 | 50.000 inlogpogingen | |
| 6 | Zichzelf manager maken | |

**Controlewoord (1 t/m 6):** _ _ _ _ _ _

**Extra vraag:** bij welke aanval had een threat model het meeste verschil gemaakt, en waarom?

---

## Kamer 2 — De Domeinmodel-kluis

| # | Bewering | J / F |
|---|---|---|
| A | Werknemer: eigen aanvraag, alleen Concept | |
| B | Werknemer leest alle salarisgegevens | |
| C | Manager leest/beoordeelt eigen team | |
| D | Anoniem leest SalarisRapport | |
| E | Alle rollen mogen verwijderen | |
| F | OpmerkingManager alleen voor manager/HR | |
| G | Alleen Salarisbeheer schrijft salaris | |
| H | Non-persistent = geen rechten nodig | |

**Kluiscombinatie — "er zijn er ___":** ______

**Extra vraag:** welke XPath-constraint hoort bij bewering A?

---

## Kamer 3 — De Anonieme Deur

| # | Object | OK / DEUR |
|---|---|---|
| 1 | Loginpagina | |
| 2 | Evenement-aanmelding (pagina + create) | |
| 3 | Read op alle Aanmeldingen | |
| 4 | DS_MijnVerlofOverzicht | |
| 5 | Read op Verlofaanvraag | |
| 6 | MF_ZoekMedewerker (BSN + salaris) | |

**Deurcode:** ___ - ___ - ___ - ___

**Extra vragen:** wat is het probleem met "dat e-mailadres bestaat niet"-meldingen? En wat moet er met object 5 gebeuren?

---

## Kamer 4 — De Nanoflow-val

| Versie | Implementatie | V / K |
|---|---|---|
| A | Nanoflow met rolcheck + commit | |
| B | Microflow met XPath + serverrolcheck | |
| C | Microflow met losse ID-parameter | |
| D | Verborgen knop + nanoflow-commit | |

**Aantal sluitgaten:** ______

**Extra vragen:** waarom kunnen A en D worden omzeild? En hoe heet de aanvalsfamilie van versie C (vier letters)?

---

## Kamer 5 — De Serverkamer

| # | Bevinding | BLIKSEM / FOUW-DIEFSTAL |
|---|---|---|
| 1 | Security level Prototype | |
| 2 | API-key in constante | |
| 3 | Alleen client-side validatie | |
| 4 | "Ignore security" op 2 microflows | |
| 5 | Geen audit trail | |
| 6 | Demo-accounts in productie | |
| 7 | Ongecontroleerde nachtelijke export | |
| 8 | Nooit een threat model gemaakt | |

**Aantal bloedende wonden:** ______

**Extra vraag:** mini-threat model voor de nachtelijke export — 2 STRIDE-categorieën, telkens één concrete maatregel:

1.
2.

---

## De finale

Zet de zes letters in de juiste volgorde:

| 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
|   |   |   |   |   |   |

**Wachtwoord Emergency Console:** _ _ _ _ _ _

*Tijd ingevoerd op: ________*
