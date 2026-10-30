from .base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def login(self, username, password):
        self.find_element(LoginLocators.USERNAME_INPUT).send_keys(username)
        self.find_element(LoginLocators.PASSWORD_INPUT).send_keys(password)
        self.find_element(LoginLocators.LOGIN_BUTTON).click()
