from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def wait_for_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def wait_for_elements(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def switch_to_frame(self, frame_locator):
        iframe = self.wait_for_element(frame_locator)
        self.driver.switch_to.frame(iframe)