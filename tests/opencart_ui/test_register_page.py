from pages.register_page import RegisterPage
import allure

@allure.title("Проверка наличия ссылки Login в меню My Account")
@allure.description("Тест проверяет наличие пункта 'Login' в меню 'My Account' на странице регистрации")
@allure.feature("Регистрация / UI")
@allure.severity(allure.severity_level.NORMAL)
def test_check_my_account_menu(browser, register_account_page_url):
    register_page = RegisterPage(browser)

    with allure.step("Шаг 1: Открытие страницы регистрации"):
        register_page.open_page(register_account_page_url)

    with allure.step("Шаг 2: Нажатие на меню 'My Account'"):
        register_page.click_my_account_menu()

    with allure.step("Шаг 3: Проверка наличия ссылки 'Login'"):
        assert register_page.check_login_link_exists(), "Ссылка 'Login' в меню 'My Account' не найдена"


@allure.title("Проверка наличия кнопки Continue")
@allure.description("Тест проверяет наличие кнопки 'Continue' на форме регистрации")
@allure.feature("Регистрация / UI")
@allure.severity(allure.severity_level.NORMAL)
def test_check_continue_button(browser, register_account_page_url):
    register_page = RegisterPage(browser)

    with allure.step("Шаг 1: Открытие страницы регистрации"):
        register_page.open_page(register_account_page_url)

    with allure.step("Шаг 2: Проверка наличия кнопки 'Continue'"):
        assert register_page.check_continue_button_exists(), "Кнопка Continue не найдена"


@allure.title("Проверка наличия чек-бокса подписки")
@allure.description("Тест проверяет наличие чек-бокса подписки на рассылку")
@allure.feature("Регистрация / UI")
@allure.severity(allure.severity_level.NORMAL)
def test_check_subscribe_checkbox(browser, register_account_page_url):
    register_page = RegisterPage(browser)

    with allure.step("Шаг 1: Открытие страницы регистрации"):
        register_page.open_page(register_account_page_url)

    with allure.step("Шаг 2: Проверка наличия чек-бокса подписки"):
        assert register_page.check_subscribe_checkbox_exists(), "Чек-бокс подписки не найден"


@allure.title("Проверка наличия поля Email")
@allure.description("Тест проверяет наличие поля ввода email на форме регистрации")
@allure.feature("Регистрация / UI")
@allure.severity(allure.severity_level.NORMAL)
def test_check_email_field(browser, register_account_page_url):
    register_page = RegisterPage(browser)

    with allure.step("Шаг 1: Открытие страницы регистрации"):
        register_page.open_page(register_account_page_url)

    with allure.step("Шаг 2: Проверка наличия поля Email"):
        assert register_page.check_email_field_exists(), "Поле ввода email не найдено"


@allure.title("Проверка заголовка страницы регистрации")
@allure.description("Тест проверяет, что заголовок страницы регистрации равен 'Register Account'")
@allure.feature("Регистрация / UI")
@allure.severity(allure.severity_level.NORMAL)
def test_check_header(browser, register_account_page_url):
    register_page = RegisterPage(browser)

    with allure.step("Шаг 1: Открытие страницы регистрации"):
        register_page.open_page(register_account_page_url)

    with allure.step("Шаг 2: Получение заголовка страницы"):
        header_text = register_page.get_header_h1_text()

    with allure.step("Шаг 3: Проверка значения заголовка"):
        assert header_text == "Register Account", (
            f"Ожидаемый заголовок: 'Register Account', получено: '{header_text}'"
        )