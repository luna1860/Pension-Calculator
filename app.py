# Para las aplicaciones web creadas con Flask, debemos importar siempre el modulo 
from flask import Flask, request, redirect, url_for

# Para poder servir plantillas HTML desde archivos, es necesario importar el modulo render_template
from flask import render_template, request

# Flask constructor: crea una variable que nos servirá para comunicarle a Flask
# la configuración que queremos para nuestra aplicación
app = Flask(__name__)     

# Ruta para el menú principal
@app.route('/')
def menu_principal():
    return render_template('menu_principal.html')
