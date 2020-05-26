from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import getpass

login_button_xpath = ("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/"
                  "span/a[1]/button")
username_xpath = "//input[@name='username']"
password_xpath = "//input[@name='password']"
followers_xpath = '//a[@href="/nickw409/followers/"]'

class Bot:

   def __init__(self):
      self.driver = Firefox()

   def get_login_info(self):
      self.username = input("Enter username: ")
      self.password = getpass.getpass("Enter password: ")

   def login(self):
      self.driver.get("https://instagram.com")
      username_form = driver.find_element_by_xpath(username_xpath)
      username_form.send_keys(self.username)
      password_form = driver.find_element_by_xpath(password_xpath)
      password_form.send_keys(self.password)
      password_form.send_keys(Keys.RETURN)

def main():
   with Firefox() as driver:
      driver.get("https://instagram.com/nickw409")
      login_button = driver.find_element_by_xpath(login_button_xpath)
      login_button.click()
      get_login_credentials(driver)
      time.sleep(5)
      followers_button = driver.find_element_by_xpath(followers_xpath).click()
      time.sleep(5)
   
main()
