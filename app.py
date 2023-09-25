from flask import Flask
from flask_cors import CORS, cross_origin
import felixprobeersels

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