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

@app.route("/felix")
@cross_origin()
def methodefelix():
    return felixprobeersels.functiefelix()

@app.route("/luka")
@cross_origin()
def methodeluka():
    return lukaprobeersels.functieluka()

@app.route("/jeroen")
@cross_origin()
def methodejeroen():
    return jeroenprobeer.jeroenfunctie()

@app.route("/zaid")
@cross_origin()
def methodezaid():
    return zaidtest.functiezaid()

