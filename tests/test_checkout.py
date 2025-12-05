from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.checkout_page import CheckoutPage

def test_checkout(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login("standard_user", "secret_sauce")

    catalog = CatalogPage(driver)
    catalog.abrir_carrito()

    cart = ShoppingCartPage(driver)
    cart.ir_a_checkout()

    checkout = CheckoutPage(driver)
    checkout.completar_datos("Lucas", "Gonzalez", "1234")
