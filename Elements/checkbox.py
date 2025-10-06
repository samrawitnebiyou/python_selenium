from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://demoqa.com/checkbox")

driver.find_element(By.CLASS_NAME, "rct-checkbox").click()

input("Press Enter to close...")
driver.quit()

