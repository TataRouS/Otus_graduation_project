from pages.main_page import MainPage
import allure

@allure.title("Проверка наличия верхнего каруселя")
@allure.description("Тест проверяет наличие верхнего каруселя (carousel-banner-0) на главной странице")
@allure.feature("Главная страница / Карусель")
@allure.severity(allure.severity_level.NORMAL)
def test_check_carousel_item(browser, base_url):
    main_page = MainPage(browser)

    with allure.step("Шаг 1: Открытие главной страницы"):
        main_page.open_main_page(base_url)

    with allure.step("Шаг 2: Проверка наличия верхнего каруселя"):
        assert main_page.check_top_carousel_exists(), "Элемент carousel-banner-0 не найден"


@allure.title("Проверка изображения в верхнем каруселе")
@allure.description("Тест проверяет наличие изображения в верхнем каруселе на главной странице")
@allure.feature("Главная страница / Изображения")
@allure.severity(allure.severity_level.NORMAL)
def test_image_from_carousel(browser, base_url):
    main_page = MainPage(browser)

    with allure.step("Шаг 1: Открытие главной страницы"):
        main_page.open_main_page(base_url)

    with allure.step("Шаг 2: Проверка наличия изображения в верхнем каруселе"):
        assert main_page.check_top_image_exists(), "Картинка из верхней карусели не найдена"


@allure.title("Проверка изображения в нижнем каруселе")
@allure.description("Тест проверяет наличие изображения в нижнем каруселе на главной странице")
@allure.feature("Главная страница / Изображения")
@allure.severity(allure.severity_level.NORMAL)
def test_image_starbacks_coffie(browser, base_url):
    main_page = MainPage(browser)

    with allure.step("Шаг 1: Открытие главной страницы"):
        main_page.open_main_page(base_url)

    with allure.step("Шаг 2: Проверка наличия изображения в нижнем каруселе"):
        assert main_page.check_bottom_image_exists(), "Картинка из нижней карусели не найдена"


@allure.title("Проверка отображения изображения Disney после нажатия кнопки слева")
@allure.description("Тест проверяет, что после клика по левой кнопке карусели отображается изображение Disney")
@allure.feature("Главная страница / Карусель / Изображения")
@allure.severity(allure.severity_level.NORMAL)
def test_image_from_carousel_on_click(browser, base_url):
    main_page = MainPage(browser)

    with allure.step("Шаг 1: Открытие главной страницы"):
        main_page.open_main_page(base_url)

    with allure.step("Шаг 2: Наведение на элементы карусели для активации"):
        main_page.hover_on_carousel_navigation()

    with allure.step("Шаг 3: Клик по левой кнопке карусели и проверка изображения Disney"):
        assert main_page.click_left_button_and_check_disney_image(), "Изображение Disney не отображается"


@allure.title("Проверка наличия правой кнопки карусели")
@allure.description("Тест проверяет наличие правой кнопки прокрутки карусели на главной странице")
@allure.feature("Главная страница / Карусель")
@allure.severity(allure.severity_level.NORMAL)
def test_right_button_from_carousel(browser, base_url):
    main_page = MainPage(browser)

    with allure.step("Шаг 1: Открытие главной страницы"):
        main_page.open_main_page(base_url)

    with allure.step("Шаг 2: Наведение на элементы карусели для активации"):
        main_page.hover_on_carousel_navigation()

    with allure.step("Шаг 3: Проверка наличия правой кнопки карусели"):
        assert main_page.check_right_button_exists(), "Правая кнопка со стрелкой не найдена"