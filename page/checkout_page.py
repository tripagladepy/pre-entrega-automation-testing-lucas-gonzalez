from selenium.webdriver.common.by import By
from page.main_page import MainPage

class CheckoutPage(MainPage):

    FIRST = (By.ID, "first-name")
    LAST = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")

    def completar_datos(self, nombre, apellido, zip):
        self.escribir(self.FIRST, nombre)
        self.escribir(self.LAST, apellido)
        self.escribir(self.ZIP, zip)
        self.click(self.CONTINUE)

    def finalizar_compra(self):
        self.click(self.FINISH)
