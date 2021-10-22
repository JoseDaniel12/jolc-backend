val1 = 1::Int64;
val2 = 10::Int64;
val3 = 2021.2020::Float64;

println("Probando declaracion de variables");
println(val1, " ", val2, " ", val3);
println("---------------------------------");
# COMENTARIO DE UNA LINEA
val1 = val1 + 41 - 123 * 4 / (2 + 2 * 2) - (10 + (125 + 5)) * 2 ^ 2;
val2 = 11 * (11 * (12 + -10)) + 22 / 2;
val3 = 2 ^ (2 * 2 ^ 2) + 25 / 5;
println("Probando asignación de variables y aritmeticas");
println(val1, " ", val2, " ", val3);
println("---------------------------------");

rel1 = (((val1 - val2) == 24) && (true && (false || 5 >= 5))) || ((7*7) != (15+555) || -61 > 51);
rel2 = (7*7) <= (15+555) && 1 < 2;
println("Probando relacionales y logicas");
println(rel1, " ", rel2, " ");
println("---------------------------------");

iterador = 10;
while iterador > 0
    iterador = iterador - 1;
    if iterador >= 7
        print(iterador);
        println(" >= 7");
    elseif iterador >= 5
        print(iterador);
        println(" >= 5");
    elseif iterador >= 3
        print(iterador);
        println(" >= 3");
    else
        print(iterador);
        println(" < 3");
    end;
end;

palabra = "JOKLC";

for letra in palabra
    if letra == "J"
        continue;
    elseif letra == "L"
        println("#");
        break;
    else
        print("&");
    end;

    letra = letra ^ 3;
    print(letra, "-");
end;

a = -1;
while (a < 5)
    a = a + 1;
    if a == 3
        print("a");
        continue;
    elseif a == 4
        println("b");
        break;
    end;
    print("El valor de a es: ", a, ", ");
end;

for num in (4/2-1-1):(6*2-1)
    if num == 2
        continue;
    elseif num == 4
        break;
    end;

    num = num + 500;
    print(num, ",");
end;
println("");

for i in 0:9

    output = "";
    for j in 0:(10 - i)
        output = output * " ";
    end;

    for k in 0:i
        output = output * "* ";
    end;
    println(output);

end;

arreglo = [11,22,[33,44,[55,66]]];
dosdimen = arreglo[3];
tresdimen = arreglo[3][3];
dosnum = 2;

println(arreglo[dosnum]);
println(dosdimen[dosnum]);
println(tresdimen[1]);
println(arreglo[3][3][dosnum]);

mayores5 = [6,7,8,9,10];
numeros = [1,2,3,4,5,mayores5];

mayores5[1] = 11;
println(numeros[6][1]);
numeros[6][1] = 22;
println(mayores5[1]);

arr = [1,2,3,4,5,6];
for i in [1,2,3,4,5,6]
    println(arr[i] == 1, arr[i] == 2, arr[i] == 3, arr[i] == 4, arr[i] == 5, arr[i] == 6);
end;

struct Actor
    nombre:: String;
    edad:: Int64;
end;

struct Pelicula
    nombre::String;
    posicion::Int64;
end;

struct Contrato
    actor::Actor;
    pelicula::Pelicula;
end;

actorProta = Actor("Joaquin",51);
contratoProta = Contrato(nothing,nothing);

println("Actor viejo: " * actorProta.nombre);
if contratoProta.actor == nothing
    contratoProta.actor = actorProta;
    actorProta.nombre = "BradPit";
    println("Nuevo actor: " * contratoProta.actor.nombre);
end;

contratoProta.actor.nombre = "DeNiro";
println("Actor siguiente: " * actorProta.nombre);

actores = ["Elizabeth Olsen", "Adam Sandler", "Christian Bale", "Jennifer Aniston"];
peliculas = ["Avengers: Age of Ultron", "Mr. Deeds", "Batman: The Dark Knight", "Marley & Me"];

function contratar(actor::Actor, pelicula::Pelicula)::Contrato
    return Contrato(actor,pelicula);
end;

function crearActor(nombre::String, edad::Int64)::Actor
    return Actor(nombre,edad);
end;

function crearPelicula(nombre::String, posicion::Int64)::Pelicula
    return Pelicula(nombre,posicion);
end;

function imprimir(contrato::Contrato)::Nothing
    println("Actor: ", contrato.actor.nombre, "   Edad: ", contrato.actor.edad);
    println("Pelicula: ", contrato.pelicula.nombre, "   Genero: ", contrato.pelicula.posicion);
end;

function contratos()::Nothing
    for i in 1:(1*1+2)
        contrato = Contrato(Actor("",0),Pelicula("",0)) ::Contrato;
        if(i < 4)
            actor = crearActor(actores[i], i+38) ::Actor;
            pelicula = crearPelicula(peliculas[i], i) ::Pelicula;
            contrato = contratar(actor, pelicula);
        end;
        imprimir(contrato);
    end;
end;

contratos();

function referencias(act::Actor)::Nothing
    act.nombre = "Pedro";
    return nothing;
end;

referencias(actorProta);
println(actorProta.nombre);

function potenciaNativa(base::Int64, exponente::Int64)::Int64
    resultado = base;
    while exponente > 1
        resultado = resultado * base;
        exponente = exponente - 1;
    end;
    return resultado;
end;

println(potenciaNativa(5, 7));
println(potenciaNativa(2, 2));
println(potenciaNativa(4, 2));

function sumarTodo(num1::Int64, num2::Int64)::Int64
    result = 0;
    if num1 < 0 || num2 < 0
        return -1;
    end;

    while num1 > 0 || num2 > 0
        result = result + (num1 + num2);
        num1 = num1 - 1;
        num2 = num2 - 1;
    end;
    return result;
end;

println(sumarTodo(5, 4));
println(sumarTodo(-1, -5));
println(sumarTodo(7, 7));

function factorial(num::Int64) ::Int64
    if (num == 1)
        return 1;
    else
        return num * factorial(num-1);
    end;
end;

println(factorial(5));

function hanoi(discos::Int64, origen::Int64, auxiliar::Int64, destino::Int64) ::Nothing
    if (discos == 1)
        println("Mover de ", origen, " a ", destino);
    else
        hanoi(discos-1, origen, destino, auxiliar);
        println("Mover de ", origen, " a ", destino);
        hanoi(discos-1, auxiliar, origen, destino);
    end;
end;

hanoi(3, 1, 2, 3);

function ackerman(m::Int64, n::Int64)::Int64
    if m == 0
        return n + 1;
    elseif m > 0 && n == 0
        return ackerman(m - 1, 1);
    else
        return ackerman(m - 1, ackerman(m, n - 1));
    end;
end;

println(ackerman(3, 4));

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

println(uppercase("Hola Mundo! ") * lowercase("WeNaS! :z"));
println(trunc(Int64, parse(Float64, "58.92") + 11.03));
println(parse(Int64, "24.941"));





