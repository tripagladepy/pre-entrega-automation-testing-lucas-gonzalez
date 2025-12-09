<!-- # pre-entrega-automation-testing-lucas-gonzalez

Proyecto Automatizacion QA - TALENTOTECH - Lucas Gonzalez

Propósito del proyecto
Automatizar diferentes procesos sobre una pagina web (saucedemo):

    1. Realizar un inicio de sesion exitoso.
    2. Verificar si existen los productos dentro de la pagina.
    3. Verificar si funciona correctamente el carrito de compras.

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

        pytest -v --html=reporte.
        
         -->

# 🧪 Proyecto Final – Framework de Automatización de Pruebas en Python

Este repositorio contiene el Trabajo Final Integrador del curso de Automatización con Python.  
El objetivo del proyecto es desarrollar un framework de testing automatizado completo, combinando pruebas de UI con Selenium WebDriver y pruebas de API con Requests, aplicando el patrón de diseño Page Object Model (POM), generando reportes HTML y ejecutando los tests de forma automática mediante GitHub Actions (CI/CD).


---

## 🚀 Tecnologías utilizadas

- Python 3.10
- Pytest
- Selenium WebDriver
- Requests
- Page Object Model (POM)
- Pytest-HTML
- Faker
- Webdriver Manager
- Git & GitHub
- GitHub Actions

---

## 📁 Estructura del Proyecto
```
proyecto-final-automation-testing-Gonzalez-Lucas/
│
├── api_tests/ # Tests de API
├── pages/ # Page Object Model (POM)
├── tests/ # Tests de UI
├── utils/ # Utilidades
├── reports/ # Reportes HTML
├── screenshots/ # Capturas de fallos
├── conftest.py # Fixtures
├── pytest.ini # Configuración
├── requirements.txt # Dependencias
└── .github/workflows/ # CI/CD
```
---

## ✅ Funcionalidades Implementadas

### 🔹 Pruebas de UI (Selenium)

- Login exitoso
- Login con credenciales inválidas (escenario negativo)
- Navegación por catálogo
- Agregado de productos al carrito
- Checkout completo
- Implementadas con Page Object Model
- Parametrización de datos
- Captura automática de screenshots en fallos
- Pruebas independientes

### 🔹 Pruebas de API (Requests)

- GET – Obtener recursos
- POST – Crear recursos
- DELETE – Eliminar recursos
- Validación de códigos de estado
- Validación de estructura JSON
- Assertions de contenido

---

## 📊 Reportes HTML

- Los reportes se generan automáticamente con `pytest-html`.
- Incluyen detalle de tests ejecutados, estado, duración y capturas de pantalla en fallos.

**Ubicación del reporte:** `reports/report.html`

---

## 📝 Logging

Se implementó un sistema de logging para registrar los pasos principales de cada prueba y facilitar la depuración de errores.

---

## 🤖 Integración Continua – GitHub Actions (CI/CD)

Las pruebas se ejecutan automáticamente al realizar un push al repositorio.  
El pipeline realiza:

1. Instalación de dependencias
2. Ejecución de todos los tests
3. Generación de reportes
4. Publicación de reportes como artifacts descargables

---

## ⚙️ Instalación del Proyecto

1. Clonar el repositorio:

    ```bash
    git clone https://github.com/tripagladepy/proyecto-final-automation-testing-Gonzalez-Lucas.git
    cd proyecto-final-automation-testing-Gonzalez-Lucas
    ```

2. Crear entorno virtual:

    ```bash
    python -m venv .venv
    ```

3. Activar entorno virtual:

    - Windows Git Bash:

        ```bash
        source .venv/Scripts/activate
        ```

4. Instalar dependencias:

    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ Ejecución de las Pruebas

- Ejecutar todos los tests:

    ```bash
    pytest
    ```

- Ejecutar con reporte HTML:

    ```bash
    pytest --html=reports/report.html --self-contained-html
    ```

---

## 📄 Visualización del Reporte

Abrir en el navegador:
```
reports/report.html
```

También se puede descargar desde GitHub Actions como artifact.

---

## 🧠 Objetivo del Proyecto

Desarrollar un framework de testing completo aplicando:

- Automatización de UI
- Automatización de API
- Page Object Model
- Parametrización
- Manejo de evidencias
- Reportes HTML
- CI/CD con GitHub Actions

---

## 👤 Autor

Lucas González  
Proyecto Final – Automatización de Pruebas  
Curso de Automation Testing - Talento Tech