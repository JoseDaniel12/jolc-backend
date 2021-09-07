from src.Errores.Error import *

tablaErrores = []

def agregarError(error: Error):
    tablaErrores.append(error)

def getTablaErroresAsString():
    texto = ""
    for i in tablaErrores:
        texto += i.getAsString() + "\n"
    return  texto

def limpiarTablaErrores():
    tablaErrores.clear()