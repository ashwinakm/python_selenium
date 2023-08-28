from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time as t

from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach",True)
service_obj = Service("C:\\Users\\ashwini.mishra\\webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj, options = options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


class ActioonChain:
    pass


action = ActionChains(driver)     ### Note to remember
action.double_click(driver.find_element(By.CSS_SELECTOR,"#checkBoxOption1")).perform()
t.sleep(2)
action.click(driver.find_element(By.XPATH,"//input[@value='radio1']")).perform()
action.click(driver.find_element(By.CSS_SELECTOR,"#checkBoxOption1")).perform()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
t.sleep(2)
# action.context_click(driver.find_element(By.ID,"mousehover")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
t.sleep(5)
driver.close()

