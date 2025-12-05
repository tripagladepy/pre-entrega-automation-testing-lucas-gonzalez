from selenium.webdriver.common.by import By
from page.main_page import MainPage

class CatalogPage(MainPage):

    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_BUTTON = (By.ID, "shopping_cart_container")

    def obtener_cantidad_items(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def abrir_carrito(self):
        self.click(self.CART_BUTTON)
