'''Implicit Waits
An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available.
The default setting is 0 (zero). Once set, the implicit wait is set for the life of the WebDriver object.'''

from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element(By.ID, "myDynamicElement")