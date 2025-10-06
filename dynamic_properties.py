from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")

wait = WebDriverWait(driver, 10)

# Wait for button to become clickable
button = wait.until(EC.element_to_be_clickable((By.ID, "enableAfter")))
print("Button is now clickable")
button.click()

# Check color change button
color_button = driver.find_element(By.ID, "colorChange")
print("Color before change:", color_button.value_of_css_property("color"))

# Wait for visible text
visible_text = wait.until(EC.visibility_of_element_located((By.ID, "visibleAfter")))
print("Text appeared:", visible_text.text)

input("Press Enter to close...")
driver.quit()
