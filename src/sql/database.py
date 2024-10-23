import sys
import os
import psycopg2


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pension_Calculator.pension_calculator import *
from sql.config import *

def database_connection():

    PGHOST = 'ep-fancy-wildflower-a5e2d0by.us-east-2.aws.neon.tech'
    PGDATABASE = 'neondb'
    PGUSER = 'neondb_owner'
    PGPASSWORD = 'nd6fXMFaw2Px'
    
    try:
        # Conectar a la base de datos
        connection = psycopg2.connect(
            database= PGDATABASE,
            user= PGUSER,
            password= PGPASSWORD,
            host= PGHOST,
            port=5432
        )
        print("Conexión exitosa a la base de datos.")
        cursor = connection.cursor()

        # Aquí puedes realizar una consulta inicial si lo deseas
        cursor.execute("SELECT VERSION();")  # Consulta de ejemplo
        record = cursor.fetchone()
        print("Versión de la base de datos:", record)

        return connection, cursor  # Devolver conexión y cursor

    except Exception as e:
        print(f"Error en la conexión a la base de datos: {e}")
        return None, None  # Devolver None si hay un error
