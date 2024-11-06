# Para poder servir plantillas HTML desde archivos, es necesario importar el modulo render_template
from flask import Flask, flash, render_template, request
import sys
sys.path.append('src')

from model.pension import Pension
from controller.controller_pension import ControladorPension
from pension_calculator_folder.pension_calculator import Calcular

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
        try:
            edad_actual = int(request.form['edad_actual'])
            sexo = request.form['sexo']
            salario_actual = float(request.form['salario_actual'])
            semanas_laboradas = int(request.form['semanas_laboradas'])
            ahorro_actual = float(request.form['ahorro_actual'])
            rentabilidad_fondo = float(request.form['rentabilidad_fondo'])
            tasa_administracion = float(request.form['tasa_administracion'])

            # Calcular la pensión usando la clase Calcular
            calculadora = Calcular(edad_actual=edad_actual,sexo=sexo,salario_actual=salario_actual,semanas_laboradas=semanas_laboradas,ahorro_actual=ahorro_actual,rentabilidad_fondo=rentabilidad_fondo,tasa_administracion=tasa_administracion)

            # Realizar el cálculo
            ahorro_esperado, pension_anual, pension_mensual = calculadora.calcular_pension()

            pension = Pension(edad_actual=edad_actual, sexo=sexo, salario_actual=salario_actual, semanas_laboradas=semanas_laboradas, ahorro_actual=ahorro_actual, rentabilidad_fondo=rentabilidad_fondo, tasa_administracion=tasa_administracion)

            # Guardar en la base de datos
            ControladorPension.InsertarPension(pension)
            flash('Simulación guardada correctamente', 'success')
            # Resultados del cálculo a la plantilla           
            return render_template('pension.html',ahorro_esperado=ahorro_esperado,pension_anual=pension_anual,pension_mensual=pension_mensual)
    
        except ValueError:
            flash('Por favor, ingrese datos numéricos válidos.')
        except Exception as e:
            flash(f'Ocurrió un error al procesar la simulación: {str(e)}')

    return render_template('nueva_simulacion.html')


@app.route('/historial_simulaciones')
def history():
    """
    Muestra el historial de simulaciones guardadas.

    - Obtiene todas las simulaciones de la base de datos a través del controlador y
      renderiza la página de historial con los datos obtenidos.
    """
    data = ControladorPension.SelectAll()
    return render_template('historial_simulaciones.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
