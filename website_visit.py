import time
from selenium import webdriver

driver = webdriver.Firefox()

#Proxy configurations for my system
#profile = webdriver.FirefoxProfile()
#profile.set_preference("network.proxy.type", 1)
#profile.set_preference("network.proxy.http", "172.31.16.10")
#profile.set_preference("network.proxy.http_port", "8080")
#profile.update_preferences()
#driver = webdriver.Firefox(firefox_profile=profile)"""


driver.get('https://www.youtube.com/')
time.sleep(15)
driver.quit()