from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage:
    USERNAME_IMPUT = (By.ID, "user-name")
    PASSWORD_IMPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def