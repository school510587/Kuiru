from __future__ import print_function
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


browser = webdriver.Firefox()

friend_list = {'friend_name':[], 'friend_link':[]}


def login():
	email = raw_input("Facebook email:");
	password = raw_input("Facebook password:")

	browser.get("https://www.facebook.com/login.php")
	browser.find_element_by_id("email").send_keys(email)
	browser.find_element_by_id("pass").send_keys(password)
	browser.find_element_by_id("loginbutton").click()

	print("Successfully login the Facebook!")

def webpage_goto_end():
	browser.find_element_by_id("mainContainer").send_keys(Keys.END)

def friend_list_mode():
	browser.get("https://www.facebook.com/friends")
	web_parser = BeautifulSoup(browser.page_source)

	print("Friend list mode(press n to refresh the list)")

	global friend_list_count

	i = 0
	for unparsed_data in web_parser.findAll("div", {'class': 'fsl fwb fcb'}):
		friend_list['friend_name'].append(unparsed_data.a.get_text())
		friend_list['friend_link'].append(unparsed_data.a.get('href'))
	
		print('%d-%s-%s' %(i, friend_list['friend_name'][i], friend_list['friend_link'][i]))
		
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
				if i >= len(friend_list['friend_name']):
					friend_list['friend_name'].append(unparsed_data.a.get_text())
					friend_list['friend_link'].append(unparsed_data.a.get("href"))
	
					print('%d-%s-%s' %(i, friend_list['friend_name'][i], friend_list['friend_link'][i]))
				i += 1
		

def chat_mode():
	friend_index = 0
	#Play some tricks with the profile link address
	chatroom_address = friend_list['friend_link'][friend_index].replace('?fref=pb&hc_location=friends_tab', '')
	chatroom_address = chatroom_address.replace('https://www.facebook.com/', 'https://www.facebook.com/messages/')

	#print(chatroom_address)

	browser.get(chatroom_address)

	browser.find_element_by_name("message_body").send_keys("message")


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

		if key == 'c':
			chat_mode() #Chat mode
		elif key == 'f':
			friend_list_mode() #Friend list mode
		elif key == "h":
			pass #Help mode
		elif key == "q":
			quit_mode()

main()
