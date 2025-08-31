from selenium.webdriver.common.by import By
from pages.admin_login_page import AdminLoginPage
import time
import random
import allure



class TopPage(AdminLoginPage):
    # Локаторы
    CURRENCY = (By.XPATH, '//*[@id="form-currency"]/div/a')
    CURRENCY_SYMBOL = (By.XPATH, '//*[@id="form-currency"]/div/a/strong')
    DROP_CURRENCY_MENU = (By.XPATH, '//*[@id="form-currency"]/div/ul')

    @allure.step("Получение текущей валюты из меню")
    def get_previous_currency(self):
        currency = self.find_element(self.CURRENCY_SYMBOL).text
        with allure.step(f"Текущая валюта: {currency}"):
            pass
        return currency

    @allure.step("Смена валюты на случайную из списка")
    def change_currency(self):
        self.click_on_element(self.CURRENCY)
        time.sleep(3)

        drop_menu_items = self.find_elements(self.DROP_CURRENCY_MENU)
        selected_currency = random.choice(drop_menu_items)

        with allure.step("Выбор случайной валюты из выпадающего списка"):
            selected_currency.click()

        new_currency = self.find_element(self.CURRENCY_SYMBOL).text
        with allure.step(f"Новая валюта: {new_currency}"):
            pass

        return new_currency