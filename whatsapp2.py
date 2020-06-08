import time 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#chrome_options.add_argument("--profile-directory=/home/p4pz0l/Desktop/WhatsApp-bot-selenium")
chrome_options.add_argument("--user-data-dir=cookies")
#driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=chrome_options)
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver = webdriver.Chrome()
caption ="*isi* kasjgdkjahsdkjahsgdkjahsgdkjahsgdkjahsgdkjhagsd_dari_%0apesan ```ljl```%0a%0a%0a%0a*Santai Jangan Ngegas*"
##nowhatsapp="6287722086621"

#driver.get('https://web.whatsapp.com/send?phone=' + nowhatsapp + '&text=' + caption)
#time.sleep(8)
#tombolsend=driver.find_element_by_class_name('_1U1xa')
#tombolsend.click()

b = '''6282371597662
6282371597662
6282371597662
6282371597662
6282371597662
'''
a = '''6287722086621
6287722086621
6287722086621
6287722086621
6287722086621
'''
nowas = a.splitlines()
for nowhaltsapp in nowas:
    driver.get('https://web.whatsapp.com/send?phone=' + nowhaltsapp + '&text=' + caption)
    time.sleep(8)
    tombolsend=driver.find_element_by_class_name('_1U1xa')
    tombolsend.click()
    time.sleep(1)
    driver.switchTo().alert().accept();

