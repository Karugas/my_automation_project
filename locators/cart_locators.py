from selenium.webdriver.common.by import By


class CartLocators:
    CART_LIST = (By.XPATH, '//div[@class="cart_item"]')
    CART_PRICE = (By.XPATH, './/div[@class="inventory_item_price"][1]')
    CART_NAME = (By.XPATH, './/div[@class="inventory_item_name"][1]')
