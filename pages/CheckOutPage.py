from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class CheckOutPage():

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.lbl_GuestCheckOut = '//label[contains(text(),"Guest Checkout")]'
         self.input_firstname = '//input[@name="firstname"]'
         self.input_lastname = '//input[@name="lastname"]'
         self.input_email = '//input[@name="email"]'
         self.input_telephone = '//input[@name="telephone"]'
         self.input_adress_1 = '//input[@name="address_1"]'
         self.input_city = '//input[@name="city"]'
         self.input_postcode = '//input[@name="postcode"]'
         self.input_country = 'input-payment-country'
         self.input_state = 'input-payment-zone'  
         self.lbl_AcceptTherms = '//label[@for="input-agree"]' 
         self.btn_Continue = '//button[contains(text(),"Continue")]'    


    def clickOn_GestCheckOut(self):
         c_lbl_GestCheckOut = self.driver.find_element(By.XPATH,self.lbl_GuestCheckOut)
         c_lbl_GestCheckOut.click()


    def Input_FirstName(self, firstname: str):
         c_input_firstname = self.driver.find_element(By.XPATH,self.input_firstname)
         c_input_firstname.send_keys(firstname)

    def Input_LastName(self, lastname: str):
         c_input_lasttname = self.driver.find_element(By.XPATH,self.input_lastname)
         c_input_lasttname.send_keys(lastname)     
         
    def Input_Email(self, email: str):
         c_input_email = self.driver.find_element(By.XPATH,self.input_email)
         c_input_email.send_keys(email)

    def Input_Telephone(self, telephone: str):
         c_input_telephone = self.driver.find_element(By.XPATH,self.input_telephone)
         c_input_telephone.send_keys(telephone) 

    def Input_Adress_1(self, adress_1: str):
         c_input_adress_1 = self.driver.find_element(By.XPATH,self.input_adress_1)
         c_input_adress_1.send_keys(adress_1)     

    def Input_City(self, city: str):
         c_input_city = self.driver.find_element(By.XPATH,self.input_city)
         c_input_city.send_keys(city)         

    def Input_PostCode(self, postcode: str):
         c_input_postcode = self.driver.find_element(By.XPATH,self.input_postcode)
         c_input_postcode.send_keys(postcode)          

    def Input_Country(self, country: str):
         select_element = self.driver.find_element(By.ID, self.input_country)
         select_country = Select(select_element)
         select_country.select_by_visible_text(country)

    def Input_State(self, state: str):
         select_element = self.driver.find_element(By.ID, self.input_state)
         select_country = Select(select_element)
         select_country.select_by_visible_text(state)

    def clickOn_AcceptTherms(self):
         c_lbl_AcceptTherms = self.driver.find_element(By.XPATH,self.lbl_AcceptTherms)
         c_lbl_AcceptTherms.click()
    
    def clickOn_Continue(self):
         c_btn_Continue = self.driver.find_element(By.XPATH,self.btn_Continue)
         c_btn_Continue.click()
    
    
         