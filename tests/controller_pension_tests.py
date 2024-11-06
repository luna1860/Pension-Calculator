import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.model.pension import Pension
from src.controller.controller_pension import ControladorPension
import psycopg2

class TestControladorPension(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Configuración inicial para las pruebas: crear la conexión y la tabla """
        ControladorPension.CrearTabla()

    def test_crear_tabla(self):
        """ Prueba la creación de la tabla """
        try:
            ControladorPension.CrearTabla()
        except Exception as e:
            self.fail(f"Falló al crear la tabla: {e}")

    def test_insertar_pension(self):
        """ Prueba insertar un registro de pensión válido """
        pension = Pension(edad_actual=25, sexo='hombre', salario_actual=1000, semanas_laboradas=1150,
                          ahorro_actual=40000, rentabilidad_fondo=5.5, tasa_administracion=1.2)
        try:
            ControladorPension.InsertarPension(pension)
        except Exception as e:
            self.fail(f"Falló al insertar un registro de pensión: {e}")

    def test_insertar_pension_error(self):
        """ Prueba insertar un registro con datos inválidos """
        pension_invalida = Pension(edad_actual=17, sexo='hombre', salario_actual=1000, semanas_laboradas=1150,
                                   ahorro_actual=40000, rentabilidad_fondo=5.5, tasa_administracion=1.2)
        with self.assertRaises(psycopg2.Error):
            ControladorPension.InsertarPension(pension_invalida)      

    def test_buscar_pension_por_id(self):
        """ Prueba la búsqueda de un registro existente por ID """
        pension = Pension(edad_actual=21, sexo='mujer', salario_actual=1200, semanas_laboradas=1250,
                          ahorro_actual=45000, rentabilidad_fondo=6.0, tasa_administracion=1.5)
        ControladorPension.InsertarPension(pension)
        
        resultado = ControladorPension.BuscarPensionPorId(1)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.edad_actual, pension.edad_actual)

    def test_insertar_pension_datos_minimos(self):
        """ Prueba insertar una pensión con datos mínimos válidos """
        pension = Pension(edad_actual=18, sexo='mujer', salario_actual=1000, semanas_laboradas=52,
                      ahorro_actual=5000, rentabilidad_fondo=4.0, tasa_administracion=1.0)
        try:
            ControladorPension.InsertarPension(pension)
        except Exception as e:
            self.fail(f"Falló al insertar una pensión con datos mínimos: {e}")
    

    def test_insertar_pension_datos_frontera(self):
        """ Prueba insertar una pensión con edad en el límite permitido"""
        pension = Pension(edad_actual=65, sexo='mujer', salario_actual=3000, semanas_laboradas=1500,
                          ahorro_actual=70000, rentabilidad_fondo=7.0, tasa_administracion=1.0)  
        try:
            ControladorPension.InsertarPension(pension)
        except Exception as e:
            self.fail(f"Falló al insertar un registro de pensión con datos en el límite {e}")      

    def test_buscar_pension_por_id_no_existente(self):
        """ Prueba la búsqueda de un ID que no existe """
        resultado = ControladorPension.BuscarPensionPorId(9999)
        self.assertIsNone(resultado)

    def test_eliminar_tabla(self):
        """ Prueba la eliminación de la tabla """
        try:
            ControladorPension.EliminarTabla()
            ControladorPension.CrearTabla()  # La recrea para otros tests
        except Exception as e:
            self.fail(f"Falló al eliminar la tabla: {e}")     

    @classmethod
    def tearDownClass(cls):
        """ Limpieza final: eliminar la tabla y cerrar la conexión """
        ControladorPension.EliminarTabla()

if __name__ == '__main__':
    unittest.main()
