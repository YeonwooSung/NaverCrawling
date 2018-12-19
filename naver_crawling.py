from selenium import webdriver
from bs4 import BeautifulSoup
import time

# download chromedriver from <https://sites.google.com/a/chromium.org/chromedriver/downloads>
driver = webdriver.Chrome('./chromedriver') #replace the file path string with the file path of the chrome driver

driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
driver.implicitly_wait(5)

# insert ID
id = driver.find_element_by_id('id')
id.send_keys('ID_String') # put your id

# insert password
id = driver.find_element_by_id('pw')
id.send_keys('PW_String') # put your pw

time.sleep(2)

driver.implicitly_wait(15)

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click() #naver log in

driver.implicitly_wait(15)

# If the log in success, enter 1. Otherwise, input the shown security code!
value = input('Enter security code: ')

if (value == '1'):
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span[1]/a').click()
else:
    time.sleep(3)
    # insert password
    id = driver.find_element_by_id('pw')
    id.send_keys('PW_String')  # put your pw

    time.sleep(5)

    id = driver.find_element_by_name('chptcha')
    id.send_keys(value)

    time.sleep(5)

    driver.implicitly_wait(15)

    driver.find_element_by_xpath('//*[@id="login_submit"]').click()  # naver log in

    driver.implicitly_wait(10)

    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span[1]/a').click()


time.sleep(5)
