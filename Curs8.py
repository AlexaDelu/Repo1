from selenium import webdriver
from selenium.webdriver.common.by import By

chrome= webdriver.Chrome()
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/form')
'''Cate tipuri de selectors/locators cunoasteti?
Care considerati ca e de preferat sa se foloseasca? De ce?
Care e cel mai flexibil din punctul tau de vedere? De ce?
Exercitiu practic: Se va da un url si cateva elemente pe care sa le identificati voi dupa ce selector doriti. 
Demo sites for practice:
https://www.phptravels.net/
http://automationpractice.com/index.php
https://formy-project.herokuapp.com/
https://the-internet.herokuapp.com/
https://www.techlistic.com/p/selenium-practice-form.html'''

'''In Terminal: pip install webdriver-manager si pip install selenium
Deschidem Chrome
Navigam catre url dorit (ex: https://formy-project.herokuapp.com/form)
Click dreapta pe elementul ce dorim sa il inspectam
Selectati optiunea ‘Inspect’
Veti gasi partea de html a unui website
Structura e urmatoarea:
tag sau webelement (ex: <input>)
atribut=”valoare” (ex: type=”text” id=”first-name”)
Copiem ID al elementului dorit (ex: ‘first-name’)'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#deschidem un browser chrome
chrome = webdriver.Chrome()
chrome.maximize_window()
#punem siteul pe care sa navigheze selenium
chrome.get('https://formy-project.herokuapp.com/form')
sleep(1)
#cautam text fieldul first name dupa id si introducem un text
first_name = chrome.find_element(By.ID, 'first-name')
first_name.send_keys("tiberiu")
sleep(2)

#cautam text fieldul last name dupa clasa si salvam intr-o lista toate elementele gasite si introducem un text
last_name = chrome.find_elements(By.CLASS_NAME, 'form-control')
last_name[1].send_keys('Serban')
sleep(2)

#cautam text fieldul job title dupa id folosind css selectorul si introducem un text
chrome.find_element(By.CSS_SELECTOR, "input#job-title").send_keys("ing")
sleep(2)

#cautam radio button dupa id folosind expath si dam click pe el
chrome.find_element(By.XPATH, '//input[@id="radio-button-1"]').click()
sleep(2)

#cautam radio button dupa id folosind css selector si dam click pe el
check = chrome.find_element(By.CSS_SELECTOR, "input#checkbox-1")
print(check)
check.click()
sleep(2)

#metoda care primeste ca si parametru idul fieldului si care implementeaza o cautare dinamica a elementelor din pagina
#folosind xpath
def form_input(id_value):
    input = chrome.find_element(By.XPATH, f'//input[@id="{id_value}"]')
    input.click()

form_input("checkbox-1")
form_input("checkbox-2")
form_input("checkbox-3")
sleep(2)

#cautare button submit dupa partial link text a linkului si dam click pe el
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Submit').click()
sleep(2)

#Xpath este tinta unde tb sa se duca Selenium sa execute actiunea

#LINK TEXT
'''A Link Text in Selenium is used to identify the hyperlinks on a web page. 
It is determined with the help of an anchor tag. 
For creating the hyperlinks on a web page, we can use an anchor tag followed by the link Text'''


