from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ShoppingCartPage(BasePage):

    ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def obtener_items(self):
        # Espera a que al menos un item sea VISIBLE (no solo presente)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.ITEMS)
        )
        return len(self.driver.find_elements(*self.ITEMS))

    def ir_a_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
