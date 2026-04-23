# Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]
#Respuesta:
print(puntajes)
puntajes[1][0] = 600
print(puntajes)

# Lista de creadores de contenido en una plataforma de streaming
streamers = [
    {"nombre": "GameNinjaPro", "seguidores": 250000},
    {"nombre": "PixelWarrior", "seguidores": 180000}
]
#Respuesta:
print(streamers[0]["nombre"])
streamers[0]["nombre"] = "EliteGamerX"
print(streamers[0]["nombre"])

# Eventos en distintas ciudades del mundo
eventos = {
    "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
    "España": ["Madrid", "Barcelona", "Valencia"]
}
#Respuesta:
print(eventos["Estados Unidos"][2])
eventos["Estados Unidos"][2] = "San Francisco"
print(eventos["Estados Unidos"][2])


# Coordenadas de la sede de un torneo internacional
ubicacion = [
    {"latitud": 34.052235, "longitud": -118.243683}
]
print(ubicacion)

#Respuesta:
ubicacion[0]["latitud"] = 40.712776 
print(ubicacion)

#Funciones para recorrer y representar datos
#Respuesta:

def mostrar_streamers(lista):
    for item in lista:
        print(f"Streamers: {item['nombre']} - Seguidores: {item['seguidores']}")

mostrar_streamers(streamers)


twitch = {
    "nombre": ["EliteGamerX", "PixelWarrior"],
    "seguidores": ["250000", "180000"]
}

for separacion, orden in twitch.items():
    print(separacion)
    for item in orden:
        print(item)

#Mostrar información de un diccionario con listas
#Respuesta
categorias = {
    "juegos_populares": [
        "Fortnite", 
        "Minecraft", 
        "Valorant", 
        "GTA V",
    ],
    "ciudades_eventos": [
        "Nueva York",
        "Madrid",
        "Tokio",
    ]
}

def mostrar_categorias(diccionario):
    for categoria, items in diccionario.items():
        print(f"{len(items)} {categoria.upper()}")
        for item in items:
            print(item)

mostrar_categorias(categorias)