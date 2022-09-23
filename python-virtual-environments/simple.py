from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time 

DRIVER_PATH = '/home/this/Downloads/web_selenium/python-virtual-environments/chromedriver105'

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://www.tripadvisor.com")


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