import pytest
from pages.login_page import LoginPage
from utils.data_reader import load_credentials

@pytest.mark.parametrize("cred", load_credentials())
def test_login_param(driver, cred):   
    
    #Test parametrizado de login: usa datos desde data/credentials.json
    #cred: diccionario con keys username, password, valid
    
    login = LoginPage(driver)
    login.abrir()
    login.login(cred["username"], cred["password"])

    if cred.get("valid"):
        # en saucedemo un login valido redirige al inventario (url contiene "inventory")
        assert "inventory" in driver.current_url, f"Se esperaba redireccion a inventory para {cred['username']}"
    else:
        # comprobación de mensaje de error (puede variar dependiendo de la pagina)
        error = login.obtener_error()
        assert error and len(error) > 0, f"Se esperaba mensaje de error para {cred['username']}"
