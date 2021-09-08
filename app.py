from flask import Flask, request, jsonify
from flask_cors import CORS

from src.Analizador.grammar import parse
from src.Entorno.Ambito import *
from src.Errores.TablaErrores import  *

app = Flask(__name__)
CORS(app)

@app.route("/compilar", methods=['POST'])
def index():
    texto = request.json['entrada']
    resCompilado = parse(texto)
    return jsonify(resCompilado)

@app.route("/")
def pruebas():
    f = open("src/Analizador/entrada.txt", "r")
    texto = f.read()
    return jsonify(parse(texto)['tablaSimbolos'])

if __name__ == '__main__':
    app.run(port=5000)