from pages.admin_login_page import AdminLoginPage
from selenium.webdriver.common.by import By
import allure



class AdminPage(AdminLoginPage):
    # Локаторы
    # USERNAME_FIELD = (By.ID, "input-username")
    # PASSWORD_FIELD = (By.NAME, "input-meta-title-1")
    # LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CATALOG_IN_NAVIGATION = (By.XPATH, '//*[@id="menu-catalog"]/a')
    PRODUCTS = (By.XPATH, '//*[@id="collapse-1"]/li[2]/a')
    ADD_NEW_PRODUCT_BUTTON = (By.XPATH, '//*[@id="content"]/div[1]/div/div/a')
    SAVE_NEW_PRODUCT_BUTTON = (By.XPATH, '//*[@id="content"]/div[1]/div/div/button')
    PRODUCT_NAME_FIELD = (By.ID, "input-name-1")
    META_TAG_TITLE_FIELD = (By.ID, "input-meta-title-1")
    DATA_TAP = (By.XPATH, '//*[@id="form-product"]/ul/li[2]/a')
    MODEL_FIELD = (By.ID, "input-model")
    SEO_TAP = (By.XPATH, '//*[@id="form-product"]/ul/li[11]/a')
    SEO_FIELD = (By.ID, "input-keyword-0-1")
    BACK_BUTTON = (By.XPATH, '//*[@id="content"]/div[1]/div/div/a')
    FILTER_PRODUCT_NAME_FIELD = (By.ID, "input-name")
    FILTER_BUTTON_ON_FORM = (By.ID, "button-filter")
    PRODUCT_NAME_IN_FILTER_LIST = (
        By.XPATH,
        '//*[@id="form-product"]/div[1]/table/tbody/tr/td[3]',
    )
    CHECK_BOX_IN_FILTER_LIST = (By.NAME, "selected[]")
    DELETE_BUTTON = (By.XPATH, '//*[@id="content"]/div[1]/div/div/button[3]')
    FILTER_EMPTY = (By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr/td')



    @allure.step("Добавление нового товара: {product_name}, {meta_teg}, {model}, {seo}")
    def add_new_product(self, product_name, meta_teg, model, seo):
        self.click_on_element(self.CATALOG_IN_NAVIGATION)
        self.click_on_element(self.PRODUCTS)
        self.click_on_element(self.ADD_NEW_PRODUCT_BUTTON)
        self.input_text(self.PRODUCT_NAME_FIELD, product_name)
        self.input_text(self.META_TAG_TITLE_FIELD, meta_teg)
        self.click_on_element(self.DATA_TAP)
        self.input_text(self.MODEL_FIELD, model)
        self.click_on_element(self.SEO_TAP)
        self.input_text(self.SEO_FIELD, seo)
        self.click_on_element(self.SAVE_NEW_PRODUCT_BUTTON)
        self.click_on_element(self.BACK_BUTTON)

    @allure.step("Получение списка товаров после фильтрации по имени: {product_name}")
    def get_new_product_text_from_filter_list(self, product_name):
        self.input_text(self.FILTER_PRODUCT_NAME_FIELD, product_name)
        self.click_on_element(self.FILTER_BUTTON_ON_FORM)
        new_product = self.find_elements(self.PRODUCT_NAME_IN_FILTER_LIST)
        return new_product

    @allure.step("Применение фильтра без результатов")
    def get_filter_list(self):
        self.click_on_element(self.FILTER_BUTTON_ON_FORM)
        product = self.find_element(self.FILTER_EMPTY)
        return product

    @allure.step("Удаление выбранного товара")
    def delete_product(self):
        self.click_on_element(self.CHECK_BOX_IN_FILTER_LIST)
        self.click_on_element(self.DELETE_BUTTON)
        alert = self.alert()
        print("Сообщение alert:", alert.text)
        alert.accept()
