#-----------------------------------------------------------------------------------------
#1-Crear una función que reciba una lista de números enteros
#y muestre cuál es el número mayor y cuál es el menor.
#ejemplo para la estructura
def numeroMayorMenor(listado):
    menor = min(listado)
    mayor = max(listado)
    print(f"El numero menor es: {menor}\nEl numero mayor es: {mayor}")

def ejercicio1():
    limit = int(input("Ingrese un limite de valores: "))
    listadoNum = []
    i = 1
    while i <= limit:
        num = int(input("Ingrese un numero entero: "))
        listadoNum.append(num)
        i += 1
    numeroMayorMenor(listadoNum)
#-----------------------------------------------------------------------------------------
#2-Crear una función que reciba una cadena de texto
#y cuente cuántas vocales contiene.
def esVocal(letra):
    vocales = "aeiouAEIOU"
    return letra in  vocales

def contarVocales(texto):
    contador = 0
    for letra in texto:
        if esVocal (letra):
            contador += 1
    print(f"La cadena contiene {contador} vocales.")

def ejercicio2():
    texto = input("Ingrese una cadena de texto: ")
    contarVocales(texto)

#-----------------------------------------------------------------------------------------
#3-Crear una función que reciba una lista de nombres y
#muestre únicamente aquellos que tengan más de 5 letras.


def ejercicio3():
    pass

#-----------------------------------------------------------------------------------------
#4-Crear una función que reciba una lista de notas (números decimales),
#calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
def ejercicio4():
    pass

#-----------------------------------------------------------------------------------------
#5-Crear una función que reciba una lista de precios de productos
#y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.
def ejercicio5():
    pass

#-----------------------------------------------------------------------------------------
#6-Crear una función que reciba un número entero
#y determine si es par o impar.
def ejercicio6():
    pass

#-----------------------------------------------------------------------------------------
#7-Crear una función que reciba una lista de edades y
#muestre cuántas personas son mayores de edad (18 años o más).
def ejercicio7():
    pass

#-----------------------------------------------------------------------------------------
#8-Crear una función que reciba una lista de palabras
#y permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.
def ejercicio8():
    pass

#-----------------------------------------------------------------------------------------
#9-Crear una función que reciba una lista de números
#y genere una nueva lista que contenga únicamente los números positivos.
def ejercicio9():
    pass

#-----------------------------------------------------------------------------------------
#10-Crear una función que reciba una lista de productos
#(utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.
def ejercicio10():
    pass


continuar = True
while continuar:
    print("\n--- Ejercicos Python---")
    print("--- 1.- Ejercicio 1 ---")
    print("--- 2.- Ejercicio 2 ---")
    print("--- 3.- Ejercicio 3 ---")
    print("--- 4.- Ejercicio 4 ---")
    print("--- 5.- Ejercicio 5 ---")
    print("--- 6.- Ejercicio 6 ---")
    print("--- 7.- Ejercicio 7 ---")
    print("--- 8.- Ejercicio 8 ---")
    print("--- 9.- Ejercicio 9 ---")
    print("--- 10.- Ejercicio 10 ---")
    opcion = input("\n---- Elige una opción: (1-10) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1: ")
        ejercicio1()
    elif opcion == "2":
        print("\nEjecutando ejercicio 2: ")
        ejercicio2()
    elif opcion == "3":
        print("\nEjecutando ejercicio 3: ")
        ejercicio3()
    elif opcion == "4":
        print("\nEjecutando ejercicio 4: ")
        ejercicio4()
    elif opcion == "5":
        print("\nEjecutando ejercicio 5: ")
        ejercicio5()
    elif opcion == "6":
        print("\nEjecutando ejercicio 6: ")
        ejercicio6()
    elif opcion == "7":
        print("\nEjecutando ejercicio 7: ")
        ejercicio7()
    elif opcion == "8":
        print("\nEjecutando ejercicio 8: ")
        ejercicio8()
    elif opcion == "9":
        print("\nEjecutando ejercicio 9: ")
        ejercicio9()
    elif opcion == "10":
        print("\nEjecutando ejercicio 10: ")
        ejercicio10()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opcion no valida, intenta otra vez")