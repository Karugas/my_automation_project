from selenium.webdriver.common.by import By


class CheckoutLocators:
    FIRST_NAME = (By.XPATH, '//input[@name="firstName"]')
    LAST_NAME = (By.XPATH, '//input[@name="lastName"]')
    ZIP_CODE = (By.XPATH, '//input[@name="postalCode"]')
    BUTTON_CONTINUE = (By.XPATH, '//input[@name="continue"]')
    BUTTON_CANCEL = (By.XPATH, '//button[@name="cancel"]')
    BUTTON_CANCEL_OVERVIEW = (By.XPATH, '//button[@name="cancel"]')
    BUTTON_FINISH = (By.XPATH, '//button[@name="finish"]')
    BUTTON_BACK_HOME = (By.XPATH, '//button[@name="back-to-products"]')
    CHECKOUT_LIST = (By.XPATH, '//div[@class="cart_item"]')
    CHECKOUT_PRICE = (By.XPATH, './/div[@class="inventory_item_price"]')
    CHECKOUT_NAME = (By.XPATH, './/div[@class="inventory_item_name"]')
    CHECKOUT_ITEM_TOTAL = (By.XPATH, '//div[@class="summary_subtotal_label"]')
    TAX = (By.XPATH, '//div[@class="summary_tax_label"]')
    TOTAL_PRICE = (By.XPATH, '//div[@class="summary_total_label"]')
