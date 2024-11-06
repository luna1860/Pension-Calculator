# Para poder servir plantillas HTML desde archivos, es necesario importar el modulo render_template
from flask import Flask, flash, render_template, request, redirect
import sys
sys.path.append('src')

from model.pension import Pension
from controller.controller_pension import ControladorPension

# Flask constructor: crea una variable que nos servirá para comunicarle a Flask
# la configuración que queremos para nuestra aplicación
app = Flask(__name__)     
app.config['SECRET_KEY'] = '48hj'

@app.route('/')
def menu_principal():
    """Renderiza el menú principal y asegura que la tabla de pensiones exista en la base de datos."""
    ControladorPension.CrearTabla()
    return render_template('menu_principal.html')

@app.route('/nueva_simulacion', methods=['GET', 'POST'])
def new():
    """
    Maneja la creación de una nueva simulación de pensión.

    - Si el método es 'POST', se obtiene la información del formulario, se crea un objeto Pension,
      y se guarda en la base de datos. Luego, muestra un mensaje de éxito.
    - Si el método es 'GET', renderiza la página de formulario para crear una nueva simulación.
    """
    if request.method == 'POST':
        edad_actual = request.form['edad_actual']
        sexo = request.form['sexo']
        salario_actual = request.form['salario_actual']
        semanas_laboradas = request.form['semanas_laboradas']
        ahorro_actual = request.form['ahorro_actual']
        rentabilidad_fondo = request.form['rentabilidad_fondo']
        tasa_administracion = request.form['tasa_administracion']

        pension = Pension(edad_actual=edad_actual, sexo=sexo, salario_actual=salario_actual, semanas_laboradas=semanas_laboradas, ahorro_actual=ahorro_actual, rentabilidad_fondo=rentabilidad_fondo, tasa_administracion=tasa_administracion)

        # Guardar en la base de datos
        ControladorPension.InsertarPension(pension)
        flash('Simulación guardada correctamente', 'success')
        return redirect('/historial_simulaciones')

    return render_template('nueva_simulacion.html')


@app.route('/historial_simulaciones')
def history():
    simulaciones = ControladorPension.SelectAll()
    return render_template('historial_simulaciones.html', simulaciones=simulaciones)

@app.route('/eliminar_historial', methods=['POST'])
def delete_history():
    """
    Maneja la eliminación del historial de simulaciones de pensión.
    """
    ControladorPension.EliminarTabla()
    flash('Historial de simulaciones eliminado correctamente', 'success')
    return render_template('historial_simulaciones.html', simulaciones=[])

if __name__ == '__main__':
    app.run(debug=True)
