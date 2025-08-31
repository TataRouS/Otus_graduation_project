from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class LoginPage(BasePage):
    # Locators
    CONTAINER = (By.ID, "account-login")
    LOGIN_BUTTON = (By.XPATH, '//*[@id="form-login"]/div[3]/button')

    @allure.step("Открытие страницы по URL: {url}")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Проверка наличия контейнера формы входа")
    def check_container_exists(self):
        exists = self.find_element(self.CONTAINER) is not None
        with allure.step(f"Результат проверки: {exists}"):
            pass
        return exists

    @allure.step("Проверка наличия кнопки 'Login'")
    def check_login_button_exists(self):
        exists = self.find_element(self.LOGIN_BUTTON) is not None
        with allure.step(f"Результат проверки: {exists}"):
            pass
        return exists