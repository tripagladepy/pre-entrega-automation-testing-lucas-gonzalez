# pre-entrega-automation-testing-lucas-gonzalez

Proyecto Automatizacion QA - TALENTOTECH - Lucas Gonzalez

Propósito del proyecto
Automatizar diferentes procesos sobre una pagina web (saucedemo):

    - Realizar un inicio de sesion exitoso.
    - Verificar si existen los productos dentro de la pagina.
    - Verificar si funciona correctamente el carrito de compras.

Tecnologías utilizadas
    
    - Python
    - Pytest y Pytest-html
    - Selenium
    - Webdriver Manager

Instalación de dependencias

    - Se deberá ejecutar el siguiente comando:

        pip install -r requirements.txt


Ejecución de las pruebas

    - Para ejecutar todos los casos de prueba:

        pytest -v

    - Para ejecutar todos los casos de prueba con reporte html:

        pytest -v --html=reporte.html
