from flask import Flask, request, jsonify
from flask_cors import CORS
import sys

from src.Analizador.grammar import *
from src.Analizador.gramOptimizacion import *
from src.Optimizacion.Reportes.ReporteOptimizacion import *

sys.setrecursionlimit(10000000)
app = Flask(__name__)
CORS(app)


@app.route("/compilar", methods=['POST'])
def getSalida():
    texto = request.json['entrada']
    resCompilado = parse(texto)
    return jsonify(resCompilado['textoSalida'])


@app.route("/simbolos", methods=['POST'])
def getSimbolos():
    texto = request.json['entrada']
    resCompilado = parse(texto)
    return jsonify(resCompilado['tablaSimbolos'])


@app.route("/errores", methods=['POST'])
def getErrores():
    texto = request.json['entrada']
    resCompilado = parse(texto)
    return jsonify(resCompilado['tablaErrores'])


@app.route("/cst", methods=['POST'])
def getCst():
    texto = request.json['entrada']
    return jsonify(armarCst(texto))


@app.route("/compilar3d", methods=['POST'])
def compilar3d():
    limpiarReporteOptimizacion()
    texto = request.json['entrada']
    return jsonify(generarCodigo3d(texto))


@app.route("/optimizarMirilla", methods=['POST'])
def optimizarMirilla():
    texto = request.json['entrada']
    optimizador = parseCode3d(texto)
    optimizador.optimizarMirilla()
    return jsonify(optimizador.getCode())


@app.route("/reporteOptimizacion", methods=['POST'])
def reporteOptimizacion():
    return jsonify(getReporteOptimizacionAsSerializable())


@app.route("/")
def pruebas():
    f = open("src/Analizador/entrada.txt", "r")
    texto = f.read()
    return jsonify(parse(texto)['textoSalida'])


if __name__ == '__main__':
    app.run(port=5000)