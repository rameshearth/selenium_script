from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request as ur
import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")


#Local APIS links
fetch_places_api = 'https://xplore-now.co/index.php/index.php/apis/getPlaceDetail';
update_place_data_api = 'https://xplore-now.co/index.php/index.php/apis/insertPlaceDetail';

#Live APIS Links
#fetch_places_api = 'https://xplore-now.co/index.php/apis/getPlaceDetail';
#update_place_data_api = 'https://xplore-now.co/index.php/apis/insertPlaceDetail';

response = ur.urlopen(fetch_places_api)
PlaceDetail = json.loads(response.read())

# 1) Trip Advisor configration
DRIVER_PATH1='/home/ubuntu/python_selenium/chromedriver'
driver1=webdriver.Chrome(executable_path=DRIVER_PATH1,options=options)
trip_rating_xpath = 'ZDEqb'
trip_review_xpath = 'IcelI'


# 2) Open Table  configration
DRIVER_PATH2 = '/home/ubuntu/python_selenium/chromedriver'
driver2 = webdriver.Chrome(executable_path=DRIVER_PATH2,options=options)
open_rating_xpath = 'ratingInfo' #using ID
open_review_xpath = 'reviewInfo' #using ID

# 3) Google configration 
DRIVER_PATH3 = '/home/ubuntu/python_selenium/chromedriver'
driver3 = webdriver.Chrome(executable_path=DRIVER_PATH3,options=options)
google_rating_xpath = 'Aq14fc'  #using ClassName
google_review_xpath = 'hqzQac'  #using ClassName

#4) Door Dash configration 
DRIVER_PATH4 = '/home/ubuntu/python_selenium/chromedriver'
driver4 = webdriver.Chrome(executable_path=DRIVER_PATH4,options=options)
door_rating_xpath = '/html/body/div[1]/main/div/div[1]/div[1]/div/header/div[2]/div[1]/div[1]/div/div[3]/div/span[1]'
door_review_xpath = '/html/body/div[1]/main/div/div[1]/div[1]/div/header/div[2]/div[1]/div[1]/div/div[3]/div/span[2]'

# Yelp  configration
DRIVER_PATH5 = '/home/this/Downloads/web_selenium/python-virtual-environments/chromedriver105_5'
driver5 = webdriver.Chrome(executable_path=DRIVER_PATH5,options=options)
yelp_rating_xpath = 'five-stars__09f24__mBKym five-stars--large__09f24__Waiqf display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY'
yelp_review_xpath = ' arrange-unit__09f24__rqHTg arrange-unit-fill__09f24__CUubG border-color--default__09f24__NPAKY nowrap__09f24__lBkC2'



os.system('cls||clear')
print("********************************************** ")

whitelist = set('1234567890.,')
final_array=[]

# ((number of review / total review) * rating)) 

