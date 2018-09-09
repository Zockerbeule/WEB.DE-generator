from selenium import webdriver
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

url = 'https://registrierung.web.de/User-Registration-Application/#.pc_page.freemail.index.hero_1.registrierung'

driver = webdriver.Chrome('C:\downloads\chromedriver.exe')
driver.get(url)
time.sleep(1)
driver.find_element_by_xpath('//*[@for="id1"]').click()
driver.find_element_by_name('personaldataPanel:first-name:textfield').send_keys('FirstName')
driver.find_element_by_name('personaldataPanel:last-name:textfield').send_keys('Lastname')
driver.find_element_by_name('personaldataPanel:countryDependentZipCodeCity-form:zipCodeAndCity:zipCode-textfield').send_keys('PLZ')
driver.find_element_by_name('personaldataPanel:countryDependentZipCodeCity-form:zipCodeAndCity:city-textfield').send_keys('City')
driver.find_element_by_name('personaldataPanel:streetAndStreetNumber:streetName-textfield').send_keys('Street')
driver.find_element_by_name('personaldataPanel:streetAndStreetNumber:streetNumber-textfield').send_keys('House')
driver.find_element_by_name('personaldataPanel:birthday:birthdata:birthday-textfield').send_keys('Day')
driver.find_element_by_name('personaldataPanel:birthday:birthdata:birthmonth-textfield').send_keys('Month')
driver.find_element_by_name('personaldataPanel:birthday:birthdata:birthyear-textfield').send_keys('Year')
driver.find_element_by_name('wishnamePanel:wishname:subForm:alias').click()
time.sleep(1)
keyboard.type('EmailPrefix')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)
driver.find_element_by_name('wishnamePanel:wishname:subForm:checkAvailability').click()
time.sleep(1.5)
driver.find_element_by_name('passwordPanel:password-form:password:textfield').send_keys('Password')
driver.find_element_by_name('passwordPanel:password-form:password-confirm:textfield').send_keys('Password')
driver.find_element_by_name('passwordPanel:email:textfield').send_keys('SaveEmail')
driver.find_element_by_name('passwordPanel:answer:textfield').send_keys('Mothers1stName')
driver.find_element_by_name('captchaPanel:captcha-response:textfield').click()
