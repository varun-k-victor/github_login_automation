from time import sleep
try:
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.common.exceptions import WebDriverException
except ModuleNotFoundError:
	print("Selenium not found")
else:
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
		try:
			driver=webdriver.Firefox()
		except WebDriverException:
			print("Geckodriver not found")
		else:
			sleep(3)
			try:
				driver.get('https://github.com/login')
			except WebDriverException:
				print("Check your network connection")
			else:
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
