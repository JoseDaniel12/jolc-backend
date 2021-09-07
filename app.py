from flask import Flask, jsonify

from src.Analizador.grammar import parse
from src.Entorno.Ambito import *
from src.Errores.TablaErrores import  *

app = Flask(__name__)

@app.route('/')
def index():
    limpiarTablaErrores()
    res = ""
    f = open("src/Analizador/entrada.txt", "r")
    texto = f.read()
    listaIns = parse(texto)
    ambitoGlobal = Ambito(None, "GLOBAL")
    for ins in listaIns:
        res += ins.ejecutar(ambitoGlobal).textoConsola
    res = getTablaErroresAsString() + res
    return jsonify(res)

if __name__ == '__main__':
    app.run(port=5000)