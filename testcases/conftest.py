import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
import os
from collections import abc
import collections
import os
import pytest



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


# Backward compatibility fix for collections.Mapping
if not hasattr(collections, 'Mapping'):
    collections.Mapping = abc.Mapping

@pytest.fixture(autouse=True)
def setup_reports_dir():
    # Create Reports directory if it doesn't exist
    reports_dir = os.path.join(os.getcwd(), 'Reports')
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

@pytest.fixture(scope="session", autouse=True)
def configure_html_report_env(request):
    request.config.option.htmlpath = os.path.join('Reports', 'report.html')





def pytest_configure(config):
    """
    Pytest configuration hook to set up the test environment
    """
    # Create Reports directory if it doesn't exist
    reports_dir = os.path.join(os.getcwd(), 'Reports')
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    # Configure the HTML report path
    if not hasattr(config.option, 'htmlpath'):
        config.option.htmlpath = os.path.join('Reports', 'report.html')

@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """
    Setup any state specific to the execution of all tests
    """
    # Create Reports directory if it doesn't exist
    reports_dir = os.path.join(os.getcwd(), 'Reports')
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    yield

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