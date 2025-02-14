class Add_to_Cart:



    sauce_Labs_Backpack = "//*[@id='add-to-cart-sauce-labs-backpack']"
    sauce_Labs_BikeLight = "//*[@id='add-to-cart-sauce-labs-bike-light']"
    sauce_Labs_Bolt_T_Shirt = "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    sauce_Labs_Fleece_Jacket = "//*[@id='add-to-cart-sauce-labs-fleece-jacket']"
    sauce_Labs_Onesie = "//*[@id='add-to-cart-sauce-labs-onesie']"
    test_allTheThings_Red_T_Shirt = "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
    click_on_cart = "//*[@class='shopping_cart_link']"
    CheckOut = "//*[@id='checkout']"


    def __init__(self ,  driver):
        self.driver = driver

    def backpack(self):
        self.driver.find_element_by_xpath(self.sauce_Labs_Backpack).click()
    def bikelight(self):
        self.driver.find_element_by_xpath(self.sauce_Labs_BikeLight).click()
    def bolt_Tshirt(self):
        self.driver.find_element_by_xpath(self.sauce_Labs_Bolt_T_Shirt).click()
    def Fleece_Jacket(self):
        self.driver.find_element_by_xpath(self.sauce_Labs_Fleece_Jacket).click()
    def Onesie(self):
        self.driver.find_element_by_xpath(self.sauce_Labs_Onesie).click()
    def Red_T_Shirt(self):
        self.driver.find_element_by_xpath(self.test_allTheThings_Red_T_Shirt).click()
    def click_on_cartIcon(self):
        self.driver.find_element_by_xpath(self.click_on_cart).click()
    def Checkout(self):
        self.driver.find_element_by_xpath(self.CheckOut).click()
