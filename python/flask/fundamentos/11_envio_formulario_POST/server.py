"""
===========================================
Formulario de Usuarios
===========================================

Aplicación Flask para recibir información
mediante un formulario utilizando POST.
"""

# ==========================================
# Importaciones
# ==========================================

from flask import Flask, render_template, request, redirect


# ==========================================
# Crear aplicación Flask
# ==========================================

app = Flask(__name__)


# ==========================================
# Ruta principal
# ==========================================

@app.route("/")
def index():
    """
    Muestra el formulario al usuario.
    """
    return render_template("index.html")


# ==========================================
# Procesar formulario
# ==========================================

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():

    # Obtener información del formulario
    nombre = request.form["nombre"]
    email = request.form["email"]
    edad = request.form["edad"]
    ciudad = request.form["ciudad"]
    telefono = request.form["telefono"]

    # Mostrar información en la terminal
    print("==================================")
    print("Usuario registrado correctamente")
    print("==================================")
    print("Nombre   :", nombre)
    print("Correo   :", email)
    print("Edad     :", edad)
    print("Ciudad   :", ciudad)
    print("Teléfono :", telefono)
    print("==================================")

    # Regresar al formulario
    return redirect("/")


# ==========================================
# Ejecutar servidor
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)