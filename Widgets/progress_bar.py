from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/progress-bar")


button=(driver.find_element(By.ID, "startStopButton"))
button.click()
print("Progess bar has started...")
time.sleep(4)

button.click()
print("Progess bar has ended...")


bar=driver.find_element(By.ID, "progressBar")

print(bar.text)

input("press enter to continue")

driver.quit()

