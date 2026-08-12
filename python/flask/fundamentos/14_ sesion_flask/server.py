from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)

# Clave secreta obligatoria para firmar las cookies de sesión
app.secret_key = "clave-secreta-4medio"

# ==========================================
# RUTA PRINCIPAL (Formulario)
# ==========================================
@app.route("/")
def index():
    return render_template("index.html")

# ==========================================
# PROCESAR FORMULARIO (POST)
# ==========================================
@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    # Capturar datos de request.form
    nombre = request.form["nombre"]
    email = request.form["email"]
    ciudad = request.form["ciudad"]

    # Guardar en session para mantener el estado
    session["nombre_usuario"] = nombre
    session["email_usuario"] = email
    session["ciudad_usuario"] = ciudad

    # Redireccionar mediante GET a /mostrar_usuario
    return redirect(url_for("mostrar_usuario"))

# ==========================================
# MOSTRAR USUARIO
# ==========================================
@app.route("/mostrar_usuario")
def mostrar_usuario():
    return render_template("mostrar.html")

# ==========================================
# DESAFÍO ADICIONAL: RUTA /perfil
# ==========================================
@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

# ==========================================
# LIMPIAR SESIÓN (Bonus util)
# ==========================================
@app.route("/limpiar")
def limpiar():
    session.clear() # Borra todos los datos guardados en la sesión
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)