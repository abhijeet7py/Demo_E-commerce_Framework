"""Base page with reusable Selenium actions and explicit waits."""

from __future__ import annotations

from typing import Tuple

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from utils.retry import retry

Locator = Tuple[str, str]


class BasePage:
    """All page objects should inherit from this class."""

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.timeout = timeout

    def wait_for_element(self, locator: Locator) -> WebElement:
        """Wait until element is visible and return it."""
        return WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located(locator)
        )

    def click(self, locator: Locator) -> None:
        """Wait and click an element."""
        retry(lambda: self.wait_for_element(locator).click())

    def send_keys(self, locator: Locator, value: str) -> None:
        """Wait, clear and type into an element."""

        def _type() -> None:
            element = self.wait_for_element(locator)
            element.clear()
            element.send_keys(value)

        retry(_type)

    def get_text(self, locator: Locator) -> str:
        """Wait and return text from an element."""
        return retry(lambda: self.wait_for_element(locator).text)

    def wait_for_url_contains(self, partial_url: str) -> None:
        """Wait until URL contains the expected value."""
        WebDriverWait(self.driver, self.timeout).until(ec.url_contains(partial_url))
