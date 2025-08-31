from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
import allure
from abc import ABC, abstractmethod


class BasePage(ABC):  # Наследуемся от ABC — делаем класс абстрактным
    def __init__(self, driver):
        self.driver = driver
        self.logger = driver.logger
        self.class_name = type(self).__name__

    @abstractmethod
    def open_page(self, url):
        """Метод для открытия страницы"""
        self.logger.info("%s: Opening url: %s" % (self.class_name, url))
        self.driver.get(url)

    @allure.step("Поиск элемента: {locator}")
    def find_element(self, locator, timeout=30):
        self.logger.info("%s: Find element %s" % (self.class_name, str(locator)))
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не найден",
        )

    @allure.step("Поиск нескольких элементов: {locator}")
    def find_elements(self, locator, timeout=30):
        self.logger.info("%s: Find elements %s" % (self.class_name, str(locator)))
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Элемент {locator} не найден",
        )

    @allure.step("Проверка наличия элемента: {locator}")
    def find_element_presence(self, locator, timeout=30):
        self.logger.info(
            "%s: Check if element %s is present" % (self.class_name, str(locator))
        )
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не найден",
        )

    @allure.step("Проверка наличия элемента: {locator}")
    def move_to_element(self, locator, timeout=30):
        self.logger.info("%s: Move to element %s " % (self.class_name, str(locator)))
        element = self.find_element(locator, timeout)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    @allure.step("Клик по элементу: {locator}")
    def click_on_element(self, locator, timeout=30):
        self.logger.debug("%s: Clicking element: %s" % (self.class_name, str(locator)))
        element = self.find_element(locator, timeout)
        element.click()

    @allure.step("Прокрутка до элемента: {locator}")
    def scroll_to_element(self, locator, timeout=30):
        self.logger.debug("%s: scroll to element: %s" % (self.class_name, str(locator)))
        element = self.find_element_presence(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)

    @allure.step("Получение текста из элемента: {locator}")
    def get_text(self, locator, timeout=30):
        self.logger.info(
            "%s: Get text from element %s " % (self.class_name, str(locator))
        )
        element = self.find_element(locator, timeout)
        return element.text

    @allure.step("Получение атрибута '{attribute_name}' у элемента: {locator}")
    def get_attribute(self, locator, attribute_name, timeout=30):
        self.logger.info(
            "%s: Get attribute  %s  of element %s "
            % (self.class_name, attribute_name, locator)
        )
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute_name)

    @allure.step("Ввод текста '{text}' в поле: {locator}")
    def input_text(self, locator, text, timeout=30):
        self.logger.debug("%s: Input %s in input %s" % (self.class_name, text, locator))
        element = self.find_element(locator, timeout)
        element.send_keys(text)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получение текста элемента: {locator}")
    def get_element_text(self, locator, timeout=30):
        self.logger.info("%s: Get text from %s " % (self.class_name, str(locator)))
        return self.find_element(locator, timeout).text

    @allure.step("Ожидание появления alert")
    def alert(self, timeout=15):
        try:
            alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            return alert
        except TimeoutException:
            raise Exception("Alert не появился в течение заданного времени")