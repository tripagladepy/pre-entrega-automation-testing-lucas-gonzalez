from selenium.webdriver.common.by import By
from page.main_page import MainPage

class ProductPage(MainPage):   #Si necesitas un producto especifico.

    BTN_ADD = (By.CLASS_NAME, "btn_inventory")

    def agregar_producto(self):
        self.click(self.BTN_ADD)
