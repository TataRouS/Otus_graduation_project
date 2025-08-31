from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure



class CurrencyPage(BasePage):
    CURRENCY_DROPDOWN = (By.XPATH, '//*[@id="form-currency"]/div/a')
    CURRENCY_LIST = (By.XPATH, '//*[@id="form-currency"]/div/ul/li')

    @allure.step("Открытие выпадающего списка валют")
    def open_currency_dropdown(self):
        self.click_on_element(self.CURRENCY_DROPDOWN)

    @allure.step("Получение списка доступных валют")
    def get_currency_list(self):
        elements = self.find_elements(self.CURRENCY_LIST)
        currencies = [element.text for element in elements]
        with allure.step(f"Найдены валюты: {currencies}"):
            pass
        return currencies

    @allure.step("Выбор валюты по названию: {currency_name}")
    def select_currency(self, currency_name):
        currency_locator = (
            By.XPATH,
            f'//*[@id="form-currency"]/div/ul/li/a[text()="{currency_name}"]',
        )
        self.click_on_element(currency_locator)
