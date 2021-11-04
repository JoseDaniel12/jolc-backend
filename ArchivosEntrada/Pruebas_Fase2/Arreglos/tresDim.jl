mapas = ["Desierto", "Bosque", "Mar", "Ciudad"];
enemigos = ["Enano", "Troll", "Caballero", "Arquero", "Maquina"];
jugadores = ["Ronald", "Manuel","Jhonatan","Cesar","Pablo"];

score = [
    [
        [
            18,16,20,15,98
        ]
    ],
    [
        [
            25,10,8,45,100
        ]
    ]
];


function imprimirReporte(value::Int64,i::Int64,j::Int64,k::Int64)
    println(mapas[i] * "          " * enemigos[j] * "          " * jugadores[k] * "          " );
end;

function imprimirScore(array::Vector{Vector{Vector{Int64}}})::Nothing
    for i in 1:length(array)
        for j in 1:length(array[i])
            for k in 1:length(array[i][j])
                imprimirReporte(array[i][j][k],i,j,k);
            end;
        end;
    end;
end;


println("Mapa" * "          " * "Enemigo" * "          " * "Jugador" * "          ");
imprimirScore(score);
