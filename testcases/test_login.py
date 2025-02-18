import logging
import os
import time

import pytest
from pageobjects.LoginPage import LoginPage
from utilities.customlogger import LogGen
from utilities.ReadProperties import ReadConfig


class Test001Login:
    # Class level setup
    baseUrl = ReadConfig.getbaseUrl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    expected_url = "https://www.saucedemo.com/inventory.html"

    @pytest.fixture(autouse=True)
    def setup_class(self):
        # Create necessary directories
        for directory in ["Logs", "Screenshots"]:
            dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), directory)
            os.makedirs(dir_path, exist_ok=True)

        # Initialize logger
        self.logger = LogGen.loggen()
        self.logger.setLevel(logging.INFO)

    @pytest.mark.order(1)
    def test_pagetitle(self, setup):
        """Test the page title of the application"""
        self.logger.info("*** Started Page Title Test ***")
        try:
            self.driver = setup
            self.logger.info("*** Opening the url ***")
            self.driver.get(self.baseUrl)

            actual_title = self.driver.title
            expected_title = "Swag Labs"

            assert actual_title == expected_title, f"Expected title '{expected_title}' but got '{actual_title}'"
            self.logger.info("*** Page Title Test Passed ***")

        except Exception as e:
            self.logger.error(f"*** Page Title Test Failed: {str(e)} ***")
            raise
        finally:
            if hasattr(self, 'driver'):
                self.driver.quit()

    @pytest.mark.order(2)
    def test_login(self, setup):
        """Test the login functionality"""
        self.logger.info("*** Started Login Test ***")
        self.driver = setup
        try:
            self.logger.info("*** Opening the url ***")
            self.driver.get(self.baseUrl)

            # Initialize page object
            self.lp = LoginPage(self.driver)
            time.sleep(5)

            # Perform login steps
            self.lp.setUserName(self.username)
            time.sleep(5)
            self.lp.setPasssword(self.password)
            time.sleep(5)
            self.lp.clicklogin()

            current_url = self.driver.current_url
            assert current_url == self.expected_url, f"Expected URL '{self.expected_url}' but got '{current_url}'"
            self.logger.info("*** Login Test Passed ***")

        except Exception as e:
            self.logger.error(f"*** Login Test Failed: {str(e)} ***")
            # Take screenshot on failure
            screenshot_path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                "Screenshots",
                "test_login.png"
            )
            self.driver.save_screenshot(screenshot_path)
            raise
        finally:
            if hasattr(self, 'driver'):
                self.driver.quit()
