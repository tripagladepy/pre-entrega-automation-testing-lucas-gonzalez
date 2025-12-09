from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    def completar_datos(self, nombre, apellido, codigo_postal):
        wait = WebDriverWait(self.driver, 20)

        # Espera sólida tanto para LOCAL como para CI
        wait.until(EC.url_contains("checkout-step-one"))

        wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(nombre)
        wait.until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(apellido)
        wait.until(EC.visibility_of_element_located(self.POSTAL_CODE)).send_keys(codigo_postal)

        wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    def finalizar_compra(self):
        wait = WebDriverWait(self.driver, 20)

        # Espera a la pantalla final del checkout
        wait.until(EC.url_contains("checkout-step-two"))

        wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()