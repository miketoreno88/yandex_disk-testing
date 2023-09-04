from pages.base_page import BasePage
from locators.elements_page_locators import DiskYandexLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException



class DiskYandexPage(BasePage):
    
    def create_file(self, file_name):
        self.button_create = self.wait_for_element(DiskYandexLocators.BUTTON_CREATE)
        self.button_create.click()
        self.button_text_doc = self.wait_for_element(DiskYandexLocators.BUTTON_TEXT_DOC)
        self.button_text_doc.click()

        self.name_text_input = self.wait_for_element(DiskYandexLocators.NAME_TEXT_INPUT)
        self.name_text_input.click()
        self.name_text_input.send_keys(Keys.CONTROL + "a")  # element.clear() не работает
        self.name_text_input.send_keys(Keys.DELETE) 

        self.name_text_input.send_keys(file_name)

        self.button_create_doc = self.wait_for_element(DiskYandexLocators.BUTTON_CREATE_DOC)
        self.button_create_doc.click()
        return file_name

    def counting_sum_elements(self):
        try:
            self.listing_items_child_elements = self.wait_for_elements(DiskYandexLocators.LISTING_ITEMS_CHILD_ELEMENTS)
            child_count = len(self.listing_items_child_elements)
        except TimeoutException:
            child_count = 0
        
        return child_count


    def created_file(self, file_name):
        file_locator = (By.XPATH, f"//span[contains(text(), '{file_name}.docx')]")
        name_created_file = name_created_file = self.wait_for_element(file_locator).text
        return name_created_file
    
    def log_out(self):
        self.button_user = self.wait_for_element(DiskYandexLocators.BUTTON_USER)
        self.button_log_out = self.wait_for_element(DiskYandexLocators.BUTTON_LOG_OUT)
        self.button_user.click()
        self.button_log_out.click()