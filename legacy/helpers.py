from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"
USERNAME = "performance_glitch_user"  # utilizo ese username para probar el rendimiento y tener que colocar una espera mas larga al momento de hacer el login.
PASSWORD = "secret_sauce"

# Me permite que se abra el navegador y se inicie la sesion con Selenium
def get_driver():
    
    # options = Options()
    # options.add_argument("--start-maximized")  #Inicia el navegador Maximizado

    #instalacion del driver:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)


    # time.sleep(5)
    driver.implicitly_wait(5)  #espera implicita de 5 segundos. (espera global)
    return driver  

def login_saucedemo(driver):
    driver.get(URL)

    # Completo el login con las credenciales:
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    # Espera explícita(aguarda hasta que el catálogo esté visible):
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )

    # Verifica que realmente estás en la página del inventario
    assert "inventory" in driver.current_url, "Error: el login no fue exitoso"

#   time.sleep(7)

