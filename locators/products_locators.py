from selenium.webdriver.common.by import By


class ProductLocators:
    PRODUCT_LIST = (By.XPATH, '//div[@class="inventory_list"]')
    INVENTORY_ITEM = (By.XPATH, '//div[@class="inventory_item"]')
    FIRST_PRODUCT_CARD = (By.XPATH, '//div[@class="inventory_item"][1]')
    CARD_TITLE = (By.XPATH, './/div[@class="inventory_item_name "]')
    CARD_PRICE = (By.XPATH, './/div[@class="inventory_item_price"]')
    CARD_ADD_BUTTON = (By.XPATH, './/button[contains(@id, "add-to-cart")]')
    SHOPPING_CART = (By.XPATH, '//div[@id="shopping_cart_container"]')
    EMPTY_CART = (By.XPATH, '//a[contains(@aria-label, "Cart")]')
    ITEM_IN_CART = (By.XPATH, '//span[@class="shopping_cart_badge"]')
    REMOVE_ITEM = (By.XPATH, '//button[contains(@id, "remove")]')
    SORT_PRODUCTS = (By.XPATH, '//select[@aria-label="Sort products"]')
    SORT_LOW_TO_HIGH = (By.XPATH, '//option[@value="lohi"]')
    SORT_HIGH_TO_LOW = (By.XPATH, '//option[@value="hilo"]')
    SORT_A_TO_Z = (By.XPATH, '//option[@value="az"]')
    SORT_Z_TO_A = (By.XPATH, '//option[@value="za"]')
    SOCIAL_MEDIA_X = (By.XPATH, '//a[@data-test="social-x"]')
    SOCIAL_MEDIA_FACEBOOK = (By.XPATH, '//a[@data-test="social-facebook"]')
    SOCIAL_MEDIA_LINKEDIN = (By.XPATH, '//a[@data-test="social-linkedin"]')
    BURGER_MENU = (By.XPATH, '//button[@type="button"]')
    LOGOUT = (By.XPATH, '//a[@id="logout_sidebar_link"]')
