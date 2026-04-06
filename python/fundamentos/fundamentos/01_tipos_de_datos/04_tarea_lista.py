'''
Actividad: Gestor de inventario
'''
'''
1.-Creacion: crea una lista llamada inventario que contenga los siguientes
articulos: "laptop", "raton", "monitor", "cable hdmi"
'''
inventario = ["laptop", "raton", "monitor", "cable hdmi"]

'''
2.- Expansion: utiliza el metodo corresóndiente para agregar "impresora" y "teclado" al final de la lista
'''
inventario.append("impresora")
inventario.append("teclado")
print(inventario)
'''
3.- Conteo: utiliza la funcion integrada para mostrar cuantos elementos totales hay en la lista
'''
print(len(inventario))
'''
4.- Acceso y modifica "teclado" por "teclado mecanico" 
'''
inventario[5] = "teclado mecanico"
print(inventario)
'''
5.- Slicing: crea una nueva lista llamada "promocion", debe contener solo los 3 elementos de la lista "inventario
'''
promocion = inventario
print(promocion[:4])
'''
6.- mostrar la lista de inventario ordenado alfabeticamente
'''
inventario.sort()
print(inventario)
'''
7.- Eliminar el ultimo elemento de la lista inventario mostrando el elemento eliminado y la lsta final XD
'''
inventario.pop()
print(inventario)