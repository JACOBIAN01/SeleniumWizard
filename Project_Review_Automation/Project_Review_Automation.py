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
    
        Review = Generate_Review(Student_Name,Lesson_Name)
        # Type text into the textarea
        textarea.send_keys(Review)

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

def Generate_Review(name,lesson):
    try:
        openings = [
            f"Congratulations {name} on completing {lesson}!",
            f"Awesome job on finishing {lesson}, {name}!",
            f"Well done {name} for submitting your {lesson} project!",
            f"{name}, great effort on your {lesson} work!",
            f"You did it, {name}! {lesson} is complete!"
        ]

        compliments = [
            f"{name}, your creativity really shines through in the {lesson} project.",
            f"I can see the effort and thought you've put into {lesson}, {name}.",
            f"{name}, you're developing some solid skills through your work on {lesson}.",
            f"You're getting better with every project, and {lesson} is a great example of that, {name}.",
            f"Your {lesson} submission reflects clear understanding and imagination, {name}.",
            f"{name}, this {lesson} project shows great progress from your previous submissions.",
            f"Impressive attention to detail in your {lesson} project, {name}.",
            f"{name}, your approach to solving challenges in {lesson} is evolving beautifully."
        ]

        encouragements = [
            f"Keep up the amazing work! {name}",
            f"You're on the right path {name} — stay consistent!",
            f"Proud of your progress{name}. Keep going!",
            "Excited to see what you'll do next!",
            f"Keep pushing your limits {name} — you're doing great!",
            "Keep challenging yourself — the sky’s the limit!"
        ]

        closings = [
            "Your dedication is truly inspiring. Keep shining!",
            "You're setting a great example for others!",
            "Keep building your skills — you're on an exciting journey!",
            "This is only the beginning. Bigger things await!",
            "Fantastic work overall. Stay passionate and persistent!"
        ]

        emojis = ["🌟", "👏", "🔥", "💪", "🚀", "✅"]

        
        review_text = (
            f"{random.choice(openings)} "
            f"{random.choice(compliments)} {random.choice(compliments)} "
            f"{random.choice(encouragements)} {random.choice(encouragements)} "
            f"{random.choice(closings)} {random.choice(emojis)}"
        )

        return review_text

    except Exception as e:
        print(f"Error in Review Generation:{e}")
        Review_text = f"Congratulations {name} on completing {lesson}! Your dedication and effort are commendable. Your work showcases creativity and skill. Keep up the excellent work! Your achievements demonstrate your potential and promise for future success. Well done {name}!"
        return Review_text

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
    time.sleep(1)
    Pending_projects = Pending_Project_Count()
    
    
# Close the browser
print("✅ All project reviews completed.")
driver.quit()
