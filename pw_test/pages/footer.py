from playwright.sync_api import Page, expect

class Footer:
    TWITTER_BUTTON = '//footer/ul/li/a[@data-test="social-twitter"]'
    FACEBOOK_BUTTON = '//footer/ul/li/a[@data-test="social-facebook"]'
    LINKEDIN_BUTTON = '//footer/ul/li/a[@data-test="social-linkedin"]'
    FOOTER_LICENSING_TEXT = '//div[@data-test="footer-copy"]'

    def twitter_button(self, page : Page) -> None:
        assert page.locator(self.TWITTER_BUTTON)

    def facebook_button(self, page : Page) -> None:
        assert page.locator(self.FACEBOOK_BUTTON)






