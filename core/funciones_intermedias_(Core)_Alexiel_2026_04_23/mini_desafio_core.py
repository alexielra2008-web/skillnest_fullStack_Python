#Desafio:
datos = [
    {"nombre": "Carlos", "puntaje": 80},
    {"nombre": "María", "puntaje": 95},
    {"nombre": "Pedro", "puntaje": 70}
]

# 1 Cambiar el puntaje de Pedro a 75:
for persona in datos:
    if persona["nombre"] == "Pedro":
        persona["puntaje"] = 75

# 2 Función que imprime "Carlos obtuvo 80 puntos":
def imprimir_puntaje(nombre, puntaje):
    print(f"{nombre} obtuvo {puntaje} puntos")

imprimir_puntaje("Carlos", 80)

# 3 Función que recibe "nombre" o "puntaje" e imprime solo esos valores:
def imprimir_valores(campo):
    for persona in datos:
        if campo in persona:
            print(persona[campo])

print("Solo nombres:")
imprimir_valores("nombre")

print("Solo puntajes:")
imprimir_valores("puntaje")
