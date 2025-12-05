from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):

    BTN_ADD = (By.CLASS_NAME, "btn_inventory")

    def agregar_producto(self):
        self.click(self.BTN_ADD)
