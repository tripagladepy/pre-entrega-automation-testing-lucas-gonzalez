import pytest
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from utils.helpers import login_saucedemo, get_driver



@pytest.fixture # defino el fixture para el driver
def driver():
    # configuracion para consultar a selenium web driver:
    driver = get_driver()  # ejecuto la funcion que me devuelve el driver y lo almaceno en la variable.
    yield driver           # me permite darle al navegador el driver correcto.
    driver.quit()         # cierro el navegador despues de ejecutar las pruebas.

def test_login(driver):  # defino la funcion

    login_saucedemo(driver)  # llamo a la funcion que me permite hacer el login.
    assert "/inventory.html" in driver.current_url  # verifico que la url contenga /inventory.html
    titulo  = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text  # busco el titulo de la pagina.
    assert titulo == 'Products'  # verifico que el titulo sea igual a Products.

def test_catalogo(driver):
    login_saucedemo(driver)

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')  # verifico si existe la clase, en este caso el producto de la pagina.
    assert len(products) > 0  # verifico que la cantidad de productos sea mayor a 0.
def test_carrito(driver):
    login_saucedemo(driver)

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    total_products = len(products)

    products[0].find_element(By.TAG_NAME, 'button').click()  # agrego al carrito el primer producto y valido que cuando doy clic se me agrega el producto al carrito.

    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text  # verifico que el carrito tenga 1 producto.
    assert badge == "1" # verifico que el carrito tenga 1 producto.

