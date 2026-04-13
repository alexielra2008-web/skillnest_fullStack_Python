#1. Números Pares Dinámicos
#Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). El programa debe imprimir los primeros $n$ números pares positivos.
def numerosDinamicos():
    n = int(input("¿Cuántos números pares deseas ver?: "))
    pares = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            pares.append
    print(f"mostrando pares: {pares}")

#2. Verificador de Edad y Acceso
#Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+). Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.
def verificador_edad():
    campo = input("ingrese su año de nacimiento: ")
    edad = 2026 - int(campo)
    if campo == "":
        print("Error")
    elif int(campo) >= 18:
        print(f"tienes acceso ya que tu edad es: {edad}")
    elif edad > 0 and edad < 18:
        print("no tienes acceso: te faltan {18 - edad} años.")
    else:
        print("ingrese valores validos")
verificador_edad()


#3. Calculadora de Descuentos
#Solicita el precio de un producto y la cantidad comprada. Si el total supera los $100, aplica un 15% de descuento. Muestra el subtotal, el descuento aplicado y el total final.
def aplicarDescuentos():
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad comprada: "))
    producto = precio * cantidad

    if producto > 100:
        descuento = producto * 0.15 # Calculamos el 15%
    else:
        descuento = 0
    total = producto
    print(f"el subtototal es: {producto} el Descuento aplicado es: {descuento} y el Total es: {total}")

#4. Clasificador de Números
#Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar, Negativo-Par, Negativo-Impar o Cero.
#II. Iteraciones y Bucles (Intermedio)
def  clasificadorNum():
    num = int(input("Ingresa un número: "))
    if num > 0:
        if num % 2 ==0:
            print("positivo-par")
        elif num % 2 ==1:
            print("positivo-impar")
    elif num <0:
        if num % 2 == 0:
            print("negativo-par")
        elif num % 2 == 1:
            print("negativo-impar")
    else:
        print("es 0")

#5. Tabla de Multiplicar Personalizada
#Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, pero solo muestra los resultados que sean múltiplos de 3.
def  tablaMultiplicar():
    num = int(input("Ingresa un número para su tabla: "))

    for i in range(1, 13):
       resultado = num * i
        # Verificamos si el resultado es múltiplo de 3 usando el operador módulo %
    if resultado % 3 == 0:
        print(f"{num} x {i} = {resultado}")

#6. Sumatoria con Centinela
#Crea un programa que pida números continuamente y los sume. El ciclo debe terminar cuando el usuario ingrese un número negativo. Al final, muestra la suma total (sin incluir el negativo).
def sumatoriaCentinela():
    suma_total = 0
    while True:
        n = float(input("Ingrese un numero (negativo para salir):"))
        if n < 0:
            break
        suma_total += n
    print(f"La suma total es: {suma_total}")

#7. Contador de Vocales
#Pide al usuario una frase o palabra. Utiliza un bucle para recorrer la cadena y contar cuántas vocales tiene en total.
def contadorVocales():
    texto = input("Ingresa una palabra o frase: ").lower()
    vocales = 0
    for i in range(len(texto)):
        if texto[i] == "a" or texto[i] == "e" or texto[i] == "i" or texto[i] == "o" or texto[i] == "u":
            vocales += 1
        elif texto[i] == "á" or texto[i] == "é" or texto[i] == "í" or texto[i] == "ó" or texto[i] == "ú":
            vocales += 1
    print(f"La cadena '{texto}' tiene {vocales} vocales en total.")

#8. Validación de Contraseña
#Define una contraseña en una variable. Pide al usuario que la intente adivinar. Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.
#III. Manejo de Arreglos / Listas (Avanzado)
def validacion():
    con = 12345678
    intentos = 1
    while True:
        ingresa = int(input("Ingresa contraseña: "))
        if ingresa == con:
            print("Acceso concedido")
            break
        else:
            intentos += 1
            if intentos > 3:
                print("Acceso denegado")
                break
            else:
                print(f"numero de intentos: {intentos}")
#9. Registro de Nombres
#Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. Guárdalos en el arreglo y, al final, imprímelos en orden inverso al que fueron ingresados.


#10. Promedio de Notas
#Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo. Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.


#11. Filtro de Arreglos
#Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que contenga solo los números que sean mayores a 50. Muestra ambos arreglos.


#12. Buscador de Elementos
#Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una ciudad y el programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está.
#IV. Retos de Lógica Combinada


#13. Simulación de Inventario
#Crea dos arreglos: uno para nombres_productos y otro para precios. Permite al usuario ingresar 3 productos con sus precios. Luego, muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].


#14. Generador de Lista de Compras
#Usa un bucle while para que el usuario agregue artículos a una lista de compras. El proceso termina cuando el usuario escribe "terminar". Al final, muestra la lista ordenada alfabéticamente.


#15. Análisis de Temperaturas
#Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
#El promedio semanal.
#Cuántos días la temperatura fue superior a 25 grados.
#El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).


#menu de navegacion para ejercicios
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
    print("--- 11.- Ejercicio 11 ---")
    print("--- 12.- Ejercicio 12 ---")
    print("--- 13.- Ejercicio 13 ---")
    print("--- 14.- Ejercicio 14 ---")
    print("--- 15.- Ejercicio 15 ---")
opcion = input("\n---- Elige una opción: (1-15) (0 para salir) =")
if opcion == "1":
    print("\nEjecutando ejercicio 1: ")
    print(numerosDinamicos())
elif opcion == "2":
    print("\nEjecutando ejercicio 2: ")
    print()
elif opcion == "3":
    print("\nEjecutando ejercicio 3: ")
    print()
elif opcion == "4":
    print("\nEjecutando ejercicio 4: ")
    print()
elif opcion == "5":
    print("\nEjecutando ejercicio 5: ")
    print()
elif opcion == "6":
    print("\nEjecutando ejercicio 6: ")
    print()
elif opcion == "0":
    print("Saliendo...")
    continuar = False
else:
    print("Opcion no valida, intenta otra vez")