from selenium.webdriver.common.by import By


class ProductLocators:
    PRODUCT_LIST = (By.XPATH, '//div[@class="inventory_list"]')
    FIRST_PRODUCT_CARD = (By.XPATH, '//div[@class="inventory_item"][1]')
    CARD_TITLE = (By.XPATH, './/div[@class="inventory_item_name "]')
    CARD_PRICE = (By.XPATH, './/div[@class="inventory_item_price"]')
    CARD_ADD_BUTTON = (By.XPATH, './/button[contains(@id, "add-to-cart")]')
    SHOPPING_CART = (By.XPATH, '//div[@id="shopping_cart_container"]')
    ITEM_IN_CART = (By.XPATH, '//span[@class="shopping_cart_badge"]')
