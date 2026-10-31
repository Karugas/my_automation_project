from .base_page import BasePage
from locators.products_locators import ProductLocators
from .cart_page import CartPage


class ProductPage(BasePage):

    def get_product_list(self):
        return self.find_element(ProductLocators.PRODUCT_LIST).text

    def add_first_product_and_get_info(self) -> dict:
        #Находим самую первую карточку
        first_card = self.find_element(ProductLocators.FIRST_PRODUCT_CARD)

        #Получаем название и цену
        product_name = first_card.find_element(*ProductLocators.CARD_TITLE).text
        product_price = first_card.find_element(*ProductLocators.CARD_PRICE).text

        #Добавляем в корзину
        first_card.find_element(*ProductLocators.CARD_ADD_BUTTON).click()
        #Возвращаем данные что нашли
        return {"name": product_name, "price": product_price}

    def go_to_cart(self):
        self.find_element(ProductLocators.SHOPPING_CART).click()
        return CartPage(self.browser, self.browser.current_url)

    def item_in_cart(self):
        return self.find_element(ProductLocators.ITEM_IN_CART).text
