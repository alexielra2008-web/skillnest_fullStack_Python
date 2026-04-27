# Creación de la clase usuario - entidad 
class Usuario:
    def __init__(self): #Constructor
        self.nombre = "Nariyoshi"
        self.apellido = "Miyagi"
        self.email = "miyagi@codingdojo.la"
        self.limite_credito = 30000
        self.saldo_pagar = 0

# Instancias de una clase
miyagi = Usuario()
daniel = Usuario()
alexiel = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(miyagi.apellido)
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)
print(daniel.nombre) #Imprime: Nariyoshi

# Nuevos valores asignados a atributos de la instancia

daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "daniel@gmail.com"
daniel.limite_credito = 100000
daniel.saldo_pagar = 300000
print(daniel.nombre) #Imprime: Daniel
print(miyagi.apellido)
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)

#valores a nueva instancia
alexiel.nombre = "Alexiel"
alexiel.apellido = "Retamales"
alexiel.email = "alexielretamales@liceovvh.cl"
alexiel.limite_credito = 10000000000
alexiel.saldo_pagar = 1000

#imprir nombre de cada instancia
print(miyagi.nombre)
print(daniel.nombre)
print(alexiel.nombre)