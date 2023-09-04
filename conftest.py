"""
Фикстура для создания и управления экземпляром WebDriver (Chrome).

Эта фикстура создает экземпляр веб-драйвера Chrome,
максимизирует окно браузера,
и завершает работу драйвера после завершения тестовой функции.

Использование:
    В тестовых функциях, которые требуют браузерное взаимодействие,
    можно передать эту фикстуру как параметр.

Пример использования:
    def test_example(driver):
        driver.get("https://www.example.com")
        # Дополнительный код теста

Фикстура будет автоматически создавать и завершать драйвер
 для каждой тестовой функции.
"""


import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
