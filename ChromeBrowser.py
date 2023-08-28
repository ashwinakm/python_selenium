from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

''' Here without adding options the browser was opening and closing automatically. To avoid that
we have imported and used Options. '''
options = Options()
options.add_experimental_option("detach", True)  # Keep the browser window open after exiting the script
service_obj = Service("C:\\Users\\ashwini.mishra\\webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=options)
driver.maximize_window()
driver.get("https://www.google.com/")
print(driver.title)                         ### Provides the title of the webpage
print(driver.current_url)                   ### Print the current URL the script has open.
driver.get("https://www.facebook.com/")     ### Opening another URL in same browser
driver.back()                               ### Going backward from current URL
driver.forward()                            ### Going forward from current URL
driver.close()
