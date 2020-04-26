from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
chromedriver = "D:\Scripts\chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("http://localhost:63342/UniversityAutomation/Calculator/calculator.html")

# Click number 1
elem = driver.find_element_by_xpath("//input[@value='1']")
elem.click()

# Click +
elem = driver.find_element_by_xpath("//input[@value='+']")
elem.click()

# Click number 2
elem = driver.find_element_by_xpath("//input[@value='2']")
elem.click()

# Click =
elem = driver.find_element_by_xpath("//input[@value='=']")
elem.click()

# Get result
result = driver.find_element_by_name('ans')
res = result.get_attribute('value')

# Check if the result passes

if res == "3":
    print("Test passed, the result is: ", res)
else:
    print("Test did not pass, the result is: ", res)

driver.close()
