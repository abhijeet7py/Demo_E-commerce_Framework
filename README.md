### Web Automation Framework with POM in Python(Selenium)


### **Tech Stack **
- Python
- PyTest
- Selenium -> 4.26
- Allure Report - Allure Pytest
- Git Ignore.  (gnore files)
- PyTest HTML - Report
- Page Object Model (with Page Factory)
- Parallel Run with xdist.

### All the dependencies used
- pip install allure-pytest selenium
- pip install pytest selenium pytest-html openpyxl 
- pip install selenium-page-factory 
- pip install pyyaml faker openpyxl
- pip install pytest-xdist 
- pip install mysql-connector-python
- pip install pytest-reportportal
- pip install python-dotenv
### How to run the Framework?
pytest -n auto tests/vwoLoginTests/pom/test_*

### How to run Testcase parallel ?
pytest -n auto 