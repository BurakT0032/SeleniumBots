from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



service = Service(executable_path="chromedriver.exe")  #yollar aynı olmalı
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME,"gLFyf")


input_element.clear() #eğer arama kısmında yazılı bir şey varsa onu siler
input_element.send_keys("instagram" + Keys.ENTER)

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"instagram"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT,"instagram")
link.click()

time.sleep(10)

driver.quit()
# Temporary change
