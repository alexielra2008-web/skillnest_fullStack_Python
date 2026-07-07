import mysql.connector
from mysql.connector import Error

class Conexion:

    def __init__(self):
        self.conexion = None

    def conectar(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",      # Cambia si tu MySQL tiene contraseña
            database="usuarios_db"
        )
        return self.conexion

    def cerrar(self):
        if self.conexion:
            self.conexion.close()