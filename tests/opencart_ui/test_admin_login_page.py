from pages.admin_login_page import AdminLoginPage
import allure

@allure.title("Успешный вход в админ-панель")
@allure.description("Проверяет возможность авторизации в административной части сайта с корректными данными")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_to_admin_panel(browser, base_url):
    admin_login_page = AdminLoginPage(browser)

    with allure.step("Шаг 1: Открытие страницы входа в админку"):
        admin_login_page.open_login_page(base_url + "/administration")

    with allure.step("Шаг 2: Ввод логина и пароля и нажатие кнопки Войти"):
        admin_login_page.login("user", "bitnami")

    with allure.step("Шаг 3: Проверка, что пользователь перешёл на Dashboard"):
        header_text = admin_login_page.get_header_text()
        assert header_text == "Dashboard", (
            f"Ожидаемый заголовок: 'Dashboard', получено: '{header_text}'"
        )
