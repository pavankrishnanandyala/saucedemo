
import pytest
from selenium import webdriver
from pytest_metadata import plugin
from datetime import datetime
from utilities.report_generator import HTMLReportGenerator


@pytest.fixture(scope="function")
def setup(request, browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge browser")
    else:
        driver = webdriver.Chrome()
        print("Launching default Chrome browser")

    request.cls.driver = driver
    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')

@pytest.fixture(scope="function")
def browser(request):
    return request.config.getoption('--browser')



# pytest HTML reports
def pytest_html_report_title(report):
    report.title = "Test Execution Report (demo Application)"


def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
    metadata.pop('Packages', None)
    metadata.pop('Platform', None)




def pytest_configure(config):
    config.stash[plugin.metadata_key]["Project"] = "demo"
    config.stash[plugin.metadata_key]["Module"] = "login module"
    config.stash[plugin.metadata_key]["Tester"] = "pavan krishna"

    """Initialize test results collection."""
    config.test_results = {
        'total': 0,
        'passed': 0,
        'failed': 0,
        'skipped': 0,
        'details': []
    }


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Collect test results during test execution."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        # Get test duration
        duration = report.duration if hasattr(report, 'duration') else 0

        # Collect test results
        test_detail = {
            'name': item.name,
            'status': report.outcome.upper(),
            'duration': duration
        }

        # Add error message if test failed
        if report.outcome == "failed":
            test_detail['error'] = str(report.longrepr)

        # Update test counts
        item.config.test_results['total'] += 1
        item.config.test_results[report.outcome] += 1
        item.config.test_results['details'].append(test_detail)


def pytest_sessionfinish(session, exitstatus):
    """Generate HTML report after all tests are complete."""
    results = session.config.test_results

    # Calculate pass rate
    total = results['total']
    if total > 0:
        results['pass_rate'] = (results['passed'] / total) * 100
    else:
        results['pass_rate'] = 0

    # Generate HTML report
    report_generator = HTMLReportGenerator()
    report_path = report_generator.generate_html_report(results)

    print(f"\nHTML Report generated: {report_path}")