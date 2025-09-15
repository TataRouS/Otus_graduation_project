import pytest
import logging
import datetime
import allure
import json
import pymysql

from selenium import webdriver

from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", help="browser to run tests")
    parser.addoption(
        "--drivers", help="drivers storage", default="Users/tata_rous/Downloads"
    )
    parser.addoption("--headless", action="store_true", help="headless")
    parser.addoption(
        "--base_url", help="Base application url", default="192.168.0.10:8081"
    )
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--selenoid_url", action="store", default="http://localhost:4444/wd/hub")
    parser.addoption("--host", action="store", default="localhost", help="Database host")
    parser.addoption("--port", action="store", default=3306, type=int, help="Database port")
    parser.addoption("--database", action="store", default="opencart", help="Database name")
    parser.addoption("--user", action="store", default="root", help="Database user")
    parser.addoption("--password", action="store", default="", help="Database password")

@pytest.fixture(scope="session")
def connection(request):
    host = request.config.getoption("--host")
    port = request.config.getoption("--port")
    database = request.config.getoption("--database")
    user = request.config.getoption("--user")
    password = request.config.getoption("--password")

    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        charset='utf8mb4',
        autocommit=True
    )

    yield conn

    conn.close()

@pytest.fixture(scope="session")
def base_url(request):
    return "http://" + request.config.getoption("--base_url")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


@pytest.fixture(scope="function")
def browser(request):
    driver = None
    browser_name = request.config.getoption("--browser")
    drivers_storage = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")
    selenoid_url = request.config.getoption("--selenoid_url")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test started at %s" % datetime.datetime.now())
    logger.info("===> SELENOID URL %s" % selenoid_url)

    try:
        if browser_name in ["ch", "chrome"]:
            options = ChromeOptions()
            if headless:
                options.add_argument("headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome(options=options)
        elif browser_name in ["ff", "firefox"]:
            options = FFOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
        elif browser_name in ["ya", "yandex"]:
            options = ChromiumOptions()
            options.binary_location = "Users/tata_rous/Downloads/yandexdriver"
            if headless:
                options.add_argument("headless-new")
            driver = webdriver.Chrome(
                options=options,
                service=ChromiumService(executable_path=f"{drivers_storage}/yandexdriver"),
            )
        elif browser_name in ["remote"]:
            options = ChromeOptions()
            if headless:
                options.add_argument("headless=new")

            # Add Selenoid-specific capabilities
            capabilities = {
                "browserName": "chrome",
                "browserVersion": "latest",
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": False
                }
            }
            options.set_capability("selenoid:options", capabilities["selenoid:options"])

            driver = webdriver.Remote(
                command_executor=selenoid_url,
                options=options)

        allure.attach(
            name=driver.session_id,
            body=json.dumps(driver.capabilities, indent=4, ensure_ascii=False),
            attachment_type=allure.attachment_type.JSON)

        driver.log_level = log_level
        driver.logger = logger
        driver.test_name = request.node.name

        logger.info("Browser %s started" % browser)
        yield driver

    except Exception as e:
        logger.error("Browser setup failed: %s" % str(e))
        raise

    finally:
        # Cleanup - this runs whether the test passes or fails
        if driver is not None:
            try:
                # Take screenshots and attachments on failure
                if hasattr(request.node, 'status') and request.node.status == "failed":
                    try:
                        allure.attach(
                            name="failure_screenshot",
                            body=driver.get_screenshot_as_png(),
                            attachment_type=allure.attachment_type.PNG
                        )
                    except Exception as e:
                        logger.error("Failed to take screenshot: %s" % str(e))

                    try:
                        allure.attach(
                            name="page_source",
                            body=driver.page_source,
                            attachment_type=allure.attachment_type.HTML
                        )
                    except Exception as e:
                        logger.error("Failed to get page source: %s" % str(e))

                # Quit the driver
                driver.quit()
                logger.info("Browser quit successfully")

            except WebDriverException as e:
                logger.warning("Driver quit failed (session may already be terminated): %s" % str(e))
            except Exception as e:
                logger.error("Unexpected error during cleanup: %s" % str(e))

        logger.info("===> Test finished at %s" % datetime.datetime.now())


@pytest.fixture(scope="session")
def catalog_page_url(request):
    return (
            "http://" + request.config.getoption("--base_url") + "/en-gb/catalog/desktops"
    )


@pytest.fixture(scope="session")
def login_page_url(request):
    return (
            "http://"
            + request.config.getoption("--base_url")
            + "/en-gb?route=account/login"
    )


@pytest.fixture(scope="session")
def product_page_url(request):
    return (
            "http://"
            + request.config.getoption("--base_url")
            + "/en-gb/product/desktops/mac/imac"
    )


@pytest.fixture(scope="session")
def register_account_page_url(request):
    return (
            "http://"
            + request.config.getoption("--base_url")
            + "/en-gb?route=account/register"
    )

