from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller
import time

wd=webdriver.Chrome(chromedriver_autoinstaller.install())
wd.maximize_window()

wd.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe_frameborder")
time.sleep(5)
wd.switch_to.frame(1)
h2Tag=wd.find_elements(By.TAG_NAME, "H2")
for h2 in h2Tag:
    print(h2.text)
