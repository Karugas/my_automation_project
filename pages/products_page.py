from .base_page import BasePage
from locators.products_locators import ProductLocators
from .cart_page import CartPage


class ProductPage(BasePage):

    def get_product_list(self):
        return self.find_element(ProductLocators.PRODUCT_LIST).text

    # Добавить 1 товар в корзину
    def add_first_product_and_get_info(self) -> dict:
        # Находим все продукты
        all_cards = self.find_elements(ProductLocators.INVENTORY_ITEM)
        target_cards = all_cards[:1]

        selected_name = []
        selected_price = []

        for card in target_cards:
            # Получаем название и цену
            product_name = card.find_element(*ProductLocators.CARD_TITLE)
            selected_name.append(product_name.text)

            product_price = card.find_element(*ProductLocators.CARD_PRICE)
            selected_price.append(product_price.text)

            # Добавляем в корзину
            card.find_element(*ProductLocators.CARD_ADD_BUTTON).click()

        # Возвращаем данные что нашли
        return {"name": selected_name, "price": selected_price}

    # Добавить 4 товара в корзину
    def add_products_and_get_info(self) -> dict:
        #Находим все продукты
        all_cards = self.find_elements(ProductLocators.INVENTORY_ITEM)
        target_cards = all_cards[:4]

        selected_name = []
        selected_price = []

        for card in target_cards:

            #Получаем название и цену
            product_name = card.find_element(*ProductLocators.CARD_TITLE)
            selected_name.append(product_name.text)

            product_price = card.find_element(*ProductLocators.CARD_PRICE)
            selected_price.append(product_price.text)

            #Добавляем в корзину
            card.find_element(*ProductLocators.CARD_ADD_BUTTON).click()

        #Возвращаем данные что нашли
        return {"name": selected_name, "price": selected_price}

    # Кнопка Delete -> Add to cart
    def check_switch_delete_on_add_to_cart(self):
        # Находим самую первую карточку
        first_card = self.find_element(ProductLocators.FIRST_PRODUCT_CARD)
        # Есть кнопка Add to cart
        return first_card.find_element(*ProductLocators.CARD_ADD_BUTTON).text

    def go_to_cart(self):
        self.find_element(ProductLocators.SHOPPING_CART).click()
        return CartPage(self.browser, self.browser.current_url)

    def item_in_cart(self):
        return self.find_element(ProductLocators.ITEM_IN_CART).text

    def delete_item(self):
        self.find_element(ProductLocators.REMOVE_ITEM).click()

    def empty_cart(self):
        return self.find_element(ProductLocators.EMPTY_CART).get_attribute("aria-label")

    def price_all_products(self):
        self.find_element(ProductLocators.PRODUCT_LIST)
        elements = self.browser.find_elements(*ProductLocators.CARD_PRICE)
        element = [element.text.replace("$", "") for element in elements]
        price = [float(x) for x in element]
        return price

    def sort_products_low_to_high(self):
        self.find_element(ProductLocators.SORT_PRODUCTS).click()
        self.find_element(ProductLocators.SORT_LOW_TO_HIGH).click()

    def sort_products_high_to_low(self):
        self.find_element(ProductLocators.SORT_PRODUCTS).click()
        self.find_element(ProductLocators.SORT_HIGH_TO_LOW).click()

    def sort_products_z_to_a(self):
        self.find_element(ProductLocators.SORT_PRODUCTS).click()
        self.find_element(ProductLocators.SORT_Z_TO_A).click()
