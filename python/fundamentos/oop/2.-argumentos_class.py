# ➡️ Pasar argumentos 
# Para poder personalizar nuestras instancia vamos a pasar algunos argumentos al método __init__
# y que de esta manera podamos asignarle a los atributos los valores correspondientes.

class Usuario:
   def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

#Creacion de instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 30000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 100000, 300000)
alexiel = Usuario("Alexiel", "Retamales", "alexielretamales@liceovvh.cl", 10000000000, 1000)

#Imprimos valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel
print(alexiel.nombre)

#-----------------
#Tarea rapida
'''
Crea una clase Estudiante, y asignale los siguientes atributos:
(rut, nombre, apellido, fecha_nac)
-Crear 3 instancias para ñaclase con distintos estudiantes.
-imprimir el nombre y apellido concatenado + especialidad
'''

class Estudiante:
   def __init__(self, rut, nombre, apellido, fecha_nac):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha_nac

Jony = Usuario("22.222.222-2", "Jony", "Cartas", "01-01-1970")
Miguel = Usuario("11.111.111-1", "Miguel", "Ortos", "13-01-1999")
alexiel = Usuario("22.745.437-7", "Alexiel", "Retamales", "14-06-2008")
