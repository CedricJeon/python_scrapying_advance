from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome("/Users/Cedric1/Documents/section3/webdriver/chrome/chrome.dmg")
driver.set_window_size(1920,1280)
driver.implicitly_wait(3)

driver.get("https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F")
time.sleep(3)
driver.implicitly_wait(3)

driver.find_element_by_name("log").send_keys("id")
driver.find_element_by_name("pwd").send_keys("pw")
driver.find_element_by_xpath("//*[@id='wp-submit']").click()
