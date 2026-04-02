"""Login page object for SauceDemo."""

from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object containing only login actions and interactions."""

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        super().__init__(driver=driver, timeout=timeout)

    def login(self, username: str, password: str) -> None:
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)
