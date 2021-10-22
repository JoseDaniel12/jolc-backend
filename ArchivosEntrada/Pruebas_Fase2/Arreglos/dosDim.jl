random = [1, 5, 8, -1, 21, 42, -55, 123, -5, 5, 11];

a = [
    [
        random[1] * 3,
        51,
        random[4] / 2,
        (random[3] * 10) % 7
    ],
    [
        1,
        2,
        3,
        4
    ]
];

b = [
    [
        1,
        2,
        3,
        4
    ],
    [
        random[1] * 3,
        51,
        random[4] / 2,
        (random[3] * 10) % 7
    ]
];

auxiliar = [
    [
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0
    ]
];


# Si no tienen implementado este for, pueden cambiarlo por algún otro ciclo que funcione parecido.
function printMatriz()::None
    println("[");
    for i in matrix
        print("[");
        for j in i
            print(j, " ");
        end;
        println("]");
    end;
    println("]");
end;

function sumarMatrices()::Array
    if length(a) != length(b)
        return "NO SE PUEDEN SUMAR. NO SON DE LA MISMA LONGITUD";
    end;
    for i in 1:length(a)
        for j in 1:length(a[1])
            auxiliar[i][j] = a[i][j] + b[i][j];
        end;
    end;
    return auxiliar;
end;

function compararMatrices()::Bool
    if length(a) != length(b)
        return false;
    end;
    for i in 1:length(a)
        for j in 1:length(a[1])
            if a[i][j] != b[i][j]
                return false;
            end;
        end;
    end;
    return true;
end;

println("MATRIZ a");
for fila in a
    for elemento in fila
        print(elemento, ", ")
    end
    println("")
end
println();
println("MATRIZ b");
for fila in b
    for elemento in fila
        print(elemento, ", ")
    end
    println("")
end

println();
println("LAS DOS MATRICES SUMADAS");
suma = sumarMatrices();
for fila in suma
    for elemento in fila
        print(elemento, ", ")
    end
    println("")
end

println();
println("COMPARAR MATRICES. SON IGUALES?");
println(compararMatrices());

println();
println("Pop Matriz a");

println();
println("Push a b");
for fila in b
    for elemento in fila
        print(elemento, ", ")
    end
    println("")
end



b = a;
println();
println("COMPARAR MATRICES. SON IGUALES?");
println(compararMatrices());
