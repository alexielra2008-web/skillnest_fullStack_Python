#condicionales
#estructura else - if
num = 15
if num > 20:
    print("Número mayor a 20")
else:
    print("Número menor a 20")
'''
La variable num es menor a 20, por lo que el bloque de código de else será ejecutado.
Es decir que vamos a imprimir "Número menor a 20"
'''
num = 101
if num > 50:
    print("Número mayor a 50")
elif num > 100:
    print("Número mayor a 100")
else:
    print("Número menor a 10")
'''
A pesar de que num es mayor que 50 y 100, la primera condicional que se cumpla es la única que se ejecutará.
Es por eso que solo imprimirá: "Número mayor a 50"
'''
if num < 60:
    print("Número menor a 50")

#No se cumple con la condicional, por lo que no se ejecuta el bloque de código

#tarea desafio
#ingresar 3 numeros por teclado e identificar cual es el mayor y 
# cual es el menor. mostrar ambos.
num1 = int(input("Ingresar primer numero: "))
num2 = int(input("Ingresar segundo numero: "))
num3 = int(input("Ingresar tercer numero: "))

#Gracias Donovan
#detecta menor
if num1 == num2 and num1 == num3:
    print(f"Todos los numeros son iguales")
elif num1 < num2 and num1 < num3:
    print(f"{num1} es menor que {num2} y {num3}")
elif num2 < num1 and num2 < num3:
    print(f"{num2} es menor que {num1} y {num3}.")
elif num3 < num1 and num3 < num2:
    print(f"{num3} es menor que {num1} y {num2}")
else:
    print("Ingrese un valor valido")

#detectar mayor
if num1 == num2 and num1 == num3:
    print(f"Todos los numeros son iguales")
elif num1 > num2 and num1 > num3:
    print(f"{num1} es mayor que {num2} y {num3}")
elif num2 > num1 and num2 > num3:
    print(f"{num2} es mayor que {num1} y {num3}.")
elif num3 > num1 and num3 > num2:
    print(f"{num3} es mayor que {num1} y {num2}")
else:
    print("Ingrese un valor valido")

#ejemplo para la estructura
n1 = int(input("Ingresar primer numero: "))
n2 = int(input("Ingresar segundo numero: "))
n3 = int(input("Ingresar tercer numero: "))
menorr = ""
mayorr = ""
#estructura if elif else
if n1 >= n2 and n1 >= n3:
    mayorr = n1
    if n2 <= n3:
        menorr = n2
    else:
        menorr = n2
elif n2 >= n1 and n2 >= n3:
    mayorr = n2
    if n1 <= n3:
        menorr = n1
    else:
        menorr = n3
else:
    mayorr = n3
    if n1 <= n2:
        menorr = n1
    else:
        menorr = n2
print(f"El mayor es {mayorr} y el menor es {menorr}")