from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os
import random

#Load Environment Variable
load_dotenv()
Phone = os.getenv("PHONE")
Password = os.getenv("PASSWORD")


#Set up WebDriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def Login():
    #Open Codingal Login Page
    driver.get("https://www.codingal.com/login/")
    
    phone_input = wait.until(EC.presence_of_element_located((By.NAME, "phone")))
    phone_input.send_keys(Phone)
    #Click "Login with Password" Button
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with password')]")))
    login_btn.click()

    #Enter Password
    password_input = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
    password_input.click()  # Click to activate it
    password_input.send_keys(Password)
    password_input.send_keys(Keys.RETURN)



def Pending_Project_Count():
    # Step 5: Navigate to Dashboard Project
    driver.get("https://www.codingal.com/teacher/dashboard/projects/")
    try:
        project_number = driver.find_element(By.XPATH, "//p[contains(@class, 'font-600') and contains(@class, 'text-lg') and contains(@class, 'text-yellow-200')]")
        Pending_project = int(project_number.text)
        return Pending_project
    except Exception as e:
        print(f"Could not find project count, assuming 0. Error{e}")
        return 0
    


def Review_Project():
    try:
        #Review Now Button
        anchor = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(), 'Review now')])[1]")))
        anchor.click()

        #Project Page
        #Find Student Name
        Student_Name_element = driver.find_element(By.XPATH, "//p[contains(text(), 'Submitted by')]/preceding-sibling::p")
        Student_Name = Student_Name_element.text  # Output: Student Name
        #Find Lesson Name
        Lesson_Name_element = driver.find_element(By.XPATH, "//p[contains(text(), 'Lesson')]")
        Lesson_Name = Lesson_Name_element.text
        print(f"Reviewing project for {Student_Name} - {Lesson_Name}") 

        #Review Now Button 
        review_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Review now')]")))
        review_btn.click()

        #Write Review
        textarea = wait.until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))

        #Review Text
        Review_text = f"Congratulations {Student_Name} on completing {Lesson_Name}! Your dedication and effort are commendable. Your work showcases creativity and skill. Keep up the excellent work! Your achievements demonstrate your potential and promise for future success. Well done {Student_Name}!"

        # Type text into the textarea
        textarea.send_keys(Review_text)

        #Give Star
        stars = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "rating-star")))

        given_stars = random.choice([3,4])

        # Click the 5th star (index 4 in zero-based index)
        stars[given_stars].click()

        review_project = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Review project')]")))
        #Submit Button Click
        review_project.click()  

        back_to_Project = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(), 'Back to projects')])")))
        back_to_Project.click()

        print("Review completed successfully.")
    except Exception as e:
        print(f"Error during review: {e}")



#Main Execution
Login()

Pending_projects = Pending_Project_Count()
print(f"Pending Project:{Pending_projects}")

if Pending_projects == 0:
    print("No pending projects to review.")
    print("✅ All project reviews completed.")
    driver.quit()
    exit()

while(Pending_projects>0):
    Review_Project()
    driver.implicitly_wait(5) 
    Pending_projects = Pending_Project_Count()
    
    
# Close the browser
print("✅ All project reviews completed.")
driver.quit()
