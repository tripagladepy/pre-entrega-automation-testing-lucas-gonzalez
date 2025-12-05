from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage

def test_login_valido(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login("standard_user", "secret_sauce")

    catalog = CatalogPage(driver)
    assert catalog.obtener_cantidad_items() > 0


def test_login_invalido(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login("fake_user", "wrong_pass")

    assert "Username and password do not match" in login.obtener_error()
