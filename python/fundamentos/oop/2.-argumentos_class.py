# ➡️ Pasar argumentos 
# Para poder personalizar nuestras instancia vamos a pasar algunos argumentos al método __init__
# y que de esta manera podamos asignarle a los atributos los valores correspondientes.

class Usuario:
   def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar

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
   def __init__(self, rut, nombre, apellido, especialidad, fecha_nac):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.fecha_nac = fecha_nac

Jony = Estudiante("22.222.222-2", "Jony", "Cartas", "Programacion", "01-01-1970")
Miguel = Estudiante("11.111.111-1", "Miguel", "Ortos", "Programacion", "13-01-1999")
Jacobo = Estudiante("22.745.437-7", "Jacobo", "Montes", "Programacion", "14-06-2008")

print(f"hola mi nombre es {Jacobo.nombre} {Jacobo.apellido} y soy {Jacobo.especialidad}")