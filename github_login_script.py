from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def userin_username():
    username=input("Enter username: ")
    return username

def userin_passwd():
    password=input("Enter password: ")
    return password

def main():
	USERNAME=userin_username()
	PASSWORD=userin_passwd()
	print("Code running....")
	sleep(3)
	driver=webdriver.Firefox()
	sleep(3)
	driver.get('https://github.com/login')
	sleep(3)
	username=driver.find_element_by_name('login')
	username.send_keys(USERNAME)
	sleep(3)
	password=driver.find_element_by_name('password')
	password.send_keys(PASSWORD)
	sleep(3)
	password.send_keys(Keys.ENTER)
	
if __name__=="__main__":
	main()
