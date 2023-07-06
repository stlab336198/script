from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,800")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
driver.implicitly_wait(5)
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
driver.close()
