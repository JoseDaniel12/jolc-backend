mutable struct Node
    value::Int64;
    izq::Node;
    der::Node;
end;

mutable struct Tree
    root::Node;
end;

arbol = Tree(nothing);

    function insertar(nodo::Node, value::Int64)::Node
        if nodo == nothing
            nodo = Node(value, nothing, nothing);
        elseif value < nodo.value
            nodo.izq = insertar(nodo.izq, value);
        else
            nodo.der = insertar(nodo.der, value);
        end;
        return nodo;
    end;

function preOrden(nodo::Node)::Nothing
    if nodo != nothing
        println(nodo.value);
        preOrden(nodo.izq);
        preOrden(nodo.der);
    end;
end;

function inOrden(nodo::Node)::Nothing
    if nodo != nothing
        inOrden(nodo.izq);
        println(nodo.value);
        inOrden(nodo.der);
    end;
end;

function postOrden(nodo::Node)::Nothing
    if nodo != nothing
        postOrden(nodo.izq);
        postOrden(nodo.der);
        println(nodo.value);
    end;
end;

function encontrarValor(nodo::Node, valor::Int64)::Bool
    aux = nodo;
    while aux != nothing
        if aux.value == valor
            return true;
        elseif aux.value > valor
            aux = aux.izq;
        else
            aux = aux.der;
        end;
    end;
    return false;
end;

function encontrarValorR(nodo::Node, valor::Int64)::Int64
    if nodo == nothing
        return -1;
    end;
    if nodo.value == valor
        return nodo.value;
    elseif nodo.value > valor
        return encontrarValorR(nodo.izq, valor);
    else
        return encontrarValorR(nodo.der, valor);
    end;
end;

arbol.root = insertar(arbol.root, 35);
arbol.root = insertar(arbol.root, 15);
arbol.root = insertar(arbol.root, 55);
arbol.root = insertar(arbol.root, 4);
arbol.root = insertar(arbol.root, 67);
arbol.root = insertar(arbol.root, 100);
arbol.root = insertar(arbol.root, 36);
arbol.root = insertar(arbol.root, 10);
arbol.root = insertar(arbol.root, 1);
arbol.root = insertar(arbol.root, 3);

println("PREORDEN");
preOrden(arbol.root);
println("INORDEN");
inOrden(arbol.root);
println("POSTORDEN");
postOrden(arbol.root);

println("BUSCANDO VALORES");
print("Existe 7: ");
println(encontrarValor(arbol.root, 7));
print("Existe 36: ");
println(encontrarValor(arbol.root, 36));
print("Existe 1: ");
println(encontrarValor(arbol.root, 1));
print("Existe 58: ");
println(encontrarValor(arbol.root, 58));

println("BUSCANDO VALORES RECURSIVAMENTE");
print("Existe 7: ");
println(encontrarValorR(arbol.root, 7));
print("Existe 36: ");
println(encontrarValorR(arbol.root, 36));
print("Existe 1: ");
println(encontrarValorR(arbol.root, 1));
print("Existe 58: ");
println(encontrarValorR(arbol.root, 58));
