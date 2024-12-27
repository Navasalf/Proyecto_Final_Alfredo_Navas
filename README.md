Proyecto FInal 

link Video de Youtube: funcionalidad de la interfaz:
https://youtu.be/I_OjJheKxmw

Descripción Este proyecto, desarrollado en Python utilizando el framework Django, es una aplicación web tipo blog, a traves de la cual puedes crear un usuario y guardar post y ver los post de las otras personas, al igual que puedes comunicarte con otras personas.

Tecnologías Utilizadas Python: Lenguaje de programación principal. Django: marco web Python. SQLite: Base de datos ligera para el desarrollo. HTML: Lenguaje de marcado para estructurar las páginas web. CSS: Lenguaje de estilo para diseñar la apariencia de las páginas web.

Requisitos Python: Asegúrate de tener instalado Python 3.x. Puedes descargarlo desde https://www.python.org/downloads/ Virtualenv (opcional): Recomendado para aislar los entornos de proyecto. Un editor de código: Visual Studio Code, PyCharm, Sublime Text, etc.

Instalación Clonar el repositorio: Intento

git clone https://github.com/Navasalf/Proyecto_Final_Alfredo_Navas

Crear un entorno virtual (opcional): Intento: python -m venv venv source venv/bin/activate # En Linux/macOS venv\Scripts\activate # En Windows

Instalar las dependencias: Intento: pip install -r requirements.txt

Realizar las migraciones: Intento: python3 manage.py migrate

Crear un superusuario (opcional): Intento pytho:n manage.py createsuperuser

Ejecutar el servidor de desarrollo Intento: python3 manage.py runserver Ahora puedes acceder a tu aplicación en http://127.0.0.1:8000/

Estructura del proyecto app_nombre: Contiene los modelos, vistas y plantillas de tu aplicación. static: Carpeta para almacenar archivos estáticos (CSS, JavaScript, imágenes). templates: Carpeta para almacenar las plantillas HTML. Consideraciones adicionales Configuración de la base de datos: Verifica que la configuración de la base de datos en el archivo settings.py sea correcta. Colección de estáticos: Para producción, deberás recolectar los archivos estáticos usando un comando como collectstatic. Seguridad: Siempre ten en cuenta la seguridad al desarrollar aplicaciones web. Utiliza contraseñas seguras, valida los datos de entrada y mantén tus dependencias actualizadas. Pruebas: Implementa pruebas unitarias para garantizar la calidad de tu código.