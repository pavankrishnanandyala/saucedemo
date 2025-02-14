import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        yield
        self.driver.quit()

    def test_login(self, setup):
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("standard_user")
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        assert "Swag Labs" in self.driver.title