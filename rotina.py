from selenium import webdriver
import time
import os

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://br.investing.com/currencies/usd-brl-historical-data')

time.sleep(5)
while len(driver.find_elements_by_id("onetrust-accept-btn-handler")) == 0:
    time.sleep(3)
driver.find_element_by_id("onetrust-accept-btn-handler").click()


driver.find_element_by_partial_link_text("Baixar dados").click()
driver.find_element_by_id("loginFormUser_email").send_keys("rubenstome15@gmail.com")
driver.find_element_by_id("loginForm_password").send_keys(os.environ["SENHA1"])

elementos = driver.find_elements_by_css_selector("a.orange")

elementos[2].click()

time.sleep(3)
driver.find_element_by_class_name("downloadBlueIcon").click()
