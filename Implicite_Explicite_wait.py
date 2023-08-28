import driver as driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time as t

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_experimental_option('detach',True)
service_obj = Service("C:\\Users\\ashwini.mishra\\webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj,options=options)
#### Adding implicit wait globally for the application
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com//seleniumPractise//")
driver.maximize_window()

search_list=["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
display_list =[]

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")

items = driver.find_elements(By.XPATH,"//div[@class = 'product']/h4")
for item in items:
    display_list.append(item.text)
assert search_list == display_list
print("Item list matched perfectly")

results = driver.find_elements(By.XPATH,"//div[@class='product']/div/button")
print(len(results))
for result in results:
    result.click()

driver.find_element(By.CSS_SELECTOR,'.cart-icon').click()
driver.find_element(By.XPATH,"//button[text() ='PROCEED TO CHECKOUT']").click()
print("Executed till this step")
# t.sleep(3)
driver.find_element(By.CSS_SELECTOR,'.promoCode').send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR,'.promoBtn').click()

### Adding explicit wait for a particular element in the webpage.
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'.promoInfo')))
print(driver.find_element(By.CSS_SELECTOR,'.promoInfo').text)

### Functional Validation for checking sum of all selected items against the total amount displayed.
sum = 0
amounts = driver.find_elements(By.CSS_SELECTOR,'tr td:nth-child(5) p')
for amount in amounts:
    sum = sum + int(amount.text)

print(f"total amount is {sum}")
tot_amount = int(driver.find_element(By.CSS_SELECTOR,'.totAmt').text)


assert sum == tot_amount
print(f"The calculated total amount of Rs.{sum} matched with the displayed sum of Rs.{tot_amount} amount")
discounted_amt = float(driver.find_element(By.CSS_SELECTOR, '.discountAmt').text)
assert discounted_amt < tot_amount
print(f"Discounted price Rs.{discounted_amt} is always less than Total price Rs.{tot_amount}")





t.sleep(3)
driver.close()


