import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller


wd=webdriver.Chrome(chromedriver_autoinstaller.install())
wd.maximize_window()
wd.get("https://tools.usps.com/zip-code-lookup.htm?byaddress")
time.sleep(5)        
vStreetTB= wd.find_element(By.ID,"tAddress")
vStreetTB.send_keys("11610 Memorial Pkwy South")
time.sleep(2) 

vCityTB=wd.find_element(By.ID,'tCity')
vCityTB.send_keys("Huntsville")
time.sleep(2) 

vStateCB= wd.find_element(By.ID,'tState')
vStateCB.send_keys("AL")
time.sleep(2) 

ZipTb=wd.find_element(By.ID,'tZip-byaddress')
ZipTb.send_keys("3803")
time.sleep(5) 

vFindBtn=wd.find_element(By.ID,'zip-by-address')
vFindBtn.click()
time.sleep(10)
       

    

    


    



