from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
assert "Swag Labs" in driver.title

elem=driver.find_element(By.ID,"user-name")
elem.clear()
elem.send_keys("standard_user")
elem.send_keys(Keys.RETURN)
passwd=driver.find_element(By.ID,"password")
passwd.clear()
passwd.send_keys("secret_sauce")
passwd.send_keys(Keys.RETURN)
button=driver.find_element(By.ID,"login-button")
button.click()
time.sleep(5)
driver.close()