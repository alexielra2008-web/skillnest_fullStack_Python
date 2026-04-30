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
def cuentaLetras(lista):
    resultado = []
    for nombre in lista:
        if len(nombre) > 5:
            resultado.append(nombre)
        return resultado

def ejercicio3():
    nombres = []
    cantidad = int(input ("Cuantos nombres quiere colocar: "))

    for i in range(cantidad):
        nombre = input("Ingrese un nombre: ")
        print(f"{nombre} agregado con exito en la lista.")
        nombres.append(nombre)
        
    listaNombres = ejercicio3(nombre)
    print(f"Los nombres con mas de 5 letras son: \n- {("\n- ").join(listaNombres)} ")

ejercicio3()

#-----------------------------------------------------------------------------------------
#4-Crear una función que reciba una lista de notas (números decimales),
#calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
def listaNotas(notas):
    lista = 0
    proedio = 0
    for i in range(len(notas)):
        lista += notas[i]
        promedio = lista / (len(notas))

    if promedio[i] >= 4.0 and promedio[i] <= 7.0:
        print(f"Felicidades pasaste con {promedio}")
    elif promedio[i] >= 1.0 and promedio[i] <= 3.9:
        print(f"Usted no aprueba ya que tiene un {promedio}")
    else:
        return"Error"

def ejercicio4():
    largo = int(input("Cuantas notas va a ingresar: "))
    nota = []
    for i in range(largo):
        inp = float(input(f"Ingrese nota {i + 1}"))
        if inp != "":
            nota.append(inp)
    print(listaNotas(nota))
ejercicio4()

#-----------------------------------------------------------------------------------------
#5-Crear una función que reciba una lista de precios de productos
#y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.
def descuento(valor):
    sumaLista = sum(valor)
    precioInicial = sumaLista
    descuento = sumaLista * 0.1
    precioFinal = precioInicial - descuento
    print(f"El precio inicial del producto es: \n{precioInicial}\ny con descuento \n{precioFinal}")

def ejercicio5():
    cantidadProductos = int(input("Ingrese la cantidad de productos que quiera:\n"))
    listaPrecios = []
    for i in range(cantidadProductos):
        valorProducto = float(input("Inrese el valor del producto:\n"))
        listaPrecios.append(valorProducto)
    descuento(listaPrecios)
ejercicio5()

#-----------------------------------------------------------------------------------------
#6-Crear una función que reciba un número entero
#y determine si es par o impar.
def parImpar(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es Par.")
    elif numero % 3 == 0:
        print(f"El numero {numero} es Impar.")
    else:
        print("Error")

def ejercicio6():
    num = int(input("Ingrese un numero: "))
    parImpar(num)

ejercicio6()

#-----------------------------------------------------------------------------------------
#7-Crear una función que reciba una lista de edades y
#muestre cuántas personas son mayores de edad (18 años o más).
def edades(lista):
    num = 0
    for i in range(len(lista)):
        if lista[i] >= 18:
            num += 1
    return num

def ejercicio7():
    edad = []
    inp = int(input("Cuantas personas van a ingresar hoy?: "))
    for i in range(inp):
        var = int(input(">> "))
        if var !="":
            edad.append(var)
        else:
            print("Por favor ingresar valor valido")
    resultado = edades(edad)
    print(f"Hay {resultado} personas mayores de edad")
ejercicio7()

#-----------------------------------------------------------------------------------------
#8-Crear una función que reciba una lista de palabras
#y permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.
def vecesAparicion(palabras):
    buscar = input("Ingrese la palabra que desea buscar: ")
    vecesAparicion = 0
    for i in range(len(palabras)):
        if buscar == palabras[i]:
            vecesAparicion += 1
    print(f"La palabra {buscar} aparece {vecesAparicion} en la lista.")

def ejercicio8():
    cantidad = int(input("Ingrese la cantidad de palabras: "))
    listaPalabras = []
    for i in range(cantidad):
        palabra = input(f"{i + 1}. ")
        listaPalabras.append(palabra)
    vecesAparicion(listaPalabras)

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