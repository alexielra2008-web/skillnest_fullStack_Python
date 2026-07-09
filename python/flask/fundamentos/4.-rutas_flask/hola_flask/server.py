from flask import Flask  

app = Flask(__name__)  

@app.route('/')   
def inicio():
    return '¡Hola Mundo!' 

@app.route('/exito')   
def exito():
    return '¡EXITOSOOOOO!' 

@app.route('/Fabri')   
def fabri():
    return '¡Hola Fabrizio Mendieta!' 

@app.route('/color/<nombre>/<color>')
def color_favorito(nombre, color):
    print(nombre)
    print(color)
    return f'Hola {nombre}, tu color favorito es el {color}'

@app.route('/saludo/<nombre>/<int:num>')
def hola_cantidad(nombre, num):
    return f'¡Hola {nombre}!'*num

# desafio 1
@app.route('/despedida/<nombre>')   
def despedida(nombre):
    print(nombre)
    return f'¡Adios {nombre} y hasta la proxia!' 

# desafio 2
@app.route('/presentacion/<nombre>/<int:edad>')
def presentacion(nombre, edad):
    return f'Hola {nombre}, tienes {edad} años de edad.'

if __name__=="__main__": 
    app.run(debug=True)