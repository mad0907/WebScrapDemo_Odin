from threading import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller
import time

def validateAdd1():
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
    time.sleep(30)

def validateAdd2():
    wd1=webdriver.Chrome(chromedriver_autoinstaller.install())
    wd1.maximize_window()
    wd1.get("https://tools.usps.com/zip-code-lookup.htm?byaddress")
    time.sleep(5)        
    vStreetTB= wd1.find_element(By.ID,"tAddress")
    vStreetTB.send_keys("2200 Sparkman Drive")
    time.sleep(2) 

    vCityTB=wd1.find_element(By.ID,'tCity')
    vCityTB.send_keys("Huntsville")
    time.sleep(2) 

    vStateCB= wd1.find_element(By.ID,'tState')
    vStateCB.send_keys("AL")
    time.sleep(2) 

    ZipTb=wd1.find_element(By.ID,'tZip-byaddress')
    ZipTb.send_keys("35810")
    time.sleep(5) 

    vFindBtn=wd1.find_element(By.ID,'zip-by-address')
    vFindBtn.click()
    time.sleep(30)


def main():
    t1=Thread(target=validateAdd1)
    t2=Thread(target=validateAdd2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Completed')

main()
    


