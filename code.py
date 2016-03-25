import time
from selenium import webdriver

def enter_code(command):
	text_area = driver.find_element_by_id('textarea')
	text_area.send_keys(command)
	time.sleep(10)
	#text is submitted
	submit_button = driver.find_element_by_name('submit')
	submit_button.click()

def comment(msg):

	comment_area = driver.find_element_by_xpath("//textarea[@name='text']")
	comment_area.send_keys(msg)
	time.sleep(10)
	comment_button  = driver.find_elements_by_name('submit')[1]
	comment_button.click()

def login():

	username_area = driver.find_element_by_name('username')
	username_area.send_keys("smarshy")
	password_area = driver.find_element_by_name('password')
	password_area.send_keys("systers")
	time.sleep(10)
	login_button = driver.find_element_by_name('submit')
	login_button.click()

#main function
if __name__ == '__main__':

	driver = webdriver.Firefox()
	driver.maximize_window()
	driver.get('http://codepad.org')
	python_link = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
	python_link.click()

	enter_code("print 'Hi!! :) My Name is Vatsala!'")
	time.sleep(10)
	comment("Nice to meet you!")

	# Should lead to login page as comments without login not allowed
	time.sleep(10)
	login()

	#answer back to the comment
	time.sleep(10)
	enter_code("print '\n Nice to meet you too! What is your name?'")
	time.sleep(10)
	driver.quit()