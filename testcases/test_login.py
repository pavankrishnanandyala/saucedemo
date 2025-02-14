from pageobjects.LoginPage import LoginPage
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
import pytest


class test_001_Login():


    baseUrl = ReadConfig.getbaseUrl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = logGen.logger()
    expected_url = "https://www.saucedemo.com/inventory.html"



    def test_pagetitle(self, setup):
       self.logger.info("*** Started Page Title Test ***")
       self.driver = setup
       self.logger.info("*** Opening the url ***")
       self.driver.get(self.baseUrl)

       if self.driver.title == "Swag Labs":
          self.logger.info("*** Page Title Test Passed ***")
          self.driver.close()
          assert True
       else:
           self.logger.error("*** Page Title Test Failed")
           self.driver.close()
           assert False


    def test_login(self, setup):
         self.logger.info("*** Started Login Test ***")
         self.driver = setup
         self.driver.get(self.baseUrl)
         self.lp = LoginPage(self.driver)
         self.lp.setUserName(self.username)
         self.lp.setPasssword(self.password)
         self.lp.clicklogin()
         if self.driver.current_url == self.expected_url:
            self.logger.info("*** Login Test Passed ***")
            self.driver.close()
            assert True
         else:
            self.logger.error("*** Login Test Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            assert False
