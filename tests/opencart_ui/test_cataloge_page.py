from pages.catalog_page import CatalogPage
import allure

@allure.title("Проверка наличия меню на странице каталога")
@allure.description("Тест проверяет наличие основного меню навигации на странице каталога")
@allure.feature("Каталог / UI")
@allure.severity(allure.severity_level.NORMAL)
def test_check_categories(browser, catalog_page_url):
    catalog_page = CatalogPage(browser)

    with allure.step("Шаг 1: Открытие страницы каталога"):
        catalog_page.open_page(catalog_page_url)

    with allure.step("Шаг 2: Проверка наличия элемента меню"):
        assert catalog_page.check_menu_exists(), "Элемент меню не найден"


@allure.title("Проверка кнопки 'Add to Cart' у первого товара")
@allure.description("Тест проверяет наличие кнопки добавления в корзину у первого товара")
@allure.feature("Каталог / Корзина")
@allure.severity(allure.severity_level.NORMAL)
def test_check_shop_cart_of_first_product(browser, catalog_page_url):
    catalog_page = CatalogPage(browser)

    with allure.step("Шаг 1: Открытие страницы каталога"):
        catalog_page.open_page(catalog_page_url)

    with allure.step("Шаг 2: Проверка наличия кнопки 'Add to Cart' у первого товара"):
        assert catalog_page.check_first_product_cart_exists(), "Кнопка добавления в корзину не найдена"


@allure.title("Проверка подменю при наведении на категорию")
@allure.description("Тест проверяет текст подменю при наведении на пункт меню 'Laptops & Notebooks'")
@allure.feature("Каталог / Меню")
@allure.severity(allure.severity_level.NORMAL)
def test_check_menu_item(browser, catalog_page_url):
    catalog_page = CatalogPage(browser)

    with allure.step("Шаг 1: Открытие страницы каталога"):
        catalog_page.open_page(catalog_page_url)

    with allure.step("Шаг 2: Наведение курсора на пункт меню 'Laptops & Notebooks'"):
        catalog_page.hover_navbar_menu_item()

    with allure.step("Шаг 3: Проверка текста подменю"):
        assert catalog_page.get_submenu_text() == "Show All Laptops & Notebooks", (
            f"Ожидаемый текст: 'Show All Laptops & Notebooks', получено: '{catalog_page.get_submenu_text()}'"
        )


@allure.title("Проверка названия категории")
@allure.description("Тест проверяет, что заголовок категории соответствует ожидаемому значению")
@allure.feature("Каталог / Категории")
@allure.severity(allure.severity_level.NORMAL)
def test_check_category_name(browser, catalog_page_url):
    catalog_page = CatalogPage(browser)

    with allure.step("Шаг 1: Открытие страницы каталога"):
        catalog_page.open_page(catalog_page_url)

    with allure.step("Шаг 2: Получение названия категории"):
        category_name = catalog_page.get_category_name_text()

    with allure.step("Шаг 3: Проверка соответствия названия категории"):
        assert category_name == "Phones & PDAs (3)", (
            f"Ожидаемое название категории: 'Phones & PDAs (3)', получено: '{category_name}'"
        )


@allure.title("Проверка мобильного меню")
@allure.description("Тест проверяет наличие ссылки категории в мобильном меню")
@allure.feature("Каталог / Мобильный интерфейс")
@allure.severity(allure.severity_level.MINOR)
def test_check_category_on_click_menu(browser, catalog_page_url):
    catalog_page = CatalogPage(browser)

    with allure.step("Шаг 1: Открытие страницы каталога"):
        catalog_page.open_page(catalog_page_url)

    with allure.step("Шаг 2: Изменение размера окна браузера на мобильный"):
        browser.set_window_size(800, 800)

    with allure.step("Шаг 3: Открытие мобильного меню"):
        catalog_page.open_mobile_menu()

    with allure.step("Шаг 4: Восстановление исходного размера окна"):
        browser.set_window_size(1200, 1000)

    with allure.step("Шаг 5: Проверка наличия ссылки категории в мобильном меню"):
        assert catalog_page.check_mobile_category_exists(), "Мобильная категория не найдена"