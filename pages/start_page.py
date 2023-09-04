from .base_page import BasePage
from locators.elements_page_locators import StartPageLocators

class StartPage(BasePage):

    def start_page(self):
        self.button_enter = self.wait_for_element(StartPageLocators.BUTTON_ENTER)
        self.button_enter.click()

    def open_yandex_disk(self):
        self.avatar = self.wait_for_element(StartPageLocators.AVATAR)
        self.avatar.click()  

        self.switch_to_frame(StartPageLocators.IFRAME)
        self.disk_button = self.wait_for_element(StartPageLocators.DISK)
        self.disk_button.click()
