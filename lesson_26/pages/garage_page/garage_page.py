from playwright.sync_api import Page

from lesson_26.base_classes.base_page import BasePage

class GaragePage(BasePage):

    MY_PROFILE_BUTTON = "#userNavDropdown"

    def check_url(self, expected_url):
        return self.get_current_url() == expected_url

    def check_my_profile_button(self):
        return self.is_visible(self.MY_PROFILE_BUTTON)

