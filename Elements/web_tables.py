from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/webtables")

# Add a new record
driver.find_element(By.ID, "addNewRecordButton").click()
driver.find_element(By.ID, "firstName").send_keys("Samrawit")
driver.find_element(By.ID, "lastName").send_keys("Nebiyou")
driver.find_element(By.ID, "userEmail").send_keys("samrawit.merhatsidk@gmail.com")
driver.find_element(By.ID, "age").send_keys("23")
driver.find_element(By.ID, "salary").send_keys("10000")
driver.find_element(By.ID, "department").send_keys("IT & Technology")
driver.find_element(By.ID, "submit").click()

# Edit existing data
driver.find_element(By.ID, "edit-record-1").click()
age_field = driver.find_element(By.ID, "age")
age_field.clear()
age_field.send_keys("50")
department_field = driver.find_element(By.ID, "department")
department_field.clear()
department_field.send_keys("Management")
driver.find_element(By.ID, "submit").click()

# Delete a record
driver.find_element(By.ID, "delete-record-2").click()

# Extract data
rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")

print("Table data:")
for index, row in enumerate(rows, start=1):
    text = row.text.strip()
    if text:
        print(f"Row {index}: {text}")

input("Press Enter to continue...")
driver.quit()
