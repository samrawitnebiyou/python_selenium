import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demoqa.com/menu")


menu_items = driver.find_elements(By.CSS_SELECTOR, "#nav > li > a")

for item in menu_items:
    print(f"Top Menu :{item.text}")
    ActionChains(driver).move_to_element(item).perform()
    time.sleep(1)

    sub_items = item.find_elements(By.XPATH, ".//following-sibling::ul/li/a")
    for sub in sub_items:
        print(f"Sub Item: {sub.text}")
        ActionChains(driver).move_to_element(sub).perform()
        time.sleep(1)

        sub_sub_items = sub.find_elements(By.XPATH, "../ul/li/a")
        for sub_sub in sub_sub_items:
            print(f"Sub Sub Item: {sub_sub.text}")

time.sleep(1)
input("Press enter to continue...")
driver.quit()

