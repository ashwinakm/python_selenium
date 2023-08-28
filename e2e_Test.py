# This is an example of e2e web automation test case
# PyTest Framework
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time as t

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options=Options()
options.add_experimental_option("detach",True)
service_obj = Service("C:\\Users\\ashwini.mishra\\webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    product_name = product.find_element(By.XPATH, "div/h4/a").text
    if product_name == "Blackberry":
        print("success")
        product.find_element(By.XPATH, "div/button").click()
        driver.implicitly_wait(2)
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

driver.find_element(By.CSS_SELECTOR,".btn.btn-success").click()

driver.find_element(By.CSS_SELECTOR,'#country').send_keys("Ind")
# driver.implicitly_wait(7)
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,'India')))
driver.find_element(By.LINK_TEXT,'India').click()

driver.find_element(By.CSS_SELECTOR, ".checkbox.checkbox-primary").click()
driver.find_element(By.CSS_SELECTOR,".btn.btn-success.btn-lg").click()
message = driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text

assert "Success" in message
print("Hurray, your order is placed successfully")


driver.close()
