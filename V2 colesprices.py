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
coleslink = "https://shop.coles.com.au/a/national/everything/search/soft%20drinks"
itembox = "product-header"
itembrand = "product-brand"
itemtitle = "product-name"
itemsize = "package-size"
itemprice = "dollar-value"
itemprice2 = "cent-value"
pagination = "number"

#the chrome driver can have multiple options adjusted including making it headless.
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
#chrome_options.add_argument("--headless")
#chrome_options.headless = True # also works

#create a txt file
doc= open("itemscoles.csv","w+")
doc.write("brand,title,size,price"+"\n")

#make sure your chromedriver is with the current version of chrome installed.
#go to https://chromedriver.chromium.org/downloads to get chromedrivers
print("Opening Chrome Driver")
PATH = "C:\Python39\chromedriver.exe"
driver = webdriver.Chrome(PATH,options=(chrome_options))
driver.implicitly_wait(10)

#opening the page
print("Opening link")
driver.get(coleslink)
print("Link Opened")

#getting number of pages
lastbox = driver.find_elements_by_class_name(pagination)[-1]
pages = int(lastbox.text)
print("Number of Pages...",pages)

#what to do for each page
def gather(page):

    if pages != 0:
        driver.get(coleslink+"?pageNumber="+str(page))

    print("Acquiring items")
    content = driver.find_elements_by_class_name(itembox)
    print("All items Acquired")

    count = len(content)
    print("There are this many items...",count)

    for item in content:
        print("Items left...",count)
        try:
            brand = item.find_element_by_class_name(itembrand).text
            doc.write(brand+",")
            title = item.find_element_by_class_name(itemtitle).text
            doc.write(title+",")
            size = item.find_element_by_class_name(itemsize).text
            doc.write(size+",")
            price = item.find_element_by_class_name(itemprice).text
            doc.write(price)
            decimal = item.find_element_by_class_name(itemprice2).text
            doc.write(decimal+"\n")
            print("Saved line for "+title)
        except Exception as e:
            print("Error in item")
            print(e)
            doc.write("error"+"\n")
        count += -1

#starting the page loops
if pages==0:
    gather(0)
else:
    for page in range(1,pages+1):
        print("Starting Page...",page)
        gather(page)
        print("Page Complete")

#close Driver
driver.quit()
