from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/radio-button")

# Click Yes
driver.find_element(By.XPATH, "//label[text()='Yes']").click()
msg = driver.find_element(By.CLASS_NAME, "text-success").text
print("Message after Yes click:", msg)

# Click Impressive
driver.find_element(By.XPATH, "//label[text()='Impressive']").click()
msg = driver.find_element(By.CLASS_NAME, "text-success").text
print("Message after Impressive click:", msg)

# Try clicking No (disabled)
try:
    driver.find_element(By.XPATH, "//label[text()='No']").click()
except Exception as e:
    print("Cannot click 'No':", e)

input("Press Enter to close...")
driver.quit()
