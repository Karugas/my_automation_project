from selenium.webdriver.common.by import By

class CheckoutLocators:
    FIRST_NAME = (By.XPATH, '//input[@name="firstName"]')
    LAST_NAME = (By.XPATH, '//input[@name="lastName"]')
    ZIP_CODE = (By.XPATH, '//input[@name="postalCode"]')
    BUTTON_CONTINUE = (By.XPATH, '//input[@name="continue"]')
    BUTTON_CANCEL = (By.XPATH, '//button[@name="cancel"]')
