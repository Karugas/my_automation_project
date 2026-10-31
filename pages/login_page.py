from .base_page import BasePage
from locators.login_locators import LoginLocators
from .products_page import ProductPage


class LoginPage(BasePage):

    def login(self, username, password):
        self.find_element(LoginLocators.USERNAME_INPUT).send_keys(username)
        self.find_element(LoginLocators.PASSWORD_INPUT).send_keys(password)
        self.find_element(LoginLocators.LOGIN_BUTTON).click()

        return ProductPage(self.browser, self.browser.current_url)

    def get_error_message(self):
        return self.find_element(LoginLocators.USER_LOCKED_OUT).text
