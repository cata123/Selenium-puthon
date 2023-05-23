from selenium import webdriver
import unittest
from pyunitreport import HTMLTestRunner
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


class checkBox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'D:\Laura\Documentos\Laura\selenium_python\chromedriver_win32\chromedriver.exe')
        driver =self.driver
        driver.implicitly_wait(5)
        driver.maximize_window()        

    def test_checkBox(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
        assert "Selenium Easy - Checkbox demo for automation using selenium" in driver.title
        checkBoxSolo = driver.find_element_by_id("isAgeSelected")

        self.assertTrue(checkBoxSolo.is_enabled())
        checkBoxSolo.click()
        #time.sleep(5)

    def tearDown(self):
        self.driver.implicitly_wait(1)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output= 'reportes', report_name = 'CheckBoxSolo'))