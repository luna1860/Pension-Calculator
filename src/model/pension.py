# src/model/Pension.py

class Pension:
    def __init__(self, edad_actual, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion, id=None):
        self.id = id
        self.edad_actual = edad_actual
        self.sexo = sexo
        self.salario_actual = salario_actual
        self.semanas_laboradas = semanas_laboradas
        self.ahorro_actual = ahorro_actual
        self.rentabilidad_fondo = rentabilidad_fondo
        self.tasa_administracion = tasa_administracion

    def __str__(self):
        return f"Pensión Usuario {self.id}: Edad {self.edad_actual}, Sexo {self.sexo}, Salario {self.salario_actual}, Semanas Laboradas {self.semanas_laboradas}, Ahorro Actual {self.ahorro_actual}, Rentabilidad Fondo {self.rentabilidad_fondo}, Tasa Administración {self.tasa_administracion}"

def esIgual( self, comparar_con ) :
        """
        Compara el objeto actual, con otra instancia de la clase Pension
        """

        assert( self.id == comparar_con.id )
        assert( self.edad_actual == comparar_con.edad_actual )
        assert( self.sexo == comparar_con.sexo )
        assert( self.salario_actual == comparar_con.salario_actual )
        assert( self.semanas_laboradas == comparar_con.semanas_laboradas )
        assert( self.ahorro_actual == comparar_con.ahorro_actual )
        assert( self.rentabilidad_fondo == comparar_con.rentabilidad_fondo )
        assert( self.tasa_administracion == comparar_con.tasa_administracion )
