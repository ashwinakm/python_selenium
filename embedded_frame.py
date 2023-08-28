from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time as t

from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach",True)
service_obj = Service("C:\\Users\\ashwini.mishra\\webdrivers\\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj,options=options)
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Frames").click()
driver.implicitly_wait(3)

# windowoptions = driver.window_handles
# driver.switch_to.window(windowoptions[1])
driver.find_element(By.LINK_TEXT,"iFrame").click()
driver.implicitly_wait(3)
driver.switch_to.frame("1")
driver.find_element(By.CSS_SELECTOR,"div[class='example'] textarea").clear()
driver.find_element(By.CSS_SELECTOR,"div[class='example'] textarea").send_keys("Hello Ashwin")






# t.sleep(3)
# driver.close()

