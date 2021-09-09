import uuid

cst = {
    "nodes": [],
    "edges": [],
}

def getNewId():
    return uuid.uuid4()

def limpiarCst():
    cst['nodes'].clear()
    cst['edges'].clear()


def defNodoCst(idNodo, label):
    cst['nodes'].append(
        {
            "id": idNodo,
            "label": label,
        }
    )

def defEdgeCst(idPare, idHijo):
    cst['edges'].append(
        {
            "from": idPare,
            "to": idHijo
        }
    )

def defElementCst(idNodo, label, idPare):
    defNodoCst(idNodo, label)
    defEdgeCst(idPare, idNodo)