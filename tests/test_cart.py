import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from pages.shopping_cart_page import ShoppingCartPage
from utils.data_reader import load_products


@pytest.mark.parametrize("product", load_products())
def test_carrito(driver, product):
    
    login = LoginPage(driver)   # Login
    login.abrir()
    login.login("standard_user", "secret_sauce")

    catalog = CatalogPage(driver)   # Catálogo de productos
    
    agregado = catalog.add_product_by_name(product["name"])   # Agregar producto parametrizado
    assert agregado, f"No se pudo agregar el producto '{product['name']}'"

    catalog.abrir_carrito()     # Ir al carrito

    cart = ShoppingCartPage(driver)

    items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")    # Obtener lista de nombres en el carrito
    nombres = [i.text for i in items]

    assert product["name"] in nombres, (
        f"El producto '{product['name']}' no está dentro del carrito."   # Verificar que el producto está realmente dentro
    )
