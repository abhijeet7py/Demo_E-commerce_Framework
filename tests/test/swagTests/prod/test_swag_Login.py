import allure
import pytest
import time
from selenium import webdriver
from tests.constants.constants import Constants
from tests.pageobjects.pom.login_page import LoginPage

#Assertions and use of page object class
# Webdriver start
# User Interaction + assertion
# close driver

@pytest.fixture()
# It marks a function as a fixture.
# A fixture is a reusable piece of code that sets up some state or context before a test runs, and optionally cleans it up afterward.
# Fixtures are commonly used to initialize test data, set up connections, or configure environments that are needed by your tests.
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.login_url())
    return driver

@allure.epic("Swag Login Tests")
@allure.feature("TC_1 - Negative Login Tests without any Username and Password")
@pytest.mark.negative

def test_Swag_Login_negative1(setup):
    login = LoginPage(driver=setup)
    login.login_to_swag(usr="",pwd="")
    error = login.get_error_msg()
    assert error == "Epic sadface: Username is required"

@allure.epic("Swag Login Tests")
@allure.feature("TC_2 - Negative Login Tests without Password")
@pytest.mark.negative
def test_Swag_Login_negative2(setup):
    login = LoginPage(driver= setup)
    login.login_to_swag(usr="abc",pwd="")
    error = login.get_error_msg()
    assert error == "Epic sadface: Password is required"

@allure.epic("Swag Login Tests")
@allure.feature("TC_3 - Negative Login Tests without any Username")
@pytest.mark.negative
def test_Swag_Login_negative3(setup):
    login = LoginPage(driver=setup)
    login.login_to_swag(usr="",pwd="123")
    error = login.get_error_msg()
    assert error == "Epic sadface: Username is required"

@allure.epic("Swag Login Tests")
@allure.feature("TC_4 - Negative Login Tests with wrong Username and Password")
@pytest.mark.negative
def test_Swag_Login_negative4(setup):
    login = LoginPage(driver=setup)
    login.login_to_swag(usr="abc",pwd="123")
    error = login.get_error_msg()
    assert error == "Epic sadface: Username and password do not match any user in this service"

@allure.epic("Swag Login Tests")
@allure.feature("TC_5 - Positive Login Test")
@pytest.mark.positive

def test_Swag_Login_positive(setup):
    login = LoginPage(driver=setup)
    login.login_to_swag(usr="standard_user",pwd="secret_sauce")
    login.get_change_url()
    # time.sleep(5)


