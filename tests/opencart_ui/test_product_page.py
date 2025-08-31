from pages.product_page import ProductPage
import allure

@allure.title("Проверка наличия секции информации о товаре")
@allure.description("Тест проверяет наличие секции 'product-info' на странице товара")
@allure.feature("Страница товара / UI")
@allure.severity(allure.severity_level.NORMAL)
def test_check_rating(browser, product_page_url):
    product_page = ProductPage(browser)

    with allure.step("Шаг 1: Открытие страницы товара"):
        product_page.open_page(product_page_url)

    with allure.step("Шаг 2: Проверка наличия секции информации о товаре"):
        assert product_page.check_product_info_exists(), "Элемент product-info не найден"


@allure.title("Проверка наличия изображения товара")
@allure.description("Тест проверяет наличие изображения товара на странице")
@allure.feature("Страница товара / Изображение")
@allure.severity(allure.severity_level.NORMAL)
def test_check_product_image(browser, product_page_url):
    product_page = ProductPage(browser)

    with allure.step("Шаг 1: Открытие страницы товара"):
        product_page.open_page(product_page_url)

    with allure.step("Шаг 2: Проверка наличия изображения товара"):
        assert product_page.check_product_image_exists(), "Изображение товара не найдено"


@allure.title("Проверка наличия раздела отзывов")
@allure.description("Тест проверяет, что раздел отзывов доступен после клика по ссылке")
@allure.feature("Страница товара / Отзывы")
@allure.severity(allure.severity_level.NORMAL)
def test_check_reviews(browser, product_page_url):
    product_page = ProductPage(browser)

    with allure.step("Шаг 1: Открытие страницы товара"):
        product_page.open_page(product_page_url)

    with allure.step("Шаг 2: Переход к разделу отзывов и проверка его наличия"):
        assert product_page.check_reviews_section(), "Раздел отзывов не отобразился"


@allure.title("Проверка атрибута alt у изображения товара")
@allure.description("Тест проверяет, что атрибут alt изображения соответствует ожидаемому значению 'iMac'")
@allure.feature("Страница товара / Изображение")
@allure.severity(allure.severity_level.MINOR)
def test_check_image_attribute(browser, product_page_url):
    product_page = ProductPage(browser)

    with allure.step("Шаг 1: Открытие страницы товара"):
        product_page.open_page(product_page_url)

    with allure.step("Шаг 2: Получение значения атрибута alt у изображения товара"):
        alt_text = product_page.get_image_alt_attribute()

    with allure.step("Шаг 3: Проверка значения атрибута alt"):
        assert alt_text == "iMac", (
            f"Атрибут alt изображения должен быть 'iMac', получено: '{alt_text}'"
        )


@allure.title("Проверка заголовка страницы товара")
@allure.description("Тест проверяет, что заголовок H1 на странице товара равен 'iMac'")
@allure.feature("Страница товара / Заголовок")
@allure.severity(allure.severity_level.NORMAL)
def test_check_header(browser, product_page_url):
    product_page = ProductPage(browser)

    with allure.step("Шаг 1: Открытие страницы товара"):
        product_page.open_page(product_page_url)

    with allure.step("Шаг 2: Получение заголовка H1 страницы товара"):
        header_text = product_page.get_header_h1_text()

    with allure.step("Шаг 3: Проверка совпадения заголовка с ожидаемым"):
        assert header_text == "iMac", (
            f"Заголовок должен быть 'iMac', получено: '{header_text}'"
        )