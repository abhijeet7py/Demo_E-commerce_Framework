### Demo E-commerce Selenium Framework (Refactored)

Production-oriented, beginner-friendly test automation framework using:
- Python + Selenium + Pytest
- Page Object Model (POM)
- Centralized driver fixture
- JSON-based environment configuration
- Allure reporting + failure screenshots
- Logging and retry utility for flaky UI interactions

## Refactored Structure

```text
project_root/
│── tests/
│   └── test_login.py
│── pages/
│   ├── base_page.py
│   └── login_page.py
│── utils/
│   ├── logger.py
│   └── retry.py
│── config/
│   ├── config_reader.py
│   └── settings.json
│── data/
│   └── login_test_data.py
│── reports/
│── conftest.py
│── pytest.ini
```

## Run Tests

```bash
pytest
```

## Switch Environment

```bash
TEST_ENV=dev pytest
```

## Allure Report

```bash
allure serve reports/allure-results
```
