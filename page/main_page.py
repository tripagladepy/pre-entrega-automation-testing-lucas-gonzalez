from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_url(self, url):
        self.driver.get(url)

    def encontrar(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def escribir(self, locator, texto):
        self.encontrar(locator).clear()
        self.encontrar(locator).send_keys(texto)

    def obtener_texto(self, locator):
        return self.encontrar(locator).text
