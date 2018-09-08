from selenium import webdriver
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

url = 'https://registrierung.web.de/User-Registration-Application/#.pc_page.freemail.index.hero_1.registrierung'

driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
driver.get(url)
time.sleep(1)
driver.find_element_by_xpath('//*[@for="id1"]').click()
driver.find_element_by_name('personaldataPanel:first-name:textfield').send_keys('Marlon')
driver.find_element_by_name('personaldataPanel:last-name:textfield').send_keys('Buga')
