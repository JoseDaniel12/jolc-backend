val1 = 1::Int64;
val2 = 10::Int64;
val3 = 2021.2020::Float64;

println("Probando declaracion de variables");
println(val1, " ", val2, " ", val3);
println("---------------------------------");
# COMENTARIO DE UNA LINEA
val1 = val1 + 41 - 123 * 4 / (2 + 2 * 2) - (10 + (125 % 5)) * 2 ^ 2;
val2 = 11 * (11 % (12 + -10)) + 22 / 2;
val3 = 2 ^ (2 * 12 / 6) + 25 / 5#= COMENTARIO
MULTILINEA =#;
println("Probando asignación de variables y aritmeticas");
println(val1, " ", val2, " ", val3);
println("---------------------------------");

rel1 = (((val1 - val2) == 24) && (true && (false || 5 >= 5))) || ((7*7) != (15+555) || -61 > 51);
rel2 = (7*7) <= (15+555) && 1 < 2;
rel3 = true;
println("Probando relacionales y logicas");
println(rel1, " ", rel2, " ", rel3);
println("---------------------------------");

println("OPERACIONES " * "CON " * "Cadenas"^3);
despedida = "Adios mundo :c";
println(uppercase("Hola Mundo! ") * lowercase(despedida));

println("Probando funciones nativas de JOLC");
println(trunc(35.156105));
println(float(11));
println(uppercase("Hola Mundo! ") * lowercase("WeNaS! :z"));
carnet = "201807394";
println("---------------------------------");

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
