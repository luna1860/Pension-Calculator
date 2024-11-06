import sys
import psycopg2
sys.path.append('.')
from src.pension_calculator_folder import pension_calculator
import secret_config

def database_connection():
    try:
        # Conectar a la base de datos
        connection = psycopg2.connect(
            database= secret_config.PGDATABASE,
            user= secret_config.PGUSER,
            password= secret_config.PGPASSWORD,
            host= secret_config.PGHOST,
            port= secret_config.PGPORT
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
