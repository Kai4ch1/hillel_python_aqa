import os
import dotenv
dotenv.load_dotenv()

import pytest
from playwright.sync_api import sync_playwright, Page

from lesson_26.base_classes.base_fake_info import BaseFakeInfo
from lesson_26.pages.login_page.login_page import RegistrationModalWithLoop



@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as sp:
        browser = sp.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    page : Page = browser.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def create_valid_user(page):

        user = BaseFakeInfo()
        user_name = user.get_firstname()
        last_name = user.get_lastname()
        user_email = user.get_email()
        user_password = user.get_password()


        login_page = RegistrationModalWithLoop(page)
        login_page.goto(os.getenv("BASE_PAGE_URL_WITH_CREDENTIALS"))
        login_page.click(login_page.SIGN_UP_BUTTON)
        login_page.fill(login_page.NAME_FIELD, user_name,)
        login_page.fill(login_page.LAST_NAME_FIELD, last_name)
        login_page.fill(login_page.EMAIL_FIELD, user_email)
        login_page.fill(login_page.PASSWORD_FIELD, user_password,)
        login_page.fill(login_page.RE_ENTER_PASSWORD, user_password)


        valid_user_data = {
        "name": user_name,
        "last_name": last_name,
        "email": user_email,
        "password": user_password
        }
        yield valid_user_data


@pytest.fixture(scope="function")
def open_registration_modal(page):
    login_page = RegistrationModalWithLoop(page)
    login_page.goto(os.getenv("BASE_PAGE_URL_WITH_CREDENTIALS"))
    login_page.click(login_page.SIGN_UP_BUTTON)
    yield page
