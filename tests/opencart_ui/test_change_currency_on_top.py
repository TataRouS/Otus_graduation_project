# Переключение валют из верхнего меню opencart_ui
from pages.currency_top import TopPage
import allure


@allure.title("Смена валюты через верхнее меню")
@allure.description("Проверяет возможность смены валюты через выпадающее меню в шапке сайта")
@allure.feature("Интерфейс / Валюта")
@allure.severity(allure.severity_level.NORMAL)
def test_check_change_currency_in_top(browser, base_url):
    top_page = TopPage(browser)

    with allure.step("Шаг 1: Открытие главной страницы"):
        top_page.open_login_page(base_url)

    with allure.step("Шаг 2: Получение текущей валюты"):
        previous_currency = top_page.get_previous_currency()

    with allure.step("Шаг 3: Смена валюты на Euro"):
        actual_currency = top_page.change_currency()

    with allure.step("Шаг 4: Проверка, что валюта изменилась"):
        assert previous_currency != actual_currency, (
            f"Ожидаемый результат: валюта изменилась, получено: '{previous_currency}' -> '{actual_currency}'"
        )