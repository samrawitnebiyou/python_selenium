import time

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

driver.find_element(By.ID, "userName").send_keys("Samrawit")
driver.find_element(By.ID, "userEmail").send_keys("samrawit.merhatsidk@gmail.com");
driver.find_element(By.ID,"currentAddress").send_keys("Addis Ababa")
driver.find_element(By.ID, "permanentAddress").send_keys("Ethiopia")

driver.find_element(By.ID, "submit").click()

input("Press Enter to close...")
driver.quit()
