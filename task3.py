
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox


import os
from selenium import webdriver

#chromedriver = "/usr/local/bin/chromedriver"
geckodriver = "/usr/local/bin/geckodriver"
#os.environ["webdriver.chrome.driver"] = chromedriver
os.environ["webdriver.gecko.driver"] = geckodriver
#driver = webdriver.Chrome(chromedriver)
driver = webdriver.Firefox()
driver.get("https://altinity.com/")

driver.find_element_by_css_selector('#mega-menu-item-7537 > a:nth-child(1)').click()
URL = driver.current_url
assert URL == 'https://altinity.com/blog/'
Title = driver.title
print()

fullstring = driver.title
substring = "Altinity Blog"

if substring in fullstring:
    print ("Title of the page is Altinity Blog")
else:
    print ("oops it is a differetn page")

driver.quit()