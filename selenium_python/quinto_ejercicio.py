from selenium import webdriver
import unittest
from pyunitreport import HTMLTestRunner
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


class alert(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'D:\Laura\Documentos\Laura\selenium_python\chromedriver_win32\chromedriver.exe')
        driver =self.driver
        driver.implicitly_wait(5)
        driver.maximize_window()        

    def test_alert(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
        #driver.maximize_window()
        assert "Selenium Easy Demo - Automate All Scenarios" in driver.title

        AlertDisplayBtn=driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/button')
        AlertDisplayBtn.click()

        alert = driver.switch_to_alert()
        alert_text = alert.text

        self.assertEqual('I am an alert box!', alert_text)

        alert.accept()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output= 'reportes', report_name = 'alert'))