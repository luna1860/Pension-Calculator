import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import psycopg2
from model.pension import Pension
from sql import SecretConfig

class ControladorPension:

    @staticmethod
    def CrearTabla():
        """ Crea la tabla pension en la BD """
        cursor = ControladorPension.ObtenerCursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS pension (
                            id SERIAL PRIMARY KEY,
                            edad_actual INT NOT NULL CHECK (edad_actual >= 18),
                            sexo VARCHAR(10) NOT NULL CHECK (sexo IN ('hombre', 'mujer')),
                            salario_actual DECIMAL(10, 2) NOT NULL CHECK (salario_actual >= 0),
                            semanas_laboradas INT NOT NULL CHECK (semanas_laboradas >= 0),
                            ahorro_actual DECIMAL(12, 2) NOT NULL CHECK (ahorro_actual >= 0),
                            rentabilidad_fondo DECIMAL(5, 2) NOT NULL CHECK (rentabilidad_fondo BETWEEN 0 AND 100),
                            tasa_administracion DECIMAL(5, 2) NOT NULL CHECK (tasa_administracion >= 0)
                        );""")
        cursor.connection.commit()

    @staticmethod
    def EliminarTabla():
        """ Borra la tabla de usuarios de la BD """
        cursor = ControladorPension.ObtenerCursor()

        cursor.execute("""drop table pension""" )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()

    @staticmethod
    def InsertarPension(pension: Pension):
        """ Inserta una pensión en la tabla """
        cursor = ControladorPension.ObtenerCursor()
        cursor.execute("""
            INSERT INTO pension (edad_actual, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (pension.edad_actual, pension.sexo, pension.salario_actual, pension.semanas_laboradas, pension.ahorro_actual, pension.rentabilidad_fondo, pension.tasa_administracion))
        cursor.connection.commit()

    @staticmethod
    def BuscarPensionPorId(id_usuario):
        """ Busca la pensión de un usuario por su ID """
        cursor = ControladorPension.ObtenerCursor()
        cursor.execute("""
            SELECT id, edad_actual, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion 
            FROM pension WHERE id = %s;
        """, (id_usuario,))
        fila = cursor.fetchone()
        if fila:
            return Pension(id=fila[0], edad_actual=fila[1], sexo=fila[2], salario_actual=fila[3], semanas_laboradas=fila[4], ahorro_actual=fila[5], rentabilidad_fondo=fila[6], tasa_administracion=fila[7])
        return None

    @staticmethod
    def ObtenerCursor():
        """ Conecta a la BD y devuelve el cursor """
        connection = psycopg2.connect(
            database=SecretConfig.PGDATABASE,
            user=SecretConfig.PGUSER,
            password=SecretConfig.PGPASSWORD,
            host=SecretConfig.PGHOST,
            port=SecretConfig.PGPORT
        )
        return connection.cursor()

if __name__ == "__main__":
    ControladorPension.CrearTabla()

    # Puedes insertar un registro de prueba si ya tienes la clase Pension lista
    nuevo_registro = Pension(edad_actual=30, sexo='hombre', salario_actual=5000, semanas_laboradas=100, ahorro_actual=20000, rentabilidad_fondo=5.5, tasa_administracion=1.2)
    ControladorPension.InsertarPension(nuevo_registro)
    
    # Buscar un registro (ajustado a lo que implementes, por ejemplo, por ID)
    resultado = ControladorPension.BuscarPensionPorId(1)
    print(resultado)

    ### ControladorPension.EliminarTabla()
    