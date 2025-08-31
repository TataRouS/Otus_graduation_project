from pages.main_page import MainPage
import allure


@allure.title("Проверка наличия товара в корзине после добавления")
@allure.description("Тест проверяет, что после добавления товара в корзину он отображается в списке")
@allure.feature("Корзина / Добавление товара")
@allure.severity(allure.severity_level.NORMAL)
def test_check_item_in_cart(browser, base_url):
    main_page = MainPage(browser)

    with allure.step("Шаг 1: Открытие главной страницы"):
        main_page.open_main_page(base_url)

    with allure.step("Шаг 2: Добавление первого товара в корзину"):
        main_page.add_first_product_to_cart()

    with allure.step("Шаг 3: Открытие корзины"):
        main_page.open_cart()

    with allure.step("Шаг 4: Проверка названия товара в корзине"):
        item_name = main_page.get_item_name_in_cart()
        assert item_name == "MacBook", (
            f"Ожидаемый товар: 'MacBook', получено: '{item_name}'"
        )