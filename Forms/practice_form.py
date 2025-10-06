from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

# Fill basic info
driver.find_element(By.ID, "firstName").send_keys("Samrawit")
driver.find_element(By.ID, "lastName").send_keys("Nebiyou")
driver.find_element(By.ID, "userEmail").send_keys("samrawit.merhatsidk@gmail.com")
driver.find_element(By.XPATH, "//label[text()='Female']").click()
driver.find_element(By.ID, "userNumber").send_keys("0904175661")

# Subject
subject_input = driver.find_element(By.ID, "subjectsInput")
subject_input.send_keys("English")
subject_input.send_keys("\n")  # Press Enter to select

# Hobbies
driver.find_element(By.XPATH, "//label[text()='Sports']").click()
driver.find_element(By.XPATH, "//label[text()='Reading']").click()

# Upload picture
driver.find_element(By.ID, "uploadPicture").send_keys(r"C:\Users\Samrawit\Documents\sample.png")

# Address
driver.find_element(By.ID, "currentAddress").send_keys("Ethiopia, Addis Ababa")

# Scroll down to reveal dropdowns
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# State and City
driver.find_element(By.ID, "state").click()
driver.find_element(By.ID, "react-select-3-input").send_keys("NCR\n")

driver.find_element(By.ID, "city").click()
driver.find_element(By.ID, "react-select-4-input").send_keys("Delhi\n")

# Submit
driver.find_element(By.ID, "submit").click()

input("Press enter to close...")
driver.quit()


