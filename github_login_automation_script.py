from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import geckodriver_autoinstaller
from selenium.webdriver.common.by import By

geckodriver_autoinstaller.install() 

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
    username= driver.find_element(By.NAME, "login")
    username.send_keys(USERNAME)
    sleep(3)
    password= driver.find_element(By.NAME, "password")
    password.send_keys(PASSWORD)
    sleep(3)
    password.send_keys(Keys.ENTER)
    
if __name__=="__main__":
    main()