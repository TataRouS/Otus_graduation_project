from pages.admin_login_page import AdminLoginPage
from selenium.webdriver.common.by import By
import time
import allure


class RegisterPage(AdminLoginPage):
    # Locators
    MY_ACCOUNT_MENU_BUTTON = (By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/a')
    MY_ACCOUNT_REGISTER_LINK = (
        By.XPATH,
        '//*[@id="top"]/div/div[2]/ul/li[2]/div/ul/li[1]/a',
    )
    MY_ACCOUNT_LOGIN_LINK = (
        By.XPATH,
        '//*[@id="top"]/div/div[2]/ul/li[2]/div/ul/li[2]/a',
    )
    FIRST_NAME_FIELD = (By.ID, "input-firstname")
    LAST_NAME_FIELD = (By.ID, "input-lastname")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.ID, "input-password")
    CHECKBOX = (By.XPATH, '//*[@id="form-register"]/div/div/input')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="form-register"]/div/button')
    HEADER_H1 = (By.XPATH, '//*[@id="content"]/h1')
    SUBSCRIBE_CHECKBOX = (By.ID, "input-newsletter")

    @allure.step("Заполнение формы регистрации: '{first_name}', '{last_name}', '{email}'")
    def add_new_user(self, first_name, last_name, email, password):
        self.input_text(self.FIRST_NAME_FIELD, first_name)
        self.input_text(self.LAST_NAME_FIELD, last_name)
        self.input_text(self.EMAIL_FIELD, email)
        self.input_text(self.PASSWORD_FIELD, password)
        self.click_on_element(self.CHECKBOX)
        self.click_on_element(self.CONTINUE_BUTTON)
        time.sleep(5)
        header = self.find_element(self.HEADER_H1)
        return header.text

    @allure.step("Открытие страницы по URL: '{url}' ")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Нажатие на меню 'My Account'")
    def click_my_account_menu(self):
        self.click_on_element(self.MY_ACCOUNT_MENU_BUTTON)

    @allure.step("Проверка наличия ссылки 'Login'")
    def check_login_link_exists(self):
        return self.find_element(self.MY_ACCOUNT_LOGIN_LINK) is not None

    @allure.step("Проверка наличия кнопки 'Continue'")
    def check_continue_button_exists(self):
        return self.find_element(self.CONTINUE_BUTTON) is not None

    @allure.step("Проверка наличия чекбокса подписки")
    def check_subscribe_checkbox_exists(self):
        return self.find_element(self.SUBSCRIBE_CHECKBOX) is not None

    @allure.step("Проверка наличия поля Email")
    def check_email_field_exists(self):
        return self.find_element(self.EMAIL_FIELD) is not None

    @allure.step("Получение текста заголовка H1")
    def get_header_h1_text(self):
        return self.get_text(self.HEADER_H1)
