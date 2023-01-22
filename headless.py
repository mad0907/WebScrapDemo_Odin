from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller
import time
import os

options = Options()  
# this parameter tells Chrome that
# it should be run without UI (Headless)
options.headless = True


driver = webdriver.Chrome(chrome_options=options, executable_path='C:/Users/munmun.a.das/AppData/Local/SeleniumBasic/chromedriver.exe')
driver.get("https://www.youtube.com/")
time.sleep(5)
txtSearch= driver.find_element(By.NAME, 'search_query')
txtSearch.send_keys("Odin School Videos")
btnSearch= driver.find_element(By.ID, "search-icon-legacy")
btnSearch.click()
time.sleep(10)
# capture the screen
print(driver.title)
driver.get_screenshot_as_file("./capture.png")
time.sleep(5)