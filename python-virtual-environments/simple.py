from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
#driver = webdriver.Chrome(options=options)
DRIVER_PATH = '/home/ubuntu/python_selenium/chromedriver'
DRIVER_PATH='/home/this/Downloads/web_selenium/python-virtual-environments/chromedriver105_1'
driver = webdriver.Chrome(executable_path=DRIVER_PATH,options=options)
whitelist = set(',1234567890.,')
total_reviews=0
#door_dash_url="https://www.doordash.com/store/little-v-vietnamese-bistro-(fm-1463-rd)-katy-24002/"
#door_rating_xpath = '/html/body/div[1]/main/div/div[1]/div[1]/div/header/div[2]/div[1]/div[1]/div/div[3]/div/span[1]'
#door_review_xpath = '/html/body/div[1]/main/div/div[1]/div[1]/div/header/div[2]/div[1]/div[1]/div/div[3]/div/span[2]'
"""
door_dash_url="https://xplore-now.co/index.php"
door_rating_xpath = '/html/body/h5'
driver.get(door_dash_url)
doordash_rating=driver.find_element('xpath',door_rating_xpath)
door_rating = doordash_rating.text
print("Door Dash Rating : ",door_rating)



door_dash_url="https://www.opentable.com/nm-cafe-at-neiman-marcus-roosevelt-field?corrid=4d1c472f-8a52-4bd5-aa79-b56db717026e&avt=eyJ2IjoyLCJtIjowLCJwIjowLCJzIjowLCJuIjowfQ&p=2&sd=2022-09-21T19%3A00%3A00"
driver.get(door_dash_url)
doordash_rating=driver.find_element(By.CLASS_NAME, "reviewInfo")
door_rating = doordash_rating.text
print("tripadvisor Rating : ",door_rating)
"""
trip_advisor_url ="https://www.tripadvisor.com/Restaurant_Review-g56255-d1898015-Reviews-Roosevelt_s_at_7-McAllen_Texas.html"
trip_rating_xpath = 'ZDEqb'
trip_review_xpath = 'IcelI'

driver.get(trip_advisor_url)
rating=driver.find_element(By.CLASS_NAME,trip_rating_xpath)
trip_rating = ''.join(filter(whitelist.__contains__,rating.text)).replace(",", "")
print("trip_advisor Rating : ",trip_rating)
reviews=driver.find_element(By.CLASS_NAME,trip_review_xpath)
trip_review = ''.join(filter(whitelist.__contains__,reviews.text)).replace(",", "")
print("trip_advisor Review : ",trip_review)
