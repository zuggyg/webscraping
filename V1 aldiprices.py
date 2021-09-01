# Zuggyg 26/08/21
# aim of this script is to take names and prices of special buy items

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import urllib
import urllib.request
from selenium.webdriver.chrome.options import Options
import unicodedata
import re

#enter the aldi website in this variable
aldilink = "https://www.aldi.com.au/en/special-buys/special-buys-wed-8-september/"
itembox = "box--description"
itemtitle = "box--description--header"
itemprice = "box--value"
itemprice2 = "box--decimal"

#the chrome driver can have multiple options adjusted including making it headless.
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
#chrome_options.add_argument("--headless")
#chrome_options.headless = True # also works

#create a txt file
doc= open("itemsaldi.csv","w+")

#make sure your chromedriver is with the current version of chrome installed.
#go to https://chromedriver.chromium.org/downloads to get chromedrivers
print("Opening Chrome Driver")
PATH = "C:\Python39\chromedriver.exe"
driver = webdriver.Chrome(PATH,options=(chrome_options))

#opening the page
print("Opening link")
driver.get(aldilink)
print("Link Opened")

print("Acquiring items")
content = driver.find_elements_by_class_name(itembox)
print("All items Acquired")

doc.write("title,price"+"\n")
count = len(content)
print("There are this many items...",count)


for item in content:
    print("Items left...",count)
    title = item.find_element_by_class_name(itemtitle).text
    price = item.find_element_by_class_name(itemprice).text
    decimal = item.find_element_by_class_name(itemprice2).text
    doc.write(title+","+price+decimal+"\n")
    print("Saved line for "+title)
    count += -1

#close Driver
driver.quit()
