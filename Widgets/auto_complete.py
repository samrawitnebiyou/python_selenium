from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import time
driver=webdriver.Chrome()

driver.get("https://demoqa.com/auto-complete")

multi_input=driver.find_element(By.ID, "autoCompleteMultipleInput")
multi_input.send_keys("Red")
multi_input.send_keys(Keys.ENTER)
time.sleep(1)

multi_input.send_keys("Green")
multi_input.send_keys(Keys.ENTER)
time.sleep(1)


multi_input.send_keys("Yellow")
multi_input.send_keys(Keys.ENTER)
time.sleep(1)

print("colores added red, green, yellow")



single_input = driver.find_element(By.ID, "autoCompleteSingleInput")
single_input.send_keys("purple")
single_input.send_keys(Keys.ENTER)
time.sleep(1)
print("only purple added")
input("press enter to continue")
driver.quit()










