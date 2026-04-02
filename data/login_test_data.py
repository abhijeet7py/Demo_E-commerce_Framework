"""Centralized test data for login scenarios."""

INVALID_LOGIN_CASES = [
    ("", "", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
    ("", "secret_sauce", "Epic sadface: Username is required"),
    (
        "locked_user",
        "wrong_password",
        "Epic sadface: Username and password do not match any user in this service",
    ),
]
