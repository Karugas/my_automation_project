from pages.login_page import LoginPage
from data.user_data import TestUsers

link = "https://www.saucedemo.com/"


def test_login_standard_user(browser):
    page = LoginPage(browser, link)

    page.open()
    page.login(**TestUsers.STANDARD_USER)

    assert "inventory" in browser.current_url, "Не удалось войти!"

#def test_locked_out_user(browser):