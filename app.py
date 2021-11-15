# Archivos de calificaciones: https://github.com/ManuelMiranda99/JOLC (los de la segunda fase tienen errores de tipos o comas de mas y asi)
# Proyecto del aux de typescript: https://manuelmiranda99.github.io/OLC2Proyecto2/#BCBCBC

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
    res = {
        'codigo': resCompilado['textoSalida'],
        'simbolos': getTablaSimbolosAsSerializable(),
        'errores': getTablaErroresAsJson(),
    }
    return jsonify(res)


@app.route("/cst", methods=['POST'])
def getCst():
    texto = request.json['entrada']
    return jsonify(armarCst(texto))


@app.route("/compilar3d", methods=['POST'])
def compilar3d():
    limpiarTablaErrores()
    texto = request.json['entrada']
    res = {
        'codigo3d': generarCodigo3d(texto),
        'simbolos': getTablaSimbolosAsSerializable(),
        'errores': getTablaErroresAsJson(),
    }
    return jsonify(res)


@app.route("/optimizarMirilla", methods=['POST'])
def optimizarMirilla():
    limpiarReporteOptimizacion()
    texto = request.json['entrada']
    optimizador = parseCode3d(texto)
    optimizador.optimizarMirilla()
    res = {
        'codigo3d': optimizador.getCode(),
        'optimizaciones': getReporteOptimizacionAsSerializable()
    }
    return jsonify(res)


@app.route("/optimizarBloques", methods=['POST'])
def optimizarBloques():
    limpiarReporteOptimizacion()
    texto = request.json['entrada']
    optimizador = parseCode3d(texto)
    optimizador.optimizar_bloques()
    res = {
        'codigo3d': optimizador.getCode(),
        'optimizaciones': getReporteOptimizacionAsSerializable()
    }
    return jsonify(res)


@app.route("/mirillaBloques", methods=['POST'])
def mirillaBloques():
    limpiarReporteOptimizacion()
    texto = request.json['entrada']
    optimizador = parseCode3d(texto)
    optimizador.optimizarMirilla()
    optimizador.optimizar_bloques()
    res = {
        'codigo3d': optimizador.getCode(),
        'optimizaciones': getReporteOptimizacionAsSerializable()
    }
    return jsonify(res)


@app.route("/")
def pruebas():
    f = open("src/Analizador/entrada.txt", "r")
    texto = f.read()
    return jsonify(parse(texto)['textoSalida'])


if __name__ == '__main__':
    app.run(port=5000)