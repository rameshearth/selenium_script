from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
import urllib.request as ur
import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os


DRIVER_PATH = '/home/this/Downloads/web_selenium/python-virtual-environments/chromedriver105_1'
driver4 = webdriver.Chrome(executable_path=DRIVER_PATH)
whitelist = set(',1234567890.,')
total_reviews=0
door_dash_url="https://www.doordash.com/store/little-v-vietnamese-bistro-(fm-1463-rd)-katy-24002/"
door_rating_xpath = '/html/body/div[1]/main/div/div[1]/div[1]/div/header/div[2]/div[1]/div[1]/div/div[3]/div/span[1]'
door_review_xpath = '/html/body/div[1]/main/div/div[1]/div[1]/div/header/div[2]/div[1]/div[1]/div/div[3]/div/span[2]'
driver4.get(door_dash_url)
doordash_rating=driver4.find_element('xpath',door_rating_xpath)
door_rating = ''.join(filter(whitelist.__contains__,doordash_rating.text)).replace(",", "")
print("Door Dash Rating : ",door_rating)
reviews=driver4.find_element('xpath',door_review_xpath)
door_review = ''.join(filter(whitelist.__contains__,reviews.text)).replace(",", "")
print("Door Dash reviews : ",door_review)
total_reviews=total_reviews +float(door_review);
#open_review = ''.join(filter(whitelist.__contains__,reviews.text))
#print(open_review);
print("door_review",door_review);
print("door_rating",door_rating);

"""
driver.find_element("link text","Restaurants").click();
time.sleep(3)
driver.find_element("xpath","/html/body/div[2]/div/form/input[1]").send_keys("Immm Rice & Beyond");
time.sleep(3)

#driver.find_element("xpath","/html/body/div[4]/div/form/div/a[1]").click();
#print("Rating : ",listings.text)
#for listing in listings:
#driver.quit()

#//*[@id="component_50"]/div[1]/div/div[1]/div/div[1]/div[1]
#//*[@id="component_50"]/div[1]/div/div[1]/div/div[1]/div[1]/span[1]

#/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/span[1]
"""