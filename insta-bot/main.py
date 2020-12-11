from time import sleep
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

# username_input = browser.find_element_by_xpath("//label[@class='f0n8F']/input[@class='_2hvTZ' and @type='text' and @name='username']").click()

sleep(2)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("praful_pathare")
password_input.send_keys("imking_instagram98patharepraful")

login_button = browser.find_element_by_css_selector("button[type='submit']")
login_button.click()

sleep(15)

browser.close()
