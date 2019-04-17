from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless") #Command Line Interface

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/Users/Cedric1/Documents/section3/webdriver/chrome/chrome")

#drive.set_window_size(1920,1280)

driver.get("https://google.com")
#time.sleep(5)
driver.save_screenshot(/Users/Cedric1/Documents/section3/webdriver/chrome/shot1.png)

driver.get("https://www.daum.net")
#time.sleep(5)
driver.save_screenshot(/Users/Cedric1/Documents/section3/webdriver/chrome/shot2.png)

driver.quit()

print("스크린샷 완료")
