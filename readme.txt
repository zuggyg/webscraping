-----------------
Uses the following Python Libraries
-----------------
Selenium: https://selenium-python.readthedocs.io/installation.html
Used to control the webdriver

Additionally you will need to download the relevant webdriver you have for your browser for Chrome I use:
https://sites.google.com/a/chromium.org/chromedriver/downloads


-----------------
To use this script
-----------------

Towards the top you will need to adjust the variables for the different websites you wish to use.
This includes the link to the page with the data, the container that holds the data, and each of the variables you wish to save.

You may also want to adjust chrome driver options. I normally run it as headless.

Following that you will need to name your text/csv file you are saving and add the first line for your column headers. 

And finally within the function gather, make sure you adjust what you want to save in your text/csv file. 