from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time as t

from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach",True)

service_obj = Service("C:\\Users\\ashwini.mishra\\webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(2)

VeggieList =[]

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
veggitables = driver.find_elements(By.XPATH,"//tr/td[1]")

for veggi in veggitables:
    VeggieList.append(veggi.text)
sorted_veggie = VeggieList
print(sorted_veggie)
VeggieList.sort()
print(f"Veg list after sorting is {VeggieList}")

assert sorted_veggie == VeggieList
print("Veggi list is sorted correctly")

t.sleep(3)
driver.close()

