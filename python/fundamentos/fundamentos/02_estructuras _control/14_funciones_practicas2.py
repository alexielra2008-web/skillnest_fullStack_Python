import os
#Ejercicio 1
# Calcula experiencia
def multiplica_por_2(num):
    result = []
    for i in range(num + 1):
        result.append(i * 2)
    return result
def ejercicio1():
    result1 = multiplica_por_2(5)
    print(result1)
# Debe retornar: [0, 2, 4, 6, 8, 10]


#Ejercicio 2
# Analiza publicaciones
def suma_y_resta():
    suma = list[0] + list[1]
    resta = list[0] - list[1]
    print(f"suma: {suma}")
    return resta

def ejercicio2():
    resta = suma_y_resta([120, 115])
    print(f"retorno / resta: {resta}")
# Imprime: 235 y retorna: 5

#Ejercicio 3
# Puntaje ajustado
def sumatoria_menos_longitud(sumatoria):
    total = sum(sumatoria)
    longitud = len(sumatoria)
    resultado = total - longitud
    print(f"total = {total}, longitud = {longitud}")
    return resultado

def ejercicio3():
    retornar = sumatoria_menos_longitud([10, 5, 3, 7])    
    print(f"El resultado del retorno es: {retornar}")
# Suma total = 25, longitud = 4, debe retornar: 21

#Ejercicio 4
# Ajusta visualizaciones
def valores_multiplicados_segundo(lista):
    if len(lista) < 2:
        print(len(lista))
        return = []
    else
        segE

def ejercicio4():
    # Imprime: 4 y retorna: [300, 9, 150, 60]
    valores_multiplicados_segundo([100, 3, 50, 20])
    valores_multiplicados_segundo([100])
# Imprime: 1 y retorna: []


# Genera precio fijo

def ejercicio5():
    valor_multiplicado_longitud(5, 2)
    # Debe retornar: [10, 10]
    valor_multiplicado_longitud(7, 5)
    # Debe retornar: [35, 35, 35, 35, 35]

def limpiar_consola():
    os.system('cls')

continuar = True
while continuar:
    print("\n--- Ejercicos Python---")
    print("--- 1.- Ejercicio 1 ---")
    print("--- 2.- Ejercicio 2 ---")
    print("--- 3.- Ejercicio 3 ---")
    print("--- 4.- Ejercicio 4 ---")
    print("--- 5.- Ejercicio 5 ---")
    opcion = input("\n---- Elige una opción: (1-5) (0 para salir) =")
    if opcion == "1":
        limpiar_consola()
        print("\nEjecutando ejercicio 1: ")
        multiplica_por_2()
    elif opcion == "2":
        limpiar_consola()
        print("\nEjecutando ejercicio 2: ")
        verificador_edad()
    elif opcion == "3":
        limpiar_consola()
        print("\nEjecutando ejercicio 3: ")
        aplicarDescuentos()
    elif opcion == "4":
        limpiar_consola()
        print("\nEjecutando ejercicio 4: ")
        clasificadorNum()
    elif opcion == "5":
        limpiar_consola()
        print("\nEjecutando ejercicio 5: ")
        tablaMultiplicar()
    elif opcion == "0":
        limpiar_consola()
        print("Saliendo...")
        continuar = False
    else:
        limpiar_consola()
        print("Opcion no valida, intenta otra vez")