for place in PlaceDetail:
	print('SrNumber',place['SrNumber']);
	overall_rating=0
	trip_advisor_url=place['trip_advisor_url']
	trip_rating=0
	trip_review=0
	open_table_url=place['open_table_url']
	open_rating=0
	open_review=0
	google_url=place['google_url']
	google_rating=0
	google_review=0
	door_dash_url=place['door_dash_url']
	door_rating=0
	door_review=0
	yelp_url=place['yelp_url']
	yelp_rating=0
	yelp_review=0
	total_reviews=0;

	#############
	############# Trip advisor website rating
	if trip_advisor_url is not None:
		try:
			driver1.get(trip_advisor_url)
			rating=driver1.find_element(By.CLASS_NAME,trip_rating_xpath)
			trip_rating = ''.join(filter(whitelist.__contains__,rating.text)).replace(",", "")
			print("trip_advisor Rating : ",trip_rating)
			reviews=driver1.find_element(By.CLASS_NAME,trip_review_xpath)
			trip_review = ''.join(filter(whitelist.__contains__,reviews.text)).replace(",", "")
			print("trip_advisor Review : ",trip_review)
			total_reviews=total_reviews +float(trip_review);
		except Exception as e:
			if 'particular message' in str(e):
				continue
			########## open table rating
	if open_table_url is not None:
		try:
			driver2.get(open_table_url)
			open_table_rating=driver2.find_element(By.ID, open_rating_xpath)
			open_rating = ''.join(filter(whitelist.__contains__,open_table_rating.text)).replace(",", "")
			print("Open table Rating : ",open_rating)
			reviews=driver2.find_element(By.ID,open_review_xpath)
			open_review = ''.join(filter(whitelist.__contains__,reviews.text)).replace(",", "")
			print("Open table reviews : ",open_review)
			total_reviews=total_reviews +float(open_review);
		except Exception as e:
			if 'particular message' in str(e):
				continue
	####
	###################### door
	if google_url is not None:
		try:
			driver3.get(google_url)
			google_rating1=driver3.find_element(By.CLASS_NAME, google_rating_xpath)
			google_rating=''.join(filter(whitelist.__contains__,google_rating1.text)).replace(",", "")
			print("Google Rating : ",google_rating)
			reviews=driver3.find_element(By.CLASS_NAME,google_review_xpath)
			google_review=''.join(filter(whitelist.__contains__,reviews.text)).replace(",", "")
			print("Google reviews : ",google_review)
			total_reviews=total_reviews +float(google_review);
		except Exception as e:
			if 'particular message' in str(e):
				continue
			######################
	if door_dash_url is not None:
		try:
			#driver4.get(door_dash_url)
			#doordash_rating=driver4.find_element('xpath',door_rating_xpath)
			#door_rating = ''.join(filter(whitelist.__contains__,doordash_rating.text)).replace(",", "")
			#print("Door Dash Rating : ",door_rating)
			#reviews=driver4.find_element('xpath',door_review_xpath)
			#door_review = ''.join(filter(whitelist.__contains__,reviews.text)).replace(",", "")
			#print("Door Dash reviews : ",door_review)
			total_reviews=total_reviews +float(door_review);
		except Exception as e:
			if 'particular message' in str(e):
				continue

	if yelp_url is not None:
		try:
			driver5.get(yelp_url)
			yelp_url_rating=driver5.find_element(By.CLASS_NAME,yelp_rating_xpath)
			text = yelp_url_rating.get_attribute("aria-label")
			answer = ''.join(filter(whitelist.__contains__, text)).replace(",", "")
			yelp_rating = answer
			print("Yelp Rating : ",yelp_rating)
			reviews=driver5.find_element(By.CLASS_NAME,yelp_review_xpath)
			yelp_review = ''.join(filter(whitelist.__contains__,reviews.text)).replace(",", "")
			print("Yelp Reviews : ",yelp_review)
			total_reviews=total_reviews +float(yelp_review);
		except Exception as e:
			if 'particular message' in str(e):
				continue
	print("total_reviews :",total_reviews )
	#overall_rating = float(trip_rating)+float(open_rating)+float(door_rating)+float(yelp_rating)
	#overall_rating = (float(trip_rating)+float(open_rating)+float(google_rating)+float(yelp_rating)+float(yelp_rating))/5
	if(total_reviews == 0):
		overall_rating = 0
	else:
		overall_rating = ((float(trip_review)/total_reviews)*float(trip_rating)) + ((float(open_review)/total_reviews)*float(open_rating)) + ((float(google_review)/total_reviews)*float(google_rating)) + ((float(door_review)/total_reviews)*float(door_rating)) + ((float(yelp_review)/total_reviews)*float(yelp_rating))

	final_array.append({"SrNumber": place['SrNumber'], "overall_rating": overall_rating,"total_reviews":total_reviews});


params = {"final_array": json.dumps(final_array)}
print(params)

"""
data = MultipartEncoder(fields = params)
headers = {'Content-type': data.content_type}
response = requests.post(
    update_place_data_api,
    data = data,
    headers = headers
)
print(response.text)
"""
#program end



	
#driver1.quit()driver2.quit()driver3.quit()
#print(url.json());

"""
driver.get("https://www.tripadvisor.com/Restaurant_Review-g35805-d10066453-Reviews-Immm_Rice_Beyond-Chicago_Illinois.html")


rating = driver.find_element("xpath", '/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/span[1]');
print("Rating : ",rating.text)
#for listing in listings:
reviews = driver.find_element("xpath", '/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/a');
print("Reviews : ",reviews.text)
driver.quit()
"""