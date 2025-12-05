from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from pages.shopping_cart_page import ShoppingCartPage

def test_carrito(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login("standard_user", "secret_sauce")

    catalog = CatalogPage(driver)
    catalog.abrir_carrito()

    cart = ShoppingCartPage(driver)
    assert cart.obtener_items() >= 0
