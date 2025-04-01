from selenium import webdriver
import os , time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/explore/home/vijayawada")
driver.implicitly_wait(5)

Movies = driver.find_elements(By.XPATH,"//div[contains(@class, 'sc-7o7nez-0') and contains(@class, 'daKrZU')]")
driver.implicitly_wait(5)

MovieList = [f"{movie.text}" for movie in Movies]

MyMovie = driver.find_elements(By.XPATH, "//a[contains(@class,'sc-133848s-11') and contains(@class,'sc-lnhrs7-5') and contains(@class,'fHgWnO')]")

MovieLink = [movie.get_attribute("href") for movie in MyMovie]

print("Available Movies")
for i,(M_name , M_link) in enumerate(zip(MovieList,MovieLink),start=1):
    print(f"{i}.{M_name} - {M_link}")

choice = int(input("Enter Movie Number to Proceed: "))

driver.implicitly_wait(5)
MovieLinkElement = driver.find_element(By.XPATH,f"//a[@href='{MovieLink[choice-1]}']")
MovieLinkElement.click()


Book_Ticket_Button = driver.find_element(By.XPATH,"//button[contains(@class,'sc-8f9mtj-0') and contains(@class,'sc-8f9mtj-1') and contains(@class,'sc-1vmod7e-0 bGKFux')]")
Book_Ticket_Button.click()
driver.implicitly_wait(5)

try:
    
    language = driver.find_elements(By.XPATH,"//li[contains(@class,'sc-vhz3gb-0')]//section[contains(@class,'sc-vhz3gb-1')]//span")
    print("Available Language")
    for i,lang in enumerate(language):
        print(f"{i}-{lang.text}")
    lang_choice = int(input("Select Language: "))
    selected_lang = language[lang_choice].text

    lang_button = driver.find(By.XPATH,f"//li[.//span[text()='{selected_lang}']]//div[contains(@class,'sc-vhz3gb-3')and contains(@class,'ksLpgw')]//span[text()='2D']")

    lang_button.click()
    driver.implicitly_wait(5)
    
    
except:
    print("No Language Section Available. Proceed to Booking page")





driver.quit()
