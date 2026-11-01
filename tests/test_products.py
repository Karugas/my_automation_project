from data.user_data import TestUsers
from pages.login_page import LoginPage

link = "https://www.saucedemo.com/"


def test_add_product_to_cart(browser):
    # Авторизация
    page = LoginPage(browser, link)
    page.open()
    product_page = page.login(**TestUsers.STANDARD_USER)

    # Добавляем первый товар запоминая название и цену
    expected_info = product_page.add_first_product_and_get_info()
    print(f"\n[Каталог] Запомнил товар: {expected_info}")

    # Корзина заполнилась на +1
    cart = product_page.item_in_cart()
    assert int(cart) == 1, f"В корзине должен быть 1 товар, а их {int(cart)}"
    print(f"Товаров в корзине {int(cart)}")

    # Переходим в корзину
    cart_page = product_page.go_to_cart()

    # Проверяем название и цену товара в корзине
    actual_info = cart_page.check_price_and_name()
    print(f"[Корзина] Видим товар: {actual_info}")

    assert actual_info["name"] == expected_info["name"], "Наименования товаров в корзине не совпадают"
    assert actual_info["price"] == expected_info["price"], "Цены товаров в корзине не совпадают"


def test_delete_product_in_cart(browser):
    # Авторизация
    page = LoginPage(browser, link)
    page.open()
    product_page = page.login(**TestUsers.STANDARD_USER)

    # Добавляем первый товар в корзину
    product_page.add_first_product_and_get_info()

    # Переходим в корзину
    cart_page = product_page.go_to_cart()

    # Удаляем товар
    cart_page.remove_item_in_cart()
    print("\nТовар удалён")

    # Корзина -1
    empty_cart = cart_page.empty_cart()
    assert empty_cart == "Cart, empty", "Корзина не очистилась"


def test_delete_product(browser):
    # Авторизация
    page = LoginPage(browser, link)
    page.open()
    product_page = page.login(**TestUsers.STANDARD_USER)

    # Добавляем первый товар в корзину
    product_page.add_first_product_and_get_info()

    # Корзина заполнилась на +1
    cart = product_page.item_in_cart()
    assert int(cart) == 1, f"В корзине должен быть 1 товар, а их {int(cart)}"
    print(f"\nТоваров в корзине {int(cart)}")

    # Удаляем продукт
    product_page.delete_item()

    # "Delete" -> "Add to cart"
    product_page.check_switch_delete_on_add_to_cart()
    print("Товар удалён")

    # Корзина -1
    empty_cart = product_page.empty_cart()
    assert empty_cart == "Cart, empty", "Корзина не очистилась"
