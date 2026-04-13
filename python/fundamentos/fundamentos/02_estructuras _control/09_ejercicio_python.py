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
clave = "1234"
intentos = 0

while intentos < 3:
    intento = input("Ingresa la contraseña: ")
    if intento == clave:
        print("Acceso concedido")
        break
    intentos += 1

if intentos == 3:
    print("Acceso bloqueado")

#9. Registro de Nombres
#Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. Guárdalos en el arreglo y, al final, imprímelos en orden inverso al que fueron ingresados.
nombres = []

for i in range(5):
    nombre = input("Ingresa un nombre: ")
    nombres.append(nombre)

print("Orden inverso:")
for nombre in reversed(nombres):
    print(nombre)

#10. Promedio de Notas
#Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo. Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.
cantidad = int(input("¿Cuántas notas ingresarás? "))
notas = []

for i in range(cantidad):
    nota = float(input("Ingresa la nota: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)
print("Promedio:", promedio)
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

#11. Filtro de Arreglos
#Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que contenga solo los números que sean mayores a 50. Muestra ambos arreglos.
numeros = []
cantidad = int(input("¿Cuántos números deseas ingresar? "))

for i in range(cantidad):
    numeros.append(int(input("Número: ")))

mayores = [n for n in numeros if n > 50]

print("Original:", numeros)
print("Mayores a 50:", mayores)

#12. Buscador de Elementos
#Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una ciudad y el programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está.
#IV. Retos de Lógica Combinada
ciudades = ["Santiago", "Valparaíso", "Concepción", "La Serena", "Antofagasta", "Temuco", "Iquique", "Rancagua", "Talca", "Arica"]

buscar = input("Ingresa una ciudad: ")

if buscar in ciudades:
    print("Ciudad encontrada en posición:", ciudades.index(buscar))
else:
    print("Ciudad no encontrada")

#13. Simulación de Inventario
#Crea dos arreglos: uno para nombres_productos y otro para precios. Permite al usuario ingresar 3 productos con sus precios. Luego, muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].
productos = []
precios = []

for i in range(3):
    productos.append(input("Nombre del producto: "))
    precios.append(float(input("Precio: ")))

for i in range(len(productos)):
    print(f"Producto: {productos[i]} - Precio: ${precios[i]}")

#14. Generador de Lista de Compras
#Usa un bucle while para que el usuario agregue artículos a una lista de compras. El proceso termina cuando el usuario escribe "terminar". Al final, muestra la lista ordenada alfabéticamente.
lista = []

while True:
    item = input("Agrega un artículo (escribe 'terminar' para finalizar): ")
    if item.lower() == "terminar":
        break
    lista.append(item)

lista.sort()

print("Lista ordenada:")
for item in lista:
    print(item)

#15. Análisis de Temperaturas
#Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
#El promedio semanal.
#Cuántos días la temperatura fue superior a 25 grados.
#El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).
temps = []

for i in range(7):
    temps.append(float(input(f"Temperatura del día {i+1}: ")))

promedio = sum(temps) / 7
mayores_25 = len([t for t in temps if t > 25])
min_temp = min(temps)
dia_min = temps.index(min_temp)

print("Promedio semanal:", promedio)
print("Días sobre 25°C:", mayores_25)
print("Día más frío (0=Lunes):", dia_min)

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