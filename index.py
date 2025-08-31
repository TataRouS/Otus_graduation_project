import time
from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.chromium.service import ChromiumService

options = ChromiumOptions()
options.binary_location = "Users/tata_rous/Downloads/yandexdriver"
options.add_argument("headless-new")

driver = webdriver.Chrome(
    options=options,
    service=ChromiumService(executable_path="Users/tata_rous/Downloads/yandexdriver"),
)
time.sleep(10)
