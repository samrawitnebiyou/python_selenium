from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://demoqa.com/nestedframes")

driver.switch_to.frame("frame1")

text1= driver.find_element(By.TAG_NAME,"body").text

print("Parent text: ",text1)

child_frame = driver.find_element(By.TAG_NAME,"iframe")

driver.switch_to.frame(child_frame)
text2= driver.find_element(By.TAG_NAME,"p").text
print("Child text: ",text2)

input("Press enter to close...")
driver.quit()

