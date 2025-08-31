import time
from selenium.webdriver.common.by import By
import allure

@allure.step("Смена валюты на '€ Euro'")
def change_currency(browser, base_url):
    browser.get(base_url)
    # Клик по кнопке выбора валюты
    browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/i').click()
    time.sleep(3)  # для демонстрации

    # Получаем текущую валюту
    current_currency = browser.find_element(
        By.XPATH, '//*[@id="form-currency"]/div/a/strong'
    ).text
    drop_menu = browser.find_elements(By.XPATH, '//*[@id="form-currency"]/div/ul/li')
    time.sleep(3)

    # Выбираем новую валюту (по первому символу)
    for item in drop_menu:
        item_text = item.text.strip()
        if item_text[:1] != current_currency[:1]:
            item.click()
            break
