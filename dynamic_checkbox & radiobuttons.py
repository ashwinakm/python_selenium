from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time as t

from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach",True)

service_obj = Service("C:\\Users\\ashwini.mishra\\webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service =service_obj , options = options)
driver.get("https://rahulshettyacademy.com//AutomationPractice//")


checkboxes = driver.find_elements(By.XPATH,"//input[@type ='checkbox']")
radiobuttons = driver.find_elements(By.XPATH,"//input[@type ='radio']")

## Clicking for the checkbox
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

## Clicking for the radio button
for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio1":
        radiobutton.click()
        assert radiobutton.is_selected()

t.sleep(3)
driver.close()