from pages.catalog_page import CatalogPage
from utils.currency_utils import change_currency
import allure


@allure.title("Смена валюты влияет на цену товара в каталоге")
@allure.description("Проверяет, что при смене валюты изменяется цена товара на странице каталога")
@allure.feature("Каталог / Валюта")
@allure.severity(allure.severity_level.NORMAL)
def test_check_change_currency_in_catalog(browser, catalog_page_url, base_url):
    catalog_page = CatalogPage(browser)

    with allure.step("Шаг 1: Открытие страницы каталога и получение начальной цены"):
        catalog_page.open_page(catalog_page_url)
        initial_price = catalog_page.get_product_price()

    with allure.step("Шаг 2: Смена валюты на Euro через меню"):
        change_currency(browser, base_url)

    with allure.step("Шаг 3: Повторное открытие страницы каталога и получение новой цены"):
        catalog_page.open_page(catalog_page_url)
        changed_price = catalog_page.get_product_price()

    print("Исходная цена:", initial_price)
    print("Цена после смены валюты:", changed_price)

    with allure.step("Шаг 4: Проверка, что цена изменилась после смены валюты"):
        assert changed_price != initial_price, "Цена на товар не изменилась при смене валюты"
