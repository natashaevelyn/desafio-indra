from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()


browser.get('https://www.americanas.com.br/')
element = browser.find_element_by_id('h_usr-link')
element.click()
time.sleep(1)
entrar = browser.find_element_by_id('h_usr-signin')
entrar.click()
email = browser.find_element_by_id('email-input')
email.send_keys('armor1beare@gmail.com')
senha = browser.find_element_by_id('password-input')
senha.send_keys('testeindra')
entrar = browser.find_element_by_id('login-button')
entrar.click()

time.sleep(5)