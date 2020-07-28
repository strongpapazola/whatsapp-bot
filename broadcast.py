from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

nomer = ['628123456789','628123456789','628123456789']
pesan = 'test'
delay = 7 # seconds

for i in nomer:
 url = 'https://web.whatsapp.com/send?phone='+i+'&text='+pesan
 print(url)
 chrome_options = Options()
 chrome_options.add_argument("user-data-dir=cookie")
 driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"./chromedriver")
 driver.get(url)
 time.sleep(2)

 while True:
  try:
   myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, '_1U1xa')))
   driver.find_element_by_class_name('_1U1xa').click()
   print("button ada!")
   time.sleep(3)
   break
  except TimeoutException:
   try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'S7_rT FV2Qy')))
    driver.find_element_by_class_name('S7_rT FV2Qy').click()
   except TimeoutException:
    print('nomer ada')
   print("nyari button send!")
 driver.quit()
