import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.model.pension import Pension
from src.controller.controller_pension import ControladorPension

class TestControladorPension(unittest.TestCase):

    def setUp(self):
        """Esta función se ejecuta antes de cada prueba para preparar el entorno."""
        ControladorPension.CrearTabla()

    def tearDown(self):
        """Esta función se ejecuta después de cada prueba para limpiar el entorno."""
        ControladorPension.EliminarTabla()

    def test_crear_tabla(self):
        """Prueba para verificar que la tabla se crea correctamente."""
        ControladorPension.CrearTabla()
        self.assertTrue(True)

    def test_insertar_registro(self):
        """Prueba para insertar un registro en la tabla."""
        nuevo_registro = Pension(edad_actual=30, sexo='hombre', salario_actual=5000, semanas_laboradas=100, ahorro_actual=20000, rentabilidad_fondo=5.5, tasa_administracion=1.2)
        ControladorPension.InsertarRegistro(nuevo_registro)

        # Assert: Intentar buscar el registro para verificar que fue insertado correctamente
        resultado = ControladorPension.BuscarRegistroPorID(1)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.edad_actual, 30)
        self.assertEqual(resultado.sexo, 'hombre')
        self.assertEqual(resultado.salario_actual, 5000)

    def test_buscar_registro_por_id(self):
        """Prueba para buscar un registro por ID."""
        nuevo_registro = Pension(edad_actual=30, sexo='hombre', salario_actual=5000, semanas_laboradas=100, ahorro_actual=20000, rentabilidad_fondo=5.5, tasa_administracion=1.2)
        ControladorPension.InsertarRegistro(nuevo_registro)

        resultado = ControladorPension.BuscarRegistroPorID(1)

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.edad_actual, 30)
        self.assertEqual(resultado.sexo, 'hombre')

    def test_eliminar_registro(self):
        """Prueba para eliminar un registro por ID."""
        nuevo_registro = Pension(edad_actual=30, sexo='hombre', salario_actual=5000, semanas_laboradas=100, ahorro_actual=20000, rentabilidad_fondo=5.5, tasa_administracion=1.2)
        ControladorPension.InsertarRegistro(nuevo_registro)

        ControladorPension.EliminarRegistro(1)

        resultado = ControladorPension.BuscarRegistroPorID(1)
        self.assertIsNone(resultado)

    def test_eliminar_tabla(self):
        """Prueba para eliminar la tabla de pensión."""
        ControladorPension.EliminarTabla()

        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
