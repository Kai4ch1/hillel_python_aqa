import pytest
from playwright.sync_api import Page

import os
import dotenv
from lesson_26.pages.login_page.login_page import RegistrationModalWithLoop
from lesson_26.pages.garage_page.garage_page import GaragePage
from lesson_26.base_classes.base_fake_info import BaseFakeInfo

dotenv.load_dotenv()


class TestRegistration:
    @pytest.fixture(autouse=True)
    def setup(self, page : Page):
        self.page = page
        self.driver = GaragePage(self.page)
        self.login_page = RegistrationModalWithLoop(self.page)
        self.fake = BaseFakeInfo()
        self.user = self.fake.get_full_info()
        self.username = self.user["Firstname"]
        self.lastname = self.user["Lastname"]
        self.email = self.user["Email"]
        self.password = self.user["Password"]


    def test_successful_registration_with_valid_data(self, page, create_valid_user):
        self.driver.click(self.login_page.REGISTER_BUTTON)
        self.driver.expect_url(os.getenv("GARAGE_PAGE"))
        assert self.driver.check_my_profile_button()

    def test_name_field_validation(self, page, open_registration_modal):
        # 1 symbol in last name is prohibited for the user name field

        self.driver.fill(self.login_page.NAME_FIELD, "q")
        self.driver.fill(self.login_page.LAST_NAME_FIELD, self.lastname)
        self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
        self.driver.fill(self.login_page.EMAIL_FIELD, self.email)
        self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
        self.driver.fill(self.login_page.RE_ENTER_PASSWORD, self.password)
        self.driver.expect_disabled(self.login_page.REGISTER_BUTTON)

    def test_last_name_field_validation(self, page, open_registration_modal):
        # 1 symbol in last name is prohibited for the last name field

        self.driver.fill(self.login_page.NAME_FIELD, self.username)
        self.driver.fill(self.login_page.LAST_NAME_FIELD, "q")
        self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
        self.driver.fill(self.login_page.EMAIL_FIELD, self.email)
        self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
        self.driver.fill(self.login_page.RE_ENTER_PASSWORD, self.password)
        self.driver.expect_disabled(self.login_page.REGISTER_BUTTON)

    def test_email_field_validation(self, page, open_registration_modal):
        # Register using email without "@" char

        self.driver.fill(self.login_page.NAME_FIELD, self.username)
        self.driver.fill(self.login_page.LAST_NAME_FIELD, self.lastname)
        self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
        self.driver.fill(self.login_page.EMAIL_FIELD, self.email.replace("@", ""))
        self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
        self.driver.fill(self.login_page.RE_ENTER_PASSWORD, self.password)
        self.driver.expect_disabled(self.login_page.REGISTER_BUTTON)

    def test_password_field_validation(self, page, open_registration_modal):
        # insert 1 char to password field
        self.driver.fill(self.login_page.NAME_FIELD, self.username)
        self.driver.fill(self.login_page.LAST_NAME_FIELD, self.lastname)
        self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
        self.driver.fill(self.login_page.EMAIL_FIELD, self.email)
        self.driver.fill(self.login_page.PASSWORD_FIELD, self.password[0:1])
        self.driver.fill(self.login_page.RE_ENTER_PASSWORD, self.password)
        self.driver.expect_disabled(self.login_page.REGISTER_BUTTON)

    def test_reenter_password_field_validation(self, page, open_registration_modal):
        # enter 1 char to re-enter password field

        self.driver.fill(self.login_page.NAME_FIELD, self.username)
        self.driver.fill(self.login_page.LAST_NAME_FIELD, self.lastname)
        self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
        self.driver.fill(self.login_page.EMAIL_FIELD, self.email)
        self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
        self.driver.fill(self.login_page.RE_ENTER_PASSWORD, self.password[0:1])
        self.driver.expect_disabled(self.login_page.REGISTER_BUTTON)