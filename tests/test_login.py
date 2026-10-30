from pages.login_page import LoginPage
from locators.login_locators import LoginLocators
from data.user_data import TestUsers


link = "https://www.saucedemo.com/"


def test_login_standard_user(browser):
    page = LoginPage(browser, link)
    page.open()
    page.login(**TestUsers.STANDARD_USER)

    assert "inventory" in browser.current_url, "Не удалось войти!"


def test_locked_out_user(browser):
    page = LoginPage(browser, link)
    page.open()
    page.login(**TestUsers.LOCKED_OUT_USER)
    message_error = page.get_error_message()
    assert "Sorry, this user has been locked out." in message_error, \
        f"Ожидали ошибку блокировки, но выдало '{message_error}'"

