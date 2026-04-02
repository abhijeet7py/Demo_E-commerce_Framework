"""Sample login tests using fixture-driven driver injection."""

from __future__ import annotations

import pytest

from data.login_test_data import INVALID_LOGIN_CASES
from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("username,password,expected_error", INVALID_LOGIN_CASES)
def test_invalid_login(
    driver,
    framework_config,
    username: str,
    password: str,
    expected_error: str,
) -> None:
    """Validate error handling for invalid login scenarios."""
    login_page = LoginPage(driver=driver, timeout=framework_config["timeout"])
    login_page.login(username=username, password=password)
    assert login_page.error_message() == expected_error


@pytest.mark.smoke
@pytest.mark.regression
def test_valid_login(driver, framework_config) -> None:
    """Validate successful login redirection for a valid user."""
    login_page = LoginPage(driver=driver, timeout=framework_config["timeout"])
    login_page.login(username="standard_user", password="secret_sauce")
    login_page.wait_for_url_contains("inventory")
    assert "inventory" in driver.current_url
