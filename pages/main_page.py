from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
import allure


class MainPage(BasePage):
    # Locators
    CAROUSEL_TOP = (By.ID, "carousel-banner-0")
    CAROUSEL_TOP_IMAGE = (By.XPATH, '//*[@id="carousel-banner-0"]/div[2]/div[2]/div/div')
    CAROUSEL_BOTTOM_IMAGE = (By.XPATH, '//*[@id="carousel-banner-1"]/div[2]/div[2]/div/div[5]/img')
    CAROUSEL_LEFT_BUTTON = (By.XPATH, '//*[@id="carousel-banner-1"]/div[1]/button[1]')
    CAROUSEL_RIGHT_BUTTON = (By.XPATH, '//*[@id="carousel-banner-1"]/button[2]')
    CAROUSEL_NAVIGATION = (By.XPATH, '//*[@id="carousel-banner-1"]/div[1]/button[2]')
    DISNEY_IMAGE = (By.XPATH, '//*[@id="carousel-banner-1"]/div[2]/div[1]/div/div[3]/img')
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]')
    CART_BUTTON = (By.XPATH, '//*[@id="header-cart"]/div/button')
    ITEM_IN_CART = (By.XPATH, '//*[@id="header-cart"]/div/ul/li/table/tbody/tr/td[2]/a')
    FIRST_PRODUCT_PRICE = (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/div/div/span[1]')
    CURRENCY_MENU_BUTTON = (By.XPATH, '//*[@id="form-currency"]/div/a')
    CURRENCY_EURO = (By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a')

    def open_page(self, url):
        """Метод для открытия страницы"""
        self.logger.info("%s: Opening url: %s" % (self.class_name, url))
        self.driver.get(url)

    @allure.step("Открытие главной страницы по URL: {url}")
    def open_main_page(self, url):
        self.driver.get(url)

    @allure.step("Проверка наличия верхнего каруселя")
    def check_top_carousel_exists(self):
        exists = self.find_element(self.CAROUSEL_TOP) is not None
        with allure.step(f"Результат проверки: {exists}"):
            pass
        return exists

    @allure.step("Проверка наличия изображения в верхнем каруселе")
    def check_top_image_exists(self):
        exists = self.find_element(self.CAROUSEL_TOP_IMAGE) is not None
        with allure.step(f"Результат проверки: {exists}"):
            pass
        return exists

    @allure.step("Проверка наличия нижнего изображения карусели")
    def check_bottom_image_exists(self):
        exists = self.find_element(self.CAROUSEL_BOTTOM_IMAGE) is not None
        with allure.step(f"Результат проверки: {exists}"):
            pass
        return exists

    @allure.step("Клик по левой кнопке карусели и проверка изображения Disney")
    def click_left_button_and_check_disney_image(self):
        self.click_on_element(self.CAROUSEL_LEFT_BUTTON)
        disney_image = self.find_element(self.DISNEY_IMAGE)
        alt_text = disney_image.get_attribute("alt") == "Disney"
        with allure.step(f"Изображение Disney найдено: {alt_text}"):
            pass
        return alt_text

    @allure.step("Наведение на навигацию карусели")
    def hover_on_carousel_navigation(self):
        self.scroll_to_element(self.CAROUSEL_NAVIGATION)
        time.sleep(3)
        self.move_to_element(self.CAROUSEL_NAVIGATION)

    @allure.step("Проверка наличия правой кнопки карусели")
    def check_right_button_exists(self):
        exists = self.find_element(self.CAROUSEL_RIGHT_BUTTON) is not None
        with allure.step(f"Результат проверки: {exists}"):
            pass
        return exists

    @allure.step("Добавление первого товара в корзину")
    def add_first_product_to_cart(self):
        self.scroll_to_element(self.ADD_TO_CART_BUTTON)
        self.click_on_element(self.ADD_TO_CART_BUTTON)

    @allure.step("Открытие корзины")
    def open_cart(self):
        self.scroll_to_element(self.CART_BUTTON)
        time.sleep(3)
        self.click_on_element(self.CART_BUTTON)

    @allure.step("Получение названия товара в корзине")
    def get_item_name_in_cart(self):
        item_name = self.get_text(self.ITEM_IN_CART)
        with allure.step(f"Товар в корзине: '{item_name}'"):
            pass
        return item_name

    @allure.step("Получение цены товара")
    def get_product_price(self):
        price = self.get_text(self.FIRST_PRODUCT_PRICE)
        with allure.step(f"Цена товара: {price}"):
            pass
        return price

    @allure.step("Смена валюты на Euro")
    def change_currency_to_euro(self):
        self.click_on_element(self.CURRENCY_MENU_BUTTON)
        self.click_on_element(self.CURRENCY_EURO)