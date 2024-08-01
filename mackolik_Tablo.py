from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://arsiv.mackolik.com/Default.aspx")

# Puan durumu tablosunun yüklenmesini bekleyin
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "tblLightStanding"))
)

# Tablonun içindeki tüm satırları bulun
rows = driver.find_elements(By.XPATH, "//table[@id='tblLightStanding']//tbody//tr")

# Her bir satırdaki hücreleri yazdırın, virgülleri ve köşeli parantezleri kaldırarak
for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")
    row_text = " ".join([column.text for column in columns])
    print(row_text)

driver.quit()
