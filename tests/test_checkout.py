from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.checkout_page import CheckoutPage
from utils.data_reader import load_products


def test_checkout(driver):
    
    login = LoginPage(driver)   # Login
    login.abrir()
    login.login("standard_user", "secret_sauce")

    catalog = CatalogPage(driver)   # Catálogo

    products = load_products()   # Cargar productos desde JSON
    assert len(products) > 0, "No hay productos en products.json"

    producto = products[0]   # Agregar primer producto
    producto_agregado = catalog.add_product_by_name(producto["name"])
    assert producto_agregado, f"No se pudo agregar el producto '{producto['name']}'"

    catalog.abrir_carrito()   # Ir al carrito

    cart = ShoppingCartPage(driver)

    assert cart.obtener_items() >= 1   # Verificar que al menos hay 1 item

    cart.ir_a_checkout()   # Ir a checkout

    checkout = CheckoutPage(driver)   # Completar datos
    checkout.completar_datos("Lucas", "Gonzalez", "1674")

    checkout.finalizar_compra()   # Finalizar compra