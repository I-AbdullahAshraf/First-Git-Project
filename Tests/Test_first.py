from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://radical.talentadore.com/login")

driver.maximize_window()

email = driver.find_element(By.ID, 'email')
print("Found Email")
email.send_keys("abdullah.ashraf@talentadore.com")

time.sleep(2)

password = driver.find_element(By.ID, 'password')
print("Found password")
password.send_keys("hello12345678")
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

positions = driver.find_element(By.XPATH, '//a[@href="/positions"]')
positions.click()
time.sleep(4)

driver.find_element(By.ID, 'create-job').click()

job_title = driver.find_element(By.ID, 'new_job-job_name')
job_title.send_keys("Automated Job")

scroll_to_job_des = driver.find_element(By.XPATH, "//label[@for='new_job-duedate']")
driver.execute_script("arguments[0].scrollIntoView();", scroll_to_job_des)

iframe = driver.find_element(By.XPATH, "//iframe[@title='Rich Text Editor, new_job-job_description']")
driver.switch_to.frame(iframe)
job_des = driver.find_element(By.XPATH, "//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")
job_des.send_keys("This is the Automated job Description")


driver.switch_to.default_content()


driver.find_element(By.XPATH, "//select[@id='recruitment_flow']/option[text()='New Recruitment Flow']").click()

driver.find_element(By.XPATH, "//select[@id='approval-process-select']/option[text()='Default approval process']").click()

scroll_to_reason_for_vacancy = driver.find_element(By.XPATH, "//label[@for='new_job-reason_for_vacancy']")

driver.find_element(By.XPATH, "//select[@data-id='asking_for_approval']/option[text()='abdullah.ashraf@talentadore.com']").click()

requirements = driver.find_element(By.XPATH, "//a[contains(text(),'Next: Requirements')]")
requirements.click()

time.sleep(4)

skills = driver.find_element(By.ID, 'skillsinput')
print("Found Skills")
add_skills = driver.find_element(By.ID, 'skills')
print("Found Add Skills Button")

skills.send_keys("PHP")
add_skills.click()
skills.send_keys("Java Script")
add_skills.click()
skills.send_keys("HTML")
add_skills.click()
skills.send_keys("CSS")
add_skills.click()

trait = driver.find_element(By.ID, 'traitsinput')
add_trait = driver.find_element(By.ID, 'traits')

trait.send_keys("communication")
add_trait.click()
trait.send_keys("Verbal / Written")
add_trait.click()
trait.send_keys("documentation")
add_trait.click()

language = driver.find_element(By.ID, 'languagesinput')
add_language = driver.find_element(By.ID, 'languages')

language.send_keys("English")
add_language.click()
language.send_keys("Finnish")
add_language.click()
language.send_keys("Swedish")
add_language.click()
language.send_keys("German")
add_language.click()
time.sleep(5)
musthave1 = driver.find_element(By.ID, 'requirement-HTML',)
musthave2 = driver.find_element(By.ID, 'requirement-CSS',)
musthave3 = driver.find_element(By.ID, 'requirement-Java_32_Script',)
musthave4 = driver.find_element(By.ID, 'requirement-communication',)
musthave5 = driver.find_element(By.ID, 'requirement-English',)

musthave1.click()
musthave2.click()
musthave3.click()
musthave4.click()
musthave5.click()

calibration = driver.find_element(By.ID, 'calibration-button')
calibration.click()

submit_calibration = driver.find_element(By.ID, 'submit-skills')
submit_calibration.click()




about_us = driver.find_element(By.XPATH, "//a[contains(text(),'Next: About us')]")
about_us.click()

# submit_calibration = driver.find_element(By.ID, 'submit-skills')
# submit_calibration.click()

driver.find_element(By.XPATH, "//select[@id='business-unit']/option[text()='Testing Company Profile']").click()

update_profile_button = driver.find_element(By.XPATH, "//a[@class='submit-button update-company-profile']")
update_profile_button.click()

preview = driver.find_element(By.XPATH, "//a[contains(text(),'Next: Preview')]")
preview.click()


template = driver.find_element(By.XPATH, "//label[contains(text(),'Chic')]")
print("found template")
template.click()

driver.find_element(By.XPATH, "//div[@class='sp-preview-inner']").click()
time.sleep(2)
color = driver.find_element(By.XPATH, "//input[@class='sp-input']")
color.clear()
color.send_keys("#000000")
driver.find_element(By.XPATH, "//button[@class='sp-choose']").click()
time.sleep(2)
save_update = driver.find_element(By.XPATH, "//a[contains(text(),'Save & Update Preview')]")
print("Save and button found")
save_update.click()

time.sleep(60)




