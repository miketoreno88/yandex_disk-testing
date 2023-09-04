from selenium.webdriver.common.by import By


class LogInLocators():

    LOGIN = (By.ID, 'passp-field-login')
    PASS = (By.ID, 'passp-field-passwd')
    BATTON_LOG_IN = (By.ID, 'passp:sign-in')
    HINT = (By.ID, 'field:input-login:hint')
    PHONE_BATTON = (By.CSS_SELECTOR, 'button[data-type="phone"]')
    PHONE = (By.ID, 'passp-field-phone')
    PHONE_HINT = (By.ID, 'field:input-phone:hint')
    PHONE_CODE = (By.ID, 'passp-field-phoneCode')


class StartPageLocators():
    BUTTON_ENTER = (By.XPATH, '//a[contains(@href, "passport.yandex.ru/auth")]')
    AVATAR = (By.XPATH, '//a[@href="https://passport.yandex.ru"]')
    IFRAME = (By.XPATH, '//iframe[@class="usermenu-portal__iframe"]')
    DISK = (By.XPATH, "//a[@href='https://disk.yandex.ru?source=main-loginmenu']")


class DiskYandexLocators():
    BUTTON_CREATE = (By.CSS_SELECTOR,
                     'button[class="Button2 Button2_view_raised Button2_size_m Button2_width_max"]')
    BUTTON_TEXT_DOC = (By.CSS_SELECTOR,
                       'button[aria-label="Текстовый документ"]')
    NAME_TEXT_INPUT = (By.CSS_SELECTOR,
                       'span[class="Textinput Textinput_view_default Textinput_size_m"] > input')
    BUTTON_CREATE_DOC = (By.CSS_SELECTOR,
                         'button[class="Button2 Button2_view_action Button2_size_m confirmation-dialog__button confirmation-dialog__button_submit "]')
    LISTING_ITEMS_CHILD_ELEMENTS = (By.XPATH,
                                    "//div[@class='listing__items']//div[contains(@class, 'listing-item_type_file')]")
    BUTTON_USER = (By.XPATH, "//img[@class='user-pic__image']")
    BUTTON_LOG_OUT = (By.XPATH, "//a[@class='menu__item menu__item_type_link legouser__menu-item legouser__menu-item_action_exit']")
    

class EditorPageLocators():
    NAME_FILE = (By.XPATH, "//title")
