from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://demoqa.com/slider")

slider = driver.find_element(By.XPATH, "//input[@type='range']")
time.sleep(5)
print ("Before moving: ", slider.get_attribute('value'))

actions = ActionChains(driver)
actions.click_and_hold(slider).move_by_offset(40, 0).release().perform()

time.sleep(5)

print("After moving: ", slider.get_attribute('value'))

input("press enter to continue")

driver.quit()
