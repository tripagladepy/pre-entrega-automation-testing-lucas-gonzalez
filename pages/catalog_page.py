from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CatalogPage(BasePage):

    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_BUTTON = (By.ID, "shopping_cart_container")

    def obtener_cantidad_items(self):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.INVENTORY_ITEMS)
        )
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return len(items)

    def add_product_by_name(self, product_name):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.INVENTORY_ITEMS)
        )

        items = self.driver.find_elements(*self.INVENTORY_ITEMS)

        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name.strip() == product_name.strip():
                boton = item.find_element(By.TAG_NAME, "button")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", boton)
                boton.click()
                return True

        return False

    def abrir_carrito(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_BUTTON)
        )
        self.click(self.CART_BUTTON)
