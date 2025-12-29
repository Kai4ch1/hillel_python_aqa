from pw_test.pages.login import login_page
from playwright.sync_api import Page
login_page_info = login_page.LoginPage


class TestLogin:
    def __int__(self, page : Page, timeout):
        self.page = page
        self.timeout = timeout


    def test_login(self, page, timeout=5000):
        page.set_default_timeout(timeout)

        page.goto(url=login_page_info.URL)
        page.locator(login_page_info.LOGIN_FIELD).fill(login_page_info.USERNAME)
        page.locator(login_page_info.PASS_FIELD).fill(login_page_info.USER_PASS)
        page.locator(login_page_info.LOGIN_BUTTON).click()
        page.wait_for_url("https://www.saucedemo.com/inventory.html")
        assert page.locator("div.app_logo")