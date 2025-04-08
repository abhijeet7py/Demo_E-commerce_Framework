#Inventory psge class
# Page locators
# Page Actions

from selenium.webdriver.common.by import By
from tests.constants.constants import Constants
from tests.utils.common_utils import webdriver_wait,webdriver_wait_url


class InventoryPage:
    def __init__(self,driver):
        self.driver = driver

    #Page locators
    cart = (By.XPATH,"//a[@data-test='shopping-cart-link']")
    filters = (By.CSS_SELECTOR,".product_sort_container")
    add_to_cart = (By.ID,"add-to-cart-sauce-labs-backpack")
    hamburger = (By.ID,"react-burger-menu-btn")
    cart_badge = (By.XPATH,"//span[@class='shopping_cart_badge' and text()='1']")

    # Page Actions
    # Write functions to access page locators

