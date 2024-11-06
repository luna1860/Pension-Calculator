# Para poder servir plantillas HTML desde archivos, es necesario importar el modulo render_template
from contextlib import redirect_stderr
from flask import Flask, flash, render_template, request

from src.model.pension import Pension
from src.controller.controller_pension import ControladorPension
from src.pension_calculator_folder.pension_calculator import Calcular

# Flask constructor: crea una variable que nos servirá para comunicarle a Flask
# la configuración que queremos para nuestra aplicación
app = Flask(__name__)     
app.config['SECRET_KEY'] = '48hj'

# Ruta para el menú principal
@app.route('/')
def menu_principal():
    ControladorPension.CrearTabla()
    return render_template('menu_principal.html')

@app.route('/nueva_simulacion', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        try:
            # Obtener y validar datos del formulario
            edad_actual = int(request.form.get('edad_actual'))
            sexo = request.form.get('sexo')
            salario_actual = int(request.form.get('salario_actual'))
            semanas_laboradas = int(request.form.get('semanas_laboradas'))
            ahorro_actual = int(request.form.get('ahorro_actual'))
            rentabilidad_fondo = int(request.form.get('rentabilidad_fondo'))
            tasa_administracion = int(request.form.get('tasa_administracion'))

            # Calcular la pensión usando la clase Calcular
            calculadora = Calcular(
                edad_actual=edad_actual,
                sexo=sexo,
                salario_actual=salario_actual,
                semanas_laboradas=semanas_laboradas,
                ahorro_actual=ahorro_actual,
                rentabilidad_fondo=rentabilidad_fondo,
                tasa_administracion=tasa_administracion
            )

            # Realizar el cálculo
            ahorro_esperado, pension_anual, pension_mensual = calculadora.calcular_pension()

            # Crear una nueva instancia de Pension
            nueva_pension = Pension(
                edad_actual,
                sexo,
                salario_actual,
                semanas_laboradas,
                ahorro_actual,
                rentabilidad_fondo,
                tasa_administracion
            )
            
            # Guardar en la base de datos
            ControladorPension.InsertarPension(nueva_pension)
            
            flash('¡Simulación creada exitosamente!')
            # Pasar los resultados del cálculo a la plantilla
            return render_template('/pension.html',
                                   ahorro_esperado=ahorro_esperado,
                                    pension_anual=pension_anual,
                                     pension_mensual=pension_mensual )  # Redirigir tras el éxito

        except ValueError:
            flash('Por favor, ingrese datos numéricos válidos.')
        except Exception as e:
            flash(f'Ocurrió un error al procesar la simulación: {str(e)}')
            # Se puede incluir un logging para registrar errores inesperados

    return render_template('nueva_simulacion.html')


@app.route('/historial_simulaciones')
def history():
    data = ControladorPension.SelectAll()
    return render_template('historial_simulaciones.html', data=data)    

if __name__ == '__main__':
    app.run(debug=True)
