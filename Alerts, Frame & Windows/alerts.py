from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome()

driver.get("https://demoqa.com/alerts")

driver.find_element(By.ID, "alertButton").click()
time.sleep(2)

alert = driver.switch_to.alert
print("Simple alert text:", alert.text)

time.sleep(2)

alert.accept()
print("simple alert accepted")

#timed alert
driver.find_element(By.ID, "timerAlertButton").click()

print("Waiting for alert to appear...")

WebDriverWait(driver, 10).until(EC.alert_is_present())

alert=driver.switch_to.alert
print("Alert appeared")
print("Alert text:", alert.text)
time.sleep(2)


alert.accept()
print("Alert accepted")


#Confirm alert ok
driver.find_element(By.ID, "confirmButton").click()
time.sleep(2)

alert = driver.switch_to.alert
print("Alert text:", alert.text)
time.sleep(2)
alert.accept()
print("Alert accepted")


#Confirm alert Cancel
driver.find_element(By.ID, "confirmButton").click()
time.sleep(2)

alert = driver.switch_to.alert
print("Alert text:", alert.text)
time.sleep(2)
alert.dismiss()
print("Alert Dismissed")


#Prompt Alert
driver.find_element(By.ID, "promtButton").click()
time.sleep(2)
alert = driver.switch_to.alert
print("Alert text:", alert.text)
time.sleep(2)
alert.send_keys("Samrawit")
time.sleep(2)
alert.accept()
print("Alert Accepted")
result = driver.find_element(By.ID, "promptResult").text
print("Result message on page:", result)

input("Press enter to close...")
driver.quit()


