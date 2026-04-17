from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class CheckOutconfirmPage():

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.btn_ConfirmOrder = '//button[contains(text(),"Confirm Order ")]'

    def clickOn_btn_ConfirmOrder(self):
         clickOn_btn_ConfirmOrder = self.driver.find_element(By.XPATH,self.btn_ConfirmOrder)
         clickOn_btn_ConfirmOrder.click()     