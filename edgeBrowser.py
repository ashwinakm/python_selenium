
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.edge.options import Options

options = Options()
options.add_experimental_option("detach", True)  # Keep the browser window open after exiting the script

service_obj = Service("C:/Users/ashwini.mishra/webdrivers/msedgedriver.exe")
# driver = webdriver.Edge(service=service_obj)
driver = webdriver.Edge(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://www.google.com/")