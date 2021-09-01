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
allhomeslink = "https://www.allhomes.com.au/sale/search?region=canberra-act"
itembox = "css-1r6lu77"
itemaddress = "css-1l8qi96"
itemsuburb = "css-31ko1n"
itemprice = "css-1dwkvzy"
itembedbathcar = "css-12mytvy"
pagination = "css-3ebg57"

#the chrome driver can have multiple options adjusted including making it headless.
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
#chrome_options.add_argument("--headless")
#chrome_options.headless = True # also works

#create a txt file
doc= open("homes.csv","w+")
doc.write("address,suburb,price,bed,bath,car"+"\n")

#make sure your chromedriver is with the current version of chrome installed.
#go to https://chromedriver.chromium.org/downloads to get chromedrivers
print("Opening Chrome Driver")
PATH = "C:\Python39\chromedriver.exe"
driver = webdriver.Chrome(PATH,options=(chrome_options))
driver.implicitly_wait(10)

#opening the page
print("Opening link")
driver.get(allhomeslink)
print("Link Opened")

#getting number of pages
boxes = driver.find_elements_by_class_name(pagination)
pages = 0
if len(boxes) != 0:
    pages = int(boxes[-1].text)
print("Number of Pages...",pages)

#what to do for each page
def gather(page):

    if pages != 0:
        driver.get(allhomeslink+"&page="+str(page))

    print("Acquiring items")
    content = driver.find_elements_by_class_name(itembox)
    print("All items Acquired")

    count = len(content)
    print("There are this many items...",count)

    for item in content:
        print("Items left...",count)
        try:
            address = item.find_element_by_class_name(itemaddress).text
            doc.write("\""+address+"\""+",")
            sub = item.find_element_by_class_name(itemsuburb).text
            doc.write(sub+",")
            price = item.find_element_by_class_name(itemprice).text
            doc.write("\""+price+"\""+",")
            bedbathcar = item.find_elements_by_class_name(itembedbathcar)
            for thingo in bedbathcar:
                doc.write(thingo.text)
                if thingo !=bedbathcar[-1]:
                    doc.write(",")
            doc.write("\n")
            print("Saved line for "+address)
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
