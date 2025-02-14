from enum import verify


class CheckOut_Information:
    checkout_Your_Information =  "//*[@class='title']"
    textbox_firstname = "//*[@id='first-name']"
    textbox_lastname = "//*[@id='last-name']"
    textbox_ZipCode = "//*[@id='postal-code']"
    click_on_continue_button = "//*[@id='continue']"
    Checkout_Overview_Title = "//*[@class='title']"
    Click_on_finish_button = "//*[@class='btn btn_action btn_medium cart_button']"
    checkout_Page_Tilte = "//*[@class='title']"
    complete_header = "//*[@class='complete-header']"

    def __init__(self , driver):
        self.driver = driver

    def informationPage(self):
         verify == self.driver.find_element_by_xpath(self.checkout_Your_Information).text
         print(verify)
         #assert == 'Checkout: Your Information'

    def FirstName(self , firstname):
        self.driver.find_element_by_xpath(self.textbox_firstname).clear()
        self.driver.find_element_by_xpath(self.textbox_firstname).send_keys(firstname)

    def LastName(self, lastname):
        self.driver.find_element_by_xpath(self.textbox_lastname).clear()
        self.driver.find_element_by_xpath(self.textbox_lastname).send_keys(lastname)

    def Zipcode(self, postalcode):
        self.driver.find_element_by_xpath(self.textbox_ZipCode).clear()
        self.driver.find_element_by_xpath(self.textbox_ZipCode).send_keys(postalcode)

    def continueButton(self):
        self.driver.find_element_by_xpath(self.click_on_continue_button).click()

    def overviewPage(self):
        verify = self.driver.find_element_by_xpath(self.Checkout_Overview_Title).text
        print(verify)
        #assert.verify == 'Checkout: Overview'

    def finishButton(self):
        self.driver.find_element_by_xpath(self.Click_on_finish_button).click()


    def checkoutPage (self):
        verify = self.driver.find_element_by_xpath(self.checkout_Page_Tilte).text
        print(verify)
        #assert.verify == 'Checkout: Complete!'

    def completedMessage(self):
        verify = self.driver.find_element_by_xpath(self.complete_header).text
        print(verify)
        #assert.verify == 'Thank you for your order!'