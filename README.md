## Sistema de Registro de Infracciones de Tránsito

El Sistema de Registro de Infracciones de Tránsito es una plataforma integral diseñada para administrar y gestionar información relacionada con personas, vehículos y oficiales de tránsito, con el objetivo de registrar y mantener un seguimiento eficiente de las infracciones de tráfico.

## Características principales:

  1.Interfaz Web Intuitiva:
  El sistema cuenta con una interfaz web intuitiva y fácil de usar, accesible desde cualquier navegador web y dispositivo compatible.
  Los usuarios pueden acceder al sistema mediante autenticación, garantizando la seguridad y la privacidad de los datos.

  2.Registro de Personas:
  Permite el registro de personas involucradas en infracciones de tránsito, con información detallada como nombre y correo electrónico.
  Proporciona herramientas para buscar, editar y eliminar registros de personas según sea necesario.
  
  3.Registro de Vehículos:
  Facilita el registro de vehículos involucrados en infracciones de tránsito, incluyendo detalles como placa de patente, marca y color.
  Establece relaciones entre personas y vehículos, permitiendo un seguimiento efectivo de la propiedad y la responsabilidad.
  
  4.Registro de Oficiales de Tránsito:
  Permite la gestión de oficiales de tránsito con información personal y un número único identificatorio.
  Facilita la asignación de infracciones a oficiales específicos para un seguimiento adecuado.
  
  5.Funcionalidades Administrativas:
  Ofrece funcionalidades administrativas para agregar, modificar y eliminar registros de personas, vehículos y oficiales.
  Proporciona herramientas de búsqueda y filtrado para acceder rápidamente a la información necesaria.
  
  6.Registro de Infracciones:
  Además de los registros básicos, el sistema permite registrar y documentar infracciones de tránsito, incluyendo detalles como la fecha, la ubicación y la descripción de la infracción.
  Asocia automáticamente las infracciones con las personas, vehículos y oficiales involucrados, proporcionando un historial completo de cada incidente.
  
  7.Generación de Informes:
  Facilita la generación de informes detallados sobre infracciones de tránsito, con opciones de filtrado y clasificación personalizables.
  Los informes pueden exportarse en diversos formatos para su posterior análisis y presentación.
  El Sistema de Registro de Infracciones de Tránsito es una herramienta indispensable para las autoridades encargadas de hacer cumplir las leyes de tránsito, proporcionando una plataforma centralizada para la gestión eficiente de datos y el mantenimiento de la seguridad vial. 


## Estado del Proyecto

  - En desarrollo

## Estructura del proyecto
    .
    ├── Core
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-38.pyc
    │   │   ├── settings.cpython-38.pyc
    │   │   ├── urls.cpython-38.pyc
    │   │   └── wsgi.cpython-38.pyc
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── db.sqlite3
    ├── django.log
    ├── docker-compose.yml
    ├── Dockerfile
    ├── infraccionesAPI
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       ├── 0001_initial.cpython-38.pyc
    │   │       └── __init__.cpython-38.pyc
    │   ├── models.py
    │   ├── __pycache__
    │   │   ├── admin.cpython-38.pyc
    │   │   ├── apps.cpython-38.pyc
    │   │   ├── __init__.cpython-38.pyc
    │   │   ├── models.cpython-38.pyc
    │   │   ├── serializers.cpython-38.pyc
    │   │   ├── urls.cpython-38.pyc
    │   │   └── views.cpython-38.pyc
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── infraccionesApp
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       ├── 0001_initial.cpython-38.pyc
    │   │       ├── 0002_alter_oficial_id.cpython-38.pyc
    │   │       ├── 0002_alter_persona_email.cpython-38.pyc
    │   │       ├── 0002_alter_vehiculo_options.cpython-38.pyc
    │   │       ├── 0002_remove_infraccion_email.cpython-38.pyc
    │   │       ├── 0002_rename_vehiculo_infraccion_placa_patente.cpython-38.pyc
    │   │       ├── 0003_alter_infraccion_placa_patente.cpython-38.pyc
    │   │       ├── 0003_alter_oficial_id.cpython-38.pyc
    │   │       ├── 0003_alter_persona_email.cpython-38.pyc
    │   │       ├── 0003_remove_infraccion_vehiculo.cpython-38.pyc
    │   │       ├── 0004_alter_infraccion_email.cpython-38.pyc
    │   │       ├── 0004_alter_infraccion_placa_patente.cpython-38.pyc
    │   │       ├── 0005_alter_infraccion_placa_patente.cpython-38.pyc
    │   │       └── __init__.cpython-38.pyc
    │   ├── models.py
    │   ├── __pycache__
    │   │   ├── admin.cpython-38.pyc
    │   │   ├── apps.cpython-38.pyc
    │   │   ├── __init__.cpython-38.pyc
    │   │   └── models.cpython-38.pyc
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    ├── requirements.txt
    └── users
        ├── admin.py
        ├── apps.py
        ├── __init__.py
        ├── migrations
        │   ├── 0001_initial.py
        │   ├── __init__.py
        │   └── __pycache__
        │       ├── 0001_initial.cpython-38.pyc
        │       └── __init__.cpython-38.pyc
        ├── models.py
        ├── __pycache__
        │   ├── admin.cpython-38.pyc
        │   ├── apps.cpython-38.pyc
        │   ├── __init__.cpython-38.pyc
        │   ├── models.cpython-38.pyc
        │   ├── serializers.cpython-38.pyc
        │   ├── urls.cpython-38.pyc
        │   └── views.cpython-38.pyc
        ├── serializers.py
        ├── tests.py
        ├── urls.py
        └── views.py
## Uso:
Para podes ejecutar y probar las funcionalidades del proyecto se detallan los siguientes pasos:

1. Descargar la imagen docker de la siguiente url: https://hub.docker.com/repository/docker/mergretcode/challenge_n5-app/tags
2. Descargar desde la terminal:

        docker pull mergretcode/challenge_n5-app:latest

3. Ejecutar:

        docker run -p 8000:8000 mergretcode/challenge_n5-app:latest

4. Una vez que este corriendo el servidor podremos ingresar a aplicación web:

        http://0.0.0.0:8000/admin

5. Credenciales de acceso:

        email: user_test@gmail.com
        pass: 123456
   
6. Probar funcionalidades esperadas - Personas, Vehiculos, Oficiales,

7. Infracciones API - Authentication - Endpoint:

        POST: http://127.0.0.1:8000/api/v1.0/authentication/token/

8. Parametros de entrada - Body - Postman

        {
           "email":"user_test@gmail.com",
           "password": "123456"
        }

9. Parametros de salida:

        {
          "token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        }

10. Infracciones API - cargar_infraccion - Endpoint:

        POST: http://127.0.0.1:8000/api/v1.0/cargar_infraccion/

11. Enviar en Headers el Token

12. Body:

        {
          "placa_patente": "ASD123",
          "email":"persona1@gmail.com",
          "timestamp": "",
          "comentarios": "Estacionamiento en lugar no permitido"
        
        }

13. Infracciones API - generar_informe - Endpoint:

        POST: http://127.0.0.1:8000/api/v1.0/generar_informe/
  
14.Body:
        
        {
          "email":"persona2@gmail.com"
        }
      
       
       
        
