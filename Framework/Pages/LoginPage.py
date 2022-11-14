from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    SEARCH_INPUT = (By.NAME, "q")
    POP_UP_LIST = (By.XPATH, ".//li[@role='presentation'][not (@id)]")

    def __init__(self, driver):
        super().__init__(driver)
