from page.login_page import LoginPage
from page.catalog_page import CatalogPage

def test_catalogo_muestra_items(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login("standard_user", "secret_sauce")

    catalog = CatalogPage(driver)
    assert catalog.obtener_cantidad_items() > 0
