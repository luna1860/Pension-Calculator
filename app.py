from flask import Flask, flash, render_template, request
import sys
sys.path.append('src')

from model.pension import Pension
from controller.controller_pension import ControladorPension

app = Flask(__name__)     
app.config['SECRET_KEY'] = '48hj'

@app.route('/')
def menu_principal():
    ControladorPension.CrearTabla()
    return render_template('menu_principal.html')

@app.route('/nueva_simulacion', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        edad_actual = request.form['edad_actual']
        sexo = request.form['sexo']
        salario_actual = request.form['salario_actual']
        semanas_laboradas = request.form['semanas_laboradas']
        ahorro_actual = request.form['ahorro_actual']
        rentabilidad_fondo = request.form['rentabilidad_fondo']
        tasa_administracion = request.form['tasa_administracion']

        pension = Pension(edad_actual=edad_actual, sexo=sexo, salario_actual=salario_actual, semanas_laboradas=semanas_laboradas, ahorro_actual=ahorro_actual, rentabilidad_fondo=rentabilidad_fondo, tasa_administracion=tasa_administracion)
        ControladorPension.InsertarPension(pension)
        flash('Simulación guardada correctamente', 'success')
        return render_template('nueva_simulacion.html')

    return render_template('nueva_simulacion.html')


@app.route('/historial_simulaciones')
def history():
    data: None = ControladorPension.SelectAll()
    return render_template('historial_simulaciones.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
