from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    FIRST = (By.ID, "first-name")
    LAST = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")

    def completar_datos(self, nombre, apellido, zip):
        self.escribir(self.FIRST, nombre)
        self.escribir(self.LAST, apellido)
        self.escribir(self.ZIP, zip)
        self.click(self.CONTINUE)

    def finalizar_compra(self):
        self.click(self.FINISH)

    def obtener_mensaje_final(self):
        """Retorna el texto final luego de finalizar la compra."""
        return self.obtener_texto(self.SUCCESS_MSG)
