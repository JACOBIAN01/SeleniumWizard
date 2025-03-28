from selenium import webdriver
import os , time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.codingal.com/login/")

# element = driver.find_element(By.ID,"Welcome_to_Wikipedia")

# element = driver.find_element(By.XPATH,"//div[@id='mp-welcomecount']")

# element = driver.find_element(By.XPATH,"//div[@id='mp-left']")

element = driver.find_element(By.ID,"phone")
time.sleep(1)
element.send_keys("7029043892")
time.sleep(1)
login = driver.find_element(By.XPATH,"//button[contains(text(),'Login with password')]")
time.sleep(1)
login.click()
time.sleep(2)
password_input = driver.find_element(By.ID,"password")
password_input.send_keys("Chiku@(2003)")
login_again = driver.find_element(By.XPATH,"//button[contains(text(),'Login with password')]")
login_again.click()
# print(element.text)
time.sleep(5)
