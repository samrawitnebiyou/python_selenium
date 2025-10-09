from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://demoqa.com/accordian")

header1= (driver.find_element(By.ID, "section1Heading"))
time.sleep(5)
header1.click()
content1= driver.find_element(By.ID, "section1Content").text
print("content from heading 1 :", content1[:100])
time.sleep(5)
header1.click()
time.sleep(5)
print("Content from heading 1 closed")



header2= (driver.find_element(By.ID, "section2Heading"))
time.sleep(5)
header2.click()
content2= driver.find_element(By.ID, "section2Content").text
print("content from heading 2 :", content2[:100])
time.sleep(5)
header2.click()
time.sleep(5)
print("Content from heading 2 closed")



header3= (driver.find_element(By.ID, "section3Heading"))
time.sleep(5)
header3.click()
content3= driver.find_element(By.ID, "section3Content").text
print("content from heading 3 :", content1[:100])
time.sleep(5)
header3.click()
time.sleep(5)
print("Content from heading 3 closed")

input("Press enter to continue...")
driver.quit()



