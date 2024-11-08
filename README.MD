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

## Instrucciones de Uso:
1. **Clonar el repositorio:**
    Clona el repositorio con el comando `git clone https://github.com/luna1860/Pension-Calculator`

2. **Acceder a la ruta del proyecto:**
    Accede al proyecto con el comando 

    `cd ruta\a\ReverseMortgageSimulator`

    Ejemplo: Si clonaste el repositorio en C:\Proyectos, debes ejecutar:

    `cd C:\Proyectos\ReverseMortgageSimulator`

3. **Crear entorno virtual:**
    Antes de instalar los paquetes requeridos, se recomienda crear un entorno virtual. Ejecuta los siguientes comandos:

    `py -m venv .venv`
    `.venv\Scripts\activate`

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
