from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from lesson_26.base_classes.base_page import BasePage


class RegistrationModalWithLoop(BasePage):

    NAME_FIELD = '#signupName'
    LAST_NAME_FIELD = '#signupLastName'
    SIGN_UP_BUTTON = '//div/button[@class="hero-descriptor_btn btn btn-primary"]'
    EMAIL_FIELD = '#signupEmail'
    PASSWORD_FIELD = '#signupPassword'
    RE_ENTER_PASSWORD = '#signupRepeatPassword'
    REGISTER_BUTTON = '//div/button[@class="btn btn-primary"]'

    REQUIRED_FIELDS = [
        SIGN_UP_BUTTON,
        NAME_FIELD,
        LAST_NAME_FIELD,
        EMAIL_FIELD,
        PASSWORD_FIELD,
        RE_ENTER_PASSWORD,
        REGISTER_BUTTON
    ]
    def check_if_register_button_is_disabled(self):
        raise NotImplementedError

    def __init__(self, page: Page):
        super().__init__(page)

    def test_modal_opened_with_loop(self, timeout: int = 5000):
        failed_locators = []

        for locator in self.REQUIRED_FIELDS:
            try:
                self.page.wait_for_selector(locator, state="visible", timeout=timeout)
            except PlaywrightTimeoutError:
                failed_locators.append(locator)
            except Exception as e:
                failed_locators.append(f"{locator} (Error: {str(e)})")
        if failed_locators:
            raise AssertionError(
                f"Modal verification failed. List of no visible locators: {', '.join(failed_locators)}"
            )

        return self