from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
'''Alegeti-va unu sau mai multe din sugestiile de site-uri de mai jos
https://www.phptravels.net/
http://automationpractice.com/index.php
https://formy-project.herokuapp.com/
https://the-internet.herokuapp.com/
https://www.techlistic.com/p/selenium-practice-form.html
jules.app

Alegeti cate 3 elemente din fiecare tip de selector din urmatoarele categorii:

Id
Link text
Partial link text
Name
Tag*
Class name*
Css (1 dupa id, 1 dupa clasa, 1 dupa atribut=valoare_partiala)

obs:
Probabil nu veti gasi un singur website care sa cuprinda toate variantele de mai sus, astfel ca va recomandam sa folositi mai multe site-uri
Optional: La tag si class name veti folosi find elementS! - salvati in lista. Interactionati cu un element la alegere din lista'''

#deschidem un browser chrome
chrome = webdriver.Chrome()
chrome.maximize_window()
#punem siteul pe care sa navigheze selenium
chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
#name
chrome.find_element(By.NAME, 'firstname').send_keys('Alexa')
chrome.find_element(By.NAME, 'lastname').send_keys('Delureanu')
chrome.find_element(By.ID, 'datepicker').send_keys('14-11-2022')
chrome.find_element(By.CSS_SELECTOR, "input#sex-1").click()
chrome.find_element(By.CSS_SELECTOR, 'input#exp-0').click()
chrome.find_element(By.CSS_SELECTOR, "input#profession-1").click()
chrome.find_element(By.CSS_SELECTOR, "input#tool-2").click()
chrome.find_element(By.ID, 'continents').send_keys('Europe')
chrome.find_element(By.ID, 'selenium_commands').click()
chrome.find_element(By.ID, 'submit').click()
sleep(5)

#selector By LINK_TEXT
chrome.get('https://formy-project.herokuapp.com')
chrome.find_element(By.LINK_TEXT, 'Checkbox').click()
sleep(3)

#Selector By PARTIAL_LINK_TEXT
chrome.get('https://formy-project.herokuapp.com')
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Key').click()
sleep(2)



'''Pentru xpath identificati elemente dupa criteriile de mai jos:

3 dupa atribut valoare
3 dupa textul de pe element
1 dupa partial text
1 cu SAU, folosind pipe |
1 cu * 
1 in care le iei ca pe o lista de xpath si in python ajunge 1 element, deci cu (xpath)[1]
1 in care sa folosesti parent::
1 in care sa folosesti fratele anterior sau de dupa (la alegere)
1 functie ca si cea de la clasa prin care sa pot alege eu prin param cu ce element vreau sa interactionez. '''

#deschidem un browser chrome
chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/form')

'''Pentru xpath identificati elemente dupa criteriile de mai jos:
 dupa atribut valoare'''
chrome.find_element(By.XPATH,'//button[@id="button"]').click()
sleep(3)

#3 dupa textul de pe element




'''Studiu extra daca doriti:
https://www.automatetheplanet.com/most-exhaustive-xpath-locators-cheat-sheet/

Studiu extra daca doriti:
https://www.automatetheplanet.com/most-exhaustive-xpath-locators-cheat-sheet/

De urmarit: 
https://testautomationu.applitools.com/web-element-locator-strategies/

De citit:

https://www.guru99.com/locators-in-selenium-ide.html
https://oxylabs.io/blog/xpath-vs-css
https://www.pythonpool.com/python-unittest-vs-pytest/
ro-in-web-scraping-5c937e027244https://towardsdatascience.com/top-25-selenium-functions-that-will-make-you-p
https://www.geeksforgeeks.org/how-to-use-close-and-quit-method-in-selenium-python/'''

