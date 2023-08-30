from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://stage.talentadore.com/login")

driver.maximize_window()

email = driver.find_element(By.ID, 'email')
print("Found Email")
email.send_keys("abdullah.ashraf+testing@talentadore.com")

time.sleep(2)

password = driver.find_element(By.ID, 'password')
print("Found password")
password.send_keys("password")
time.sleep(2)

submit = driver.find_element(By.ID, 'submit')
print("Found Submit")
submit.click()
time.sleep(4)

print(driver.title)

try:
    title = driver.title
    assert 'Home | TalentAdore - Superior Candidate Experience' in title
    print('Test passed')
except Exception as e:
    print('Test failed', format(e))

Candiate_Intro = driver.find_element(By.XPATH, '//a[@href="/introductions"]')
Candiate_Intro.click()
time.sleep(4)


