import sys
import os

# Añadir el directorio superior a sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pension_Calculator.pension_calculator import *
from sql.database import database_connection


import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# Configuración de la pantalla
Window.clearcolor = (1, 1, 1, 1)  # Color de fondo blanco

# Pantalla de Resultados
class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Imagen de título con tamaño más grande
        image = Image(source='Calculadora_pensional.jpg', size_hint_y=None, height=250)  # Aumenté el tamaño
        layout.add_widget(image)

        # Resultados: ahorro pensional, pensión anual y mensual
        self.result_labels = []
        result_data = [
            "Valor del ahorro pensional esperado:",
            "Pensión anual:",
            "Pensión mensual:"
        ]

        for result in result_data:
            name_label = Label(text=result, font_size=30, color="black", bold=True)
            value_label = Label(text="", font_size=30, color="black")
            self.result_labels.append(value_label)
            layout.add_widget(name_label)
            layout.add_widget(value_label)

        # Botones Volver y Salir
        button_layout = BoxLayout(spacing=10, size_hint_y=None, height=50)  # Ajusta el tamaño del layout de botones
        layout.add_widget(button_layout)

        volver_button = Button(text='Volver', font_size=20, size_hint=(0.4, None), size=(100, 40))  # Botón más pequeño
        volver_button.bind(on_press=self.volver_formulario)
        button_layout.add_widget(volver_button)

        salir_button = Button(text='Salir', font_size=20, size_hint=(0.4, None), size=(100, 40))  # Botón más pequeño
        salir_button.bind(on_press=self.salir)
        button_layout.add_widget(salir_button)

        self.add_widget(layout)

    def mostrar_resultado(self, valor_ahorro_pensional, pension_anual, pension_mensual):
        self.result_labels[0].text = f"{valor_ahorro_pensional:.3f}"
        self.result_labels[1].text = f"{pension_anual:.3f}"
        self.result_labels[2].text = f"{pension_mensual:.3f}"

    def volver_formulario(self, instance):
        self.manager.current = 'formulario'

    def salir(self, instance):
        App.get_running_app().stop()


# Pantalla Principal
class PrincipalScreen(Screen):
    def __init__(self, **kwargs):
        super(PrincipalScreen, self).__init__(**kwargs)
        layout = GridLayout(cols=1)
        self.add_widget(layout)

        # Imagen de bienvenida con tamaño más grande
        image = Image(source='Calculadora_pensional.jpg', size_hint_y=None, height=300)  # Aumenté el tamaño
        layout.add_widget(image)

        # Mensaje de bienvenida en color negro
        welcome_label = Label(text="[color=000000][size=40]¡Bienvenido a la calculadora de pensiones![/size][/color]", font_size=20, markup=True)
        layout.add_widget(welcome_label)

        # Botones en un layout horizontal centrados
        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        layout.add_widget(button_layout)

        # Botón Ir al Formulario
        form_button = Button(text='Ir al formulario', font_size=25, size_hint=(0.4, None), size=(150, 40))  # Botón más pequeño
        form_button.bind(on_press=self.ir_al_formulario)
        button_layout.add_widget(form_button)

        # Botón Salir
        salir_button = Button(text='Salir', font_size=25, size_hint=(0.4, None), size=(150, 40))  # Botón más pequeño
        salir_button.bind(on_press=self.salir)
        button_layout.add_widget(salir_button)

    def ir_al_formulario(self, instance):
        self.manager.current = 'formulario'

    def salir(self, instance):
        App.get_running_app().stop()


# Pantalla del Formulario
class FormScreen(Screen):
    def __init__(self, **kwargs):
        super(FormScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=[50, 20], spacing=10)
        self.add_widget(layout)

        # Imagen de título
        image = Image(source='Calculadora_pensional.jpg', size_hint_y=None, height=250)  # Aumenté el tamaño
        layout.add_widget(image)

        # Formulario
        form_layout = GridLayout(cols=2, spacing=[10, 10])
        layout.add_widget(form_layout)

        labels = ["Edad actual:", "Sexo (mujer/hombre):", "Salario actual:",
                  "Semanas laboradas:", "Ahorro actual:",
                  "Rentabilidad del fondo (%):", "Tasa de administración (%)"]

        self.inputs = []
        for label in labels:
            form_layout.add_widget(Label(text=label, font_size=20, color="black"))  # Tamaño de etiqueta reducido a 20
            input_field = TextInput(multiline=False, font_size=20)  # Tamaño del cuadro de texto igualado a 20
            form_layout.add_widget(input_field)
            self.inputs.append(input_field)

        # Botones
        button_layout = BoxLayout(spacing=10)
        layout.add_widget(button_layout)

        calcular_button = Button(text='Calcular', font_size=25, size_hint=(None, None), size=(150, 40))  # Botón más pequeño
        calcular_button.bind(on_press=self.calcular_pension)
        button_layout.add_widget(calcular_button)

        volver_button = Button(text='Volver', font_size=25, size_hint=(None, None), size=(150, 40))  # Botón más pequeño
        volver_button.bind(on_press=self.volver_principal)
        button_layout.add_widget(volver_button)

    def calcular_pension(self, instance):
        conn = None
        cursor = None
        try:
        # Obtener conexión desde la función database_connection
            conn, cursor = database_connection()  # Llama a la función sin 'self'

            if conn is None or cursor is None:
                raise Exception("No se pudo establecer la conexión a la base de datos.")

        # Aquí ya puedes hacer el cálculo y la inserción como antes
            edad_actual = int(self.inputs[0].text)
            sexo = self.inputs[1].text.lower()
            salario_actual = float(self.inputs[2].text)
            semanas_laboradas = int(self.inputs[3].text)
            ahorro_actual = float(self.inputs[4].text)
            rentabilidad_fondo = float(self.inputs[5].text)
            tasa_administracion = float(self.inputs[6].text)

            pension_calculator = Calcular(edad_actual, sexo, salario_actual, semanas_laboradas, ahorro_actual,
                                      rentabilidad_fondo, tasa_administracion)
            valor_ahorro_pensional, pension_anual, pension_mensual = pension_calculator.calcular_pension()

        # Insertar los datos en la base de datos PostgreSQL
            cursor.execute('''
                INSERT INTO pension (edad_actual, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (edad_actual, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion))

            conn.commit()

        # Mostrar el resultado en la pantalla de resultados
            result_screen = self.manager.get_screen('resultado')
            result_screen.mostrar_resultado(valor_ahorro_pensional, pension_anual, pension_mensual)
            self.manager.current = 'resultado'

        except Exception as e:
            popup = Popup(title='Error', content=Label(text=str(e)), size_hint=(None, None), size=(900, 300))
            popup.open()

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


    def volver_principal(self, instance):
        self.manager.current = 'principal'


# Clase principal de la aplicación
class PensionCalculatorApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PrincipalScreen(name='principal'))
        sm.add_widget(FormScreen(name='formulario'))
        sm.add_widget(ResultScreen(name='resultado'))
        return sm


if __name__ == '__main__':
    PensionCalculatorApp().run()

