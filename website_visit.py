import time
import unittest
from selenium import webdriver

class YouTube(unittest.TestCase):

    def setUp(self):

    	#Proxy configurations for my system
    	#profile = webdriver.FirefoxProfile()
    	#profile.set_preference("network.proxy.type", 1)
    	#profile.set_preference("network.proxy.http", "172.31.16.10")
    	#profile.set_preference("network.proxy.http_port", "8080")
    	#profile.update_preferences()
    	#driver = webdriver.Firefox(firefox_profile=profile)"""
        self.homepage = 'https://www.youtube.com/'
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_youtube(self):
        driver = self.driver
        driver.get('https://www.youtube.com/')
        #match tite and url
        self.assertIn("YouTube", driver.title)
        self.assertEqual(self.driver.current_url,self.homepage)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
