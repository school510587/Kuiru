import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


browser = webdriver.Firefox()

friend_list = []

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

def friend_list_mode():
	browser.get("https://www.facebook.com/friends")
	web_parser = BeautifulSoup(browser.page_source)

	print "Friend list mode(press n to refresh the list)"

	global friend_list_count

	i = 0
	for unparsed_data in web_parser.findAll("div", {'class': 'fsl fwb fcb'}):
		friend_list.append(unparsed_data.a.get_text())
		print '%d-%s' %(i, friend_list[i])
		
		i += 1

	webpage_goto_end()

	key = 0
	while(key != "q"):
		key = read_key()

		if key == "n":
			webpage_goto_end()

			web_parser = BeautifulSoup(browser.page_source)

			i = 0
			for unparsed_data in web_parser.findAll("div", {'class': 'fsl fwb fcb'}):
				if i >= len(friend_list):
					friend_list.append(unparsed_data.a.get_text())
					print '%d-%s' %(i, friend_list[i])
				i += 1
		

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
			friend_list_mode() #Friend list mode
		elif key == "h":
			pass #Help mode
		elif key == "q":
			quit_mode()

main()
