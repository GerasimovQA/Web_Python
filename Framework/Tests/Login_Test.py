import time

from selenium.webdriver.common.by import By

from Config.Config import Config
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Tests.Base_Test import BaseTest
import pytest


class TestCat(BaseTest):

    # def setup_method(self):
    # def teardown_method(self):

    @pytest.mark.parametrize("url, text", [(Config.URL, "666"), (Config.URL, "777")])
    def test_1(self, url, text):
        self.base_Page = BasePage(self.driver)
        self.driver.get(url)
        print(self.driver.title)
        self.base_Page.enter_text(LoginPage.SEARCH_INPUT, text)
        self.base_Page.click(LoginPage.POP_UP_LIST)
        time.sleep(3)

    @pytest.mark.parametrize("text", ["888", "999"])
    def test_2(self, text):
        self.driver.get(Config.URL)
        print(self.driver.title)
        locator = self.driver.find_element(By.NAME, "q")
        locator.send_keys(text)
        print(locator.get_attribute("name"))
        time.sleep(3)
