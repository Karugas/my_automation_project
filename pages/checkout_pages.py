from .base_page import BasePage
from locators.checkout_locators import CheckoutLocators


class CheckoutPage(BasePage):
    def input_information_user(self, first_name, last_name, postal_code):
        self.find_element(CheckoutLocators.FIRST_NAME).send_keys(first_name)
        self.find_element(CheckoutLocators.LAST_NAME).send_keys(last_name)
        self.find_element(CheckoutLocators.ZIP_CODE).send_keys(postal_code)

    def checkout_continue(self):
        self.find_element(CheckoutLocators.BUTTON_CONTINUE).click()
