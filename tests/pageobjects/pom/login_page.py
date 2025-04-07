#Login page class
#Page locators
#page actions

from selenium.webdriver.common.by import By
from tests.constants.constants import Constants

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    # Page locators
    username = (By.XPATH,"//input[@id='user-name']")
    password = (By.ID,"password")
    login = (By.ID,"login-button")

    #Page actions
    #Write functions to access page locators

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_login(self):
        return self.driver.find_element(*LoginPage.login)
