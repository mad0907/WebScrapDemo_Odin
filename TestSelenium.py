from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller
import time

wd=webdriver.Chrome(chromedriver_autoinstaller.install())
wd.maximize_window()

wd.get("https://www.youtube.com/")
time.sleep(10)
txtSearch= wd.find_element(By.NAME, 'search_query')
txtSearch.send_keys("Blockchain")
time.sleep(2)
btnSearch= wd.find_element(By.ID, "search-icon-legacy")
btnSearch.click()
time.sleep(10)




















