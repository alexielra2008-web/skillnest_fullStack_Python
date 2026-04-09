#1. Números Pares Dinámicos
#Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). El programa debe imprimir los primeros $n$ números pares positivos.
n = int(input("¿Cuántos números pares deseas ver? "))

for i in range(1, n + 1):
    print(i * 2)

#2. Verificador de Edad y Acceso
#Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+). Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.
from datetime import datetime

nacimiento = int(input("Ingresa tu año de nacimiento: "))
edad = datetime.now().year - nacimiento

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Te faltan", 18 - edad, "años para ser mayor de edad")

#3. Calculadora de Descuentos
#Solicita el precio de un producto y la cantidad comprada. Si el total supera los $100, aplica un 15% de descuento. Muestra el subtotal, el descuento aplicado y el total final.
precio = float(input("Precio del producto: "))
cantidad = int(input("Cantidad: "))

subtotal = precio * cantidad
descuento = 0

if subtotal > 100:
    descuento = subtotal * 0.15

total = subtotal - descuento

print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("Total final:", total)

#4. Clasificador de Números
#Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar, Negativo-Par, Negativo-Impar o Cero.
#II. Iteraciones y Bucles (Intermedio)
num = int(input("Ingresa un número: "))

if num == 0:
    print("Cero")
else:
    tipo = "Positivo" if num > 0 else "Negativo"
    paridad = "Par" if num % 2 == 0 else "Impar"
    print(f"{tipo}-{paridad}")

#5. Tabla de Multiplicar Personalizada
#Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, pero solo muestra los resultados que sean múltiplos de 3.
numero = int(input("Ingresa un número: "))

for i in range(1, 13):
    resultado = numero * i
    if resultado % 3 == 0:
        print(f"{numero} x {i} = {resultado}")

#6. Sumatoria con Centinela
#Crea un programa que pida números continuamente y los sume. El ciclo debe terminar cuando el usuario ingrese un número negativo. Al final, muestra la suma total (sin incluir el negativo).
suma = 0

while True:
    valor = float(input("Ingresa un número (negativo para terminar): "))
    if valor < 0:
        break
    suma += valor

print("Suma total:", suma)

#7. Contador de Vocales
#Pide al usuario una frase o palabra. Utiliza un bucle para recorrer la cadena y contar cuántas vocales tiene en total.
texto = input("Ingresa una frase: ")
contador = 0

for letra in texto.lower():
    if letra in "aeiou":
        contador += 1

print("Cantidad de vocales:", contador)

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