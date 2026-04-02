"""Shared pytest fixtures and hooks for webdriver lifecycle."""

from __future__ import annotations

import importlib
import importlib.util
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver

from config.config_reader import ConfigReader
from utils.logger import get_logger


LOGGER = get_logger(__name__)


def _create_driver(browser: str, headless: bool = False) -> WebDriver:
    """Driver factory keeping browser creation in one place."""
    if browser.lower() != "chrome":
        raise ValueError(f"Unsupported browser: {browser}")

    options = ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    return webdriver.Chrome(service=ChromeService(), options=options)


def _attach_to_allure(name: str, file_path: Path) -> None:
    """Attach file to Allure only when allure is installed."""
    if importlib.util.find_spec("allure") is None:
        return

    allure = importlib.import_module("allure")
    attachment_type = importlib.import_module("allure_commons.types").AttachmentType
    allure.attach.file(str(file_path), name=name, attachment_type=attachment_type.PNG)


@pytest.fixture(scope="function")
def driver() -> WebDriver:
    """Single source of truth for WebDriver initialization per test."""
    env_config = ConfigReader().get_env_config()
    web_driver = _create_driver(
        browser=env_config["browser"],
        headless=env_config.get("headless", False),
    )
    web_driver.get(env_config["base_url"])
    LOGGER.info("Browser launched: %s", env_config["browser"])

    yield web_driver

    web_driver.quit()
    LOGGER.info("Browser closed")


@pytest.fixture(scope="session")
def framework_config() -> dict:
    """Expose active environment configuration to tests/pages."""
    return ConfigReader().get_env_config()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    """Capture screenshot on test failure and attach to Allure."""
    outcome = yield
    result = outcome.get_result()

    if result.when != "call" or result.passed:
        return

    failed_driver: WebDriver | None = item.funcargs.get("driver")
    if not failed_driver:
        return

    screenshot_dir = Path("reports/screenshots")
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    screenshot_path = screenshot_dir / f"{item.name}.png"
    failed_driver.save_screenshot(str(screenshot_path))
    _attach_to_allure(name=f"failure-{item.name}", file_path=screenshot_path)
