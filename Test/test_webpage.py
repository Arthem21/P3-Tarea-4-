import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


user = "Alberto"
password = "Montez"

name = "Dr Moriarti"
country = "Dominican Republic"
city = "Santo Domingo"
creditCard = "************"
month = "may"
year = "2025"

email = "AG@gmail.com"
contact = "Mr Fox"
message = ("Do a barrel roll")


class Prueba(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        time.sleep(2)

    def search_element(self, xpath):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()

    def write(self, xpath, text):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        element.clear()
        element.send_keys(text)

    def tearDown(self):
        self.driver.quit()

   
    def test_cart(self):
        try:
            self.search_element('//*[@id="navbarExample"]/ul/li[4]/a')

            time.sleep(2)
            self.driver.save_screenshot("./Results/Cart/ViewCart.png")
            time.sleep(2)

            self.search_element('//*[@id="navbarExample"]/ul/li[1]/a')
            self.search_element('//*[@id="tbodyid"]/div[2]/div/div/h4/a')
            self.search_element('//*[@id="tbodyid"]/div[2]/div/a')

            alert = self.wait.until(EC.alert_is_present())
            alert.accept()  

            self.search_element('//*[@id="navbarExample"]/ul/li[1]/a')
            self.search_element('//*[@id="tbodyid"]/div[5]/div/div/h4/a')
            self.search_element('//*[@id="tbodyid"]/div[2]/div/a')
            alert = self.wait.until(EC.alert_is_present())
            alert.accept() 

            self.search_element('//*[@id="navbarExample"]/ul/li[1]/a')
            self.search_element('//*[@id="tbodyid"]/div[7]/div/div/h4/a')
            self.search_element('//*[@id="tbodyid"]/div[2]/div/a')
            alert = self.wait.until(EC.alert_is_present())
            alert.accept() 

            self.search_element('//*[@id="cartur"]')

            time.sleep(2)
            self.driver.save_screenshot("./Results/Cart/CartWhithItiems.png")
            time.sleep(2)
  
            self.search_element('//*[@id="tbodyid"]/tr[1]/td[4]/a')  

            time.sleep(2)
            self.driver.save_screenshot("./Results/Cart/RemoveItem.png")
            time.sleep(2)

            self.search_element('//*[@id="page-wrapper"]/div/div[2]/button')

            time.sleep(2)
            self.driver.save_screenshot("./Results/Cart/OrderForm.png")
            time.sleep(2)
            
            self.write('//*[@id="name"]', name)
            self.write('//*[@id="country"]', country)
            self.write('//*[@id="city"]', city)
            self.write('//*[@id="card"]', creditCard)
            self.write('//*[@id="month"]', month)
            self.write('//*[@id="year"]', year)         

            time.sleep(2)
            self.driver.save_screenshot("./Results/Cart/CompleteOrderForm.png")
            time.sleep(2)

            self.search_element('/html/body/div[3]/div/div/div[3]/button[2]')
          
        except Exception as e:
            self.fail(f"Fallo en la prueba del carrito: {e}")

    

    def test_shop(self):

        try:
            time.sleep(2)
            self.driver.save_screenshot("./Results/Shop/EnterShop.png")
            time.sleep(2)

            
            list_group_items = self.driver.find_elements(By.CLASS_NAME, "list-group-item")

            for item in list_group_items:
                if item.get_attribute("id") == "itemc":
                    item.click()
                    time.sleep(2)
                    self.driver.save_screenshot(f"./Results/Shop/View_{item.text}.png")
                    time.sleep(2)
            
            self.search_element('//*[@id="tbodyid"]/div[2]/div/div/h4/a')

            time.sleep(2)
            self.driver.save_screenshot("./Results/Shop/ViewItem.png")
            time.sleep(2)

        except Exception as e:
            self.fail(f"Fallo en la prueba de navegación por la tienda: {e}")



    def test_contact(self):
            
            try:
                self.search_element('//*[@id="navbarExample"]/ul/li[2]/a')

                time.sleep(2)
                self.driver.save_screenshot("./Results/Contact/EnterContactForm.png")
                time.sleep(2)

                self.write('//*[@id="recipient-email"]', email)
                self.write('//*[@id="recipient-name"]', contact)
                self.write('//*[@id="message-text"]', message)

                time.sleep(2)
                self.driver.save_screenshot("./Results/Contact/CompleteContactForm.png")
                time.sleep(2)
                
                self.search_element('//*[@id="exampleModal"]/div/div/div[3]/button[2]')

                time.sleep(2)
                alert = self.wait.until(EC.alert_is_present())
                alert.accept()  

            except Exception as e:
                self.fail(f"Fallo en la prueba de contacto: {e}")

         
    
    

    def test_login(self):

            try:

                self.search_element("//*[@id='login2']")

                time.sleep(2)
                self.driver.save_screenshot("./Results/LogIn/EnterLogIn.png")
                time.sleep(2)

                self.write("//*[@id='loginusername']", user)
                self.write("//*[@id='loginpassword']", password)

                time.sleep(2)
                self.driver.save_screenshot("./Results/LogIn/CompleteLogIn.png")
                time.sleep(2)
                
                self.search_element("//*[@id='logInModal']/div/div/div[3]/button[2]")

                time.sleep(2)
                self.driver.save_screenshot("./Results/LogIn/AfterLogIn.png")
                time.sleep(2)

            except Exception as e:
                self.fail(f"Fallo en la prueba de inicio de sesión: {e}")

             
    
    
        
    def test_signin(self):
        
            try:

                self.search_element("//*[@id='signin2']")

                time.sleep(2)
                self.driver.save_screenshot("./Results/SingIn/EnterSingIn.png")
                time.sleep(2)

                self.write("//*[@id='sign-username']", "Monica Perez")
                self.write("//*[@id='sign-password']", password)

                time.sleep(2)
                self.driver.save_screenshot("./Results/SingIn/CompleteSingIn.png")
                time.sleep(2)
                
                self.search_element("//*[@id='signInModal']/div/div/div[3]/button[2]")

                time.sleep(2)
                self.driver.save_screenshot("./Results/SingIn/AfterSingIn.png")
                time.sleep(2)

            except Exception as e:
                self.fail(f"Fallo en la prueba de registro: {e}")



if __name__ == '__main__':
    unittest.main(verbosity=2)


