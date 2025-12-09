# from selenium.webdriver.common.by import By
# from pages.base_page import BasePage

# class ShoppingCartPage(BasePage):

#     ITEMS = (By.CLASS_NAME, "cart_item")
#     CHECKOUT_BTN = (By.ID, "checkout")

#     def obtener_items(self):
#         return len(self.driver.find_elements(*self.ITEMS))

#     def ir_a_checkout(self):
#         self.click(self.CHECKOUT_BTN)


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ShoppingCartPage(BasePage):

    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def obtener_items(self):
        # Espera explicita para github actions
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CART_ITEMS)
        )

        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)

    def ir_a_checkout(self):
        self.click((By.ID, "checkout"))
