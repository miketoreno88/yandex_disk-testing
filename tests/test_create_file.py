import pytest
from pages.login_page import LoginPage
from pages.start_page import StartPage
from pages.disk_yandex_page import DiskYandexPage
from pages.editor_page import EditorPage

import json
import time


# Function to read data from login_credentials.json
@pytest.fixture
def user_data():
    with open("data/login_credentials.json", "r", encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@pytest.mark.usefixtures("driver")
class TestCreateFile:
    def test_create_file(self, driver, user_data):
        start_page = StartPage(driver, 'http://ya.ru/')
        start_page.open()
        time.sleep(20)  # captcha
        start_page.start_page()

        login_page = LoginPage(driver)
        login_page.login(user_data["username"])
        login_page.password(user_data["password"])

        start_page.open_yandex_disk()

        driver.switch_to.window(driver.window_handles[1])

        disk_page = DiskYandexPage(driver)
        sum_elements_befor = disk_page.counting_sum_elements()

        name_file = disk_page.create_file("new_file")
 
        name_created_file = disk_page.created_file(name_file)

        print(name_created_file)
        driver.switch_to.window(driver.window_handles[2])

        editor_page = EditorPage(driver)
        editor_page.wait_name()

        driver.close()
        driver.switch_to.window(driver.window_handles[1])

        sum_elements_after = disk_page.counting_sum_elements()

        assert sum_elements_befor == sum_elements_after - 1, "Файл не создан"
        assert name_file + '.docx' == name_created_file, "Неверное имя файла"

        disk_page.log_out()