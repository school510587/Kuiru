import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


browser = webdriver.Firefox()

def login():
	email = raw_input("Facebook email:");
	password = raw_input("Facebook password:")

	browser.get("https://www.facebook.com/login.php")
	browser.find_element_by_id("email").send_keys(email)
	browser.find_element_by_id("pass").send_keys(password)
	browser.find_element_by_id("loginbutton").click()

	print "Successfully login the Facebook!"

def webpage_goto_end():
	browser.find_element_by_id("mainContainer").send_keys(Keys.END)

def show_friend_list():
	browser.get("https://www.facebook.com/friends")
	web_parser = BeautifulSoup(browser.page_source)

	print "Friend list mode(press n to refresh the list)"

	for unparsed_data in web_parser.findAll("div", {'class': 'fsl fwb fcb'}):
		print unparsed_data.a.get_text()

	key = 0
	while(key != "q"):
		key = read_key()

		if key == "n":
			webpage_goto_end()

def quit_mode():
	key = raw_input("Confirm to exit the program (Y/N)")

	while key != "Y" and key != "y" and key != "N" and key != "n":
		key = raw_input("Please input the valid answer (Y/N)")

	if key == "Y" or key == "y":
		sys.exit(0)
		

def read_key():
	return sys.stdin.read(1)

def main():
	login()

	while(True):
		key = read_key()

		if key == 'f':
			show_friend_list() #Friend list mode
		elif key == "h":
			pass #Help mode
		elif key == "q":
			quit_mode()

main()
