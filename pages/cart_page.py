from .base_page import BasePage
from locators.cart_locators import CartLocators


class CartPage(BasePage):
    def check_price_and_name(self) -> dict:
        cart = self.find_element(CartLocators.CART_LIST)

        cart_price = cart.find_element(*CartLocators.CART_PRICE).text
        cart_name = cart.find_element(*CartLocators.CART_NAME).text
        return {"name": cart_name, "price": cart_price}
