from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
# La llave secreta es obligatoria para usar sesiones
app.secret_key = 'clave_secreta_super_segura'


@app.route('/')
def principal():
    # Comprobar e inicializar el contador de visitas
    if 'visitas' in session:
        session['visitas'] += 1
    else:
        session['visitas'] = 1

    # Comprobar e inicializar el contador de reinicios
    if 'reinicios' not in session:
        session['reinicios'] = 0

    return render_template(
        'index.html',
        visitas=session['visitas'],
        reinicios=session['reinicios'],
    )


@app.route('/sumar_dos', methods=['POST'])
def sumar_dos():
    # Sumamos 1 adicional (ya que la redirección a '/' sumará 1 más, dando un total de +2)
    if 'visitas' in session:
        session['visitas'] += 1
    return redirect('/')


@app.route('/incrementar_personalizado', methods=['POST'])
def incrementar_personalizado():
    # Formulario del Nivel 3 / Bonus de Oro
    cantidad = request.form.get('cantidad', type=int)
    if cantidad and 'visitas' in session:
        # Restamos 1 antes de sumar 'cantidad' para compensar el +1 automático de la ruta raíz
        session['visitas'] += cantidad - 1
    return redirect('/')


@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    # Reinicia el contador de visitas a 0 e incrementa el contador de reinicios
    session['visitas'] = 0
    if 'reinicios' in session:
        session['reinicios'] += 1
    else:
        session['reinicios'] = 1
    return redirect('/')


@app.route('/destruir_sesion')
def destruir_sesion():
    # Elimina toda la sesión
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)