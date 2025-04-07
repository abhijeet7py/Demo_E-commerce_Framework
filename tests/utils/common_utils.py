from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tests.constants.constants import Constants

# Method overloading

def webdriver_wait(driver,element_tuple,timeout):
    WebDriverWait(driver=driver,timeout=timeout).until(
        EC.visibility_of_element_located(element_tuple))

def webdriver_wait_url(driver,timeout):
    WebDriverWait(driver = driver, timeout=timeout).until(EC.url_to_be(Constants.inventory_url()))