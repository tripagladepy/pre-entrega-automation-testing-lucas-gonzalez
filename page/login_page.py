from selenium.webdriver.common.by import By
from page.main_page import MainPage

class LoginPage(MainPage):

    USER = (By.ID, "user-name")
    PASS = (By.ID, "password")
    BTN_LOGIN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def abrir(self):
        self.abrir_url("https://www.saucedemo.com/")

    def login(self, usuario, contraseña):
        self.escribir(self.USER, usuario)
        self.escribir(self.PASS, contraseña)
        self.click(self.BTN_LOGIN)

    def obtener_error(self):
        return self.obtener_texto(self.ERROR_MSG)