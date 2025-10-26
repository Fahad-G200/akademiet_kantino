from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/meny")
def meny():
    # Enkelt: liste med tekstlinjer som har dag + rett + kort beskrivelse
    ukens_meny = [
        "Mandag: Pizza – sprø bunn",
        "Tirsdag: Taco – mild salsa",
        "Onsdag: Pasta – kremet saus",
        "Torsdag: Kylling – ris og salat",
        "Fredag: Pizza – ost og skinke",
    ]
    return render_template("meny.html", ukens_meny=ukens_meny)

@app.route("/varer")
def varer():
    # Enkel liste: navn, pris og bildenavn
    varer = [
        {"navn": "Bagett",   "pris": 45, "bilde": "Bagett.jpeg"},
        {"navn": "Kaffe",    "pris": 20, "bilde": "Kaffe.jpeg"},
        {"navn": "Smoothie", "pris": 35, "bilde": "Smoothie.jpeg"},
        {"navn": "Salat",    "pris": 50, "bilde": "Salat.jpeg"},
    ]
    return render_template("varer.html", varer=varer)

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

if __name__ == "__main__":
    app.run(debug=True)