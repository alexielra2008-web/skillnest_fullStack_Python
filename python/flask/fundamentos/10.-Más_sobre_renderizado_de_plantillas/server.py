from flask import Flask, render_template

app = Flask(__name__)

# La lista ejemplificadora
@app.route("/listas")
def renderizar_listas():
    numeros = [7, 15, 22]
    
    listado_estudiantes = [
        {"nombre": "Florencia", "edad": 25},
        {"nombre": "Valentina", "edad": 30},
        {"nombre": "José", "edad": 27},
        {"nombre": "Patricio", "edad": 21}
    ]
    
    return render_template(
        "listas.html",
        numeros=numeros,
        estudiantes=listado_estudiantes
    )

# La actividdad cabronzona DEA!
@app.route("/videojuegos")
def renderizar_videojuegos():
    lista_videojuegos = [
        {"nombre": "Minecraft", "plataforma": "PC", "anio": 2011},
        {"nombre": "The Legend of Zelda: BotW", "plataforma": "Nintendo Switch", "anio": 2017},
        {"nombre": "Guilty Gear Strive", "plataforma": "PS4 / PS5", "anio": 2021},
        {"nombre": "Red Dead Redemption 2", "plataforma": "PS4 / Xbox One", "anio": 2018},
        {"nombre": "Elden Ring", "plataforma": "Multiplataforma", "anio": 2022},
        {"nombre": "Grand Theft Auto V", "plataforma": "PC / Consolas", "anio": 2013}
    ]
    
    return render_template(
        "videojuegos.html",
        videojuegos=lista_videojuegos
    )

if __name__ == "__main__":
    app.run(debug=True)