from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_url(self, url):
        logger.info(f"Abrir URL: {url}")
        self.driver.get(url)

    def encontrar(self, locator):
        logger.info(f"Encontrar elemento: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        logger.info(f"Click en: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def escribir(self, locator, texto):
        logger.info(f"Escribir '{texto}' en: {locator}")
        elem = self.encontrar(locator)
        elem.clear()
        elem.send_keys(texto)

    def obtener_texto(self, locator):
        logger.info(f"Obtener texto de: {locator}")
        return self.encontrar(locator).text
