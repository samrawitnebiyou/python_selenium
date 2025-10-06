from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/links")

#simple link
'''
driver.find_element(By.ID, "simpleLink").click()

tabs =  driver.window_handles
driver.switch_to.window(tabs[1])

print("Now on:", driver.current_url)
'''


#following links will send an api call
import time

driver.find_element(By.ID, "created").click()
time.sleep(1)  # wait for the message to appear
msg = driver.find_element(By.ID, "linkResponse").text
print("Message after clicking 'Created':", msg)

input("Press Enter to close...")
driver.quit()
