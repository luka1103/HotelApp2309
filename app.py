from flask import Flask
from flask_cors import CORS, cross_origin
import felixprobeersels
import lukaprobeersels
import jeroenprobeer
import zaidtest
import searchRestaurants
import marktKaart
from flask import render_template,jsonify, request

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

@app.route("/marktenkaart")
@cross_origin()
def methodemarktkaart():
    marktKaart.marktKaart()
    return render_template('markten_kaart.html')

@app.route("/jeroen/<mijngegeven>")
@cross_origin()
def methodejeroen(mijngegeven):
    return jeroenprobeer.jeroenfunctie(mijngegeven)

@app.route("/jeroen2/<invoer>")
@cross_origin()
def methodejeroen2(invoer):
    return searchRestaurants.search_csv_for_keywords(invoer)

@app.route("/Zaid2")
@cross_origin()
def functiezaid2():
    return zaidtest.functiezaid2()

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

@app.route("/ZoekLocatieMusea/<invoer>")
@cross_origin()
def zoek_locatie_in_CSV(invoer):
    return zaidtest.functie_zoek_locatie_in_CSV(invoer)
