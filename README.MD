# FUTURO SEGURO

## Autores
-Sofia Correa Carmona
-Isabella Ceballos Bedoya

## ¿Qué es y para qué sirve?

### Descripción
Si necesitas calcular tu pensión, Futuro Seguro es tu mejor opción, con esta herramienta podrás estimar el monto de tu pensión.  La calculadora utiliza datos como la edad actual, el género, el salario, las semanas laboradas, el ahorro acumulado, la rentabilidad del fondo y la tasa de administración para proyectar el ingreso durante la jubilación. Esta herramienta digital es fundamental para planificarnos financieramente, para tomar decisiones, pero sobre todo para muestra seguridad. Es un tema que abarca todas las edades. 

## Objetivo
Nuestro objetivo como Futuro Seguro es permitir a los usuarios planificar su futuro financiero en la jubilación. Al ofrecer una estimación del ingreso futuro, los usuarios pueden tomar decisiones informadas sobre sus ahorros y contribuciones, así como ajustar su planificación financiera para asegurar un retiro cómodo.


## ¿Cómo Utilizar la Calculadora / cómo lo ejecuto?

Requisitos Previos Antes de comenzar, asegúrate de tener lo siguiente:

•	Computadora: Necesitarás una computadora (Windows, macOS o Linux).

•	Conexión a Internet: Para descargar la carpeta "CalculadoraPensional".

•	Programa de Extracción de Archivos: Como WinRAR, 7-Zip o el descompresor integrado de tu sistema.

•	Espacio en Disco: Suficiente para almacenar y ejecutar la calculadora.

•	Permisos de Ejecución: Puede que necesites permisos de administrador para ejecutar el archivo "main_console_interfaz".


## Instrucciones de Uso

### 1.	Descarga de Archivos:
Descarga el archivo comprimido " PensionCalculator.-main ".

### 2.	Extracción de Archivos:
Usa un programa de extracción para descomprimir "PensionCalculator.-main".
Extrae los archivos en una ubicación de tu elección.

### Ubicación del Ejecutable:
En la carpeta extraída, localiza el archivo ejecutable "main_console_inferfaz.py" y "main_console.py".


### 3. Para ejecutar :

A.. Abre la terminal.

B.. Utiliza este comando para clonar el repositorio: git clone https://github.com/santiagocordobaf/PensionCalculator1.git

C.. A continuación ingresa el comando cd PensionCalculator1 

D.. Instalar las dependecias utilizando pip install -r requirements.txt 

E.. Por último ejecuta el comando python main_console.py o python3 main_cosole.py

F.. El programa ejecutará y mostrará un menú

Selecciona la opción 1, calcular pensión.
Ingresa la información requerida como edad, salario, semanas laboradas, etc.
Una vez veas los resultados selecciona el botón salir

#### Ejecución desde la consola :
Ejecuta el comando python main_console_interfaz.py o python3 main_cosole_interfaz.py.

Cuando se abra la ventana, selecciona el ícono de "Maximizar" (un cuadrado sobre otro cuadrado) en la parte superior derecha para ajustar la ventana.

#### Ejecución desde visual estudio :
Haz doble clic en " main_interfaz " para abrir la aplicación.

Cuando se abra la ventana, selecciona el ícono de "Maximizar" (un cuadrado sobre otro cuadrado) en la parte superior derecha para ajustar la ventana.


## 4. Uso de la Aplicación:
Introduce la información requerida como edad, salario, semanas laboradas, etc.
Haz clic en "Calcular" para obtener la estimación de tu pensión.
Los resultados se mostrarán en una nueva ventana.
Una vez veas los resultados selecciona el botón salir

## 5. Cerrar la Aplicación:
Una vez obtenidos los resultados, puedes cerrar la aplicación como cualquier otra.

## 6. Creación de la Base de datos:
Para la creación la base de datos, usamos Neon tech (https://neon.tech/) la cual nos permite la creacion de proyectos, en la cual creamos una tabla llamada "Pensiones".

En dicha tabla se guarda registro de los siguientes campos:

• ID

• edad_actual

• Sexo

• Salario_actual

• semanas_laboradas

• ahorro_actual

• rentabilidad_fondo

• tasa_administración

## 7. Conexión de la base de datos:
Para la conexión con el codigo proporcionado, se realizo de la siguiente manera:

• Lo primero es instalar la libreria necesaria para conexión con bases de datos PostgreSQL haciendo en la terminal "pip install psycopg2"

• Luego NeonTech al momento de elegir el "parameters only" nos da lo siguiente:

![Image Alt](https://github.com/santiagocordobaf/PensionCalculator1/blob/main/credenciales%20de%20ejemplo.jpg)

Ademas es importante mencionar que el PGPORT no nos lo proporciona NeonTech sino que por defecto es el "5432", siendo este un valor entero y no un string.


• Finalmente en la parte de tu codigo en python con la libreria "psycopg2" importada vas realizar lo siguiente:

![Image Alt](https://github.com/santiagocordobaf/PensionCalculator1/blob/main/conexion%20completa.jpg)









