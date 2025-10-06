import requests
from selenium import webdriver

from selenium.webdriver.common.by import By

driver =webdriver.Chrome()

driver.get("https://demoqa.com/broken")

#check valid image

valid_image= driver.find_element(By.XPATH, "(//img)[1]")
valid_src=valid_image.get_attribute("src")
print(f"Checking valid image : {valid_src}")
response = requests.get(valid_src)

if response.status_code == 200:
    print("Valid image is working")
else:
    print("Valid image is broken")

#check broken image

broken_image = driver.find_element(By.XPATH, "(//img)[2]")
broken_src=broken_image.get_attribute("src")
print(f"Checking broken image : {broken_src}")
response = requests.get(broken_src)
if response.status_code == 200:
    print("Broken image is working")
else:
    print("Broken image is broken")

#check valid link
valid_link = driver.find_element(By.LINK_TEXT, "Click Here for Valid Link")
valid_href = valid_link.get_attribute("href")
print(f"Checking valid href : {valid_href}")
response = requests.get(valid_href)
if response.status_code == 200:
    print("Valid href is working")
else:
    print("Valid href is broken")


#check broken link
broken_link = driver.find_element(By.LINK_TEXT, "Click Here for Broken Link")
broken_href=broken_link.get_attribute("href")
print(f"Checking broken href : {broken_href}")
response = requests.get(broken_href)
if response.status_code == 200:
    print("Broken href is working")
else:
    print("Broken href is broken")


input("Press Enter to close...")
driver.quit()
