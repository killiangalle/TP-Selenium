import sys
import os
 
import pytest
 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..")) # .. on remontepip
 
from helpers.BaseTest import BaseTest
from pages.HomePage import HomePage
from pageFragments.HeaderPageFragment import HeaderPageFragment
from pages.ProductListPage import ProductListPage
from time import sleep
from pages.ProductPage import ProductPage
from pages.AddToCartPopUpPage import AddToCartPopUpPage
from pages.CartPage import CartPage
from pages.CheckOutPage import CheckOutPage
from pages.CheckOutConfitmPage import CheckOutconfirmPage

class Test_FirstTest(BaseTest): # héritage
 
    @pytest.mark.test_FirstTest
    def test_MyFirstTest(self):
        self.open_application()
 
        home = HomePage(self.driver)
        home.is_page_visible("Your Store")

        header = HeaderPageFragment(self.driver)
        header.select_menu()
        header.select_subMenu()
        sleep(5)
        productList = ProductListPage(self.driver)
        productList.clickOn_FilterInStock()
        sleep (3)
        productList.select_img_ProductItem()

        productPage = ProductPage(self.driver)
        productPage.clickOn_AddToCard() 
        sleep (3)

        addToCartPopUpPage = AddToCartPopUpPage(self.driver)
        addToCartPopUpPage.clickOn_btn_ViewCart()
        sleep (2)

        cartPage = CartPage(self.driver)
        cartPage.clickOn_CartPage()
        sleep (2)

        checkOutPage = CheckOutPage(self.driver)
        checkOutPage.clickOn_GestCheckOut()
        checkOutPage.Input_FirstName("toto")
        checkOutPage.Input_LastName("tata")
        checkOutPage.Input_Email("toto@gmail.fr")
        checkOutPage.Input_Telephone("0102030405")
        checkOutPage.Input_Adress_1("32B rue Bernard Hinault")
        checkOutPage.Input_City("Brest")
        checkOutPage.Input_PostCode("29200")
        checkOutPage.Input_Country("France, Metropolitan")
        checkOutPage.Input_State("Finistère")
        sleep(2)
        checkOutPage.clickOn_AcceptTherms()
        checkOutPage.clickOn_Continue()
        sleep (2)

        checkOutConfirmPage = CheckOutconfirmPage(self.driver)
        checkOutConfirmPage.clickOn_btn_ConfirmOrder()
        sleep (4)