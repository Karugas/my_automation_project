from .base_page import BasePage
from locators.checkout_locators import CheckoutLocators


class CheckoutPage(BasePage):
    def input_information_user(self, first_name, last_name, postal_code):
        self.find_element(CheckoutLocators.FIRST_NAME).send_keys(first_name)
        self.find_element(CheckoutLocators.LAST_NAME).send_keys(last_name)
        self.find_element(CheckoutLocators.ZIP_CODE).send_keys(postal_code)

    def checkout_continue(self):
        self.find_element(CheckoutLocators.BUTTON_CONTINUE).click()

    def overview_finish(self):
        self.find_element(CheckoutLocators.BUTTON_FINISH).click()

    def tap_back_home(self):
        self.find_element(CheckoutLocators.BUTTON_BACK_HOME).click()

    def check_price_and_name_overview(self) -> dict:
        cart = self.find_element(CheckoutLocators.CHECKOUT_LIST)

        cart_price = cart.find_element(*CheckoutLocators.CHECKOUT_PRICE).text
        cart_name = cart.find_element(*CheckoutLocators.CHECKOUT_NAME).text
        return {"name": cart_name, "price": cart_price}

    def check_price_total(self):
        return self.find_element(CheckoutLocators.TOTAL_PRICE).text
