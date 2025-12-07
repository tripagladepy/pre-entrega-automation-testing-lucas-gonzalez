from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CatalogPage(BasePage):
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_BUTTON = (By.ID, "shopping_cart_container")
    TITLE = (By.CLASS_NAME, "title")

    def page_title(self):
        return self.obtener_texto(self.TITLE)

    def obtener_cantidad_items(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def abrir_carrito(self):
        self.click(self.CART_BUTTON)

    def add_product_by_name(self, product_name):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for item in items:
            title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if title.strip() == product_name.strip():
                btn = item.find_element(By.CSS_SELECTOR, "button.btn_inventory")
                btn.click()
                return True
        return False
