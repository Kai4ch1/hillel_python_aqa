import pytest
from playwright.sync_api import Page

import os
import dotenv
import allure

from lesson_26.base_classes.base_allure import FrontEndReports
from lesson_26.pages.login_page.login_page import RegistrationModalWithLoop
from lesson_26.pages.garage_page.garage_page import GaragePage
from lesson_26.base_classes.base_fake_info import BaseFakeInfo

dotenv.load_dotenv()


@allure.feature("Form Validation")
class TestSignUpAndSignIn(FrontEndReports):
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


    @allure.story("Registration with valid data")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_successful_registration_with_valid_data(self, page, create_valid_user):
        with allure.step("Clicking on 'Register' button with valid data"):
            self.driver.click(self.login_page.REGISTER_BUTTON)
        with allure.step("Verifying the page link after successful registration"):
            self.driver.expect_url(os.getenv("GARAGE_PAGE"))
            assert self.driver.check_my_profile_button()

    def test_name_field_validation(self, page, open_registration_modal):
        # 1 symbol in last name is prohibited for the username field
        with allure.step("entering an invalid value to 'name' field"):
            self.driver.fill(self.login_page.NAME_FIELD, "q")
        with allure.step("entering valid value to the rest of the fields"):
            self.driver.fill(self.login_page.LAST_NAME_FIELD, self.lastname)
            self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
            self.driver.fill(self.login_page.EMAIL_FIELD, self.email)
            self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
            self.driver.fill(self.login_page.RE_ENTER_PASSWORD, self.password)
        with allure.step("Verifying that button is disabled due to invalid data in the 'name' field"):
            self.driver.expect_disabled(self.login_page.REGISTER_BUTTON)

    def test_last_name_field_validation(self, page, open_registration_modal):
        # 1 symbol in last name is prohibited for the last name field
        with allure.step("entering an invalid value to 'lastname' field"):
            self.driver.fill(self.login_page.LAST_NAME_FIELD, "q")
        with allure.step("entering valid value to the rest of the fields"):
            self.driver.fill(self.login_page.NAME_FIELD, self.username)
            self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
            self.driver.fill(self.login_page.EMAIL_FIELD, self.email)
            self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
            self.driver.fill(self.login_page.RE_ENTER_PASSWORD, self.password)
        with allure.step("Verifying that button is disabled due to invalid data in the 'last_name' field"):
            self.driver.expect_disabled(self.login_page.REGISTER_BUTTON)

    def test_email_field_validation(self, page, open_registration_modal):
        # Register using email without "@" char
        with allure.step("entering an invalid value to 'email' field"):
            self.driver.fill(self.login_page.EMAIL_FIELD, self.email.replace("@", ""))
        with allure.step("entering valid value to the rest of the fields"):
            self.driver.fill(self.login_page.NAME_FIELD, self.username)
            self.driver.fill(self.login_page.LAST_NAME_FIELD, self.lastname)
            self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
            self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
            self.driver.fill(self.login_page.RE_ENTER_PASSWORD, self.password)
        with allure.step("Verifying that button is disabled due to invalid data in the 'email' field"):
            self.driver.expect_disabled(self.login_page.REGISTER_BUTTON)

    def test_password_field_validation(self, page, open_registration_modal):
        # insert 1 char to password field
        with allure.step("entering valid value to the rest of the fields"):
            self.driver.fill(self.login_page.NAME_FIELD, self.username)
            self.driver.fill(self.login_page.LAST_NAME_FIELD, self.lastname)
            self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
            self.driver.fill(self.login_page.EMAIL_FIELD, self.email)
        with allure.step("entering valid value to re-enter password field, and invalid value to 'password' field"):
            self.driver.fill(self.login_page.PASSWORD_FIELD, self.password[0:1])
            self.driver.fill(self.login_page.RE_ENTER_PASSWORD, self.password)
        with allure.step("Verifying that button is disabled due to invalid data in the 'password' field"):
            self.driver.expect_disabled(self.login_page.REGISTER_BUTTON)

    def test_reenter_password_field_validation(self, page, open_registration_modal):
        # enter 1 char to re-enter password field
        with allure.step("entering the valid password, and invalid value to 're-enter password' field"):
            self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
            self.driver.fill(self.login_page.RE_ENTER_PASSWORD, self.password[0:1])
        with allure.step("entering valid value to the rest of the fields"):
            self.driver.fill(self.login_page.NAME_FIELD, self.username)
            self.driver.fill(self.login_page.LAST_NAME_FIELD, self.lastname)
            self.driver.fill(self.login_page.PASSWORD_FIELD, self.password)
            self.driver.fill(self.login_page.EMAIL_FIELD, self.email)
        with allure.step("Verifying that button is disabled due to invalid data in the 're-enter password' field"):
            self.driver.expect_disabled(self.login_page.REGISTER_BUTTON)