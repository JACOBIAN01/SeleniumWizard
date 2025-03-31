from selenium import webdriver
import os , time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://in.bookmyshow.com/explore/home/vijayawada")

Movies = driver.find_elements(By.XPATH,"//div[contains(@class, 'sc-7o7nez-0') and contains(@class, 'daKrZU')]")
driver.implicitly_wait(10)

print(Movies)
# for movie in Movies:
#     print(movie.text)
driver.implicitly_wait(10)

driver.quit()
