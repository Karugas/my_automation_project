from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME_INPUT = (By.XPATH, '//input[@id="user-name"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@id="login-button"]')
