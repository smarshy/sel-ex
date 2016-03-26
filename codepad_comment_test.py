import time
import unittest
from selenium import webdriver

class Comment(unittest.TestCase):

    """
    Contains tests for :
    Redirection when commenting without logging in first
    Successful Commenting after login
    """

    def setUp(self):

        self.homepage = 'http://codepad.org'
        self.authentication_page = '/login'
        self.pastepage = 'http://codepad.org/4M4ezTmx'
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()   


    def tearDown(self):

        self.driver.close()


    def login(self):

    	driver = self.driver
        driver.get(self.homepage + self.authentication_page)
        username_area = driver.find_element_by_name('username')
        username_area.send_keys("smarshy")
        password_area = driver.find_element_by_name('password')
        password_area.send_keys("systers")
        login_button = driver.find_element_by_name('submit')
        login_button.click()


    def test_comment_without_login(self):

    	#go to my paste
    	driver = self.driver
        driver.get(self.pastepage)
        self.assertEqual(self.driver.current_url, self.pastepage)

        #try commenting on the paste
        comment_area = driver.find_element_by_xpath("//textarea[@name='text']")
        comment_area.send_keys("Nice to meet you!")
        comment_button  = driver.find_element_by_name('submit')
        comment_button.click()
        
        #should direct to login page
        self.assertEqual(self.driver.current_url, self.homepage + self.authentication_page)
        notice_area = driver.find_element_by_class_name('notice-box')
        self.assertEqual(notice_area.text, 'Please log in or create an account to finish posting your comment.')


    def test_comment_after_login(self):

    	self.login()

    	driver = self.driver
        driver.get(self.pastepage)
        self.assertEqual(self.driver.current_url, self.pastepage)

        #try commenting on the paste
        comment_area = driver.find_element_by_xpath("//textarea[@name='text']")
        comment_area.send_keys("Nice to meet you!")
        comment_button  = driver.find_element_by_name('submit')
        comment_button.click()

        #verify that there was no redirection - that is the comment got pasted
        self.assertNotEqual(self.driver.current_url, self.homepage + self.authentication_page)


if __name__ == "__main__":
    unittest.main()
