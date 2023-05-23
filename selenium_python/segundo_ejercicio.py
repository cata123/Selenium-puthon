from selenium import webdriver
import unittest
from pyunitreport import HTMLTestRunner
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class suma(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'D:\Laura\Documentos\Laura\selenium_python\chromedriver_win32\chromedriver.exe')
        driver =self.driver
        driver.implicitly_wait(5)
        driver.maximize_window()

    def test_suma(self):
        driver = self.driver
        driver.get("http://www.seleniumeasy.com/test/basic-first-form-demo.html")
        assert "Selenium Easy Demo - Simple Form to Automate using Selenium" in driver.title
        
        EnterA = driver.find_element_by_id("sum1")
        EnterA.clear()
        EnterA.send_keys(2)
        
        EnterB = driver.find_element_by_id("sum2")
        EnterB.clear()
        EnterB.send_keys(3)
      
        eleShowSumgBtn=driver.find_element_by_xpath('//*[@id="gettotal"]/button')
        eleShowSumgBtn.click()
      
        eleYourSum=driver.find_element_by_id("displayvalue")
        suma = eleYourSum.get_attribute("displayvalue")
       
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output= 'reportes', report_name = 'Suma'))
