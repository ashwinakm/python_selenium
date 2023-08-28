from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time as t

from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
service_obj = Service("C:\\Users\\ashwini.mishra\\webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()

windowOptions = driver.window_handles
driver.switch_to.window(windowOptions[1])
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
driver.close()
driver.switch_to.window(windowOptions[0])
assert "Opening a new window" == driver.find_element(By.XPATH,"//h3").text
print("Assertion Pass")




t.sleep(3)
driver.close()
