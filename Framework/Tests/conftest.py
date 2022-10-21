import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = None


@pytest.fixture(params=["Chrome-1024,768", "Chrome-1600,200", "FF-400,1200"], scope='function')
def init_driver(request):
    global driver
    print(request)
    resolution = request.param.split("-")[1]
    width = resolution.split(",")[0]
    height = resolution.split(",")[1]

    if "Chrome" in request.param:
        options_chrome = webdriver.ChromeOptions()
        options_chrome.headless = False
        options_chrome.add_argument("--window-size=" + resolution)
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options_chrome)
    if "FF" in request.param:
        options_ff = webdriver.FirefoxOptions()
        options_ff.headless = False
        options_ff.add_argument("--width=" + width)
        options_ff.add_argument("--height=144" + height)
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options_ff)
    request.cls.driver = driver
    yield
    driver.close()
    print("Let's close a browser")
