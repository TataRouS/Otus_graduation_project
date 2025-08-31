from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class ProductPage(BasePage):
    # Locators
    PRODUCT_INFO_SECTION = (By.ID, "product-info")
    PRODUCT_IMAGE = (By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/div/a[1]/img')
    REVIEWS_LINK = (By.XPATH, '//*[@id="content"]/ul/li[2]/a')
    REVIEW_SECTION = (By.XPATH, '//*[@id="review"]/p')
    IMAGE_ATTRIBUTE = (By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/a/img')
    HEADER_H1 = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/h1')

    @allure.step("Открытие страницы товара по URL: {url}")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Проверка наличия секции информации о товаре")
    def check_product_info_exists(self):
        exists = self.find_element(self.PRODUCT_INFO_SECTION) is not None
        with allure.step(f"Результат проверки: {exists}"):
            pass
        return exists

    @allure.step("Проверка наличия изображения товара")
    def check_product_image_exists(self):
        exists = self.find_element(self.PRODUCT_IMAGE) is not None
        with allure.step(f"Результат проверки: {exists}"):
            pass
        return exists

    @allure.step("Проверка наличия раздела отзывов")
    def check_reviews_section(self):
        self.scroll_to_element(self.REVIEWS_LINK)
        self.click_on_element(self.REVIEWS_LINK)
        exists = self.find_element(self.REVIEW_SECTION) is not None
        with allure.step(f"Результат проверки: {exists}"):
            pass
        return exists

    @allure.step("Получение атрибута alt у изображения товара")
    def get_image_alt_attribute(self):
        alt_text = self.find_element(self.IMAGE_ATTRIBUTE).get_attribute("alt")
        with allure.step(f"Атрибут alt: '{alt_text}'"):
            pass
        return alt_text

    @allure.step("Получение заголовка H1 страницы товара")
    def get_header_h1_text(self):
        text = self.find_element(self.HEADER_H1).text
        with allure.step(f"Заголовок H1: '{text}'"):
            pass
        return text