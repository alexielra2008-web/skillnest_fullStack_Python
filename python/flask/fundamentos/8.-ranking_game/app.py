from flask import Flask, render_template

app = Flask(__name__)

# Datos de jugadores con puntajes
jugadores = [
    {"nombre": "AlexGamer", "puntaje": 5000},
    {"nombre": "PixelMaster", "puntaje": 7500},
    {"nombre": "ShadowNinja", "puntaje": 8200},
    {"nombre": "CyberWarrior", "puntaje": 9100},
    {"nombre": "UltraNoob", "puntaje": 3000}
]

# Ordenar los jugadores por puntaje (de mayor a menor)
jugadores = sorted(jugadores, key=lambda x: x["puntaje"], reverse=True)


# Ruta para mostrar el ranking de jugadores
@app.route("/")
def ranking():
    return render_template(
        "ranking.html",
        jugadores=jugadores,
        color=None
    )


# Ruta para mostrar un número limitado de jugadores
@app.route("/top/<int:cantidad>")
def top(cantidad):
    return render_template(
        "ranking.html",
        jugadores=jugadores[:cantidad],
        color=None
    )


# Ruta para personalizar el color del ranking
@app.route("/color/<string:color>")
def cambiar_color(color):
    return render_template(
        "ranking.html",
        jugadores=jugadores,
        color=color
    )


# Ejecutar el servidor
if __name__ == "__main__":
    app.run(debug=True)