
'''This script will automate a simple webpage using different method on web element and
using XPATH and CSSSelector NOTE: This Page is also having a static drop down to select'''


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time as t
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

''' Here without adding options the browser was opening and closing automatically. To avoid that
we have imported and used Options. '''
options = Options()
options.add_experimental_option("detach", True)  # Keep the browser window open after exiting the script
service_obj = Service("C:\\Users\\ashwini.mishra\\webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

### Filling in data for different web element on the page
### Locators to Use - ID,XPATH,CSSSelector,name,linkText etc
driver.find_element(By.NAME, "name").send_keys("Ashwini Kumar Mishra")
driver.find_element(By.NAME, "email").send_keys("amishra@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Test@123#")
driver.find_element(By.ID, "exampleCheck1").click()

### Next line of code is for selecting static drop down from a page.
dropdown = Select(driver.find_element(By.ID,'exampleFormControlSelect1'))
dropdown.select_by_index(1)
# driver.find_element(By.ID, "inlineRadio2").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()   ### Using CSSSelector
driver.find_element(By.NAME, "bday").send_keys("07/09/1981")
# driver.find_element(By.NAME, "name").send_keys("Kumar Ashwin")
# driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Mishra Budha")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Ram Tingalu")  # ===> Using Xpath
t.sleep(4)
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
## XPATH FORMAT ==>>  //tagname[@attribute="Value"]
# driver.find_element(By.XPATH,"//input[@type='submit']").click()

## CSS Format ==>> tagname[attribute='Value'] , #id,.classname , CSS can be constructed using # and . as well.
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
print("I clicked Submit Button")
message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(message)

# assert message.__contains__("Success")
assert 'Success' in message
t.sleep(5)
driver.close()
