# Akademiet Kantine

Dette er en skoleoppgave der jeg har laget en nettside for kantina på skolen.
Nettsiden er laget med Flask, HTML og CSS.

Nettsiden inneholder:
- Hjem
- Meny
- Varer
- Kontakt

Slik starter du nettsiden (Mac):
1. python3 -m venv .venv
2. source .venv/bin/activate
3. pip install Flask
4. python app.py

Når den kjører kan du åpne nettsiden i nettleseren:
http://127.0.0.1:5000/

---

# Mappeoversikt

app.py (Flask-kode)
templates/ (HTML-sider)
static/ (CSS og bilder)

---

# Hva jeg har lært

- Lage flere nettsider med Flask
- Sende data (lister/variabler) fra Python til HTML med render_template
- Bruke CSS for å style nettsiden


# Krav som er oppfylt
- Riktig mappestruktur (app.py, templates/, static/)
- Fire ruter: /, /meny, /varer, /kontakt
- Jinja: løkke + if i meny.html
- Innhold på alle sider (hjem, meny, varer, kontakt)
- CSS og felles base.html
- README med hvordan kjøre



# Kilder
- Bilder: brukt fra safari 
- Hjelp/feilsøking: ChatGPT (prompting forenkling), Flask-dokumentasjon

# Brukertesting 
- 1 medelev testet i Chrome på Mac.
- Tilbakemelding: ønsket tydeligere mellomrom mellom elementene på meny-siden.
- Endring gjort: la inn ekstra margin i CSS og større bildekanter.



# Sikkerhet

-	Nettsiden samler ikke inn data fra brukere, så det er ingen risiko for at noe personlig kommer på avveie.
-	Nettsiden kjører kun på min egen PC (lokalt) og er ikke tilgjengelig for andre på internett.
-	Alle filer som brukes ligger trygt i prosjektet (ingen eksterne skript eller farlige kilder).