# Futuro Seguro

## Autores:
Del numeral 1 al 5:
- Sofia Correa Carmona
- Isabella Ceballos Bedoya

Del numeral 6 al 9:
- Santiago Tavera Vargas
- Santiago Córdoba

Implementación web:
- Sara Moncada Correa
- Tomas Córdoba Urquijo

## Propósito
Futuro Seguro es una herramienta diseñada para ayudar a los usuarios a planificar su futuro financiero mediante el cálculo estimado de la pensión que recibirán al momento de su jubilación. Usando datos personales como edad, género, salario, semanas laboradas, ahorro acumulado, rentabilidad del fondo y tasa de administración, esta herramienta proporciona una estimación realista del ingreso futuro durante la jubilación. Es una solución clave para tomar decisiones informadas sobre ahorros, contribuciones y seguridad financiera, y es útil para personas de todas las edades.

## Objetivo
El objetivo de Futuro Seguro es permitir a los usuarios planificar su retiro de manera eficiente, ayudándoles a tomar decisiones informadas sobre sus ahorros y contribuciones para asegurar un futuro financiero estable. Con esta herramienta, los usuarios pueden ajustar su planificación financiera para lograr una jubilación cómoda y segura.

## ¿Cómo funciona?
La calculadora solicita información personal clave como la edad, el salario, el número de semanas laboradas, el ahorro actual, entre otros. Con estos datos, la herramienta proyecta el monto estimado de la pensión a recibir durante la jubilación.

### Información que se ingresa:
- Edad
- Salario
- Semanas laboradas
- Ahorro acumulado
- Rentabilidad del fondo
- Tasa de administración

Una vez ingresados los datos, el sistema realiza los cálculos necesarios y devuelve el valor estimado de la pensión mensual.

## ¿Cómo usar la Calculadora?

### Requisitos previos:
Asegúrate de tener lo siguiente antes de comenzar:
- Computadora: Funciona en Windows, macOS o Linux.
- Conexión a Internet: Para descargar la carpeta "CalculadoraPensional".
- Programa para extraer archivos: Como WinRAR, 7-Zip o el descompresor integrado.
- Espacio en Disco: Suficiente para almacenar y ejecutar la calculadora.
- Permisos de Ejecución: Puede ser necesario tener permisos de administrador para ejecutar el archivo "main_console_interfaz".

### Instrucciones de Uso:
1. **Descarga de Archivos:**
    Descarga el archivo comprimido "PensionCalculator.-main".

2. **Extracción de Archivos:**
    Utiliza un programa de extracción para descomprimir el archivo "PensionCalculator.-main" y extrae los archivos en la ubicación que prefieras.

3. **Ubicación del Ejecutable:**
    En la carpeta extraída, localiza los archivos ejecutables: "main_console_interfaz.py" y "main_console.py".

4. **Ejecución:**
    - **Desde la Consola:**
      - Abre la terminal.
      - Clona el repositorio con el siguiente comando:
         ```bash
         git clone https://github.com/luna1860/Pension-Calculator
         ```
      - Navega a la carpeta del proyecto:
         ```bash
         cd Pension-Calculator
         ```
    - Crea un entorno virtual:
      - **Windows:**
        ```bash
        py -m venv .venv
        .venv\Scripts\activate
        ```
      - **macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    - Instala las dependencias en el entorno virtual:
      ```bash
      pip install -r requirements.txt
      ```
    - **Desde la Consola (Interfaz de Texto):**
      - Ejecuta el siguiente comando:
         ```bash
         python src\Console\pension_calculator_console.py
         ```
    - **Desde Visual Studio:**
      - Haz doble clic en el archivo "main_interfaz" para abrir la aplicación.
      - Ajusta la ventana con el ícono de maximizar en la parte superior derecha.

5. **Uso de la Aplicación:**
    Introduce los datos solicitados (edad, salario, semanas laboradas, etc.) y presiona "Calcular" para obtener la estimación de tu pensión. Los resultados se mostrarán en una nueva ventana.

6. **Cerrar la Aplicación:**
    Puedes cerrar la aplicación como cualquier otra ventana de tu sistema operativo.

## Base de Datos
La base de datos se crea utilizando Neon Tech (https://neon.tech/), que permite la creación de proyectos. En este caso, se ha creado una tabla llamada "Pensiones", que contiene los siguientes campos:
- ID
- Edad Actual
- Sexo
- Salario Actual
- Semanas Laboradas
- Ahorro Actual
- Rentabilidad del Fondo
- Tasa de Administración

### Conexión con la Base de Datos:
Las credenciales proporcionadas por NeonTech (bajo el parámetro "parameters only") se deben agregar a tu archivo de configuración.

### Modificación de archivo `secret_config_sample.py`:
Modifica el archivo `secret_config_sample.py` con tus credenciales de la base de datos y renómbralo a `secret_config.py`.