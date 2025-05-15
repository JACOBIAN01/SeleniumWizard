from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os
import random

load_dotenv()
Phone = os.getenv("PHONE")
Password = os.getenv("PASSWORD")
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def Login():
    try:
        driver.get("https://www.codingal.com/")
        time.sleep(1)
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
        login_button.click()
        time.sleep(0.5)
        phone_input = wait.until(EC.presence_of_element_located((By.NAME, "phone")))
        phone_input.send_keys(Phone)
        time.sleep(0.5)
        #Click "Login with Password" Button
        login_btn_1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with password')]")))
        login_btn_1.click()
        time.sleep(0.5)
        #Enter Password
        password_input = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
        password_input.send_keys(Password)
        time.sleep(0.5)
        login_btn_2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with password')]")))
        login_btn_2.click()
        time.sleep(2)  # Click to activate it
    except Exception as e:
        print(f"Error During Login: {e}")

def Pending_Project_Count():
    # Step 5: Navigate to Dashboard Project
    driver.get("https://www.codingal.com/teacher/dashboard/projects/")
    try:
        time.sleep(0.5)
        project_number = wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'font-600') and contains(@class, 'text-lg') and contains(@class, 'text-yellow-200')]")))
        # project_number = driver.find_element(By.XPATH, "//p[contains(@class, 'font-600') and contains(@class, 'text-lg') and contains(@class, 'text-yellow-200')]")
        Pending_project = int(project_number.text)
        return Pending_project
    except Exception as e:
        print(f"Could not find project count, assuming 0. Error{e}")
        return 0

def Review_Project():
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(), 'Review now')])[1]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)  # Allow time for scrolling
        driver.execute_script("arguments[0].click();", element)
        #Project Page
        #Find Student Name
        Student_Name_element = wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Submitted by')]/preceding-sibling::p")))
        Student_Name = Student_Name_element.text  # Output: Student Name
        #Find Lesson Name
        # Lesson_Name_element = driver.find_element(By.XPATH, "//p[contains(text(), 'Lesson')]")
        Lesson_Name_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Lesson')]"))
        )
        Lesson_Name = Lesson_Name_element.text
        print(f"Reviewing project for {Student_Name} - {Lesson_Name}") 
        #Review Now Button
        review_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Review now')]")))
        review_btn.click()
        #Write Review
        textarea = wait.until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
        #Review Text
        Review = f"Congratulations {Student_Name} on completing {Lesson_Name}! Your dedication and effort are commendable. Your work showcases creativity and skill. Keep up the excellent work! Your achievements demonstrate your potential and promise for future success. Well done {Student_Name}!"
        # Type text into the textarea
        textarea.send_keys(Review)

        #Enhance With AI
        try:
            enhance_button = wait.
        except Exception as e:
            pass
        #Give Star
        stars = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "rating-star")))
        given_stars = random.choice([3,4])
        # Click the 5th star (index 4 in zero-based index)
        stars[given_stars].click()
        review_project = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit review')]")))
        #Submit Button Click
        review_project.click()  
        back_to_Project = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(), 'Back to projects')])")))
        back_to_Project.click()
        print(f"Review completed successfully for {Student_Name}.")
    except Exception as e:
        print(f"Error during review: {e}")

#Main Execution
def Start_Project_Review():
    Login()
    while True:
        Pending_projects = Pending_Project_Count()
        if Pending_projects == 0:
            print("No pending projects to review.")
            print(" All project reviews completed.")
            break
        try:
            Review_Project()
            time.sleep(1)
        except Exception as e:
            print(f"Error reviewing a project: {e}")
            continue
    driver.quit()


Start_Project_Review()

