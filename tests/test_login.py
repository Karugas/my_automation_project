from pages.login_page import LoginPage


def test_login_standard_user(browser):
    link = "https://www.saucedemo.com/"
    page = LoginPage(browser, link)

    page.open()
    page.login("secret_sauce", "standard_user")

    assert "inventory" in browser.current_url, "Не удалось войти!"
