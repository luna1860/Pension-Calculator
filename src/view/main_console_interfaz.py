import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa la clase PensionCalculatorApp desde el archivo pension_interface.py
from GUI.gui_pension import PensionCalculatorApp
from kivy.app import App

if __name__ == '__main__':
    PensionCalculatorApp().run()
