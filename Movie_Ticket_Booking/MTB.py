from selenium import webdriver
import os , time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://in.bookmyshow.com/explore/home/kharagpur")
driver.implicitly_wait(2)