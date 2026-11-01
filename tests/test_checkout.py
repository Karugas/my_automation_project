from data.user_data import TestUsers, CheckoutInformation
from pages.login_page import LoginPage

link = "https://www.saucedemo.com/"


def test_input_information_user(browser):
    page = LoginPage(browser, link)
    page.open()
    product_page = page.login(**TestUsers.STANDARD_USER)
    # Добавляем первый товар
    product_page.add_first_product_and_get_info()
    # Переходим в корзину
    cart_page = product_page.go_to_cart()

    # Переход на Checkout
    checkout_page = cart_page.go_to_checkout()
    # Ввод данных пользователя
    checkout_page.input_information_user(**CheckoutInformation.INFORMATION)
    # Переход на экран оплаты
    checkout_page.checkout_continue()
