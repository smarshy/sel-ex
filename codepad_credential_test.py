import time
import unittest
from selenium import webdriver

class Credentials(unittest.TestCase):

    """
    Contains tests for :
    User logging in to codepad with valid credentials
    User logging in to codepad with invalid credentials
    User logout
    """

    def setUp(self):

        self.homepage = 'http://codepad.org'
        self.authentication_page = '/login'
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get(self.homepage + self.authentication_page)


    def tearDown(self):
        self.driver.close()


    def test_valid_login(self):

        driver = self.driver
        self.assertIn("Login", driver.title)
        
        #Enter correct password for user
        username_area = driver.find_element_by_name('username')
        username_area.send_keys("smarshy")
        password_area = driver.find_element_by_name('password')
        password_area.send_keys("systers")
        login_button = driver.find_element_by_name('submit')
        login_button.click()

        #verify user logged in successfully
        username = driver.find_element_by_class_name('heading')
        self.assertEqual(self.driver.current_url, self.homepage + '/users/smarshy')
        self.assertEqual(username.text, 'smarshy')

    	
    def test_invalid_login(self):

        driver = self.driver
        self.assertIn("Login", driver.title)

        #Enter incorrect password for user
        username_area = driver.find_element_by_name('username')
        username_area.send_keys("smarshy")
        password_area = driver.find_element_by_name('password')
        password_area.send_keys("system")
        login_button = driver.find_element_by_name('submit')
        login_button.click()

        #verify user wasn't able to log in
        error_area = driver.find_element_by_class_name('error-box')
        self.assertEqual(self.driver.current_url, self.homepage + self.authentication_page)
        self.assertEqual(error_area.text, 'Incorrect password')


    def test_logout(self):

        driver = self.driver

        #login first
        username_area = driver.find_element_by_name('username')
        username_area.send_keys("smarshy")
        password_area = driver.find_element_by_name('password')
        password_area.send_keys("systers")
        login_button = driver.find_element_by_name('submit')
        login_button.click()

        #logout and verify
        logout_button = driver.find_element_by_link_text('logout')
        logout_button.click()
        self.assertEqual(self.driver.current_url, 'http://codepad.org/')


if __name__ == "__main__":
    unittest.main()
