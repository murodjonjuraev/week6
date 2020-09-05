import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://google.com")
time.sleep(3)

search_text_box = driver.find_element_by_name("q")
search_text_box.clear()
search_text_box.send_keys("python selenium")
search_text_box.send_keys(Keys.ENTER)
time.sleep(3)
driver.close()