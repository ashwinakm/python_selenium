from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time as t

from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)


service_obj = Service("C:\\Users\\ashwini.mishra\\webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj , options =options)
driver.get("https://rahulshettyacademy.com//AutomationPractice//")

name = "Ashwin"
driver.find_element(By.CSS_SELECTOR,'#name').send_keys(name)
driver.find_element(By.CSS_SELECTOR,'#alertbtn').click()

alert = driver.switch_to.alert
alert_text = alert.text
assert name in alert_text
t.sleep(3)
alert.accept()

t.sleep(3)
driver.close()

