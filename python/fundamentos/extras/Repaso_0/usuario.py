from conexion import Conexion

class Usuario:

    def __init__(self, id=None, usuario="", password="", tipo=2):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.tipo = tipo

    # Registrar
    def crear_usuario(self):
        conexion = Conexion()
        con = conexion.conectar()

        cursor = con.cursor()

        sql = """
        INSERT INTO usuarios(usuario,password,tipo_usuario)
        VALUES(%s,%s,%s)
        """

        cursor.execute(sql,(self.usuario,self.password,self.tipo))

        con.commit()

        conexion.cerrar()

    # Listar
    def listar_usuarios(self):

        conexion = Conexion()
        con = conexion.conectar()

        cursor = con.cursor()

        sql="""
        SELECT u.id,
               u.usuario,
               t.nombre
        FROM usuarios u
        INNER JOIN tipo_usuario t
        ON u.tipo_usuario=t.id
        """

        cursor.execute(sql)

        datos=cursor.fetchall()

        conexion.cerrar()

        return datos

    # Buscar

    def buscar_usuario(self,id):

        conexion=Conexion()
        con=conexion.conectar()

        cursor=con.cursor()

        sql = """
SELECT
    u.id,
    u.usuario,
    u.password,
    t.nombre
FROM usuarios u
INNER JOIN tipo_usuario t
    ON u.tipo_usuario = t.id
WHERE u.id = %s
"""

        cursor.execute(sql,(id,))

        dato=cursor.fetchone()

        conexion.cerrar()

        return dato

    # Modificar

    def modificar_usuario(self):

        conexion=Conexion()
        con=conexion.conectar()

        cursor=con.cursor()

        sql="""
        UPDATE usuarios
        SET usuario=%s,
            password=%s,
            tipo_usuario=%s
        WHERE id=%s
        """

        cursor.execute(sql,
                       (self.usuario,
                        self.password,
                        self.tipo,
                        self.id))

        con.commit()

        conexion.cerrar()

    # Eliminar

    def eliminar_usuario(self,id):

        conexion=Conexion()
        con=conexion.conectar()

        cursor=con.cursor()

        sql="DELETE FROM usuarios WHERE id=%s"

        cursor.execute(sql,(id,))

        con.commit()

        conexion.cerrar()

    # Login

    def iniciar_sesion(self,usuario,password):

        conexion=Conexion()
        con=conexion.conectar()

        cursor=con.cursor()

        sql = """
SELECT
    u.id,
    u.usuario,
    u.password,
    t.nombre
FROM usuarios u
INNER JOIN tipo_usuario t
    ON u.tipo_usuario=t.id
WHERE u.usuario=%s
AND u.password=%s
"""

        cursor.execute(sql,(usuario,password))

        dato=cursor.fetchone()

        conexion.cerrar()

        return dato