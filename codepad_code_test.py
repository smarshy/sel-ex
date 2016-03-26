import time
import unittest
from selenium import webdriver

class Code(unittest.TestCase):

    """
    Contains tests for :
    Accessing Codepad website
    Output after entering correct code
    Output after entering incorrect syntax code
    """

    def setUp(self):

        self.homepage = 'http://codepad.org'
        self.authentication_page = '/login'
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.close()


    def test_codepad(self):
        #match tite and url
        driver = self.driver
        driver.get(self.homepage)
        self.assertIn("codepad", driver.title)


    def test_correct_code(self):

    	driver = self.driver
        driver.get(self.homepage)
    	#select python
    	python_link = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
    	python_link.click()

    	#enter correct code and submit
    	text_area = driver.find_element_by_id('textarea')
    	text_area.send_keys("print 'Hi!! :) My Name is Vatsala!'")
    	submit_button = driver.find_element_by_name('submit')
    	submit_button.click()

    	#verify that output is printed successfully
    	self.assertIn("Python", driver.title)
    	pre_list = driver.find_elements_by_tag_name('pre')
    	self.assertEqual(pre_list[3].text, 'Hi!! :) My Name is Vatsala!')


    def test_incorrect_syntax_code(self):

    	driver = self.driver
        driver.get(self.homepage)

    	#select python
    	python_link = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
    	python_link.click()

    	#enter incorrect code and submit
    	text_area = driver.find_element_by_id('textarea')
    	text_area.send_keys("primt 'Hi!! :) My Name is Vatsala!'")
    	submit_button = driver.find_element_by_name('submit')
    	submit_button.click()

    	#verify that error shows up
    	self.assertIn("Python", driver.title)
    	pre_list = driver.find_elements_by_tag_name('pre')
    	output = pre_list[3].text
    	self.assertNotEqual(output.find("SyntaxError"), -1)


if __name__ == "__main__":
    unittest.main()
