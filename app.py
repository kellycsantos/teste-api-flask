from flask import Flask, json, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Ola usuarios"


@app.route("/dados")
def getDados():
    with open('dados.json', 'r') as json_file:
        dadosSolar = json.load(json_file)
    return dadosSolar
