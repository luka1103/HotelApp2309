from flask import Flask
from flask_cors import CORS, cross_origin
import felixprobeersels
import lukaprobeersels
import jeroenprobeer
import zaidtest
import searchRestaurants
import marktKaart
from flask import render_template

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def helloWorld():
    return "Hello, cross-origin-world!"

@app.route("/felix/<eengegeven>")
@cross_origin()
def methodefelix(eengegeven):
    return felixprobeersels.functiefelix(eengegeven)

@app.route("/luka/<mijngegeven>")
@cross_origin()
def methodeluka(mijngegeven):
    return lukaprobeersels.functieluka(mijngegeven)

marktKaart.marktKaart()
@app.route("/marktenkaart")
@cross_origin()
def methodemarktkaart():
    return render_template('markten_kaart.html')

@app.route("/jeroen/<mijngegeven>")
@cross_origin()
def methodejeroen(mijngegeven):
    return jeroenprobeer.jeroenfunctie(mijngegeven)

@app.route("/jeroen2/<mijngegeven>")
@cross_origin()
def methodejeroen2(mijngegeven):
    return searchRestaurants.search_csv_for_keywords(mijngegeven)

@app.route("/Zaid2/<mijngegeven>")
@cross_origin()
def functiezaid2(mijngegeven):
    return zaidtest.functiezaid2(mijngegeven)

@app.route("/Zaid3/<mijngegeven>")
@cross_origin()
def functiezaid3zoek(mijngegeven):
    return zaidtest.functiezaid3zoek(mijngegeven)

@app.route("/Zaid4/<mijngegeven>")
@cross_origin()
def functiezaid4index(mijngegeven):
    return zaidtest.functiezaid4index(mijngegeven)

@app.route("/Zaid5/<mijngegeven>")
@cross_origin()
def fuctiezaid5zoek_in_csv(mijngegeven):
    return zaidtest.functiezaid4index(mijngegeven)
