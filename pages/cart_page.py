from locators.products_locators import ProductLocators
from .base_page import BasePage
from locators.cart_locators import CartLocators


class CartPage(BasePage):
    def check_price_and_name(self) -> dict:
        cart = self.find_element(CartLocators.CART_LIST)

        cart_price = cart.find_element(*CartLocators.CART_PRICE).text
        cart_name = cart.find_element(*CartLocators.CART_NAME).text
        return {"name": cart_name, "price": cart_price}

    def empty_cart(self):
        return self.find_element(ProductLocators.EMPTY_CART).get_attribute("aria-label")

    def remove_item_in_cart(self):
        self.find_element(CartLocators.REMOVE_ITEM).click()
        item_removed = self.find_element(CartLocators.CHECK_REMOVED_ITEM).is_displayed()
        assert item_removed is False, "Товар не удалён, отображается в списке"

    def cart_list_empty(self):
        return self.find_element(CartLocators.CART_LIST)