
from os import link
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
import time as ti


PATH='chromedriver.exe'
driver=webdriver.Chrome(PATH)
driver.get('https://the-internet.herokuapp.com/')

try :
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Form Authentication"))).click()
    user=driver.find_element_by_id('username')
    user.clear()
    user.send_keys('tomsmith')
    ti.sleep(3)
    password=driver.find_element_by_id('password')
    password.clear()
    password.send_keys('SuperSecretPassword!')
    ti.sleep(3)
    password.send_keys(Keys.ENTER)
    ti.sleep(5)
    driver.back()
    ti.sleep(5)
    driver.back()
    ti.sleep(10)
    
finally:
    driver.quit()

