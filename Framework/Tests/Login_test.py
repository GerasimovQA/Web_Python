import json
import time

import requests
from selenium.webdriver.common.by import By

from Config.Config import Config
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Tests.Base_test import BaseTest
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

    def test_get_request(self):
        response = requests.get("https://reqres.in/api/users/2")
        json_response = response.json()
        assert str(response) == '<Response [200]>'
        assert str(json_response["data"]["email"]) == 'janet.weaver@reqres.in'

    def test_post_request(self):
        name = "Neo"
        job = "THE ONE"
        payload = {"name": name, "job": job}
        response = requests.post("https://reqres.in/api/users", data=payload)
        json_response = response.json()
        assert str(response) == '<Response [201]>'
        print("666 - " + str(json_response))
        assert str(json_response["name"]) == name
        assert str(json_response["job"]) == job

    def test_put_request(self):
        name = "Neo"
        job = "THE ONE"
        payload = {"name": name, "job": job}
        response = requests.put("https://reqres.in/api/users/2", data=payload)
        json_response = response.json()
        assert str(response) == '<Response [200]>'
        print("666 - " + str(json_response))
        assert str(json_response["name"]) == name
        assert str(json_response["job"]) == job
        assert str(json_response["updatedAt"] != "0")

    def test_delete_request(self):
        response = requests.delete("https://reqres.in/api/users/2")
        text_response = response.text
        assert str(response) == '<Response [204]>'
        assert text_response == ''
