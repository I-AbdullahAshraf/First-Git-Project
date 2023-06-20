from selenium import webdriver
from selenium.webdriver.common.by import By
import time

Applicant_Fname = "Abdullah"
Applicant_Lname = "Applicant 11"
Applicant_Email= "abdullah.ashraf+applicant11@talentadore.com"
Applicant_tel= "1234567890"



driver = webdriver.Chrome()

driver.get("http://localhost:5000/apply/job-automation-testing/gdyOPa")

driver.maximize_window()

Apply_Button = driver.find_element(By.LINK_TEXT, "Apply for this position")
Apply_Button.click()
time.sleep(4)

scroll_to_form = driver.find_element(By.XPATH, "//a[@id='linkedin-apply']")
driver.execute_script("arguments[0].scrollIntoView();", scroll_to_form)

First_name = driver.find_element(By.ID, "first_name")
First_name.send_keys(Applicant_Fname)
time.sleep(1)

Last_name = driver.find_element(By.ID, "last_name")
Last_name.send_keys(Applicant_Lname)
time.sleep(1)

email = driver.find_element(By.ID, "email")
email.send_keys(Applicant_Email)
time.sleep(1)

telephone = driver.find_element(By.ID, "telephone")
telephone.send_keys("1234567890")
time.sleep(1)

scroll_to_submit = driver.find_element(By.XPATH, "//input[@type='submit']")
driver.execute_script("arguments[0].scrollIntoView();", scroll_to_submit)

scroll_to_submit.click()

time.sleep(4)

Message = driver.find_element(By.XPATH, "//div[@class='panel narrow public-view-container']").text

try:

    assert 'Home | TalentAdore - Superior Candidate Experience' in Message
    print('Test passed')
except Exception as e:
    print("Message", format(e))