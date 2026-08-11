from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Precios de las frutas
PRECIOS = {
    'manzana': 2.5,
    'platano': 1.8,
    'naranja': 3.0,
    'fresa': 4.5,
    'uva': 3.8,
    'pina': 5.0,
    'sandia': 4.2,
    'mango': 3.5
}

# Nombres formables de las frutas para mostrar en la interfaz
NOMBRES_FRUTAS = {
    'manzana': 'Manzana',
    'platano': 'Plátano',
    'naranja': 'Naranja',
    'fresa': 'Fresa',
    'uva': 'Uva',
    'pina': 'Piña',
    'sandia': 'Sandía',
    'mango': 'Mango'
}

# Archivos de imágenes para cada fruta
IMAGENES_FRUTAS = {
    'manzana': 'manzana.png',
    'platano': 'platano.jpg',
    'naranja': 'naranja.webp',
    'fresa': 'fresa.png',
    'uva': 'uva.png',
    'pina': 'pina.jpg',
    'sandia': 'sandia.jpg',
    'mango': 'mango.jpg'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/frutas')
def frutas():
    return render_template('frutas.html')

@app.route('/checkout', methods=['POST'])
def checkout():
    # Información del cliente recibida del formulario
    nombre = request.form.get('nombre', '')
    email = request.form.get('email', '')
    direccion = request.form.get('direccion', '')

    items_orden = []
    total_frutas = 0
    total_pagar = 0.0

    # Iterar sobre las frutas recibidas en la solicitud POST
    for fruta_id, precio in PRECIOS.items():
        cantidad_str = request.form.get(fruta_id, '0')
        # Conversión del dato recibido a número entero
        cantidad = int(cantidad_str) if cantidad_str.isdigit() else 0
        
        if cantidad > 0:
            subtotal = cantidad * precio
            items_orden.append({
                'nombre': NOMBRES_FRUTAS[fruta_id],
                'imagen': IMAGENES_FRUTAS[fruta_id],
                'precio': precio,
                'cantidad': cantidad,
                'subtotal': subtotal
            })
            total_frutas += cantidad
            total_pagar += subtotal

    return render_template(
        'checkout.html',
        nombre=nombre,
        email=email,
        direccion=direccion,
        items=items_orden,
        total_frutas=total_frutas,
        total_pagar=round(total_pagar, 2)
    )

if __name__ == '__main__':
    app.run(debug=True)