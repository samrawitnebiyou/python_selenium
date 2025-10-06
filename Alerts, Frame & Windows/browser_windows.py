from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://demoqa.com/browser-windows")

driver.find_element(By.ID, "tabButton").click()

handles= driver.window_handles
print("All window handles:",handles)
driver.switch_to.window(handles[-1])
print("Switched to new tab")
print("New tab title:",driver.title)

driver.switch_to.window(handles[0])
print("Back to main window")

driver.find_element(By.ID, "windowButton").click()
handles = driver.window_handles
driver.switch_to.window(handles[-1])

print("Switched to new window")
print("New window title:", driver.title)
driver.switch_to.window(handles[0])
print("Back to main window")

driver.find_element(By.ID, "messageWindowButton").click()

handles = driver.window_handles
print("All window handles:",handles)
driver.switch_to.window(handles[-1])
print("Switched to message window")

try:
    text = driver.find_element(By.TAG_NAME, "body").text
    print("Message window text:", text)
except Exception as e:
    print("Cannot read text (expected for message window):", e)
driver.close()

driver.switch_to.window(handles[0])
print("Back to main window")

input("Press enter to close...")
driver.quit()