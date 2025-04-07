#Login page class
#Page locators
#page actions

from selenium.webdriver.common.by import By
from tests.constants.constants import Constants
from tests.utils.common_utils import webdriver_wait
from tests.utils.common_utils import webdriver_wait,webdriver_wait_url
class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    # Page locators
    username = (By.XPATH,"//input[@id='user-name']")
    password = (By.ID,"password")
    login = (By.ID,"login-button")
    error_msg = (By.XPATH,"//h3[@data-test='error']")

    #Page actions
    #Write functions to access page locators

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_login(self):
        return self.driver.find_element(*LoginPage.login)

    def get_error_msg(self):
        webdriver_wait(self.driver,element_tuple=self.error_msg,timeout=5)
        return self.driver.find_element(*LoginPage.error_msg).text

    def login_to_swag(self,usr,pwd):
        try:
            self.get_username().send_keys(usr)
            self.get_password().send_keys(pwd)
            self.get_login().click()
        except Exception as e:
            print(e)

    def get_change_url(self):
        expected_url = Constants.inventory_url()
        webdriver_wait_url(self.driver,timeout=5)
        assert self.driver.current_url == expected_url, f"Expected {expected_url} but got {self.driver.current_url}"



