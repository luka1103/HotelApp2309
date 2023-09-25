from flask import Flask
from flask_cors import CORS, cross_origin
import felixprobeersels
import lukaprobeersels
import jeroenprobeer
import zaidtest

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

@app.route("/luka")
@cross_origin()
def methodeluka():
    return lukaprobeersels.functieluka()

@app.route("/jeroen/<mijngegeven>")
@cross_origin()
def methodejeroen(mijngegeven):
    return jeroenprobeer.jeroenfunctie(mijngegeven)

@app.route("/zaid")
@cross_origin()
def methodezaid():
    return zaidtest.functiezaid()

