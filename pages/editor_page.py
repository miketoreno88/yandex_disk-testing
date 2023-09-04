from pages.base_page import BasePage
from locators.elements_page_locators import EditorPageLocators


class EditorPage(BasePage):
    def wait_name(self):
        self.name_file = self.wait_for_element(EditorPageLocators.NAME_FILE)
