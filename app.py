from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/meny")
def meny():
    ukens_meny = [
        "Pizza pepperoni (45kr)",
        "Taco mild salsa (50kr)",
        "Pasta kremet saus (60kr)",
        "Kylling ris og salat (70kr) ",
        "Pizza ost og skinke (30kr)",
    ]
    return render_template("meny.html", ukens_meny=ukens_meny)

@app.route("/varer")
def varer():
    varer = ["Bagett (45 kr)", "Kaffe (20 kr)", "Smoothie (35 kr)", "Salat (50 kr)"]
    return render_template("varer.html", varer=varer)

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

if __name__ == "__main__":
    app.run(debug=True)