from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ProductPage():

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.btn_AddToCard = '(//button[contains(text(),"Add to Cart")])[2]'
      


    def clickOn_AddToCard(self):
         c_btn_AddToCard = self.driver.find_element(By.XPATH,self.btn_AddToCard)
         c_btn_AddToCard.click()
         

         