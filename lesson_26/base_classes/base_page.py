from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self, url : str) -> None:
        self.page.goto(url, wait_until="domcontentloaded")

    def click(self, locator : str) -> None:
        self.page.locator(locator).click()

    def is_visible(self, locator : str) :
        return self.page.locator(locator).is_visible()

    def expect_visible(self, locator : str) -> None:
        expect(self.page.locator(locator)).to_be_visible()

    def expect_url(self, url : str) -> None:
        expect(self.page).to_have_url(url)

    def fill(self, locator : str, text : str) -> None:
        self.page.locator(locator).fill(text)

    def get_current_url(self) -> str:
        return self.page.url

    def check(self, locator) -> None:
        self.page.locator(locator).check()

    def uncheck(self, locator) -> None:
        self.page.locator(locator).uncheck()

    def expect_disabled(self, locator) -> None:
        expect(self.page.locator(locator)).to_be_disabled()