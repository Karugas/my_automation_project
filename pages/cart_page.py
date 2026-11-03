from locators.products_locators import ProductLocators
from .base_page import BasePage
from locators.cart_locators import CartLocators
from pages.checkout_pages import CheckoutPage


class CartPage(BasePage):
    def check_price_and_name(self) -> dict:
        cart = self.find_elements(CartLocators.CART_LIST)

        name_item = []
        price_item = []

        for select in cart:
            # Цена товаров
            cart_price = select.find_element(*CartLocators.CART_PRICE)
            price_item.append(cart_price.text)
            # Название товаров
            cart_name = select.find_element(*CartLocators.CART_NAME)
            name_item.append(cart_name.text)

        return {"name": name_item, "price": price_item}

    def empty_cart(self):
        return self.find_element(ProductLocators.EMPTY_CART).get_attribute("aria-label")

    def remove_item_in_cart(self):
        self.find_element(CartLocators.REMOVE_ITEM).click()
        item_removed = self.find_element(CartLocators.CHECK_REMOVED_ITEM).is_displayed()
        assert item_removed is False, "Товар не удалён, отображается в списке"

    def cart_list_empty(self):
        return self.find_element(CartLocators.CART_LIST)

    def go_to_checkout(self):
        self.find_element(CartLocators.BUTTON_CHECKOUT).click()
        return CheckoutPage(self.browser, self.browser.current_url)
