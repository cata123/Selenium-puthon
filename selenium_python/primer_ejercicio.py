from selenium import webdriver
import unittest
from pyunitreport import HTMLTestRunner
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class mensaje(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'D:\Laura\Documentos\Laura\selenium_python\chromedriver_win32\chromedriver.exe')
        driver =self.driver
        driver.implicitly_wait(5)
        driver.maximize_window()        

    def test_mensaje(self):
        driver = self.driver
        driver.get("http://www.seleniumeasy.com/test/basic-first-form-demo.html")
        #driver.maximize_window()
        assert "Selenium Easy Demo - Simple Form to Automate using Selenium" in driver.title
        eleUserMessage = driver.find_element_by_id("user-message")
        eleUserMessage.clear()
        eleUserMessage.send_keys("Prueba número 1")
        eleShowMsgBtn=driver.find_element_by_css_selector('#get-input > .btn')
        eleShowMsgBtn.click()
        eleYourMsg=driver.find_element_by_id("display")
        assert "Prueba número 1" in eleYourMsg.text

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output= 'reportes', report_name = 'mensaje'))

