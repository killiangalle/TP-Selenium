from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ProductListPage():

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.lbl_Availabilityfilter = '//label[contains(text(),"In stock")][@for="mz-fss-0--1"]/..'
         self.img_ProductItem = '(//div[@class="carousel-item active"]/img[@class="lazy-load"])[3]'


    def clickOn_FilterInStock(self):
         c_lbl_AvailabilityFilter = self.driver.find_element(By.XPATH,self.lbl_Availabilityfilter)
         c_lbl_AvailabilityFilter.click()
         

    def select_img_ProductItem(self):
         c_img_ProductItem = self.driver.find_element(By.XPATH,self.img_ProductItem)
         c_img_ProductItem.click()          

          