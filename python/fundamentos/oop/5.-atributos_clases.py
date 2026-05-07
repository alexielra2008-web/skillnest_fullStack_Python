# Atributos; métodos de clase, métodos estáticos

# Función repaso.
# Crear una función que valide usuario y contraseña

def validadordeusuario(user, password):
    if user == "matias123" and password == "matias123":
        print(f"Bienvenido, {user}!")
        return True
    else:
        print("Vayase a la mierda")
        return False

def enviarDatos():
    usrname = input("Ingrese su nombre de ususario: ")
    password = input("Ingrese su contraseña: ")
    validador = validadordeusuario(usrname, password)

enviarDatos()

# Definición de la calse 
class estudiante:
    #Atributo de clase
    colegio = "Liceo Vate Vicente Huidobro"
    # Lista en donde se muestra todos los estudiantes
    # La lista en donde estan todos los estudiantes
    Estudiantes = []

    # Metodo constructor 
    def __init__(self, nombre, nota):
        #Atributos de la instancia
        self.nombre = nombre
        self.nota = nota

# Metodo de instancia

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")
    # Agregar alumnos a la lista de estudiantes
        estudiante.Estudiantes.append(self)

    # Metodo de clase
    # Usa "CLS" porque trabaja con información de la clase
    @classmethod
    def cambiar_colegio(cls, nuevo_nombre):
        cls.colegio = nuevo_nombre

    @classmethod # Contar la cantidad de estudiantes
    def cantidad_estudiantes(cls):
        return len(cls.estudiantes)
    # Metodo estático
    # Este no usa CLS ni SELF, solo parametros
    @staticmethod
    def aprobar(nota):
        if nota >= 4.0:
            return True
        else:
            return False

# Creación de objetos (Instancias)
e1 = estudiante("Donovan", 4.0)
e2 = estudiante("Randy", 6.7)

# Uso de métodos de instancias
print("== MÉTODO DE INSTANCIAS ==")
# Mostrar datos de estudiantes
e1.mostrar_info()
print()
e2.mostrar_info()
print()