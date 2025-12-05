from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ShoppingCartPage(BasePage):

    ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BTN = (By.ID, "checkout")

    def obtener_items(self):
        return len(self.driver.find_elements(*self.ITEMS))

    def ir_a_checkout(self):
        self.click(self.CHECKOUT_BTN)
