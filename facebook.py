from selenium import webdriver

browser = webdriver.Firefox()

def login():
	email = raw_input("Facebook email:");
	password = raw_input("Facebook password:")

	browser.get("https://www.facebook.com/login.php")
	browser.find_element_by_id("email").send_keys(email)
	browser.find_element_by_id("pass").send_keys(password)
	browser.find_element_by_id("loginbutton").click()

	print "Successfully login the Facebook!"

login()

