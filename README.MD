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

## Instalación y Uso

### 1. Clonar el Repositorio:

Abre tu terminal o consola de comandos y ejecuta el siguiente comando:

git clone "https://github.com/luna1860/Pension-Calculator"

### 2. Navegar al Directorio del Proyecto:

Cambia el directorio a la carpeta `Pension-Calculator`:

cd ruta\al\repositorio\Pension-Calculator

**Ejemplo:** Si clonaste el repositorio en `C:\Proyectos`, debes ejecutar:

cd C:\Proyectos\Pension-Calculator

### 3. Crear un Entorno Virtual

Antes de instalar los paquetes requeridos, es recomendable crear un entorno virtual. Ejecuta los siguientes comandos:

#### En Windows:

py -m venv .venv
.venv\Scripts\activate

#### En macOS/Linux:

python3 -m venv venv
source venv/bin/activate

### 4. Instalar los Requisitos

Una vez activado el entorno virtual, instala los paquetes necesarios desde el archivo `requirements.txt`:

pip install -r requirements.txt

### 5. Ejecutar el Programa


    
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
Las credenciales proporcionadas por NeonTech (bajo el parámetro "parameters only") se deben agregar al archivo `secret_config.py` (Puedes usar como base el archivo `secret_config_sample.py` y renombrarlo).
