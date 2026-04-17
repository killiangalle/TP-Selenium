from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class CartPage():

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.btn_CartPage = '//a[contains(text(),"Checkout")]'
      


    def clickOn_CartPage(self):
         c_btn_CartPage = self.driver.find_element(By.XPATH,self.btn_CartPage)
         c_btn_CartPage.click()
         