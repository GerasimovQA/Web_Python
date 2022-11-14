from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    LOGO = (By.XPATH, ".//div[@class='logo']")

    def wait_element_using_locator(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))

    def click_element_using_locator(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).click()
        print("locator is : " + str(locator))

    def click_element(self, element):
        ActionChains(self.driver).click(element).perform()

    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(text)

    def get_element_text(self, locator):
        text = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).get_text
        return text

    def check_title(self, expected_title):
        self.wait_element_using_locator(self.LOGO)
        actual_title = self.driver.title
        print("Check: " + actual_title + " = " + expected_title)
        assert actual_title == expected_title, "Title is wrong"

    def click_element_in_list(self, list_of_locators, result):
        elements = WebDriverWait(self.driver, 10).until(ec.visibility_of_all_elements_located(list_of_locators))
        for element in elements:
            if element.text == result:
                BasePage.click_element(self, element)
                return
