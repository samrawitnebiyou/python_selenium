from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://demoqa.com/frames")

driver.switch_to.frame("frame1")
text1=driver.find_element(By.ID,"sampleHeading").text
print("text inside frame1",text1)

driver.switch_to.default_content()

driver.switch_to.frame("frame2")
text2=driver.find_element(By.ID,"sampleHeading").text
print("text inside frame2",text2)

input("Press enter to close...")
driver.quit()




