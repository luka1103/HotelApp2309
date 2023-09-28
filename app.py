from flask import Flask
from flask_cors import CORS, cross_origin
import felixprobeersels
import lukaprobeersels
import jeroenprobeer
import zaidtest
import searchRestaurants

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

@app.route("/jeroen/<mijngegeven>")
@cross_origin()
def methodejeroen(mijngegeven):
    return jeroenprobeer.jeroenfunctie(mijngegeven)

@app.route("/zaid")
@cross_origin()
def methodezaid():
    return zaidtest.functiezaid()

@app.route("/jeroen2/<mijngegeven>")
@cross_origin()
def methodejeroen2(mijngegeven):
    return searchRestaurants.search_csv_for_keywords(mijngegeven)