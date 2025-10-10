import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/tool-tips")
driver.maximize_window()
time.sleep(2)

tooltip_elements = [
    driver.find_element(By.ID, "toolTipButton"),
    driver.find_element(By.ID, "toolTipTextField"),
    driver.find_element(By.XPATH, "//a[text()='Contrary']"),
    driver.find_element(By.XPATH, "//a[text()='1.10.32']"),
]

for elem in tooltip_elements:
    ActionChains(driver).move_to_element(elem).perform()  # create a new ActionChains for each hover
    time.sleep(1)  # wait for tooltip to appear
    tooltip_text = driver.find_element(By.CSS_SELECTOR, ".tooltip-inner").text
    print(f"Tooltip for '{elem.text or elem.get_attribute('id')}': {tooltip_text}")

input("Press enter to continue...")
driver.quit()
