from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    BASE_URL = "https://www.saucedemo.com/"

    def __init__(self, browser: WebDriver, url: str = None):
        self.browser = browser
        self.url = url or self.BASE_URL

    def open(self):
        self.browser.get(self.url)

    def find_element(self, locator):
        return self.browser.find_element(*locator)

    def find_elements(self, locator):
        return self.browser.find_elements(*locator)

    def wait_for_url(self, expected_url, timeout=5):
        """Ожидает, пока текущий URL не станет равен expected_url"""
        return WebDriverWait(self.browser, timeout).until(EC.url_to_be(expected_url))
