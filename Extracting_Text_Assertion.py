from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time as t
from datetime import datetime

from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)  # Keep the browser window open after exiting the script
service_obj = Service("C:\\Users\\ashwini.mishra\\webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH, ("//input[@type='email']")).send_keys('pchandra@rediffmail.com')
driver.find_element(By.CSS_SELECTOR,('#userPassword')).send_keys('Word@3399')
driver.find_element(By.CSS_SELECTOR,('#confirmPassword')).send_keys('Word@3399')
driver.find_element(By.CSS_SELECTOR,('.btn.btn-custom.btn-block')).click()

#
# t.sleep(8)
# driver.close()