from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os


load_dotenv()

#Set up WebDriver
driver = webdriver.Chrome()

#Open Codingal Login Page
driver.get("https://www.codingal.com/login/")
wait = WebDriverWait(driver, 10)

#Enter Phone Number
Phone = os.getenv("PHONE")
phone_input = wait.until(EC.presence_of_element_located((By.NAME, "phone")))
phone_input.send_keys(Phone)
time.sleep(2)  # Small delay for UI update

#Click "Login with Password" Button
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with password')]")))
login_btn.click()


#Enter Password
Password = os.getenv("PASSWORD")
password_input = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
password_input.click()  # Click to activate it
password_input.send_keys(Password)

password_input.send_keys(Keys.RETURN)

#Open Dashboard Wait for Dashboard to Load
time.sleep(2)
  
# Step 5: Navigate to Dashboard Project
driver.get("https://www.codingal.com/teacher/dashboard/projects/")
time.sleep(0.5)

#Find Total Number of Pending Project

project_number = driver.find_element(By.XPATH, "//p[contains(@class, 'font-600') and contains(@class, 'text-lg') and contains(@class, 'text-yellow-200')]")
time.sleep(0.2)
Pending_project = int(project_number.text)
print(f"Total Project Pending: {Pending_project}")
time.sleep(0.2)

def Review_Project():

    #Review Npw Button
    anchor = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(), 'Review now')])[1]")))
    anchor.click()

    #Project Page

    #Find Student Name
    Student_Name_element = driver.find_element(By.XPATH, "//p[contains(text(), 'Submitted by')]/preceding-sibling::p")
    Student_Name = Student_Name_element.text
    print(f"Student Name: {Student_Name}")  # Output: Student Name

    #Find Lesson Name
    Lesson_Name_element = driver.find_element(By.XPATH, "//p[contains(text(), 'Lesson')]")
    Lesson_Name = Lesson_Name_element.text
    print(f"Lesson Name: {Lesson_Name}") 

    time.sleep(1)

    #Review Npw Button 
    review_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Review now')]")))
    review_btn.click()

    #Write Review
    textarea = wait.until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))

    # Type text into the textarea
    textarea.send_keys(f"Congratulations {Student_Name} on completing {Lesson_Name}! Your dedication and effort are commendable. Your work showcases creativity and skill. Keep up the excellent work! Your achievements demonstrate your potential and promise for future success. Well done {Student_Name}!")

    #Give Star

    stars = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "rating-star")))

    # Click the 5th star (index 4 in zero-based index)
    stars[4].click()

    time.sleep(0.5)
    review_project = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Review project')]")))
    #Submit Button Click
    review_project.click()

    time.sleep(1)

    Back_to_Project = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(), 'Back to projects')])")))
    Back_to_Project.click()

    time.sleep(5)

    print("Project Review Done")

while(Pending_project!=0):
    Review_Project()
    project_number = driver.find_element(By.XPATH, "//p[contains(@class, 'font-600') and contains(@class, 'text-lg') and contains(@class, 'text-yellow-200')]")
    time.sleep(0.1)
    Pending_project = int(project_number.text)
    time.sleep(0.1)
    
    
print("All Review Done")

# Close the browser
driver.quit()
