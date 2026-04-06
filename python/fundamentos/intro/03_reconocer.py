"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""


import random #Importacion de libreria para procesos literarios


nombre = "Frida Kahlo" #Creacion de variable tipo string y se asigna un valor
print(type(nombre)) #type() = metodo de python para mostrar el tipo de una variable
print(len(nombre)) #len() = Devuelve el largo de una variable.


edad = 25 #Creacion de variable tipo numerico(int).


if edad < 18: #Se establece condicion if.
    print("Eres menor de edad.") #Imprime un mensaje
elif edad == 18: #Se establece una sub-condicion elif = else if
    print("Tienes 18 años.") #Imprime un mensaje
else: #Cierra la condicion (si no se cumplen las condiciones anteriores)
    print("Eres mayor de edad.") #Imprime mensaje


frutas = ["manzana", "pera", "fresa"] #Creacion de array con valores ya asignados
print(frutas[0]) #Mostramos la primera posicion del arreglo
frutas[0] = "banana" #A la posicion 0 del arreglo se le asigna el valor banana
frutas.append("uva") #Se le agrega "uva" al final del arreglo
frutas.remove("pera") #Se remueve la palabra "pera" del arreglo


dimensiones = (200, 50) #Creamos una variable tipo tupla (variable inmutable)
print(dimensiones[0]) #Imprime la posicion 0 de la variable creada


persona = { #Variable tipo objeto (object)
    "nombre": "Carlos", #Se establece un item y su respectivo valor
    "edad": 30 #Se establece un item y su respectivo valor
}
print(persona["nombre"]) #Imprime el valor del item (ej: "Carlos")
persona["edad"] = 31 #Se modifica el valor del item edad a 31
persona["ciudad"] = "Santiago" #Se agrega un nuevo item con un valor
del persona["ciudad"] #Se borra (del = delete) el item completo


for i in range(5): #fot range: Se crea el bucle en rango desde 0 a 5
    if i == 2: #Se establece condicion if i == 2
        continue #continue ignora el proceso y continua.
    if i == 4: #Se establece condicion if i == 4
        break #Si i = 4 se rompe el bucle
    print(i) #Imprime valor de i en cada interaccion. (hasta 4)


contador = 0 #Se crea una variable contador tipo numerica(int)
while contador < 3: #Se crea un bucle while con una condicion 
    print(f"while contador es: {contador}") #Imprime el contador en un mensaje concatenado con f"" string.
    contador += 1 #Incrementa el valor en 1 en cada iteracion


def saludar_usuario(nombre): #def - Palabra reservada oara crear una funcion
    return f"Hola, {nombre}" #Devuelve un valor a una funcion


print(saludar_usuario("Francisca")) #Se imprime "Hola Francisca" - return de la funcion