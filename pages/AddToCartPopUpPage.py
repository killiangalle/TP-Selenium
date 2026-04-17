from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class AddToCartPopUpPage():

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.btn_ViewCart = '//a[contains(text(),"View Cart ")]'
      


    def clickOn_btn_ViewCart(self):
         c_btn_ViewCart = self.driver.find_element(By.XPATH,self.btn_ViewCart)
         c_btn_ViewCart.click()