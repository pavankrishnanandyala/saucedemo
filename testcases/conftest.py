import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
import os


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge")
    else:
        driver = webdriver.Chrome()
    return driver


@pytest.fixture(autouse=True)
def setup_html_report_dir():
    # Create htmlreports directory if it doesn't exist
    reports_dir = os.path.join(os.getcwd(), 'htmlreports')
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

# pytest HTML reports
def pytest_html_report_title(report):
    report.title = "Test Execution Report (OpenCart)"

def pytest_configure(config):
    config.stash[metadata_key]["Project"] = "OpenCart"
    config.stash[metadata_key]["Module"] = "full"
    config.stash[metadata_key]["Tester"] = "pavan"

def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
    metadata.pop('Packages', None)
    metadata.pop('Platform', None)