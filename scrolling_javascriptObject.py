''' This script will have example to scroll, take screenshot,run headless browser mode,
trusting security certificate etc'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time as t

from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
# options.add_argument("headless")     ### To run test in headless mode
# options.add_argument("--ignore-certificate-errors")   ### To ignore SSL cert errors

service_obj = Service("C:\\Users\\ashwini.mishra\\webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("screen.png")

t.sleep(3)
driver.close()