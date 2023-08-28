# ### Static dropdown Example
# import selenium.webdriver
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import time as t
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# options=Options()
# options.add_experimental_option('detach',True)
# service_obj = Service("C:\\Users\\ashwini.mishra\\webdrivers\\chromedriver.exe")
# driver = webdriver.Chrome(service =service_obj,options = options)
# driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.maximize_window()
# ### Example of Static dropdown.
# dropdown = Select(driver.find_element(By.ID,'exampleFormControlSelect1'))
# dropdown.select_by_index(1)
#
# t.sleep(4)
# driver.close()

import selenium.webdriver
##### Dynamic dropdown example ########
import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time as t

from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
service_object = Service("C:\\Users\\ashwini.mishra\\webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object, options=options)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, 'autosuggest').send_keys("ind")
t.sleep(3)

# countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
countries = driver.find_elements(By.CSS_SELECTOR, "ul li[class='ui-menu-item'] a")

print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break


#### Adding assertion to validate the country we selected is actually selected and present.
## Note - Since its a dynamically passed value .text method cannot retrive its value from the field. We
### Need to use .getattribute method here.

selected_country = driver.find_element(By.ID,"autosuggest").get_attribute("value")
assert selected_country == "India"
print("Test is Pass")

t.sleep(5)
driver.close()