from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

# Clave secreta OBLIGATORIA para poder cifrar y usar session en Flask
app.secret_key = "clave_secreta_super_segura_13_redirect_flask"


@app.route("/")
def index():
    """Ruta principal: Comprueba la sesión, suma +1 por la visita

    y renderiza la plantilla.
    """
    # 1. Comprobar e incrementar contador de visitas
    if "visitas" in session:
        session["visitas"] += 1
    else:
        session["visitas"] = 1

    # 2. Comprobar e inicializar el contador de reinicios (Bonus Oro)
    if "reinicios" not in session:
        session["reinicios"] = 0

    return render_template(
        "index.html", visitas=session["visitas"], reinicios=session["reinicios"]
    )


@app.route("/incrementar_dos", methods=["POST"])
def incrementar_dos():
    """Bonus Plata: Suma +2 a las visitas.

    Sumamos +1 extra en sesión porque al redirigir a '/' se sumará el otro +1.
    """
    if "visitas" in session:
        session["visitas"] += 1
    return redirect("/")


@app.route("/incrementar_custom", methods=["POST"])
def incrementar_custom():
    """Bonus Oro: Incrementa según la cantidad ingresada en el formulario."""
    try:
        cantidad = int(request.form.get("cantidad", 0))
        if "visitas" in session:
            # Compensamos el +1 automático que ocurrirá al llegar a '/'
            session["visitas"] += cantidad - 1
    except ValueError:
        pass

    return redirect("/")


@app.route("/reiniciar", methods=["POST"])
def reiniciar():
    """Bonus Plata y Oro: Reinicia el contador de visitas a 0

    e incrementa el contador de reinicios.
    """
    # Se establece en -1 para que la recarga en '/' (visitas += 1) lo deje en 0
    session["visitas"] = -1

    if "reinicios" in session:
        session["reinicios"] += 1
    else:
        session["reinicios"] = 1

    return redirect("/")


@app.route("/destruir_sesion")
def destruir_sesion():
    """Nivel 1: Elimina toda la sesión y redirige a la ruta raíz."""
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)