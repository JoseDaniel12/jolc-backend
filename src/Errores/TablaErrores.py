from src.Errores.Error import *
import json

tablaErrores = []

def agregarError(error: Error):
    tablaErrores.append(error)

def getTablaErroresAsString():
    texto = ""
    for i in tablaErrores:
        texto += i.getAsString() + "\n"
    return  texto

def getTablaErroresAsJson():
    res  = []
    for err in tablaErrores:
        res.append(err.getAsJson())
    return res

def limpiarTablaErrores():
    tablaErrores.clear()