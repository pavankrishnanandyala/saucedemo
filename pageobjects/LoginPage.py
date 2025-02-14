from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

  textbox_username_id = "//*[@id='user-name']"
  textbox_password_id  = "//*[@id='password']"
  login_button = "//*[@id='login-button']"



  def __init__(self,driver):
    self.driver = driver
    self.WebDriverWait = WebDriverWait(self.driver, 10)

  def setUserName(self, username):
    self.WebDriverWait.until(EC.presence_of_element_located((By.XPATH, self.textbox_username_id)))
    self.driver.find_element(By.XPATH, self.textbox_username_id).clear()
    self.driver.find_element(By.XPATH, self.textbox_username_id).send_keys(username)

  def setPasssword(self, password):
    self.WebDriverWait.until(EC.presence_of_element_located((By.XPATH, self.textbox_password_id)))
    self.driver.find_element(By.XPATH, self.textbox_password_id).clear()
    self.driver.find_element(By.XPATH, self.textbox_password_id).send_keys(password)

  def clicklogin(self):
    self.driver.find_element(By.XPATH, self.login_button).click()