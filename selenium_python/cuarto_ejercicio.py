from selenium import webdriver
import unittest
from pyunitreport import HTMLTestRunner
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


class checkBoxMult(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'D:\Laura\Documentos\Laura\selenium_python\chromedriver_win32\chromedriver.exe')
        driver =self.driver
        driver.implicitly_wait(5)
        driver.maximize_window()        

    def test_checkBoxMult(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
        assert "Selenium Easy - Checkbox demo for automation using selenium" in driver.title
        checkBoxUno = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label/input')
        checkBoxDos = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label/input')
        checkBoxTres = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[3]/label/input')
        checkBoxCuatro = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[4]/label/input')

        self.assertTrue(checkBoxUno.is_enabled())
        checkBoxUno.click()
        self.assertTrue(checkBoxDos.is_enabled())
        checkBoxDos.click()
        self.assertTrue(checkBoxTres.is_enabled())
        checkBoxTres.click()
        self.assertTrue(checkBoxCuatro.is_enabled())
        checkBoxCuatro.click()
        #time.sleep(4)

        UnCheckAllBtn=driver.find_element_by_xpath('//*[@id="check1"]')
        UnCheckAllBtn.click()
        #time.sleep(4)

        CheckAllBtn=driver.find_element_by_xpath('//*[@id="check1"]')
        CheckAllBtn.click()
        #time.sleep(4)

        UnCheckAllBtn=driver.find_element_by_xpath('//*[@id="check1"]')
        UnCheckAllBtn.click()
        #time.sleep(4)

    def tearDown(self):
        self.driver.implicitly_wait(1)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output= 'reportes', report_name = 'CheckBoxMult'))