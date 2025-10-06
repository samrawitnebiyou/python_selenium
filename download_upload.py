from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("pref",{
    "download.default_directory":r"C:\Users\Samrawit\Downloads\selenium_downloads",
    "download.prompt_for_download":False,
    "download.directory_upgrade":True,
    "safebrowsing.enabled":True

})
driver = webdriver.Chrome()
driver.get("https://demoqa.com/upload-download")

driver.find_element(By.ID,"downloadButton").click()


#uploading a file
driver.find_element(By.ID, "uploadFile").send_keys(r"C:\Users\Samrawit\Documents\sample.txt"
)

input("Press Enter to close...")
driver.quit()

