from pages.main_page import MainPage
import allure


@allure.title("Проверка изменения цены товара при смене валюты на главной странице")
@allure.description("Тест проверяет, что цена товара изменяется после смены валюты на Euro")
@allure.feature("Главная страница / Валюта")
@allure.severity(allure.severity_level.NORMAL)
def test_check_change_currency_in_main_page(browser, base_url):
    main_page = MainPage(browser)

    with allure.step("Шаг 1: Открытие главной страницы"):
        main_page.open_main_page(base_url)

    with allure.step("Шаг 2: Получение начальной цены товара"):
        initial_price = main_page.get_product_price()
        allure.attach(
            f"Исходная цена: {initial_price}",
            name="Исходная цена",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Шаг 3: Смена валюты на Euro"):
        main_page.change_currency_to_euro()

    with allure.step("Шаг 4: Обновление страницы для применения новой валюты"):
        main_page.open_main_page(base_url)

    with allure.step("Шаг 5: Получение новой цены товара"):
        changed_price = main_page.get_product_price()
        allure.attach(
            f"Цена после смены валюты: {changed_price}",
            name="Новая цена",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Шаг 6: Проверка, что цена изменилась после смены валюты"):
        assert changed_price != initial_price, (
            f"Ожидаемый результат: цена изменилась, получено: '{initial_price}' -> '{changed_price}'"
        )