from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('Launch the Browser')
def lauchbrowser(context):
    context.driver = webdriver.Chrome()

@when('Open Swag Website')
def openSwag(context):
    context.driver.get("https://www.saucedemo.com/")

@when('Enter Username "{usr}" and Password "{pwd}"')
def login(context,usr,pwd):
    username = context.driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys(usr)
    password = context.driver.find_element(By.ID,"password").send_keys(pwd)
    button = context.driver.find_element(By.ID,"login-button").click()

@then('Verify Homepage URL')
def verify(context):
    assert context.driver.current_url == "https://www.saucedemo.com/inventory.html"
