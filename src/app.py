from flask import Flask, jsonify
from Analizador.grammar import parse
from src.Entorno.Ambito import *
from src.Errores.TablaErrores import  *

app = Flask(__name__)

@app.route('/')
def compile_code():
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
    app.run()
