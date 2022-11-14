import requests
from Config.Config import Config
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Tests.Base_test import BaseTest
import pytest

class TestCat(BaseTest):

    # def setup_method(self):
    # def teardown_method(self):

    @pytest.mark.parametrize("url, short_request, long_request, exp_title", [(Config.URL, "666", "666 angel number meaning", "666 angel number meaning - Google Search"),
                                                                             (Config.URL, "777", "7777 meaning", "7777 meaning - Google Search")])
    def test_1(self, url, short_request, long_request, exp_title):
        self.base_Page = BasePage(self.driver)
        self.login_Page = LoginPage(self.driver)
        self.driver.get(url)
        self.base_Page.enter_text(LoginPage.SEARCH_INPUT, short_request)
        self.base_Page.click_element_in_list(LoginPage.POP_UP_LIST, long_request)
        self.base_Page.check_title(exp_title)

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
