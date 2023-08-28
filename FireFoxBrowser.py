from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

''' Here without adding options the browser was opening and closing automatically. To avoid that
we have imported and used Options. '''
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
options.add_experimental_option("detach", True)  # Keep the browser window open after exiting the script
service_obj = Service("C:\\Users\\ashwini.mishra\\webdrivers\\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://www.google.com/")
driver.close()
