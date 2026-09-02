import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "clave_secreta_destino"

PREDICCIONES = [
    "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
    "Un gran éxito profesional o académico llegará pronto. Tu esfuerzo dará frutos.",
    "Un viaje inesperado cambiará tu perspectiva sobre la vida.",
    "Descubrirás una nueva pasión que te traerá grandes satisfacciones y paz."
]

AFINIDADES_COLOR = {
    "rojo": "revela tu pasión, energía y determinación para superar obstáculos.",
    "green": "revela tu afinidad con el misterio y descubrimiento.",
    "verde": "revela tu afinidad con el misterio y descubrimiento.",
    "azul": "revela tu tranquilidad, sabiduría y serenidad interior.",
    "morado": "revela tu conexión con la intuición, magia y espiritualidad.",
    "amarillo": "revela tu optimismo, creatividad y luz interior."
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    session["nombre"] = request.form.get("nombre")
    session["edad"] = request.form.get("edad")
    session["color"] = request.form.get("color", "").strip().lower()
    session["animal"] = request.form.get("animal", "").strip().lower()
    
    session["prediccion"] = random.choice(PREDICCIONES)
    session["numero_suerte"] = random.randint(1, 99)
    
    return redirect(url_for("futuro"))

@app.route("/futuro")
def futuro():
    if "nombre" not in session:
        return redirect(url_for("index"))
        
    color_usuario = session.get("color", "verde")
    afinidad_color = AFINIDADES_COLOR.get(
        color_usuario, 
        "revela tu afinidad con el misterio y descubrimiento."
    )
    
    return render_template("futuro.html", afinidad_color=afinidad_color)

@app.route("/limpiar")
def limpiar():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)