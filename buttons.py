from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(5)  # wait for elements

action = ActionChains(driver)

driver.get("https://demoqa.com/buttons")

# Single click
click_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
click_btn.click()

# Double click
double_btn = driver.find_element(By.ID, "doubleClickBtn")
action.double_click(double_btn).perform()

# Right click
right_btn = driver.find_element(By.ID, "rightClickBtn")
action.context_click(right_btn).perform()

input("Press Enter to close...")  # wait so you can see the results
driver.quit()
