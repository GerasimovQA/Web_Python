from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).click()
        print("locator is : " + str(locator))

    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(text)

    def get_element_text(self, locator):
        text = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).get_text
        return text
