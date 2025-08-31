from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage
import allure

@allure.title("Проверка наличия контейнера формы входа")
@allure.description("Тест проверяет наличие основного контейнера формы авторизации на странице")
@allure.feature("Авторизация / UI")
@allure.severity(allure.severity_level.NORMAL)
def test_check_container(browser, login_page_url):
    login_page = LoginPage(browser)

    with allure.step("Шаг 1: Открытие страницы входа"):
        login_page.open_page(login_page_url)

    with allure.step("Шаг 2: Проверка наличия контейнера формы входа"):
        assert login_page.check_container_exists(), "Элемент контейнера не найден"


@allure.title("Проверка наличия кнопки 'Login'")
@allure.description("Тест проверяет наличие кнопки 'Login' на странице входа")
@allure.feature("Авторизация / Кнопки")
@allure.severity(allure.severity_level.NORMAL)
def test_check_login_button(browser, login_page_url):
    login_page = LoginPage(browser)

    with allure.step("Шаг 1: Открытие страницы входа"):
        login_page.open_page(login_page_url)

    with allure.step("Шаг 2: Проверка наличия кнопки 'Login'"):
        assert login_page.check_login_button_exists(), "Кнопка входа не найдена"


@allure.title("Проверка пункта меню 'Login' в 'My Account'")
@allure.description("Тест проверяет текст элемента меню 'Login' в разделе 'My Account'")
@allure.feature("Меню / Аккаунт")
@allure.severity(allure.severity_level.NORMAL)
def test_check_my_account_item(browser, catalog_page_url):
    catalog_page = CatalogPage(browser)

    with allure.step("Шаг 1: Открытие страницы каталога"):
        catalog_page.open_page(catalog_page_url)

    with allure.step("Шаг 2: Нажатие на меню 'My Account'"):
        catalog_page.click_my_account_menu()

    with allure.step("Шаг 3: Проверка текста пункта 'Login' в выпадающем меню"):
        menu_text = catalog_page.get_login_menu_text()
        assert menu_text == "Login", (
            f"Ожидаемый текст: 'Login', получено: '{menu_text}'"
        )


@allure.title("Проверка названия валюты после открытия меню")
@allure.description("Тест проверяет, что при выборе валюты отображается правильное название '€ Euro'")
@allure.feature("Интерфейс / Валюта")
@allure.severity(allure.severity_level.NORMAL)
def test_check_currency(browser, catalog_page_url):
    catalog_page = CatalogPage(browser)

    with allure.step("Шаг 1: Открытие страницы каталога"):
        catalog_page.open_page(catalog_page_url)

    with allure.step("Шаг 2: Открытие меню выбора валюты"):
        catalog_page.click_currency_menu()

    with allure.step("Шаг 3: Проверка текста опции 'Euro' в списке валют"):
        euro_text = catalog_page.get_euro_currency_text()
        assert euro_text == "€ Euro", (
            f"Ожидаемый текст: '€ Euro', получено: '{euro_text}'"
        )


@allure.title("Проверка мобильного меню категорий")
@allure.description("Тест проверяет наличие категории в мобильном меню")
@allure.feature("Мобильный интерфейс / Меню")
@allure.severity(allure.severity_level.MINOR)
def test_check_category_on_click_menu(browser, login_page_url):
    catalog_page = CatalogPage(browser)

    with allure.step("Шаг 1: Открытие страницы входа (для тестирования мобильного меню)"):
        catalog_page.open_page(login_page_url)

    with allure.step("Шаг 2: Установка размера окна под мобильное устройство (800x800)"):
        catalog_page.driver.set_window_size(800, 800)

    with allure.step("Шаг 3: Открытие мобильного меню"):
        catalog_page.open_mobile_menu()

    with allure.step("Шаг 4: Проверка наличия категории в мобильном меню"):
        assert catalog_page.check_mobile_category_exists(), "Мобильная категория не найдена"