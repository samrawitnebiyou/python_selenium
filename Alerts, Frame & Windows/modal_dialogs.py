import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver= webdriver.Chrome()

driver.get("https://demoqa.com/modal-dialogs")

driver.find_element(By.ID,"showSmallModal").click()
time.sleep(2)

small_modal=driver.find_element(By.CLASS_NAME,"modal-body").text

print("This is text from small modal",small_modal)

driver.find_element(By.ID,"closeSmallModal").click()

time.sleep(2)

driver.find_element(By.ID,"showLargeModal").click()
time.sleep(2)

large_modal = driver.find_element(By.TAG_NAME,"p").text
print("This is text from large modal",large_modal)

driver.find_element(By.ID,"closeLargeModal").click()


input("Press enter to close...")
driver.quit()










