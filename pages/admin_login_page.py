from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class AdminLoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.ID, "input-username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    HEADER_H1 = (By.XPATH, '//*[@id="content"]/div[1]/div/h1')

    def open_page(self, url):
        """Метод для открытия страницы"""
        self.logger.info("%s: Opening url: %s" % (self.class_name, url))
        self.driver.get(url)

    @allure.step("Открытие страницы логина: {url} ")
    def open_login_page(self, url):
        self.driver.get(url)

    @allure.step("Вход в систему с логином '{username}'")
    def login(self, username, password):
        self.input_text(self.USERNAME_FIELD, username)
        self.input_text(self.PASSWORD_FIELD, password)
        self.click_on_element(self.LOGIN_BUTTON)

    @allure.step("Получение заголовка страницы после входа")
    def get_header_text(self):
        return self.get_element_text(self.HEADER_H1)
